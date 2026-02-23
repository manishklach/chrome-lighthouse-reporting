
def detect_bottleneck(metrics):
    tbt = metrics.get("tbt") or 0
    lcp = metrics.get("lcp") or 0
    cls = metrics.get("cls") or 0

    if tbt > 2000:
        return "CPU / JavaScript Execution"
    elif lcp > 8000:
        return "Network / Asset Loading"
    elif cls > 0.25:
        return "Layout Instability"
    else:
        return "Balanced / No Dominant Bottleneck"
