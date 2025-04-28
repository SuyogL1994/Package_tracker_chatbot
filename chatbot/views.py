from django.shortcuts import render
import re

# Dummy tracking data
tracking_data = {
    "IND123": {
        "item_name": "Wireless Headphones",
        "order_date": "2025-04-20",
        "expected_delivery": "2025-04-30",
        "status": "In Transit",
        "current_location": "New Delhi Hub"
    },
    "IND456": {
        "item_name": "Smartphone",
        "order_date": "2025-04-18",
        "expected_delivery": "2025-04-28",
        "status": "Out for Delivery",
        "current_location": "Mumbai Distribution Center"
    },
    "IND789": {
        "item_name": "Laptop",
        "order_date": "2025-04-15",
        "expected_delivery": "2025-04-27",
        "status": "Delivered",
        "current_location": "Delivered to Address"
    },
    "IND999": {
        "item_name": "Smartwatch",
        "order_date": "2025-04-19",
        "expected_delivery": "2025-04-29",
        "status": "In Transit",
        "current_location": "Bangalore Sorting Center"
    }
}

# Greeting message
greeting_message = (
    "👋 Hi! How may I assist you today? You can:\n"
    "1️⃣ Track Package\n"
    "2️⃣ Report Issue\n"
    "3️⃣ Check Delivery Status"
)

# Keywords
TRACK_KEYWORDS = ['track', 'status', 'find', 'location', 'where']
COMPLAINT_KEYWORDS = ['lost', 'late', 'longer', 'wait', 'waiting', 'delay', 'delayed', 'missing', 'stuck', 'problem']


def chatbot_view(request):
    response = greeting_message

    if request.method == 'POST':
        original_message = request.POST.get('message', '').strip()
        user_message = original_message.lower()

        # 1. Greetings
        if user_message in ['hi', 'hello', 'hey']:
            response = greeting_message

        # 2. Tracking-related keywords
        elif any(keyword in user_message for keyword in TRACK_KEYWORDS):
            response = "📦 Sure! Please provide your Tracking ID (format: IND123)."

        # 3. Check if message matches tracking ID pattern
        elif re.fullmatch(r'ind\d{3}', user_message):
            tracking_id = original_message.upper()
            package = tracking_data.get(tracking_id)

            if package:
                # If tracking ID is valid and found
                response = (
                    f"🔎 Tracking ID: {tracking_id}\n"
                    f"Item: {package['item_name']}\n"
                    f"Order Date: {package['order_date']}\n"
                    f"Expected Delivery: {package['expected_delivery']}\n"
                    f"Status: {package['status']}\n"
                    f"Current Location: {package['current_location']}\n\n"
                    "Is there anything else I can help you with? 😊"
                )
            else:
                # Tracking ID format valid, but not found
                response = "⚠️ Please enter a valid Tracking ID (format: IND123)."

        # 4. Complaint keywords
        elif any(word in user_message for word in COMPLAINT_KEYWORDS):
            response = (
                "😟 Sorry for the inconvenience.\n"
                "Please share your Tracking ID (format: IND123).\n"
                "Or provide Full Name, Email ID, and Delivery Address so we can assist you!"
            )

        # 5. Special scenarios
        elif "delivered" in user_message and "not received" in user_message:
            response = (
                "🚚 Your package shows 'Delivered', but you haven't received it?\n"
                "Please confirm your delivery address. We’ll start an investigation right away!"
            )

        elif "no tracking number" in user_message or "don't have tracking" in user_message:
            response = (
                "📝 No worries! Please provide:\n"
                "- Full Name\n"
                "- Email Address\n"
                "- Order Date\n"
                "- Delivery Address\n"
                "- Item Description\n"
                "I'll manually find your order! 🔍"
            )

        elif "stuck" in user_message or "in transit" in user_message:
            response = (
                "⏳ Your package is 'In Transit' for a while.\n"
                "I'll escalate to our team for faster delivery.\n"
                "Please also share your contact number for updates."
            )

        elif "update" in user_message and "delay" in user_message:
            response = (
                "📢 Update: Some deliveries are delayed at the Delhi sorting center.\n"
                "Expected delivery is delayed by 2 days.\n"
                "Apologies for the inconvenience! 🙏"
            )

        # 6. If the user tries to input a wrong tracking ID (wrong format, random text)
        else:
            response = "⚠️ Please enter a valid Tracking ID (format: IND123)."

    return render(request, 'chatbot.html', {'response': response})
