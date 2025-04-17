# logic/stats.py

class Stats:
    def __init__(self, base_stats: dict = None) -> None:
        default_stats = {
            "hp": 10, "max_hp": 10,
            "tp": 0, "max_tp": 100,
            "strength": 0,
            "agility": 0,
            "dexterity": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0,
            "luck": 0
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
            "attack": s["strength"] * 2,
            "evasion": s["agility"] * 1.5,
            "crit_chance": s["dexterity"] + (s["luck"] * 0.5)
        }

    def as_dict(self):
        return self.stats.copy()
