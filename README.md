💧 Hydration Bot: Desktop Water Reminder

A simple Python automation tool that reminds you to drink water at regular intervals while you work or study.
Built to promote healthy habits during long coding or screen sessions.

🚀 Features

Automatic Reminders
Sends desktop notifications at fixed intervals so you don’t forget to drink water.
Activity Logging
Keeps a record of each reminder in a file (hydration_log.txt) with timestamps.
Lightweight & Efficient
Runs in the background with very low CPU usage.
Safe Exit
Easily stop the program anytime using Ctrl + C without errors.

🛠️ Requirements

Make sure you have the following installed:

Python 3.x
plyer library (used for desktop notifications)'

📥 Setup & Installation

Follow these steps to run the project on your system:

1. Clone the Repository
git clone https://github.com/VarunBansal-18/Hydration-Bot.git
cd hydration-bot

3. Install Dependencies
pip install plyer

5. Run the Script
python water.py

📖 Usage

By default, the bot sends a reminder every 60 minutes.
You can change this by editing the following variable in water.py:
REMAINDER_INTERVAL = 3600  # time in seconds

Once running:
You’ll receive a desktop notification.
Each reminder is saved in hydration_log.txt.

📌 Example Output

--- Hydration Bot is now running in the background ---
I will remind you every 60 minutes.

🎯 Why This Project?

During long study or coding sessions, it’s easy to forget basic habits like drinking water.
This project is a simple solution to maintain hydration and improve focus without interrupting your workflow.
