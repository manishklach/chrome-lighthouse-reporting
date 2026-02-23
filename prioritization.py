
def prioritize_fixes(metrics):
    fixes = []

    if (metrics.get("tbt") or 0) > 2000:
        fixes.append(("P0", "Reduce JavaScript execution time"))

    if (metrics.get("lcp") or 0) > 4000:
        fixes.append(("P1", "Optimize LCP element loading"))

    if (metrics.get("speed_index") or 0) > 5000:
        fixes.append(("P2", "Improve rendering and hydration strategy"))

    return fixes
