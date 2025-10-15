# problem3.py — P3 Parte b
def function_p3(n: int) -> int:
    
    counter = 0
    i_max = n // 3
    for i in range(1, i_max + 1):
        j = 1
        while j <= n:
            counter += 1
            j += 4
    return counter

def estimate_ops_p3(n: int) -> int:
    # ≈ (n/3) * ceil(n/4)  ~ n^2/12
    if n <= 0:
        return 0
    return int((n/3) * ((n + 3)//4))
