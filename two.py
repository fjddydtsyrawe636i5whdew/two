import time
import random
import threading

import sys
from unittest import mock
 
# Mock pyautogui to prevent it breaking on import
sys.modules["pyautogui"] = mock.MagicMock()

import pyautogui
import os

os.environ['DISPLAY'] = ':0'

# List of random words to type
words = ["hello", "world", "python", "script", "idle", "prevent", "random", "typing"]

# Function to simulate typing random words
def simulate_typing():
    while True:
        word = random.choice(words)
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        time.sleep(random.randint(30, 90))  # Wait for a random interval between 30 and 90 seconds

# Function to simulate mouse activity
def simulate_mouse():
    while True:
        pyautogui.moveRel(0, 1)  # Move mouse slightly
        pyautogui.moveRel(0, -1)  # Move mouse back
        time.sleep(60)  # Wait for 60 seconds before moving the mouse again

# Main function to run both activities for 10 hours
def main():
    start_time = time.time()
    duration = 10 * 60 * 60  # 10 hours in seconds

    # Start typing and mouse simulation in separate threads
    typing_thread = threading.Thread(target=simulate_typing)
    mouse_thread = threading.Thread(target=simulate_mouse)

    typing_thread.start()
    mouse_thread.start()

    # Run for the specified duration
    while time.time() - start_time < duration:
        time.sleep(1)

    print("Script finished running for 10 hours.")

if __name__ == "__main__":
    main()
