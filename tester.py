import math

# 피타고라스: a=3, b=4 의 빗변 c
a = 3
b = 4
c = math.hypot(a, b)  # sqrt(a*a + b*b)

# 원의 넓이: r = 10
r = 10
area = math.pi * r * r

print(f"c = {c}")
print(f"area = {area}")
