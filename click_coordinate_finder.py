import pyautogui
import time

print("Move your mouse to the desired position and press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Current Position: x={x}, y={y}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped.")