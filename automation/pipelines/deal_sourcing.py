import asyncio, json
from backend.app.services.scraper import fetch_html, parse_simple_tenders

SOURCES = [
    "https://www.gov.za/tenders",
    "https://www.treasury.gov.za/tenders/"
]

async def run():
    results = []
    for url in SOURCES:
        try:
            html = await fetch_html(url)
            items = parse_simple_tenders(html)
            for it in items:
                it["source"] = url
                results.append(it)
        except Exception as e:
            results.append({"source": url, "error": str(e)})
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    asyncio.run(run())
