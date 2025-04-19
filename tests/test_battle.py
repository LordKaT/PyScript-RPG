from utils.yaml_loader import load_entity_from_yaml
from logic.battle import Battle
from js import document
import copy, sys, traceback

async def run():
    document.getElementById("output").innerHTML += "<p><h3>Battle Test</h3></p>"
    document.getElementById("output").innerHTML += "<p>[START] Loading Entity...</p>"
    goblin = await load_entity_from_yaml("data/entities/test/test_goblin.yaml")
    goblin1 = copy.deepcopy(goblin)
    goblin2 = copy.deepcopy(goblin)

    goblin1.name = "Goblin One"
    goblin2.name = "Goblin Two"

    document.getElementById("output").innerHTML += "<p>[START] Loading Battle System...</p>"
    BattleSystem = Battle()

    document.getElementById("output").innerHTML += "<p>[START] Loaded, running tests...</p>"
    try:
        document.getElementById("output").innerHTML += "<p>"
        total = 0
        miss = 0
        no_damage = 0
        for _ in range(0, 1000):
            damage = BattleSystem.physical_attack(goblin1, goblin2)
            miss += 1 if damage[0] == "miss" else 0
            no_damage += 1 if damage[0] != "miss" and damage == 0 else 0
            total += damage[1]
            document.getElementById("output").innerHTML += f"{damage[1]}, "
        document.getElementById("output").innerHTML += "</p>"
        document.getElementById("output").innerHTML += f"<p>Avg: {total / 1000}<br />Miss: {miss} ({(miss / 1000) * 100}%)<br />No Dmg: {no_damage} ({(no_damage / 1000) * 100}%)</p>"

        assert BattleSystem.magic_attack(goblin1, goblin2, None) == 0
        assert BattleSystem.magic_attack(goblin2, goblin1, None) == 0
        document.getElementById("output").innerHTML += f"<p>[PASS]</p>"
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        document.getElementById("output").innerHTML += f"<p>[FAIL] line {line}, {text}</p>"
