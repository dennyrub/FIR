import os, random
from fir_model import fir_int

# 1. Получаем абсолютный путь к папке, в которой лежит этот скрипт (FIR/model)
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Формируем путь к папке vectors (поднимаемся на уровень выше и заходим в vectors)
vectors_dir = os.path.join(script_dir, "..", "vectors")

# 3. Создаем папку
os.makedirs(vectors_dir, exist_ok=True)

# ... генерация x и y ...
random.seed(1)  # воспроизводимость
x = [random.randint(-32768, 32767) for _ in range(1000)]
x += [32767] * 10 + [-32768] * 10  # крайние значения
x += [0] * 10  # очистка окна

h = [32767] * 8  # Коэффициенты для теста насыщения!
y = fir_int(x, h)

# 4. Открываем файлы по абсолютному пути
with open(os.path.join(vectors_dir, "x.hex"), "w") as fx, open(
    os.path.join(vectors_dir, "y.hex"), "w"
) as fy:
    for xv, yv in zip(x, y):
        fx.write(f"{xv & 0xFFFF:04x}\n")
        fy.write(f"{yv & 0xFFFF:04x}\n")
print("записано отсчётов:", len(x))
