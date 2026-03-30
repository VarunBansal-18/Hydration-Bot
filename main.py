import time
from plyer import notification
from datetime import datetime

def send_water_reminder():
    title = "To: You | From: Hydration Bot 💧"
    message = "Time to take a break and drink a glass of water. Your brain will thank you!"
    
    notification.notify(
        title=title,
        message=message,
        app_name="Water Reminder",
        timeout=10
    )

def log_reminder():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("hydration_log.txt", "a") as file:
        file.write(f"Reminder sent at: {current_time}\n")

if __name__ == "__main__":
    REMAINDER_INTERVAL = 3600 

    print("--- Hydration Bot is now running in the background ---")
    print(f"I will remind you every {REMAINDER_INTERVAL // 60} minutes.")
    
    try:
        while True:
            send_water_reminder()
            log_reminder()
            time.sleep(REMAINDER_INTERVAL)
            
    except KeyboardInterrupt:
        print("\nStopping the Hydration Bot. Stay healthy!")
