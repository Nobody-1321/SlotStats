from .entity_register import EntityRegistry
from .draw_fn import *
from .bets_logic import *
from .roulette_logic import *

def rd_update_bet(key):

    bets = EntityRegistry.get("Bets")
    
    if key not in bets:
        return    
    
    img = EntityRegistry.get("Image")
    PointsBetsRec = EntityRegistry.get("PointsBetsRec")
    PointsBetsText = EntityRegistry.get("PointsBetsText")
    
    lg_update_bet(key, bets)
    dw_rectangle(key, img, list(PointsBetsRec[key])[0], list(PointsBetsRec[key])[1])
    dw_text(key, img, bets[key], PointsBetsText[key])

def rd_play_round(key):
    
    if key not in "play":
        return
    
    #only is there is one or more bets
    bets = EntityRegistry.get("Bets")
    
    if bets["total"] == 0:
        return

    img = EntityRegistry.get("Image")
    points = EntityRegistry.get("PointsRoulette")
    spins = EntityRegistry.get("CfgValRoul")["spins"]
    spin_speed = EntityRegistry.get("CfgValRoul")["spin_speed"]

    lg_simulate_roulette(img, points, spins, spin_speed)    
    dw_bets_to_cero()


    