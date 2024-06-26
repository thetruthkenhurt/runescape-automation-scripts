# RuneScape Bot Scripts

I spent some of my free time using Old School Runescape, a game which I have enjoyed in my childhood as a base for practicing my scripting skills. 
This repository contains several scripts I have written to have automate certain repetitive tasks.
These scripts were written for self-learning purposes and are not intended to encourage breaking the RuneScape Terms of Service.

## Scripts

### 1. Battlestaff Script
**File**: `battlestaff_script.py`

This script automates the process of crafting battlestaves by combining elemental orbs with battlestaves.
Note that only the two inventory slots highlighted (refer to image) will be acted upon by script.
Please ensure that your materials are placed in the following bank slots as shown in the image below:
![Bank Slots Setup](https://github.com/thetruthkenhurt/runescape-automation-scripts/blob/master/script%20item%20slots.png)
Your character will be standing on the tile beside the 2nd banker on the western counter at GE.
### 2. Herb Cleaning Script
**File**: `herb_cleaning.py`

This script automates the process of cleaning grimy herbs in your inventory.
Like previously, your character will be standing on the tile beside the 2nd banker on the western counter at GE.

### 3. Woodcutting Yews Script
**File**: `woodcutting_yews_wcguild.py`

This script automates the process of chopping yew trees and banking the logs in the Woodcutting Guild and uses OpenCV to visualize the condition of trees as a script condition. Note that this particular script is still a work in progress and only the specific spot documented in the screenshots are supported at the moment. Please upload your own screenshots to your local directory to allow for the most accurate image recognition.
#### Example Images:
- **Yew Tree Present**:
  ![Yew Tree Present](https://github.com/thetruthkenhurt/runescape-automation-scripts/blob/master/yew1_present.png)
- **Yew Tree Chopped**:
  ![Yew Tree Chopped](https://github.com/thetruthkenhurt/runescape-automation-scripts/blob/master/yew1_chopped.png)
## Disclaimer

These scripts were created to document my self-learning in scripting and automation. They are not intended for actual use in OSRS and may violate the game's Terms of Service (ToS). Using these scripts in the game can result in a ban or other penalties. I do not encourage the use of these or any other scripts that automate gameplay in RuneScape, Old School Runescape or any other online game.

## Usage

To use these scripts, follow these steps:
1. Ensure you have Python installed on your machine.
2. Install the required dependencies:
    ```sh
    pip install pyautogui opencv-python numpy keyboard pillow
    ```
3. Run the desired script:
    ```sh
    python battlestaff_script.py
    ```

## Learning and Documentation

These scripts are part of my journey to learn Python and automation. Feel free to use them as a reference for your own learning purposes.

