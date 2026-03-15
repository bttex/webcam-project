import subprocess
import pyautogui
import time


class GestureController:
    def __init__(self):
        self.last_gesture = None
        self.last_time = 0
        self.cooldown = 1.5

    def handle(self, gesture):

        now = time.time()

        if gesture == self.last_gesture and now - self.last_time < self.cooldown:
            return None

        self.last_gesture = gesture
        self.last_time = now

        if gesture == "PINCH":
            self.show_desktop()

        elif gesture == "GUN":
            self.open_steam()

        elif gesture == "PEACE":
            self.volume_down()

        elif gesture == "OPEN_HAND":
            self.volume_up()

        elif gesture == "FIST":
            self.exit_program()

        return None

    def open_steam(self):
        subprocess.Popen(r"C:\Program Files (x86)\Steam\Steam.exe")

    def volume_down(self):
        pyautogui.press("volumedown")

    def volume_up(self):
        pyautogui.press("volumeup")

    def show_desktop(self):
        pyautogui.hotkey("win", "d")

    def exit_program(self):
        print("Saindo do programa...")
        pyautogui.press("esc")
