# 모듈 == 파이썬 파일

# import calc_add

# result = calc_add.calc_add(10, 20)
# print(result)

# import random

# print(random.randint(1, 2))

from calc_add import calc_add

calc1 = calc_add()
calc2 = calc_add()
print(calc1)
print("calc1", calc1(1))
print("calc1", calc1(1))
print("calc1", calc1(1))
print("calc2", calc2(10))
print("calc2", calc2(10))
print("calc2", calc2(10))