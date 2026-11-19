from collections import deque


def fir_int(x_int, h_int):
    # 1. Задаем maxlen - дек сам контролирует свой размер
    window = deque([0] * len(h_int), maxlen=len(h_int))
    result = []

    for x in x_int:
        if x < -32768 or x > 32767:
            raise ValueError(f"{x} Out of range!")

        # 2. Одной строчкой сдвигаем окно (автоматически удаляя последний элемент)
        window.appendleft(x)

        # 3. Красивое и быстрое попарное перемножение через zip() и sum()
        acc = sum(w * h for w, h in zip(window, h_int))

        # Фиксированная точка, округление и насыщение
        acc = (acc + 2**14) >> 15
        acc = max(-32768, min(32767, acc))

        result.append(acc)

    return result


def fir_float(x_int, h_int):
    window = deque([0] * len(h_int), maxlen=len(h_int))
    result = []

    for x in x_int:
        window.appendleft(x)
        acc = sum(w * h for w, h in zip(window, h_int))
        result.append(acc)

    return result


if __name__ == "__main__":

    a = [16384] * 8 + [0, 0]
    b = [4096] * 8

    print("Hardware calculation: ", fir_int(a, b))
    print("Math calculation: ", fir_float(a, b))
