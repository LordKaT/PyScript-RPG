from utils.yaml_loader import load_entity_from_yaml
from js import document, console
import asyncio, sys, traceback

async def run():
    document.getElementById("output").innerHTML += "<p><h3>Entity Test</h3></p>"
    document.getElementById("output").innerHTML += "<p>[START] Loading Entity...</p>"
    entity = await load_entity_from_yaml("data/entities/test/test_goblin.yaml")

    document.getElementById("output").innerHTML += "<p>[START] Loaded, running tests...</p>"
    try:
        assert entity.stats.get("hp") == 40
        assert entity.stats.get("max_hp") == 40
        assert entity.stats.get("tp") == 100
        assert entity.stats.get("max_tp") == 100
        assert entity.stats.get("strength") == 2
        assert entity.stats.get("agility") == 5
        assert entity.stats.modify("agility", 10) == 15
        assert entity.stats.set("intelligence", 2) == 2
        assert entity.stats.get("intelligence") == 2
        assert entity.stats.get("level") == 1
        assert entity.stats.set("level", 2) == 2
        assert entity.stats.derived()["tnl"] == 4500
        assert entity.stats.set("xp", 100) == 100
        assert entity.stats.derived()["tnl"] == 4400
        document.getElementById("output").innerHTML += f"<p>[PASS]</p>"
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        document.getElementById("output").innerHTML += f"<p>[FAIL] {entity.name} line {line}, {text}</p>"
