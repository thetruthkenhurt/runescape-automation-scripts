#note - materials need to be in inventory before running script
#take care of xp in case theres a level up
import pyautogui
import time
import random

def right_click(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click(button='right')

def click(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()

def craft_battlestaves(orb_x, orb_y, staff_x, staff_y, make_all_x, make_all_y, bank_x, bank_y, bank_close_x, bank_close_y, right_click_staves_x, right_click_staves_y, withdraw_staves_x, withdraw_staves_y, right_click_orbs_x, right_click_orbs_y, withdraw_orbs_x, withdraw_orbs_y):
    try:
        while True:
            # Click air orb first
            click(orb_x, orb_y)
            time.sleep(random.uniform(0.05, 0.15))
            # Then click battlestaff
            click(staff_x, staff_y)
            time.sleep(random.uniform(0.6, 0.8))

            # Click on the 'Make-All' option
            click(make_all_x, make_all_y)
            time.sleep(random.uniform(18, 22))  # Wait for the crafting to finish

            # Right-click on the Banker
            right_click(bank_x, bank_y)
            time.sleep(random.uniform(0.1, 0.3))

            # Move to and click 'Bank'
            click(bank_click_x, bank_click_y)
            time.sleep(random.uniform(2, 4))  # Time to open bank and deposit items
            
            # Deposit inventory
            click(deposit_inventory_x, deposit_inventory_y)
            time.sleep(random.uniform(0.1, 0.3))

            # Right-click and withdraw 14 battlestaves
            right_click(right_click_staves_x, right_click_staves_y)  # Right-click on battlestaves in bank
            time.sleep(random.uniform(0.1, 0.3))
            click(withdraw_staves_x, withdraw_staves_y)  # Click 'Withdraw-14'
            time.sleep(random.uniform(0.1, 0.3))

            # Right-click and withdraw 14 air orbs
            right_click(right_click_orbs_x, right_click_orbs_y)  # Right-click on air orbs in bank
            time.sleep(random.uniform(0.1, 0.3))
            click(withdraw_orbs_x, withdraw_orbs_y)  # Click 'Withdraw-14'
            time.sleep(random.uniform(0.1, 0.3))

            # Close bank window
            click(bank_close_x, bank_close_y)
            time.sleep(random.uniform(0.1, 0.3))
    except KeyboardInterrupt:
        print("Script stopped by user.")

if __name__ == "__main__":
    # Replace these coordinates with the ones you recorded
    orb_x, orb_y = 1170, 1589  # Coordinates of air orbs in inventory x=1146, y=1588
    staff_x, staff_y = 1138, 1591  # Coordinates of battlestaves in inventory -in laptop window x=1148, y=1562
    make_all_x, make_all_y = 265, 1673  # Coordinates of 'Make-X' confirmation option  x=265, y=1673
    bank_x, bank_y = 680, 1422  # Coordinates of the Banker x=667, y=1415
    bank_click_x, bank_click_y = 686, 1463  # Coordinates to click 'Bank' after right-clicking the Banker NPC x=708, y=1453
    deposit_inventory_x, deposit_inventory_y = 683, 1555  # Coordinates to click 'Deposit Inventory' x=683, y=1555
    bank_close_x, bank_close_y = 738, 1120  # Coordinates to close the bank window  x=724, y=1122
    right_click_staves_x, right_click_staves_y = 616, 1413  # Coordinates to right-click battlestaves in bank  x=616, y=1413
    withdraw_staves_x, withdraw_staves_y = 616, 1502  # Coordinates to click 'Withdraw-14' for battlestaves x=616, y=1488
    right_click_orbs_x, right_click_orbs_y = 678, 1411  # Coordinates to right-click air orbs in bank        x=660, y=1415
    withdraw_orbs_x, withdraw_orbs_y = 669, 1502  # Coordinates to click 'Withdraw-14' for air orbs  x=659, y=1488

    print("Starting Battlestaff Crafting bot in 5 seconds. Switch to RuneScape window.")
    time.sleep(5)
    craft_battlestaves(orb_x, orb_y, staff_x, staff_y, make_all_x, make_all_y, bank_x, bank_y, bank_close_x, bank_close_y, right_click_staves_x, right_click_staves_y, withdraw_staves_x, withdraw_staves_y, right_click_orbs_x, right_click_orbs_y, withdraw_orbs_x, withdraw_orbs_y)
