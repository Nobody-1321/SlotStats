import time
from .entity_register import EntityRegistry
import random
import pygame
import cv2 as cv

def draw_highlighted_rectangle(img, points, rect_index, alpha=0.5):
    """Draw the highlighted rectangle with transparency."""
    overlay = img.copy()
    for j, point in enumerate(points):
        if j == rect_index:
            cv.rectangle(overlay, point[0], point[1], (0, 255, 0), -1)
    return cv.addWeighted(overlay, alpha, img, 1 - alpha, 0)

def simulate_roulette():
        
    pygame.mixer.init()
    pygame.mixer.music.load("./music/level.mp3")
    pygame.mixer.music.play(-1)  # Reproducir en bucle

    """Simulate the roulette animation with FPS calculation."""
    # Obtener entidades necesarias
    img = EntityRegistry.get("Image")
    points = EntityRegistry.get("PointsRoulette")
    vueltas = EntityRegistry.get("CfgValRoul")["vueltas"]
    velocidad = EntityRegistry.get("CfgValRoul")["velocidad"]

    total_rectangulos = len(points)
    base_img = img.copy()

    # Variables para calcular FPS
    prev_time = time.time()

    for i in range(vueltas * total_rectangulos + random.randint(0, total_rectangulos - 1)):
        # Calcular FPS
        current_time = time.time()
        fps = int(1 / (current_time - prev_time))
        prev_time = current_time

        # Actualizar la imagen
        img = base_img.copy()
        rect_index = i % total_rectangulos
        img = draw_highlighted_rectangle(img, points, rect_index)

        # Mostrar FPS en la imagen
        cv.putText(img, f"FPS: {fps}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Mostrar la imagen actualizada
        cv.imshow("Roulette", img)
        cv.waitKey(1)

        # Aumentar la velocidad si está en las últimas vueltas
        if i > vueltas * total_rectangulos * 0.8:
            velocidad += 0.02

        time.sleep(velocidad)
    
    pygame.mixer.music.stop()  # Detener la música al finalizar
