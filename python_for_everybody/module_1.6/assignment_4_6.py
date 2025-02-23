def computepay(h, r):
    if h > 40:
        ot = (h - 40) * (r * 1.5)
        rt = 40 * r
        pay = ot + rt
    else:
        pay = r * h
    
    return pay

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

p = computepay(h, r)
print("Pay", p)