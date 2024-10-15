
import unittest as un

from src.infrastructure.data.generator.nomenclature_group import NomenclatureGroupGenerator


class NomenclatureGroupGeneratorTests(un.TestCase):

    def test_creating(self):
        gen = NomenclatureGroupGenerator()

        group = gen.food
        assert group.name == "еда"