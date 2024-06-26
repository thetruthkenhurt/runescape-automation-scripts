#note: inventory must be full with items first, 14 battlestaves followed by 14 orbs
import pyautogui
import time
import random

def click(x, y, duration=0.1):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, duration))
    pyautogui.click()

def craft_battlestaves(duration, orb_x, orb_y, staff_x, staff_y, bank_x, deposit_all_x, withdraw_staves_x, withdraw_orbs_x):
    start_time = time.time()
    try:
        while True:
            # Check if the duration has passed
            if time.time() - start_time > duration:
                print("Script has reached the timeout limit. Stopping script.")
                break
            # Click air orb first
            click(orb_x, orb_y)
            time.sleep(random.uniform(0.5, 0.9))
            # Then click battlestaff
            click(staff_x, staff_y)
            time.sleep(random.uniform(1, 1.3))

            # Press 'space' for the 'Make-All' option
            pyautogui.press('space')
            time.sleep(random.uniform(18, 20))  # Wait for the crafting to finish

            # Click on the Bank booth
            click(bank_x, bank_y)
            time.sleep(random.uniform(2, 4))  # Time to open bank and deposit items

            # Deposit all items
            click(deposit_all_x, deposit_all_y)
            time.sleep(random.uniform(0.5, 0.7))

            # Withdraw 14 battlestaves
            click(withdraw_staves_x, withdraw_staves_y)
            time.sleep(random.uniform(0.3, 0.5))

            # Withdraw 14 air orbs
            click(withdraw_orbs_x, withdraw_orbs_y)
            time.sleep(random.uniform(0.3, 0.5))

            # Close bank window
            pyautogui.press('esc')
            time.sleep(random.uniform(0.3, 0.5))
    except KeyboardInterrupt:
        print("Script stopped by user.")

if __name__ == "__main__":
    # Replace these coordinates with the ones you recorded
    orb_x, orb_y = 1170, 1589  # Coordinates of air orbs in inventory
    staff_x, staff_y = 1138, 1591  # Coordinates of battlestaves in inventory
    bank_x, bank_y = 678, 1415  # Coordinates of the bank booth
    deposit_all_x, deposit_all_y = 691, 1555  # Coordinates to deposit all items
    withdraw_staves_x, withdraw_staves_y = 616, 1413  # Coordinates to withdraw battlestaves
    withdraw_orbs_x, withdraw_orbs_y = 678, 1411  # Coordinates to withdraw air orbs
    
    duration = 50 * 60  # Duration in seconds (e.g., 120 minutes)


    print("Starting Battlestaff Crafting bot in 5 seconds. Switch to RuneScape window.")
    time.sleep(5)
    craft_battlestaves(duration, orb_x, orb_y, staff_x, staff_y, bank_x, deposit_all_x, withdraw_staves_x, withdraw_orbs_x)
