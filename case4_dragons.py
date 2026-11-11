def maximum_dragon_power(total_heads):
    """Находит максимальное произведение частей от 1 до 7."""
    if not isinstance(total_heads, int) or not 0 < total_heads < 100:
        raise ValueError("N должно быть целым числом от 1 до 99.")

    dp = [0] * (total_heads + 1)
    choice = [0] * (total_heads + 1)

    dp[0] = 1

    for current_sum in range(1, total_heads + 1):
        for heads in range(1, min(7, current_sum) + 1):
            candidate = dp[current_sum - heads] * heads

            if candidate > dp[current_sum]:
                dp[current_sum] = candidate
                choice[current_sum] = heads

    dragons = []
    remaining = total_heads

    while remaining > 0:
        heads = choice[remaining]

        if heads == 0:
            raise RuntimeError("Не удалось восстановить разбиение.")

        dragons.append(heads)
        remaining -= heads

    return dp[total_heads], dragons


def main():
    try:
        n = int(input("Введите количество голов N (1–99): "))

        power, dragons = maximum_dragon_power(n)

        print("Распределение голов:", dragons)
        print("Проверка суммы:", sum(dragons))
        print("Максимальная сила стаи:", power)

    except ValueError as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()
