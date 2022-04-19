def max_difference(a: list[int]) -> tuple[int, int]:
    if len(a) == 1:
        return a[0], a[0]
    else:
        first = a[: len(a) // 2]
        second = a[len(a) // 2 :]

        small1, big1 = max_difference(first)
        small2, big2 = max_difference(second)

        minm_first = min(first)
        max_second = max(second)

        if big2 - small2 > max_second - minm_first and big2 - small2 > big1 - small1:
            return small2, big2
        elif big1 - small1 > max_second - minm_first:
            return small1, big1
        else:
            return minm_first, max_second


if __name__ == "__main__":
    import doctest

    doctest.testmod()