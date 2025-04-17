from logic.entity import Entity

entity = Entity(
    id="goblin_test",
    name="Test Goblin",
    tags=["npc", "goblin"],
    stats={
        "hp": 40,
        "max_hp": 40,
        "tp": 100,
        "max_tp": 100,
        "strength": 2,
        "agility": 5,
    },
    attributes={
        "size": "small",
        "color": "green"
    }
)

print("===ENTITY LIST===")
print(entity)

assert entity.get_stat("hp") == 40
assert entity.get_stat("max_hp") == 40
assert entity.get_stat("tp") == 100
assert entity.get_stat("max_tp") == 100
assert entity.get_stat("strength") == 2
assert entity.get_stat("agility") == 5
assert entity.modify_stat("agility", 10) == 12
assert entity.set_stat("intelligence", 2) == 2
assert entity.get_stat("intelligence") == 2

print("[PASS]")
