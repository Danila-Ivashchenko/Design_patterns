from entity import Nomenclatura


def test_eq_1():
    pizza = Nomenclatura()
    pizza.title = "apple"

    apple = Nomenclatura()
    apple.title = "apple"

    assert not pizza == apple


def test_eq_2():
    pizza_1 = Nomenclatura()
    pizza_1.title = "pizza"

    pizza_2 = Nomenclatura()
    pizza_2.title = "pizza"

    assert not pizza_1 == pizza_2


def test_eq_3():
    pizza_1 = Nomenclatura()
    pizza_1.title = "pizza"

    pizza_2 = pizza_1

    assert pizza_1 == pizza_2

