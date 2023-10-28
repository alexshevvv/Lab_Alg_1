import time


def exponent_acc(arr, i, j, n, trg):
    step = 1
    while i + step < n and arr[i + step][j] <= trg:
        step = step * 2

    start = i
    finish = min(i + (step // 2), n - 1)

    # применяем алгоритм бинарного поиска
    while start <= finish:
        mid = start + (finish - start) // 2
        if arr[mid][j] == trg:
            return mid
        elif arr[mid][j] < trg:
            start = mid + 1
        else:
            finish = mid - 1

    return start


def diagonal_search_exp(arr, trg):
    rows, cols = len(arr), len(arr[0])
    row, col = 0, cols - 1

    while 0 <= row < rows and 0 <= col < cols:
        if arr[row][col] == trg:
            return True
        elif arr[row][col] < trg:
            if row < rows - 2:
                row = exponent_acc(arr, row, col, rows, trg) # применяем экспоненциальное ускорение
            else:
                row += 1
        else:
            col -= 1

    return False


def main():
    n = 2 ** 13
    target = 2 * n - 1 # для 1-х данных
    # для 2-x: target = 16 * n - 1
    for idx in range(1, 14):
        m = 2 ** idx
        matrix = [[((n // m) * i + j) * 2 for j in range(m)] for i in range(n)] # для 1-х данных
        # для 2-x: matrix = [[((n // m) * i * j) * 2 for j in range(m)] for i in range(n)]

        # для подсчёта времени работы
        start_time = time.time()
        found = diagonal_search_exp(matrix, target)
        end_time = time.time()

        # вывод времени для каждого зн-я i и m, где m = 2^i
        if found:
            print(f"idx = {idx}, m = {m} (2^{idx}) - True")
        else:
            print(f"idx = {idx}, m = {m} (2^{idx}) - False")

        time_ms = (end_time - start_time) * 1000
        print(f"Time taken: {time_ms:.2f} ms")

    # found = diagonal_search_exp(matrix, target)
    # if found:
    #     print("True")
    # else:
    #     print("False")


if __name__ == "__main__":
    main()
