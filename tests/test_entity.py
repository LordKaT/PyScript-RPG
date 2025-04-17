from utils.yaml_loader import load_entity_from_yaml
from js import console, document
import asyncio

async def run():
    entity = await load_entity_from_yaml("data/entities/tests/test_goblin.yaml")

    console.log("Loaded: ", entity)
    
    assert entity.get_stat("hp") == 40
    assert entity.get_stat("max_hp") == 40
    assert entity.get_stat("tp") == 100
    assert entity.get_stat("max_tp") == 100
    assert entity.get_stat("strength") == 2
    assert entity.get_stat("agility") == 5
    assert entity.modify_stat("agility", 10) == 15
    assert entity.set_stat("intelligence", 2) == 2
    assert entity.get_stat("intelligence") == 2
    
    document.getElementById("output").innerHTML += f"<p>[PASS] {entity.name} loaded and tested: {entity}"
