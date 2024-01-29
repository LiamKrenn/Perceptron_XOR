from nand import nand


def xor(value1: int, value2: int) -> int:
    nand1 = nand(value1, value2)
    nand2 = nand(value1, nand1)
    nand3 = nand(value2, nand1)
    return nand(nand2, nand3)


def test() -> None:
    assert xor(0, 0) == 0
    assert xor(0, 1) == 1
    assert xor(1, 0) == 1
    assert xor(1, 1) == 0


if __name__ == "__main__":
    test()
    print("XOR works")
