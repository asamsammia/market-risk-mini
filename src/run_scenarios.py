
import csv, json, argparse, os

def load_positions(path):
    positions = []
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            row['qty'] = float(row['qty'])
            row['price'] = float(row['price'])
            positions.append(row)
    return positions

def load_scenario(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def apply_shock(positions, scenario):
    results = []
    base = scenario.get('price_shock_pct', 0.0)
    sector_over = scenario.get('sector_overrides', {})
    total_mv = 0.0
    total_pnl = 0.0
    for p in positions:
        mv = p['qty'] * p['price']
        shock = sector_over.get(p['sector'], base)
        new_price = p['price'] * (1.0 + shock)
        new_mv = p['qty'] * new_price
        pnl = new_mv - mv
        total_mv += mv
        total_pnl += pnl
        results.append({
            "position_id": p["position_id"],
            "instrument": p["instrument"],
            "sector": p["sector"],
            "mv_before": round(mv, 2),
            "mv_after": round(new_mv, 2),
            "pnl": round(pnl, 2)
        })
    summary = {
        "total_mv_before": round(total_mv, 2),
        "total_pnl": round(total_pnl, 2),
        "pnl_pct": round((total_pnl / total_mv) * 100.0, 2) if total_mv else 0.0
    }
    return results, summary

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--positions", default=os.path.join("..","data","sample_positions.csv"))
    ap.add_argument("--scenario", default=os.path.join("..","scenarios","base.json"))
    ap.add_argument("--out", default=os.path.join("..","outputs.csv"))
    args = ap.parse_args()

    positions = load_positions(args.positions)
    scenario = load_scenario(args.scenario)
    results, summary = apply_shock(positions, scenario)

    # print summary
    print("Scenario:", scenario.get("name","(unnamed)"))
    print("Summary:", summary)
    # write outputs
    with open(args.out, "w", newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=["position_id","instrument","sector","mv_before","mv_after","pnl"])
        w.writeheader()
        for r in results:
            w.writerow(r)
    print("Wrote:", args.out)

if __name__ == "__main__":
    main()
