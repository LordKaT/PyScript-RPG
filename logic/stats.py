class Stats:
    def __init__(self, base_stats: dict = None) -> None:
        default_stats = {
            "hp": 10, "max_hp": 10,
            "mp": 0, "max_mp": 0,
            "tp": 0, "max_tp": 100,
            "strength": 5.0,
            "agility": 5.0,
            "dexterity": 5.0,
            "intelligence": 5.0,
            "wisdom": 5.0,
            "charisma": 5.0,
            "luck": 5.0,
            "level": 1,
            "xp": 0,
        }
        self.stats = default_stats if base_stats is None else {**default_stats, **base_stats}

    def get(self, stat: str = None) -> int:
        return self.stats.get(stat, 0)

    def set(self, stat: str = None, value: int = 0) -> int:
        self.stats[stat] = value
        return value

    def modify(self, stat: str = None, delta: int = 0):
        self.stats[stat] = self.get(stat) + delta
        return self.stats[stat]

    def derived(self) -> dict:
        s = self.stats
        return {
            "attack": (s["strength"] * 0.75) + (s["dexterity"] * 0.25),
            "ranged_attack": 0,
            "magic_attack": s["intelligence"] * 0.75,
            "defense": (s["strength"] * 0.25) + (s["agility"] * 0.75),
            "ranged_defense": 0,
            "magic_defense": 0,
            "accuracy": (s["agility"] * 0.55) + (s["dexterity"] * 0.55),
            "ranged_accuracy": 0,
            "magic_accuracy": 0,
            "addle": 0, # spellcast time modifier,
            "crit_chance": (s["luck"] * 0.25),
            "crit_damage": (s["strength"] * 0.15) + 2.0,
            "damage_modifier": 5,
            "evasion": (s["agility"] * 0.25) + (s["dexterity"] * 0.25),
            "ranged_evasion": 0,
            "magic_evasion": 0,
            "haste": 0,
            "enmity": 0,
            "healing_potency": 0, # regen modifier while healing
            "cure_potency": 0, # regen modifier for cure spells
            "speed": 0, # movement speed
            "tnl": ((s["level"] + 1) * 1500) - s["xp"]
        }

    def as_dict(self):
        return self.stats.copy()
