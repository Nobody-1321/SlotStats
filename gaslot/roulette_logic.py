import time
from .entity_register import EntityRegistry
import random
import pygame
import cv2 as cv

def lg_draw_highlighted_rectangle(img, points, rect_index, alpha=0.5):
    """Draw the highlighted rectangle with transparency."""
    overlay = img.copy()
    for j, point in enumerate(points):
        if j == rect_index:
            cv.rectangle(overlay, point[0], point[1], (0, 255, 0), -1)
    return cv.addWeighted(overlay, alpha, img, 1 - alpha, 0)

def lg_simulate_roulette(img, points, spins, spin_speed):
        
    total_rectangulos = len(points)
    base_img = img.copy()
    
    for i in range(spins * total_rectangulos + random.randint(0, total_rectangulos - 1)):
    
        img = base_img.copy()
        rect_index = i % total_rectangulos
        img = lg_draw_highlighted_rectangle(img, points, rect_index)

        cv.imshow("Roulette", img)
        cv.waitKey(1)

        # Aumentar la velocidad si está en las últimas vueltas
        if i > spins * total_rectangulos * 0.8:
            spin_speed += 0.02

        time.sleep(spin_speed)
    
