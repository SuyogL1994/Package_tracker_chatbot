# views.py

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

# Global greeting
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
    response = greeting_message  # Default message
    if request.method == 'POST':
        user_message = request.POST.get('message', '').lower().strip()

        # 1. Greetings
        if user_message in ['hi', 'hello', 'hey']:
            response = greeting_message

        # 2. User asks to track
        elif any(keyword in user_message for keyword in TRACK_KEYWORDS):
            response = "📦 Sure! Please provide your Tracking ID (format: IND123)."

        # 3. Tracking ID provided
        elif re.match(r'^ind\d{3}$', user_message):
            tracking_id = user_message.upper()
            package = tracking_data.get(tracking_id)

            if package:
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
                response = (
                    "❌ I couldn't find any package with that ID.\n"
                    "Please double-check your Tracking ID or provide more order details like:\n"
                    "- Your Full Name\n- Email Address\n- Order Date\n- Delivery Address\n"
                    "I'll try to locate it for you!"
                )

        # 4. Complaints or delivery problems
        elif any(word in user_message for word in COMPLAINT_KEYWORDS):
            response = (
                "😟 Sorry for the inconvenience.\n"
                "Please share your Tracking ID if you have it (format: IND123).\n"
                "If you don't have it, please provide:\n"
                "- Your Full Name\n- Email ID\n- Delivery Address\n- Item description\n"
                "I'll start investigating right away! 🚀"
            )

        # 5. Delivered but not received
        elif "delivered" in user_message and "not received" in user_message:
            response = (
                "🚚 Your package shows 'Delivered', but you haven't received it?\n"
                "Please confirm your Delivery Address so I can open an investigation!\n"
                "Meanwhile, kindly check around your property or with neighbors if possible."
            )

        # 6. No tracking number case
        elif "no tracking number" in user_message or "don't have tracking" in user_message:
            response = (
                "📝 No worries! Please provide the following so I can locate your order:\n"
                "- Full Name\n- Email Address\n- Order Date\n- Delivery Address\n- Item Description\n"
                "I'll search it manually! 🔍"
            )

        # 7. Package stuck or in transit too long
        elif "stuck" in user_message or "in transit" in user_message:
            response = (
                "⏳ I see your package status as 'In Transit' for a while.\n"
                "I'll raise a quick internal check with our depot team. 📋\n"
                "Please also share your contact number for updates!"
            )

        # 8. Update about delay
        elif "update" in user_message and "delay" in user_message:
            response = (
                "📢 Important Update:\n"
                "Some packages are experiencing delays at our Delhi sorting center.\n"
                "New expected delivery: 2 days later than originally planned.\n"
                "Apologies for the inconvenience! We're working hard to deliver ASAP. 🚛💨"
            )

        # 9. Fallback if no condition matched
        else:
            response = (
                "🤔 I'm here to help you with package tracking!\n"
                "You can say things like:\n"
                "- 'Track my package'\n"
                "- 'Where is my parcel?'\n"
                "- 'My delivery is late'\n"
                "- Provide Tracking ID (e.g., IND123)\n"
                "Let's get started! 🚀"
            )

    return render(request, 'chatbot.html', {'response': response})
