class Entity:
    def __init__(self, id: str = None, name: str = None, tags: list = [],
                 attributes: dict = None, stats: dict = None) -> None:

        default_stats = {
            "hp": 10,
            "max_hp": 10,
            "tp": 10,
            "max_tp": 10,
            "strength": 0,
            "agility": 0,
            "dexterity": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0,
            "luck": 0
        }

        self.id = id
        self.name = name
        self.tags = tags
        self.attributes = attributes
        self.stats = default_stats if stats is None else {**default_stats, **stats}
        self.attributes = attributes if attributes else {}

    def has_tag(self, tag: str = None) -> bool:
        return tag in self.tags

    def modify_stat(self, stat: str = None, amount: int = 0) -> int:
        if stat in self.stats:
            self.stats[stat] += amount
            return self.stats[stat]
        else:
            return -1
    
    def get_stat(self, stat: str = None) -> int:
        return self.stats.get(stat, None)
    
    def set_stat(self, stat: str = None, amount: int = 0) -> int:
        if stat in self.stats:
            self.stats[stat] = amount
            return self.stats[stat]
        else:
            return -1
    
    def __repr__(self):
        return f"<Entity: {self.name} ({self.id}) | {self.stats['hp']}/{self.stats['max_hp']}, {self.stats['tp']}/{self.stats['max_tp']} | {self.tags} | {self.attributes}"
