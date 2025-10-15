import time
import matplotlib.pyplot as plt
from pathlib import Path
from problem3 import function_p3, estimate_ops_p3

def time_function(func, n: int) -> float:
    start = time.perf_counter(); func(n); end = time.perf_counter(); return end - start

def run_profile(ns, func, estimate_ops, safe_skip=True, max_ops=5e8, warmups=0):
    results = []
    for n in ns:
        est = estimate_ops(n)
        if safe_skip and est is not None and est > max_ops:
            results.append((n, None, est, "SKIPPED")); continue
        for _ in range(warmups): func(n)
        t = time_function(func, n)
        results.append((n, t, est, "OK"))
    return results

def main():
    ns = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]
    results = run_profile(ns, function_p3, estimate_ops_p3, safe_skip=True, max_ops=2e7)

    def fmt_time(t): return "" if t is None else f"{t:.6f}"
    print("n,tiempo_seg,ops_estimado,estado")
    for n, t, est, status in results:
        print(f"{n},{fmt_time(t)},{est},{status}")

    xs = [n for (n, t, _, s) in results if s == "OK"]
    ys = [t for (_, t, _, s) in results if s == "OK"]
    if xs:
        plt.figure()
        plt.plot(xs, ys, marker="o")
        plt.title("Problema 3 – Tamaño de input vs. tiempo (seg)")
        plt.xlabel("n"); plt.ylabel("tiempo (s)"); plt.grid(True)
        out_png = Path(__file__).with_name("p3_demo.png")   # GUARDA EN "Problem 3"
        plt.savefig(out_png, dpi=160, bbox_inches="tight")
        print(f"Gráfica guardada en: {out_png}")

if __name__ == "__main__":
    main()
