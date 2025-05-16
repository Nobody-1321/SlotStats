from .entity_register import EntityRegistry
from .sound_logic import *

def lg_update_bet(key):
    
    bets = EntityRegistry.get("Bets")

    if key not in bets:
        return False
    
    if EntityRegistry.get("Bank")["credit"] <= 0:        
        lg_initialize_sound(EntityRegistry.get("Audio")["error"], volume=0.5, loop=0)
        lg_stop_sound(0.20)        
        return False

    if bets[key] < 9:
        lg_initialize_sound(EntityRegistry.get("Audio")["coin"], volume=0.5, loop=0)
        
        bets[key] += 1
        bets["total"] += 1
        EntityRegistry.get("Bank")["credit"] -= 1
        
        lg_stop_sound(0.20)        
        return True
    
    lg_initialize_sound(EntityRegistry.get("Audio")["error"], volume=0.5, loop=0)
    lg_stop_sound(0.20)        
        
    return False