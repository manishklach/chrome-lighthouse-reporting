
def generate_narrative(metrics, bottleneck):
    tbt = metrics.get("tbt")
    lcp = metrics.get("lcp")

    narrative = []
    narrative.append(f"Primary bottleneck detected: {bottleneck}.")

    if tbt:
        narrative.append(
            f"Total Blocking Time of {tbt:.0f} ms indicates sustained main-thread blocking."
        )

    if lcp:
        narrative.append(
            f"Largest Contentful Paint of {lcp/1000:.1f}s shows delayed primary content rendering."
        )

    return "\n".join(narrative)
