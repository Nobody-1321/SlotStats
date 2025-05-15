from .entity_register import EntityRegistry

def lg_one_more_coin():    
    bank = EntityRegistry.get("Bank")
    bank["credit"] += 1

def lg_one_less_coin():
    bank = EntityRegistry.get("Bank")
    bank["credit"] -= 1

