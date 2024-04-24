def task_1() -> None:

    a: int = 5
    b: float = 17.3
    c: str = 'home work №2'
    d: list = [1, 2, 3]
    e: bool = True

    var = [a, b, c, d, e]

    for elem in var:
        print(elem, "относится к типу", type(elem))


task_1()
print(" ")


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]  # эта последовательность является списком
    return print(a[0], a[1], a[2])


task_2()
print(" ")


def task_3(a: int) -> int:
    return a ** 2


print(task_3(5))

