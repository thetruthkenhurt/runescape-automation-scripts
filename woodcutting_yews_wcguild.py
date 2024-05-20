import pyautogui
import time
import random
import cv2
import numpy as np
import keyboard
from PIL import ImageGrab

def click(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()

def check_image_presence(image_path, region, threshold=0.7):
    screen = np.array(ImageGrab.grab(bbox=region))
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image_path, 0)
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    if np.any(loc[0]):
        print(f"Image {image_path} found in region {region}")
        return True
    print(f"Image {image_path} not found in region {region}")
    return False

def chop_yew_logs(tree1_x, tree1_y, tree2_x, tree2_y, between_trees_x, between_trees_y, before_deposit_box_x, before_deposit_box_y, tree1_present_image, tree1_chopped_image, tree2_present_image, tree2_chopped_image, both_chopped_image, tree1_region, tree2_region, deposit_box_x, deposit_box_y, deposit_inventory_x, full_inventory_image, full_inventory_region):
    try:
        paused = False
        while True:
            # Check if the user pressed the 'p' key to pause or resume
            if keyboard.is_pressed('p'):
                paused = not paused
                if paused:
                    print("Script paused. Press 'p' again to resume.")
                else:
                    print("Resuming script.")
                time.sleep(1)  # Debounce delay to prevent multiple toggles

            if not paused:
                # Move to the space between the two yew trees and wait until character reaches trees
                click(between_trees_x, between_trees_y)
                time.sleep(random.uniform(6, 9))

                # Click on the first yew tree
                click(tree1_x, tree1_y)
                print("Clicked on the first tree.")

                # Wait for the first tree to be chopped down
                while check_image_presence(tree1_present_image, tree1_region):
                    print("First tree still present, waiting...")
                    time.sleep(5)  # Check every 5 seconds to see if the tree is still present

                print("First tree chopped down.")

                # Once the first tree is chopped down, check and chop the second tree
                while not check_image_presence(tree1_present_image, tree1_region):
                    click(tree2_x, tree2_y)
                    print("Clicked on the second tree.")
                    while check_image_presence(tree2_present_image, tree2_region):
                        print("Second tree still present, waiting...")
                        time.sleep(5)  # Check every 5 seconds to see if the second tree is still present

                print("Second tree chopped down.")

                # If both trees are chopped down, wait for any tree to respawn
                while not check_image_presence(tree1_present_image, tree1_region) and not check_image_presence(tree2_present_image, tree2_region):
                    print("Both trees are chopped down, waiting for respawn...")
                    time.sleep(1)  # Wait and check again

                # If inventory is full, go to deposit box
                if check_image_presence(full_inventory_image, full_inventory_region):
                    print("Inventory full, going to deposit box.")
                    # Move to position in front of the deposit box
                    click(before_deposit_box_x, before_deposit_box_y)
                    time.sleep(random.uniform(6, 9))  # Time to walk to the position

                    # Click to open the deposit box
                    click(deposit_box_x, deposit_box_y)
                    time.sleep(random.uniform(1, 2))  # Time to open the deposit box

                    # Deposit inventory
                    click(deposit_inventory_x, deposit_inventory_y)
                    time.sleep(random.uniform(0.5, 0.8))

    except KeyboardInterrupt:
        print("Script stopped by user.")

if __name__ == "__main__":
    # Replace these coordinates with the ones you recorded for the yew trees and deposit box
    tree1_x, tree1_y = 849, 1324  # Coordinates of the first yew tree x=849, y=1324
    tree2_x, tree2_y = 527, 1273  # Coordinates of the second yew tree
    between_trees_x, between_trees_y = 1170, 1169  # Coordinates of the space between the two yew trees x=1170, y=1169
    before_deposit_box_x, before_deposit_box_y = 592, 1208  # Coordinates for positioning in front of the deposit box x=592, y=1208
    deposit_box_x, deposit_box_y = 1226, 1205  # Coordinates of the deposit box on the minimap 1226 1205
    deposit_inventory_x, deposit_inventory_y = 557, 1399  # Coordinates to click 'Deposit Inventory' 557 1399

    # Image paths and regions for checking tree presence and full inventory
    tree1_present_image = 'yew1_present.png'
    tree1_chopped_image = 'yew1_chopped.png'
    tree2_present_image = 'yew2_present.png'
    tree2_chopped_image = 'yew2_chopped.png'
    both_chopped_image = 'both_chopped.png'
    tree1_region = (540, 1117, 1035, 1738)  # Adjust region based on tree location and new image sizes
    tree2_region = (316, 1106, 636, 1653)  # Adjust region based on tree location and new image sizes
    full_inventory_image = 'inventory_full.png'
    full_inventory_region = (1045, 1426, 1274, 1757)  # Adjust region based on your screen resolution and icon location

    print("Starting Yew Chopping bot in 5 seconds. Switch to RuneScape window.")
    time.sleep(5)
    chop_yew_logs(tree1_x, tree1_y, tree2_x, tree2_y, between_trees_x, between_trees_y, before_deposit_box_x, before_deposit_box_y, tree1_present_image, tree1_chopped_image, tree2_present_image, tree2_chopped_image, both_chopped_image, tree1_region, tree2_region, deposit_box_x, deposit_box_y, deposit_inventory_x, full_inventory_image, full_inventory_region)
