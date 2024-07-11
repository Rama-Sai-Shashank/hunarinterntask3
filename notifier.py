import time
import schedule
from plyer import notification
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Desktop Notifier',
        timeout=10
    )
def job():
    show_notification("Reminder", "Time to take a break!")
if __name__ == "__main__":
    schedule.every().hour.do(job)
    print("Desktop Notifier is running...")
    while True:
        schedule.run_pending()
        time.sleep(1)
