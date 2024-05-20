import pyautogui
import time
import random

def right_click(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click(button='right')

def click(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()

def clean_herbs(herb_coords, bank_npc_x, bank_npc_y, bank_click_x, bank_click_y, deposit_inventory_x, deposit_inventory_y, bank_close_x, bank_close_y, right_click_herbs_x, right_click_herbs_y, withdraw_herbs_x, withdraw_herbs_y):
    try:
        while True:
            # Clean herbs
            for (x, y) in herb_coords:
                click(x, y)
                time.sleep(random.uniform(0.1, 0.3))  # Add a small delay between clicks

            # Right-click on the Banker NPC
            right_click(bank_npc_x, bank_npc_y)
            time.sleep(random.uniform(0.7, 1))
            # Click 'Bank' to access the bank
            click(bank_click_x, bank_click_y)
            time.sleep(random.uniform(0.3, 0.7))  # Time to open bank and deposit items

            # Deposit inventory
            click(deposit_inventory_x, deposit_inventory_y)
            time.sleep(random.uniform(0.3, 0.6))

            # Right-click and withdraw 28 grimy herbs
            right_click(right_click_herbs_x, right_click_herbs_y)  # Right-click on grimy herbs in bank
            time.sleep(random.uniform(0.3, 0.8))
            click(withdraw_herbs_x, withdraw_herbs_y)  # Click 'Withdraw-28'
            time.sleep(random.uniform(0.3, 0.8))

            # Close bank window
            click(bank_close_x, bank_close_y)
            time.sleep(random.uniform(0.4, 0.9))

            # Add a delay to mimic human behavior, like inspecting the inventory
            time.sleep(random.uniform(1, 2))
    except KeyboardInterrupt:
        print("Script stopped by user.")

if __name__ == "__main__":
    # Replace these coordinates with the ones you recorded for each herb in your inventory
    herb_coords = [
        (1070, 1472),  # Coordinate of the first herb in inventory  x=1070, y=1472
        (1113, 1477),  # Coordinate of the second herb in inventory 1113, y=1477
        (1159, 1484),  # Coordinate of the third herb in inventory 1159, y=1484
        (1186, 1486),  # Coordinate of the fourth herb in inventory 1186, y=1486
        (1069, 1505),  # Coordinate of the fifth herb in inventory 1069, y=1505
        (1115, 1507),  # Coordinate of the sixth herb in inventory 1115, y=1507
        (1151, 1513),  # Coordinate of the seventh herb in inventory 1151, y=1513
        (1193, 1519),  # Coordinate of the eighth herb in inventory 1193, y=1519
        (1074, 1542),  # Coordinate of the ninth herb in inventory 1074, y=1542
        (1112, 1544),  # Coordinate of the tenth herb in inventory  1112, y=1544
        (1158, 1558),  # Coordinate of the eleventh herb in inventory 1158, y=1558
        (1191, 1557),  # Coordinate of the twelfth herb in inventory 1191, y=1557
        (1066, 1585),  # Coordinate of the thirteenth herb in inventory 1066, y=1585
        (1103, 1582),  # Coordinate of the fourteenth herb in inventory x=1103, y=1582
        (1141, 1587),  # Coordinate of the fiftenneth herb in inventory 1141, y=1587
        (1187, 1578),  # Coordinate of the sixteenth herb in inventory x=1187, y=1578
        (1068, 1621),  # Coordinate of the seventeenth herb in inventory x=1068, y=1621
        (1118, 1625),  # Coordinate of the eighteenth herb in inventory x=1118, y=1625
        (1150, 1625),  # Coordinate of the nineteenth herb in inventory x=1150, y=1625
        (1193, 1628),  # Coordinate of the twentieth eighteenth herb in inventory x=1193, y=1628
        (1065, 1660),  # Coordinate of the twenty first herb in inventory x=1065, y=1660
        (1100, 1661),  # Coordinate of the twenty-second herb in inventory x=1100, y=1661
        (1148, 1656),  # Coordinate of the twenty-third  herb in inventory x=1148, y=1656
        (1194, 1661),  # Coordinate of the twenty-fourth herb in inventory x=1194, y=1661
        (1062, 1689),  # Coordinate of the twenty-fifth herb in inventory x=1062, y=1689
        (1116, 1692),  # Coordinate of the twenty-sixth herb in inventory  x=1116, y=1692
        (1149, 1692),  # Coordinate of the twenty-seventh herb in inventory x=1149, y=1692
        (1201, 1698),  # Coordinate of the twenty-eight herb in inventory x=1201, y=1698
        
    ]

    # Replace these coordinates with the ones you recorded
    bank_npc_x, bank_npc_y = 667, 1415  # Coordinates of the Banker NPC
    bank_click_x, bank_click_y = 708, 1453  # Coordinates to click 'Bank' after right-clicking the Banker NPC
    deposit_inventory_x, deposit_inventory_y = 683, 1555  # Coordinates to click 'Deposit Inventory'
    bank_close_x, bank_close_y = 724, 1122  # Coordinates to close the bank window
    right_click_herbs_x, right_click_herbs_y = 616, 1413  # Coordinates to right-click grimy herbs in bank
    withdraw_herbs_x, withdraw_herbs_y = 616, 1488   # Coordinates to click 'Withdraw-28' for grimy herbs

    print("Starting Herb Cleaning bot in 5 seconds. Switch to RuneScape window.")
    time.sleep(5)
    clean_herbs(herb_coords, bank_npc_x, bank_npc_y, bank_click_x, bank_click_y, deposit_inventory_x, deposit_inventory_y, bank_close_x, bank_close_y, right_click_herbs_x, right_click_herbs_y, withdraw_herbs_x, withdraw_herbs_y)
