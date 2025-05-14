from xml.etree.ElementTree import tostring
from requests import get
import cv2 as cv
import numpy as np
import random
import time

cv.setUseOptimized(True)

def load_image(filepath):
    """Load the image for the roulette."""
    return cv.imread(filepath)

def draw_highlighted_rectangle(img, points, rect_index, alpha=0.5):
    """Draw the highlighted rectangle with transparency."""
    overlay = img.copy()
    for j, point in enumerate(points):
        if j == rect_index:
            cv.rectangle(overlay, point[0], point[1], (0, 255, 0), -1)
    return cv.addWeighted(overlay, alpha, img, 1 - alpha, 0)

def simulate_roulette(img, points, vueltas, velocidad):
    """Simulate the roulette animation."""
    total_rectangulos = len(points)
    base_img = img.copy()

    for i in range(vueltas * total_rectangulos + random.randint(0, total_rectangulos - 1)):
        img = base_img.copy()
        rect_index = i % total_rectangulos
        img = draw_highlighted_rectangle(img, points, rect_index)

        cv.imshow("Roulette", img)
        cv.waitKey(1)

        if i > vueltas * total_rectangulos * 0.8:
            velocidad += 0.02

        time.sleep(velocidad)

def get_user_input(apuestas, img, config_values):
    
    key = cv.waitKey(1) & 0xFF  # Captura la tecla presionada

    if key == 49:  # 1
        if apuestas["limon"] < 9:
            apuestas["limon"] += 1
            apuestas["total"] += 1
            cv.rectangle(img, (1060, 190), (1095, 230), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["limon"]), (1070, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            config_values["render_img"] = True
      
    
    elif key == 50:  # 2
        if apuestas["manzana"] < 9:
            apuestas["manzana"] += 1
            apuestas["total"] += 1
            cv.rectangle(img, (1230, 190), (1265, 230), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["manzana"]), (1230, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            config_values["render_img"] = True
      
    
    elif key == 51:  # 3
        if apuestas["cereza"] < 9:
            apuestas["cereza"] += 1
            apuestas["total"] += 1
            cv.rectangle(img, (1380, 190), (1415, 230), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["cereza"]), (1390, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            config_values["render_img"] = True
      

    elif key == 52:  # 4
        if apuestas["sietes"] < 9:
            apuestas["sietes"] += 1
            apuestas["total"] += 1
            cv.rectangle(img, (1540, 190), (1575, 230), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["sietes"]), (1550, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            config_values["render_img"] = True
      
    elif key == 53:  # 5
        if apuestas["campana"] < 9:
            apuestas["campana"] += 1
            apuestas["total"] += 1
            cv.rectangle(img, (1700, 190), (1735, 230), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["campana"]), (1710, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            config_values["render_img"] = True
      
    elif key == 54:  # 6
        if apuestas["estrella"] < 9:
            apuestas["estrella"] += 1
            apuestas["total"] += 1
            cv.rectangle(img, (1060, 430), (1095, 470), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["estrella"]), (1070, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            config_values["render_img"] = True
      
    
    elif key == 55:  # 7
        if apuestas["naranja"] < 9:
            apuestas["naranja"] += 1
            apuestas["total"] += 1
            cv.rectangle(img, (1230, 430), (1265, 470), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["naranja"]), (1230, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            config_values["render_img"] = True
      
    
    elif key == 56:  # 8
        if apuestas["sandia"] < 9:
            apuestas["sandia"] += 1
            apuestas["total"] += 1
            cv.rectangle(img, (1380, 430), (1415, 470), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["sandia"]), (1390, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            config_values["render_img"] = True
             
    elif key == 57:  #9 
        if apuestas["bar"] < 9:
            apuestas["bar"] += 1
            apuestas["total"] += 1
            cv.rectangle(img, (1540, 430), (1575, 470), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["bar"]), (1550, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            
            cv.rectangle(img, (1700, 430), (1735, 470), (0, 0, 0), -1)
            cv.putText(img, str(apuestas["bar"]), (1710, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
            config_values["render_img"] = True
           
def dibujar_apuestas(img, apuestas):
    cv.putText(img, str(apuestas["limon"]), (1070, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv.putText(img, str(apuestas["manzana"]), (1230, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv.putText(img, str(apuestas["cereza"]), (1390, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv.putText(img, str(apuestas["sietes"]), (1550, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv.putText(img, str(apuestas["campana"]), (1710, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    
    cv.putText(img, str(apuestas["estrella"]), (1070, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv.putText(img, str(apuestas["naranja"]), (1230, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv.putText(img, str(apuestas["sandia"]), (1390, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv.putText(img, str(apuestas["bar"]), (1550, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv.putText(img, str(apuestas["bar"]), (1710, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

def resetar_apuesta_to_cero(apuestas, img):

    apuestas.update({key: 0 for key in apuestas})
    cv.rectangle(img, (1060, 190), (1095, 230), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["limon"]), (1070, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv.rectangle(img, (1230, 190), (1265, 230), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["manzana"]), (1230, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv.rectangle(img, (1380, 190), (1415, 230), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["cereza"]), (1390, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv.rectangle(img, (1540, 190), (1575, 230), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["sietes"]), (1550, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv.rectangle(img, (1700, 190), (1735, 230), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["campana"]), (1710, 220), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv.rectangle(img, (1060, 430), (1095, 470), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["estrella"]), (1070, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    
    cv.rectangle(img, (1230, 430), (1265, 470), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["naranja"]), (1230, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv.rectangle(img, (1380, 430), (1415, 470), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["sandia"]), (1390, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv.rectangle(img, (1540, 430), (1575, 470), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["bar"]), (1550, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv.rectangle(img, (1700, 430), (1735, 470), (0, 0, 0), -1)
    cv.putText(img, str(apuestas["bar"]), (1710, 460), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

def main():
    img = load_image("imgs/final_img.png")

    points = [
        ((50, 60), (190, 200)),
        ((190, 60), (330, 200)),
        ((330, 60), (455, 200)),
        ((455, 55), (585, 200)),
        ((585, 60), (710, 200)),
        ((710, 60), (840, 200)),
        ((840, 55), (980, 200)),
        ((830, 205), (980, 300)),
        ((830, 305), (980, 405)),
        ((830, 405), (980, 510)),
        ((830, 510), (980, 605)),
        ((830, 610), (980, 710)),
        ((840, 710), (980, 855)),
        ((710, 710), (841, 850)),
        ((580, 710), (710, 850)),
        ((460, 710), (585, 850)),
        ((325, 710), (455, 850)),
        ((190, 710), (325, 850)),
        ((50, 710), (190, 850)),
        ((50, 610), (200, 710)),
        ((50, 510), (200, 610)),
        ((50, 400), (200, 510)),
        ((50, 310), (200, 400)),
        ((50, 200), (200, 310)),
    ]

    gan_cre = {
        "ganancias": 0,
        "credito": 0,
    }
    
    apuestas = {
        "manzana": 0,
        "estrella": 0,
        "bar": 0,
        "sandia": 0,
        "campana": 0,
        "cereza": 0,
        "naranja": 0,
        "limon": 0,
        "sietes": 0,
        "total":0
    }
    
    config_values = {
        "vueltas": 3,
        "velocidad": 0.1,
        "render_img": True,
        "playing": False,
        "doblar": False,
    }

    playing = False
    doblar = False

    dibujar_apuestas(img, apuestas)
    
    img_c = img.copy()
    
    
    while True:      
        
        if config_values["render_img"]:
            cv.imshow("Roulette", img_c)
            redender_img = False

        get_user_input(apuestas, img_c, config_values)
        
        key = cv.waitKey(1) & 0xFF
        if key == 27:
            break     
        
        if key == 13:
            #debe haber almenos una apuesta
            if apuestas["total"] > 0:
                playing = True
                doblar = False 
        
        if key  == 100:
            if credito > 0:
                doblar = True

        if playing:
            simulate_roulette(img_c, points, config_values["vueltas"], config_values["velocidad"])
            resetar_apuesta_to_cero(apuestas, img_c)
            playing = False
           
    cv.destroyAllWindows()
        

if __name__ == "__main__":
    main()