from perceptron import perceptron

weights = [-2, -2]
bias = 3


def nand(value1: int, value2: int) -> int:
    return perceptron([value1, value2], weights, bias)


def test() -> None:
    assert nand(0, 0) == 1
    assert nand(0, 1) == 1
    assert nand(1, 0) == 1
    assert nand(1, 1) == 0


if __name__ == "__main__":
    test()
    print("NAND works")
