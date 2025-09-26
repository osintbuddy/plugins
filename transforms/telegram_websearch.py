from osintbuddy import transform, Registry

@transform(
  target="telegram_websearch@1.0.0",
  label='To CSE Search',
  icon='search'
)
async def to_websearch(self, entity):
    print("ENTITY TO WEBSEARCH",  entity)
    cse_search_entity = await Registry.get_plugin('cse_search')
    cse_plugin = cse_search_entity()
    results = []
    for url in self.telegram_cse_urls:
        resp = await cse_plugin.get_cse_results(query=entity.query, url=url)
        results.append(await cse_plugin._map_cse_to_blueprint(resp=resp))
    return [result for cse_page in results for result in cse_page]
