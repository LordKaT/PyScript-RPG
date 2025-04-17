from utils.yaml_loader import load_entity_from_yaml
from js import document
import asyncio

async def run():
    entity = await load_entity_from_yaml("data/entities/test/test_goblin.yaml")
    
    assert entity.stats.get("hp") == 40
    assert entity.stats.get("max_hp") == 40
    assert entity.stats.get("tp") == 100
    assert entity.stats.get("max_tp") == 100
    assert entity.stats.get("strength") == 2
    assert entity.stats.get("agility") == 5
    assert entity.stats.modify("agility", 10) == 15
    assert entity.stats.set("intelligence", 2) == 2
    assert entity.stats.get("intelligence") == 2

    document.getElementById("output").innerHTML += f"<p>[PASS] {entity.name} loaded and tested"
