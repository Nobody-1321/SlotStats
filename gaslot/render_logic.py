from .entity_register import EntityRegistry
from .draw_fn import *
from .bets_logic import *
from .roulette_logic import *
from .sound_logic import *
from .credit_logic import *

def rd_update_bet(key):
    
    bets = EntityRegistry.get("Bets")
    
    if key not in bets:
        return
    
    bets = EntityRegistry.get("Bets")
            
    img = EntityRegistry.get("Image")
    PointsBetsRec = EntityRegistry.get("PointsBetsRec")
    PointsBetsText = EntityRegistry.get("PointsBetsText")
        
    dw_rectangle(img, list(PointsBetsRec[key])[0], list(PointsBetsRec[key])[1])
    dw_text(img, bets[key], PointsBetsText[key])
    

def rd_play_round(key):
    
    if key not in "play":
        return
    
    bets = EntityRegistry.get("Bets")    
    if bets["total"] == 0:
        return

    img = EntityRegistry.get("Image")
    points = EntityRegistry.get("PointsRoulette")
    spins = EntityRegistry.get("CfgValRoul")["spins"]
    spin_speed = EntityRegistry.get("CfgValRoul")["spin_speed"]
    
    lg_initialize_sound(EntityRegistry.get("Audio")["roulette"], volume=0.5, loop=0)
    
    lg_simulate_roulette(img, points, spins, spin_speed)
    #lg_idle_blink_animation(img, points, 40, delay=0.15)
    
    lg_stop_sound(0.20)        
    dw_bets_to_cero()

def rd_update_credits(key):
    
    img = EntityRegistry.get("Image")
    sound = EntityRegistry.get("Audio")
    PointsBankText = EntityRegistry.get("PointsBankText")
    PointsBankRec = EntityRegistry.get("PointsBankRec")    
    if key == "credit":
        lg_initialize_sound(sound["creditplus"], volume=0.5, loop=0)
    
    credits = EntityRegistry.get("Bank")["credit"]
    dw_rectangle(img, list(PointsBankRec["credit"])[0], list(PointsBankRec["credit"])[1])
    dw_text(img, credits, PointsBankText["credit"])
    
    if key == "credit":
        lg_stop_sound(0.20)
    


    