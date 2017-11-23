from scipy.stats import norm
import math


def fxoptionprice(s, k, rf, rd, vol, t, iscall):
    d1 = (math.log(s/k) + (rd-rf+vol**2/2)*t)/(vol*math.sqrt(t))
    d2 = d1-vol*math.sqrt(t)
    if iscall:
        price = s * math.exp(-rf * t) * norm.cdf(d1) - k * math.exp(-rd * t) * norm.cdf(d2)
    else:
        price = k * math.exp(-rd * t) * norm.cdf(-d2) - s * math.exp(-rf * t) * norm.cdf(-d1)
    return price
