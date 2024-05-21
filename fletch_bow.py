import pyautogui
import time
import random

# Assuming withdraw option set to withdraw-all
# knife in inventory and bank is fully filled(use fillers)
def click(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()

def fletch_longbows(log_x, log_y, knife_x, knife_y, bank_x, bank_y, withdraw_x, withdraw_y, deposit_x):
    try:
        while True:
            # Fletch the logs
            click(knife_x, knife_y)
            time.sleep(random.uniform(0.4, 0.5))
            click(log_x, log_y)
            time.sleep(random.uniform(0.6, 0.7))
            # Select bow type (space for maple longbows)
            pyautogui.press('space')
            time.sleep(random.uniform(51, 53))  # Adjust time based on fletching speed
            
            
            # Open the bank
            click(bank_x, bank_y)
            time.sleep(random.uniform(1, 2))
            
            # Deposit all
            click(deposit_x, deposit_y)
            time.sleep(random.uniform(0.5, 1))

            # Withdraw logs
            click(withdraw_x, withdraw_y)
            time.sleep(random.uniform(0.5, 1))

            # Close the bank
            pyautogui.press('esc')
            time.sleep(random.uniform(0.5, 1))

    except KeyboardInterrupt:
        print("Script stopped by user.")

if __name__ == "__main__":
    # Coordinates
    bank_x, bank_y = 660, 1421  # Coordinates of the bank
    withdraw_x, withdraw_y = 586, 1414  # Coordinates to withdraw logs
    deposit_x, deposit_y = 691, 1555  # Coordinates to deposit all items
    knife_x, knife_y = 1179, 1588  # Coordinates of the knife in inventory
    log_x, log_y = 1135, 1586  # Coordinates of the logs in inventory

    print("Starting Fletching Longbows script in 5 seconds. Switch to RuneScape window.")
    time.sleep(5)
    fletch_longbows(log_x, log_y, knife_x, knife_y, bank_x, bank_y, withdraw_x, withdraw_y, deposit_x)
