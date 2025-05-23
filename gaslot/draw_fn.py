from .entity_register import EntityRegistry
import cv2 as cv

def dw_rectangle(img, point1, point2):
    cv.rectangle(img, point1, point2, (0, 0, 0), -1)
    
def dw_text(img, text, point):
    cv.putText(img, str(text), point, cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

def dw_payouts():
    Payouts = EntityRegistry.get("Payouts")
    PointPayouts = EntityRegistry.get("PointPayoutsText")
    img = EntityRegistry.get("Image")

    for key, value in Payouts.items():
        if key in PointPayouts:
            cv.putText(img, str(value), PointPayouts[key], cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
 
def dw_bets_to_cero():
    
    for k in EntityRegistry.get("Bets"):
        EntityRegistry.get("Bets")[k] = 0
        
    EntityRegistry.get("Bets")["total"] = 0
    
    img = EntityRegistry.get("Image")
    
    PointsBetsText = EntityRegistry.get("PointsBetsText")
    PointsBetsRec  = EntityRegistry.get("PointsBetsRec")
    
    for key, value in PointsBetsText.items():
        cv.rectangle(img, list(PointsBetsRec[key])[0], list(PointsBetsRec[key])[1], (0, 0, 0), -1)
        cv.putText(img, str(0), PointsBetsText[key], cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
 

def dw_update_credits_winnings_to_cero():
    
    img = EntityRegistry.get("Image")
    bank = EntityRegistry.get("Bank")
    
    PointsBankText = EntityRegistry.get("PointsBankText")
    PointsBankRec  = EntityRegistry.get("PointsBankRec")
    
    cv.rectangle(img, list(PointsBankRec["credit"])[0], list(PointsBankRec["credit"])[1], (0, 0, 0), -1)
    cv.putText(img, str(bank["credit"]), PointsBankText["credit"], cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    
    cv.rectangle(img, list(PointsBankRec["winnings"])[0], list(PointsBankRec["winnings"])[1], (0, 0, 0), -1)
    cv.putText(img, str(bank["winnings"]), PointsBankText["winnings"], cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)