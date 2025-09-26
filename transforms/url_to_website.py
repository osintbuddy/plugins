from urllib.parse import urlparse
from osintbuddy import transform, Registry


@transform(
    target="website@1.0.0",
    label="To website",
    icon="world-www"
)
async def to_website(self, entity):
    website_entity = await Registry.get_plugin('website')
    domain = urlparse(entity.url).netloc
    return website_entity.create(domain=domain)
