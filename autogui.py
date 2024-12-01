"""pyautogui Module"""

import pyautogui

class AutoGUI():
    def get_size(self):
        """Obtains size of screen"""
        main_size = (2560, 1440)           #Size of your Main monitor
        current_size = pyautogui.size()    # Get the current size (1920, 1980)

        # Get the proportion of your main_size to the current_size
        prop = (current_size[0] / main_size[0], current_size[1] / main_size[1])

        # For Example your img is 100 x 100
        img = pyautogui.Image.open('ankidimentions.png')
        # Resize the image to (width=100px * 0.75, height=100px*0.75)
        # (Width = 75px, Height = 75px)
        resized_img = img.resize(img.size[0] * prop[0], img.size[1] * prop[1])
        # Saves the resized Image
        resized_img.save('resized_test.png')

    def move(self):
        """Moves mouse based on calculations"""
        current_size = self.get_size()
        pyautogui.moveTo(x, y, duration = length)

    def check_region(self):
        """"""
        pyautogui.screenshot(region=)