from __future__ import annotations
from typing import List

def npv(rate: float, cashflows: List[float]) -> float:
    return sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cashflows))

def irr(cashflows: List[float], tol: float = 1e-6, max_iter: int = 100) -> float:
    # Bisection between -0.999 and 1.0 (100%); expand if needed
    low, high = -0.999, 1.0
    def f(r): return npv(r, cashflows)
    f_low, f_high = f(low), f(high)
    # Expand high if same sign
    while f_low * f_high > 0 and high < 10:
        high *= 2
        f_high = f(high)
    for _ in range(max_iter):
        mid = (low + high) / 2
        f_mid = f(mid)
        if abs(f_mid) < tol:
            return mid
        if f_low * f_mid < 0:
            high, f_high = mid, f_mid
        else:
            low, f_low = mid, f_mid
    return mid
