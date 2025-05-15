import re
from .entity_register import EntityRegistry

def lg_update_bet(key, bets):

    if bets[key] < 9:
        bets[key] += 1
        bets["total"] += 1
        return True
        
    return False