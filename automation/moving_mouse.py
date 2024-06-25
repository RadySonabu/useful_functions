import pyautogui
import threading
import datetime

screenSize = pyautogui.size()


def move_mouse():
    pyautogui.moveTo(5, screenSize[1], duration=1)


def click_mouse():
    pyautogui.click()
    main()


def main():
    hour = datetime.datetime.now().hour
    if hour == 17 or hour == 12:
        print("end of day reached")
        quit()
    else:
        threading.Timer(5.0, move_mouse).start()
        threading.Timer(10.0, click_mouse).start()


main()
