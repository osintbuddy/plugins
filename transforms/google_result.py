from osintbuddy import transform, Registry
from urllib.parse import urlparse


@transform(
    target="google_result@1.0.0",
    label="To website",
    icon="world"
)
async def to_website(self, entity):
    website_entity = await Registry.get_plugin('website@1.0.0')
    blueprint = website_entity.create(
        domain=urlparse(entity.url).netloc
    )
    return blueprint

