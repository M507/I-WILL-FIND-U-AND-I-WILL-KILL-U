import pyautogui, os, time
def run():
    #in case full screen mode
    pyautogui.moveTo(980, 0, duration=0)
    time.sleep(0.15)
    #(980, 11)
    #(1151, 43)
    pyautogui.click(x=980, y=11, clicks=1, interval=0, button='left')
    pyautogui.click(x=1151, y=43, clicks=1, interval=0, button='left')
    pyautogui.click(x=650, y=650, clicks=1, interval=0, button='left')
    o_x,o_y = pyautogui.position()
    while True:
        x,y = pyautogui.position()

        # mouse
        if o_x != x or o_y != y:
            os.system("open kill.mp3")
            time.sleep(2)
            pyautogui.hotkey('command', 'shift','3')
            time.sleep(1)
            pyautogui.hotkey('command', 'ctrl','q')
            # pyautogui.hotkey('command', 'f')
            # time.sleep(1)
            # pyautogui.press('space')
            # time.sleep(7)
            # pyautogui.hotkey('command', 'ctrl','q')
            break
            #print(x,y)
def main():
    print("Run on a new terminal:")
    print("/Applications/iTunes.app/Contents/MacOS/iTunes")
    print("10 Seconds")
    time.sleep(10)
    run()

if __name__ == '__main__':
    main()
