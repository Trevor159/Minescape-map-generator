# todo: this is def just jank to test with, will be replaced
def block_from_tile(underlay_id: int, overlay_id: int) -> str:

    if overlay_id == 6:
        return "water"
    if overlay_id == 22:
        return "dirt"
    if overlay_id == 14:
        return "dirt"
    if overlay_id == 10:
        return "stone"
    if overlay_id == 5:
        return "planks" #todo dark oak or different type
    if overlay_id != 0:
        print("Overlay id not handled: " + str(overlay_id))
        return "stone"
    if underlay_id == 50:
        return "grass_block"
    if underlay_id == 48:
        return "grass_block"
    if underlay_id == 63:
        return "grass_block"
    if underlay_id == 64:
        return "grass_block"
    if underlay_id == 65:
        return "grass_block"
    if underlay_id != 0:
        print("Underlay id not handled: " + str(underlay_id))
    if underlay_id == 0:
        return None
    return "grass_block"
