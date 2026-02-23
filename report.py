
import argparse
from .lighthouse import parse_lighthouse
from .bottleneck import detect_bottleneck
from .prioritization import prioritize_fixes
from .narration import generate_narrative

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lighthouse", required=True)
    args = parser.parse_args()

    metrics = parse_lighthouse(args.lighthouse)
    bottleneck = detect_bottleneck(metrics)
    fixes = prioritize_fixes(metrics)
    narrative = generate_narrative(metrics, bottleneck)

    print("\n=== PERFORMANCE METRICS ===")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    print("\n=== PRIMARY BOTTLENECK ===")
    print(bottleneck)

    print("\n=== DIAGNOSTIC NARRATIVE ===")
    print(narrative)

    print("\n=== FIX PRIORITIES ===")
    for p, f in fixes:
        print(f"{p}: {f}")

if __name__ == "__main__":
    main()
