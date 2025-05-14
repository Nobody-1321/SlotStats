from .entity_register import EntityRegistry
import cv2 as cv

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
 
def dw_update_bet(key):
    
    bets = EntityRegistry.get("Bets")
    
    if key not in bets:
        return

    img = EntityRegistry.get("Image")
    PointsBetsText = EntityRegistry.get("PointsBetsText")
    PointsBetsRec  = EntityRegistry.get("PointsBetsRec")
    
    if bets[key] < 9:
        bets[key] += 1
        bets["total"] += 1
        cv.rectangle(img, list(PointsBetsRec[key])[0], list(PointsBetsRec[key])[1], (0, 0, 0), -1)
        cv.putText(img, str(bets[key]), PointsBetsText[key], cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
