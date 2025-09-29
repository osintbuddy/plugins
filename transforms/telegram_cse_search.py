from osintbuddy import transform, Registry
from osintbuddy.plugins import TransformPayload


telegram_cse_urls = [
    "https://cse.google.com/cse?&cx=006368593537057042503:efxu7xprihg",
    "https://cse.google.com/cse?cx=004805129374225513871:p8lhfo0g3hg",
]


@transform(
  target="telegram_cse_search@1.0.0",
  label='To CSE Search',
  icon='search'
)
async def to_cse_search(self, entity):
    cse_search_transforms  = Registry.find_transforms('cse_search', '1.0.0')
    to_cse_results_fn = cse_search_transforms['to_cse_results']
    results = []
    print(entity)
    for url in telegram_cse_urls:
        cse_search_payload = TransformPayload(**{"query": entity.query, "cse_categories": url, "max_results": 100})
        results = results + await to_cse_results_fn(cse_search_payload)
    return results
