# Reminder functionality
import time


def reminder(seconds, message):

    print(f"Reminder set for {seconds} seconds.")

    time.sleep(seconds)

    print("Reminder:", message)