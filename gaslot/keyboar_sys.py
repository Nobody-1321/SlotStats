from gaslot import EntityRegistry
import cv2 as cv

def get_keyboard_input():

    cvkey = cv.waitKey(1) & 0xFF 
    keyboard = EntityRegistry.get("Keyboard")

    for key, value in keyboard.items():
        if cvkey == value["key_code"]:
            return key
    
    return None
