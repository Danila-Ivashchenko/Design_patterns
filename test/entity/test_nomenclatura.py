from src.core.domain.entity.nomenclature import Nomenclature
from src.infrastructure.data.generator.measurement_unit import MeasurementUnitGenerator
from src.infrastructure.data.generator.nomenclature_group import NomenclatureGroupGenerator

group_gen = NomenclatureGroupGenerator()
unit_gen = MeasurementUnitGenerator()

def test_eq_1():

    group = group_gen.food
    unit = unit_gen.thing

    apple_1 = Nomenclature("apple", group.id, unit)
    apple_1.title = "apple"

    apple_2 = Nomenclature("apple", group.id, unit)
    apple_2.title = "apple"

    assert not apple_1 == apple_2


def test_eq_2():
    group = group_gen.food
    unit = unit_gen.thing

    apple_1 = Nomenclature("apple 1", group.id, unit)

    apple_2 = Nomenclature("apple 2", group.id, unit)

    assert not apple_1 == apple_2



