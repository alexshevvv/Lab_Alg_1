import time


def binary_search(arr, trg):
    rows, cols = len(arr), len(arr[0])

    for j in range(cols):
        left, right, mid = 0, rows - 1, 0
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][j] == trg:
                return True
            elif arr[mid][j] < trg:
                left = mid + 1
            else:
                right = mid - 1
    return False


def main():
    n = 2 ** 13
    target = 2 * n - 1  # для 1-х данных
    for idx in range(1, 14):
        m = 2 ** idx
        matrix = [[((n // m) * i + j) * 2 for j in range(m)] for i in range(n)]  # для 1-х данных

        # для подсчёта времени работы
        start_time = time.perf_counter()
        found = binary_search(matrix, target)
        end_time = time.perf_counter()

        # вывод времени для каждого зн-я i и m, где m = 2^i
        if found:
            print(f"idx = {idx}, M = {m} (2^{idx}) - True")
        else:
            print(f"idx = {idx}, M = {m} (2^{idx}) - False")

        time_ms = (end_time - start_time) * 1000
        print(f"Time taken: {time_ms:.3f} ms")

    # Дополнительная проверка - для разовых тестов на проверку содержания в матрице
    # искомого элемента, значение которого, рассчитал через заданную для данных формулу:

    # found = binary_search(matrix, target)
    # if found:
    #     print("True")
    # else:
    #     print("False")


if __name__ == "__main__":
    main()
