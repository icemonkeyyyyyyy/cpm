def count_divisors(num: int):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 2
            if i == num // i:
                count -= 1
    return count


def numbers_with_4_divisors(a: int, b: int):
    numbers = []
    for num in range(a, b + 1):
        if count_divisors(num) == 4:
            numbers.append(num)
    numbers.sort(reverse=True)
    for num in numbers:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        print(f"Число: {num}\n"
              f"Делители: {divisors[::-1]}")


def main():
    try:
        a = int(input())
    except ValueError:
        print("Введите число. Например 5")
    else:
        try:
            b = int(input())
        except ValueError:
            print("Введите число. Например 5")
        finally:
            numbers_with_4_divisors(a, b)


if __name__ == '__main__':
    main()
