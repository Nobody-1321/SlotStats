import time
import random
import cv2 as cv

def lg_draw_highlighted_rectangle(img, points, rect_index, alpha=0.5):
    """Draw the highlighted rectangle with transparency."""
    overlay = img.copy()
    for j, point in enumerate(points):
        if j == rect_index:
            cv.rectangle(overlay, point[0], point[1], (0, 255, 0), -1)
    return cv.addWeighted(overlay, alpha, img, 1 - alpha, 0)

def lg_simulate_roulette(img, points, spins, spin_speed):
    """Simula la ruleta y al final parpadea el último resultado."""
    total_rectangulos = len(points)
    base_img = img.copy()
    total_steps = spins * total_rectangulos + random.randint(0, total_rectangulos - 1)
    last_index = 0

    for i in range(total_steps):
        img = base_img.copy()
        rect_index = i % total_rectangulos
        last_index = rect_index
        img = lg_draw_highlighted_rectangle(img, points, rect_index)
        cv.imshow("Roulette", img)
        cv.waitKey(1)
        if i > spins * total_rectangulos * 0.8:
            spin_speed += 0.02
        time.sleep(spin_speed)

    # Parpadeo del último resultado
    blink_times = 15
    for b in range(blink_times):
        img = base_img.copy()
        if b % 2 == 0:
            img = lg_draw_highlighted_rectangle(img, points, last_index, alpha=0.8)
        cv.imshow("Roulette", img)
        cv.waitKey(1)
        time.sleep(0.18)

def lg_idle_spin_animation(img, points, delay=0.1):
    """Animación de giro lento para modo inactivo."""
    total_rectangulos = len(points)
    base_img = img.copy()
    while True:
        for rect_index in range(total_rectangulos):
            img = base_img.copy()
            img = lg_draw_highlighted_rectangle(img, points, rect_index, alpha=0.5)
            cv.imshow("Roulette", img)
            if cv.waitKey(1) & 0xFF == 27:  # Salir con ESC
                return
            time.sleep(delay)

def lg_idle_blink_animation(img, points, blink_times=20, delay=0.15):
    """Animación de parpadeo aleatorio para modo inactivo."""
    total_rectangulos = len(points)
    base_img = img.copy()
    for _ in range(blink_times):
        rect_index = random.randint(0, total_rectangulos - 1)
        img = base_img.copy()
        img = lg_draw_highlighted_rectangle(img, points, rect_index, alpha=0.7)
        cv.imshow("Roulette", img)
        if cv.waitKey(1) & 0xFF == 27:
            return
        time.sleep(delay)