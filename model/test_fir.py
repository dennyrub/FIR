import random
from fir_model import fir_int, fir_float

# Тест 1: скользящее среднее, ступенька
h = [4096] * 8
x = [16384] * 8 + [0, 0]
print("Тест 1:", fir_int(x, h))

# Тест 2: одиночный импульс, на выходе должны получиться сами коэффициенты
h = [1000, 2000, 3000, 4000, 0, 0, 0, 0]
x = [32767, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Тест 2:", fir_int(x, h))

# Тест 3: насыщение
h = [32767] * 8
x = [32767] * 10
print("Тест 3:", fir_int(x, h))

# Тест 4: отрицательные числа
h = [4096] * 8
x = [-16384] * 8
print("Тест 4:", fir_int(x, h))

# Тест 5: float против int на случайном сигнале
random.seed(1)
x_int = [random.randint(-32768, 32767) for _ in range(1000)]
x_f = [v / 32768 for v in x_int]
c = 0.1
h_int = [round(c * 32768)] * 8
h_f = [c] * 8
y_int = fir_int(x_int, h_int)
y_f = fir_float(x_f, h_f)
print("Тест 5: макс. ошибка =", max(abs(a / 32768 - b) for a, b in zip(y_int, y_f)))
