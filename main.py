import cv2 as cv
import numpy as np
import random
import time

def main():
    img = cv.imread("final_img.png")
    
    
    points = [
        ((50, 60), (190, 200)),
        ((190, 60), (330, 200)),
        ((330, 60), (455, 200)),
        ((455, 55), (585, 200)),#4
        ((585, 60), (710, 200)), #5
        ((710, 60), (840, 200)),#6
        ((840, 55), (980, 200)),#7
        ((830, 205), (980, 300)),#8
        ((830, 305), (980, 405)),#9
        ((830, 405), (980, 510)),#10
        ((830, 510), (980, 605)),#11
        ((830, 610), (980, 710)),#12
        ((840, 710), (980, 855)),#13
        ((710, 710), (841, 850)),#14
        ((580, 710), (710, 850)),#15
        ((460, 710), (585, 850)),#16
        ((325, 710), (455, 850)),#17
        ((190, 710), (325, 850)),#18
        ((50, 710), (190, 850)),#19
        ((50, 610), (200, 710)),#20
        ((50, 510), (200, 610)),#21
        ((50, 400), (200, 510)),#22
        ((50, 310), (200, 400)),#23
        ((50, 200), (200, 310)),#24
    ]

    # Number of spins and initial speed
    vueltas = 3
    velocidad = 0.1  # Time between illuminations (seconds)

    # Total number of rectangles
    total_rectangulos = len(points)

    print(f"Total rectangles: {total_rectangulos}") 

    # Create a copy of the original image
    base_img = img.copy()

    # Simulate the roulette
    for i in range(vueltas * total_rectangulos + random.randint(0, total_rectangulos - 1)):
        # Restore the base image
        img = base_img.copy()

        # Create an overlay layer
        overlay = img.copy()

        # Calculate the index of the current rectangle
        rect_index = i % total_rectangulos

        # Draw all rectangles
        for j, point in enumerate(points):
            if j == rect_index:
                # Highlight the current rectangle with transparency (green color)
                cv.rectangle(overlay, point[0], point[1], (0, 255, 0), -1)

        # Apply transparency to the highlighted rectangle
        alpha = 0.5  # Transparency level (0.0 to 1.0)
        img = cv.addWeighted(overlay, alpha, img, 1 - alpha, 0)

        # Display the image
        cv.imshow("Roulette", img)
        cv.waitKey(1)

        # Gradually reduce the speed at the end
        if i > vueltas * total_rectangulos * 0.8:
            velocidad += 0.02

        # Wait before illuminating the next rectangle
        time.sleep(velocidad)

    # Display the final highlighted rectangle
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()