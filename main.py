from turtle import up
import cv2 as cv
import numpy as np
import os 
import gaslot 

                           
def main():
    
    Base_dir = os.path.dirname(os.path.abspath(__file__))
    coin_path = os.path.join(Base_dir, "audio", "coin.mp3")

    img = cv.imread("imgs/final_img.png")

    gaslot.EntityRegistry.register("Image", img)

    gaslot.EntityRegistry.register("PointPayoutsText", {
        "limon": (1070, 60),
        "manzana": (1230, 60),
        "cereza": (1390, 60),
        "sietes": (1550, 60),
        "campana": (1710, 60),
        "estrella": (1070, 300),
        "naranja": (1230, 300),
        "sandia": (1390, 300),
        "bar50": (1550, 300),
        "bar100": (1710, 300),
    })

    gaslot.EntityRegistry.register("Payouts", {
        "limon": 15,
        "manzana": 5,
        "cereza": 2,
        "sietes": 40,
        "campana": 20,
        "estrella": 30,
        "naranja": 10,
        "sandia": 15,
        "bar50": 50,
        "bar100": 100
    })

    gaslot.EntityRegistry.register("PointsRoulette", [
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
    ])

    gaslot.EntityRegistry.register("Bank", {
        "winnings": 0,
        "credit": 0,
    })

    gaslot.EntityRegistry.register("PointsBankText", {
        "credit": (1240, 590),
        "winnings": (1500, 590),
    })

    gaslot.EntityRegistry.register("PointsBankRec", {
        "credit": {(1200, 565), (1340, 620)},
        "winnings": {(1450, 565), (1590, 620)},
    })

    gaslot.EntityRegistry.register("CfgValRoul", {
        "spins": 3,
        "spin_speed": 0.01,
    })
  
    gaslot.EntityRegistry.register("Keyboard", {
    "limon": {"key_code": 49, "active": False},  # 1
    "manzana": {"key_code": 50, "active": False},  # 2
    "cereza": {"key_code": 51, "active": False},  # 3
    "sietes": {"key_code": 52, "active": False},  # 4
    "campana": {"key_code": 53, "active": False},  # 5
    "estrella": {"key_code": 54, "active": False},  # 6
    "naranja": {"key_code": 55, "active": False},  # 7
    "sandia": {"key_code": 56, "active": False},  # 8
    "bar": {"key_code": 57, "active": False},  # 9
    "double": {"key_code": 100, "active": False},  # d
    "play": {"key_code": 13, "active": False},  # enter
    "exit": {"key_code": 27, "active": False},  # esc
    "credit": {"key_code": 99, "active": False},  # c
})

    gaslot.EntityRegistry.register("Bets", {
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
    })

    gaslot.EntityRegistry.register("PointsBetsRec", {
        "limon": {(1060, 190), (1095, 230)},
        "manzana": {(1230, 190), (1265, 230)},
        "cereza": {(1380, 190), (1415, 230)},
        "sietes": {(1540, 190), (1575, 230)},
        "campana": {(1700, 190), (1735, 230)},
        "estrella": {(1060, 430), (1095, 470)},
        "naranja":  {(1230, 430), (1265, 470)},
        "sandia": {(1380, 430), (1415, 470)},
        "bar": {(1600, 430), (1655, 470)},
    })

    gaslot.EntityRegistry.register("PointsBetsText", {
        "limon": (1070, 220),
        "manzana": (1230, 220),
        "cereza": (1390, 220),
        "sietes": (1550, 220),
        "campana": (1710, 220),
        "estrella": (1070, 460),
        "naranja": (1230, 460),
        "sandia": (1390, 460),
        "bar": (1630, 460),
    })
    
    gaslot.EntityRegistry.register("Audio", {
        "coin": os.path.join(Base_dir, "audio", "coin.mp3"),
        "error": os.path.join(Base_dir, "audio", "error.mp3"),
        "creditplus": os.path.join(Base_dir, "audio", "creditplus.mp3"),
    })

    gaslot.dw_payouts()
    gaslot.dw_bets_to_cero()
    gaslot.dw_update_credits_winnings_to_cero()
    
    imgr = gaslot.EntityRegistry.get("Image")
   
    while True:
        
        cv.imshow("Roulette", imgr)    
        key = gaslot.get_keyboard_input()
        
        if key is not None:

            gaslot.rd_update_bet(key)
            gaslot.rd_play_round(key)
            gaslot.rd_update_credits(key)
            
            if key == "exit":
                break
    
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()