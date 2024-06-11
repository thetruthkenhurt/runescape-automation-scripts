import pyautogui
import time
import random

def click(x, y, duration=0.1):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, duration))
    pyautogui.click()

def plank_make(magic_menu_key, plank_spell_x, plank_spell_y, plank_x, plank_y, bank_x, bank_y, deposit_x, deposit_y, withdraw_x, withdraw_y):
    try:
        while True:
            # Select Magic Menu
            pyautogui.press(magic_menu_key)
            time.sleep(random.uniform(1, 1.4))

            # Click Plank Make spell
            click(plank_spell_x, plank_spell_y)
            time.sleep(random.uniform(0.5, 0.7))

            # Click on plank in inventory
            click(plank_x, plank_y)
            time.sleep(random.uniform(90.1, 94))  # Wait for Plank Make spell to finish

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
    magic_menu_key = 'f6'  # Key to open magic menu
    plank_spell_x, plank_spell_y = 1192, 1625  # Example coordinates for Plank Make spell
    plank_x, plank_y = 1192, 1625  # Example coordinates for the plank in inventory
    bank_x, bank_y = 659, 1421  # Example coordinates for the bank
    deposit_x, deposit_y = 707, 1554  # Example coordinates to deposit logs/planks
    withdraw_x, withdraw_y = 635, 1414  # Example coordinates to withdraw logs/planks

    print("Starting Plank Make script in 5 seconds. Switch to RuneScape window.")
    time.sleep(5)
    plank_make(magic_menu_key, plank_spell_x, plank_spell_y, plank_x, plank_y, bank_x, bank_y, deposit_x, deposit_y, withdraw_x, withdraw_y)
