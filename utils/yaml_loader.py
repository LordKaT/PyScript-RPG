import js, yaml
from logic.entity import Entity

async def load_entity_from_yaml(path):
    res = await js.fetch(path)
    text = await res.text()
    data = yaml.safe_load(text)

    console.log(data)

    return Entity(
        id=data["id"],
        name=data["name"],
        tags=data.get(["tags"], []),
        stats=data.get("stats", {}),
        attributes=data.get("attributes", {})
    )
