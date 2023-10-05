def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = 40 * r + (h - 40) * r * 1.5
    return pay

hours_input = input("Enter hours worked: ")
rate_input = input("Enter hourly rate: ")

try:
    h = float(hours_input)
    r = float(rate_input)
except ValueError:
    print("Please enter valid numeric input for hours and rate.")
    exit()

p = computepay(h,r)
print("Pay",p)
