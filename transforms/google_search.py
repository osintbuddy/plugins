import httpx
from osintbuddy.errors import PluginError

from osintbuddy import transform, Registry


def _parse_google_data(results) -> dict:
    stats = results.get("stats")
    related_searches = []
    result_stats = []
    if stats is not None:
        for stat in stats:
            if res := stat.get("result"):
                result_stats = result_stats + res
            if related := stat.get("related"):
                related_searches = related_searches + related
    output = []
    for key in list(results.keys()):
        if key is not None and key != "stats" and key != "questions":
            if results.get(key):
                for result in results.get(key):
                    search_result = {
                        "index": result.get("index"),
                        "title": result.get("title"),
                        "description": result.get("description"),
                        "url": result.get("link"),
                        "breadcrumb": result.get("breadcrumb"),
                        "question": result.get("question"),
                        "result_type": key,
                    }
                    output.append(search_result)
    return {
        "stats": result_stats,
        "related": related_searches,
        "results": output,
    }


@transform(
    target="google_result@1.0.0",
    label="To results"
)
async def to_google_results(entity):
    # print("@todo refactor transform entity API: ", entity)
    results = []
    google_result_entity = await Registry.get_plugin('google_result@1.0.0')
    for result in await search_google(entity.query, entity.pages):
        blueprint = google_result_entity.create(
            result={
                "title": result.get("title"),
                "subtitle": result.get("breadcrumb"),
                "text": result.get("description"),
            },
            url=result.get("url"),
        )
        results.append(blueprint)
    return results


async def search_google(query, pages):
    if not query:
        raise PluginError("Query is a required field")
    try:
        async with httpx.AsyncClient() as client:
            # TODO: Extract out searxng code for this
            google_results = []
    except PluginError:
        raise PluginError((
            "There was an error crawling Google. Please try again."
            "If you keep encountering this error please open an issue on Github."
        ))

    results = _parse_google_data(google_results)["results"]
    return results
