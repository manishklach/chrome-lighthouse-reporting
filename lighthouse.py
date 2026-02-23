
import json

def parse_lighthouse(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    root = data.get("lighthouseResult", data)

    audits = root.get("audits", {})
    categories = root.get("categories", {})

    def val(key):
        return audits.get(key, {}).get("numericValue")

    return {
        "performance_score": categories.get("performance", {}).get("score"),
        "fcp": val("first-contentful-paint"),
        "lcp": val("largest-contentful-paint"),
        "tbt": val("total-blocking-time"),
        "tti": val("interactive"),
        "cls": val("cumulative-layout-shift"),
        "speed_index": val("speed-index"),
    }
