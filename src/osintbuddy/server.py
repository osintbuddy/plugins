import sys, os
from types import NoneType
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from osintbuddy import __version__, Use, Registry
from osintbuddy.plugins import load_plugins
from osintbuddy.utils import to_snake_case
from osintbuddy.utils.deps import get_driver

load_plugins()
app = FastAPI(title=f"OSINTBuddy Plugins v{__version__}")


class EntityCreate(BaseModel):
    id: int
    label: str = None
    author: str = "Unknown author"
    description: str = "No description found..."
    last_edit: str
    source: str | None


@app.get("/entities")
async def get_entities():
    entities = []
    for idx, plugin in enumerate(Registry.plugins):
        file = sys.modules[plugin.__module__].__file__ 
        file_entity = EntityCreate(
                label=plugin.label,
                author=plugin.author,
                description=plugin.description,
                last_edit=datetime.utcfromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S'),
                id=idx,
                source=open(sys.modules[plugin.__module__].__file__, "r").read()
        )
        entities.append(file_entity)
    return entities


@app.get("/entities/{hid}")
async def get_entity_source(hid: str):
    for idx, plugin in enumerate(Registry.plugins):
        if str(idx) == hid:
            file = sys.modules[plugin.__module__].__file__ 
            source = open(file).read()
            entity = EntityCreate(
                id=idx,
                label=plugin.label,
                author=plugin.author,
                description=plugin.description,
                last_edit=datetime.utcfromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S'),
                source=source
            )
            return entity
    return []


@app.get("/refresh")
async def reload_entities(blueprints: bool = False):
    Registry.labels.clear()
    Registry.plugins.clear()
    Registry.ui_labels.clear()
    load_plugins()
    return Registry.ui_labels


@app.get("/blueprint")
async def get_entity_blueprint(label: str):
    if label == '_osib_all':
        plugins = [await Registry.get_plugin(to_snake_case(label)) 
                   for label in Registry.labels]
        return [p.create() for p in plugins]
    plugin = await Registry.get_plugin(label)
    return plugin.create() if plugin else []


@app.get("/transforms")
async def get_entity_transforms(label: str):
    plugin = await Registry.get_plugin(label)
    if not isinstance(plugin, NoneType):
        return plugin().transform_labels
    return []


@app.post("/transforms")
async def run_entity_transform(context: dict):
    plugin = await Registry.get_plugin(context['data'].get("label"))
    if not isinstance(plugin, NoneType):
        transform_result = await plugin().run_transform(
            transform_type=context.get("transform"),
            entity=context,
            use=Use(get_driver=get_driver)
        )
        return transform_result
    return []
