def sum_negative_between_extremes(numbers):
    """Сумма отрицательных элементов между первым максимумом и минимумом."""
    if not numbers:
        raise ValueError("Массив не должен быть пустым")

    max_index = numbers.index(max(numbers))
    min_index = numbers.index(min(numbers))

    left, right = sorted((max_index, min_index))

    return sum(
        number
        for number in numbers[left + 1:right]
        if number < 0
    )


def main():
    try:
        numbers = list(map(
            int,
            input("Введите элементы массива через пробел: ").split()
        ))

        if not numbers:
            print("Ошибка: массив пуст.")
            return

        print("Исходный массив:", numbers)
        print("Максимальный элемент:", max(numbers))
        print("Минимальный элемент:", min(numbers))
        print(
            "Сумма отрицательных элементов между ними:",
            sum_negative_between_extremes(numbers)
        )

    except ValueError as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()
