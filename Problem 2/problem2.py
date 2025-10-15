# problem2.py  — P2 Parte b
def function_p2(n: int) -> int:
    
    if n <= 1:
        return 0
    counter = 0
    for i in range(1, n + 1):
        counter += 1  # simula la operación dentro del bucle antes del break
    return counter

def estimate_ops_p2(n: int) -> int:
    return max(0, n)
