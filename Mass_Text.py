import pyautogui
import time
import os




#====================    MASS TEXT    ====================#



recipients = ["2024561111","0668139289","3045862118"]     # replace with numbers you need to text
home_dir = os.path.expanduser('~')
file_path1 = os.path.join(home_dir, 'Mass_Text', 'open_phone_link.png')
file_path2 = os.path.join(home_dir, 'Mass_Text', 'new_message.png')   



def mass_text(recipients):

    try:
        os.system("start ms-settings:mobile-devices")

        time.sleep(1)

        open_phone_link = pyautogui.locateOnScreen(file_path1)
        pyautogui.click(open_phone_link)

        time.sleep(6)

        for name in recipients:
            new_message = pyautogui.locateOnScreen(file_path2)
            pyautogui.click(new_message)
            time.sleep(1)
            pyautogui.write(name)
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.hotkey('ctrl','v')
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)

        time.sleep(1)

    except pyautogui.ImageNotFoundException:
        print("a page was not given enough time to load")



mass_text(recipients=recipients)