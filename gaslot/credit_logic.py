from .entity_register import EntityRegistry

def lg_credit(key):
    
    if key not in "credit":
        return

    bank = EntityRegistry.get("Bank")
    bank["credit"] += 1
