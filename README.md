
# Package Tracker - Customer Service Chatbot

This project implements a simple chatbot using Django to help users track packages, report issues, and check delivery status.

## Table of Contents

1.  [Setup and Installation](#setup-and-installation)
2.  [Explanation of Approach](#explanation-of-approach)
3.  [Screenshots/Examples](#screenshotsexamples)

## 1\. Setup and Installation

To get the chatbot running on your local machine, follow these steps:

**Prerequisites:**

- Python 3.6 or later
- pip (Python package installer)

**Installation Steps:**

1.  **Clone the repository:**
    
    ```bash
    git clone https://github.com/SuyogL1994/Package_tracker_chatbot.git
    cd chatbot_project
    ```
    
2.  **Create a virtual environment (recommended):**
    
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS and Linux
    ```
    
3.  **Install the project dependencies:**
    
    ```bash
    pip install django
    ```
    
4.  **Apply database migrations:**
    
    ```bash
    python manage.py migrate
    ```
    
5.  **Run the development server:**
    
    ```bash
    python manage.py runserver
    ```
    
6.  **Access the chatbot:**
    
    Open your web browser and go to `http://127.0.0.1:8000/`
    

## 2\. Explanation of Approach

This chatbot is built using the Django web framework and follows a simple conversational flow based on keyword matching and regular expressions.

- **Core Technology:** Django is used to handle the web requests, manage the application's logic, and render the user interface. The front-end is primarily HTML with some CSS for styling and JavaScript for basic interactivity (like toggling the theme).
- **Conversational Logic:**
    - The `chatbot/views.py` file contains the main logic.
    - A dictionary (`tracking_data`) stores dummy package tracking information. In a real application, this would likely come from a database or an external API.
    - The `chatbot_view` function handles user input and generates bot responses.
    - Keyword lists (`TRACK_KEYWORDS`, `COMPLAINT_KEYWORDS`) are used to identify the user's intent.
    - Regular expressions are used to validate input formats (e.g., the tracking ID format "IND123").
    - The chat history is stored in the user's session (`request.session['chat_history']`) to maintain context across messages.
- **User Interface:**
    - The `chatbot/templates/chatbot.html` file provides the HTML structure for the chat interface.
    - CSS is used for styling the chat bubbles, layout, and theme.
    - JavaScript handles the theme toggle and ensures the chat window scrolls to the bottom on new messages.

**Limitations:**

- This chatbot uses dummy data. A real-world application would need to integrate with a proper database or package tracking API.
- The conversational logic is relatively basic, relying on keyword matching. More advanced chatbots use Natural Language Processing (NLP) to better understand user input.
- Error handling and input validation could be improved.
