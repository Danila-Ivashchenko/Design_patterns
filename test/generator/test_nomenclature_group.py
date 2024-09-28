from generator import NomenclatureGroupGenerator
import unittest as un


class NomenclatureGroupGeneratorTests(un.TestCase):

    def test_creating(self):
        gen = NomenclatureGroupGenerator()

        group = gen.food
        assert group.name == "еда"