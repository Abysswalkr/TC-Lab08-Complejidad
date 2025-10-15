# problem1.py  — P1 Parte b
def function_p1(n: int) -> int:

    counter = 0
    i_start = n // 2
    for i in range(i_start, n + 1):
        j_max = n - (n // 2)        # j <= n - n/2
        for j in range(1, j_max + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2
    return counter

def estimate_ops_p1(n: int) -> int:
    # ≈ (n/2)*(n/2)*log2(n) = n^2/4 * log2(n)
    import math
    return 0 if n <= 0 else int((n**2 / 4) * math.log2(max(2, n)))
