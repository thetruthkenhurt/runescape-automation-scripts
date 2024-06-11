# Make sure item is aligned on high alch tile, start from spellbook page 
# Adjust timeout to your liking
import pyautogui
import time
import random

def high_alch(duration):
    start_time = time.time()
    try:
        while True:
            # Check if the duration has passed
            if time.time() - start_time > duration:
                print("Script has reached the timeout limit. Stopping script.")
                break

            # Click on the High Alchemy spell and the item (same coordinates)
            pyautogui.click()
            time.sleep(random.uniform(0.2, 0.4))
            pyautogui.click()
            time.sleep(random.uniform(2.5, 3.3))  # Adjust based on High Alchemy cooldown

    except KeyboardInterrupt:
        print("Script stopped by user.")

if __name__ == "__main__":
    # Coordinates
    # Example coordinates for both the High Alchemy spell and the item(optional)
    duration = 35 * 60  # Duration in seconds (e.g., 120 minutes)

    print("Starting High Alching script in 5 seconds. Switch to RuneScape window.")
    time.sleep(5)
    high_alch(duration)
