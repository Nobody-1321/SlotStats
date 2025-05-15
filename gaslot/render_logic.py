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
    
    if EntityRegistry.get("Bank")["credit"] <= 0:        
        lg_initialize_sound(EntityRegistry.get("Audio")["error"], volume=0.5, loop=0)
        lg_stop_sound(0.20)        

        return
    
    img = EntityRegistry.get("Image")
    audio = EntityRegistry.get("Audio")
    PointsBetsRec = EntityRegistry.get("PointsBetsRec")
    PointsBetsText = EntityRegistry.get("PointsBetsText")
    
    flag = lg_update_bet(key, bets)

    if not flag:
        lg_initialize_sound(audio["error"], volume=0.5, loop=0)
        lg_stop_sound(0.28)        
        return
    
    lg_initialize_sound( audio["coin"], volume=0.5, loop=0)
    
    dw_rectangle(img, list(PointsBetsRec[key])[0], list(PointsBetsRec[key])[1])
    dw_text(img, bets[key], PointsBetsText[key])
    
    lg_stop_sound(0.28)
    
    rd_update_credits("credit", op="less")

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

def rd_update_credits(key, op="add"):
    
    if key not in "credit":
        return
    
    img = EntityRegistry.get("Image")
    sounds = EntityRegistry.get("Audio")    
    PointsBankText = EntityRegistry.get("PointsBankText")
    PointsBankRec = EntityRegistry.get("PointsBankRec")    
    
    lg_initialize_sound(sounds["creditplus"], volume=0.5, loop=0)
    
    if op == "add":
        lg_one_more_coin()
    else:
        lg_one_less_coin()

    credits = EntityRegistry.get("Bank")["credit"]

    dw_rectangle(img, list(PointsBankRec[key])[0], list(PointsBankRec[key])[1])
    dw_text(img, credits, PointsBankText[key])
    
    lg_stop_sound(0.20)


    