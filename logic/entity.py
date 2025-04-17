from logic.stats import Stats

class Entity:
    def __init__(self, id: str = None, name: str = None, tags: list = [],
                 attributes: dict = None, stats: dict = None) -> None:

        self.id = id
        self.name = name
        self.tags = tags
        self.attributes = attributes
        self.stats = Stats(stats)
        self.attributes = attributes if attributes else {}

    def has_tag(self, tag: str = None) -> bool:
        return tag in self.tags
    
    def __repr__(self):
        return f"<Entity: {self.name} ({self.id}) | {self.stats['hp']}/{self.stats['max_hp']}, {self.stats['tp']}/{self.stats['max_tp']} | {self.tags} | {self.attributes}"
