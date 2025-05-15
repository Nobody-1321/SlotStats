import cv2 as cv

def ut_exit(key):
    
    if key == "exit":
        cv.destroyAllWindows()
        exit(0)
