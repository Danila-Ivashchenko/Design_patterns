import helper
from prototype import NomenclatureFilter, NomenclaturePrototype, OperationEnum
from service import StartService
from repository.data import DataRepository
import unittest as un



class TestNomenclaturePrototype(un.TestCase):
    json_helper = helper.JsonHelper()
    data_repository = DataRepository()
    start_service = StartService(data_repository)

    def test_like(self):
        # Arrange
        data_repository = DataRepository()
        start_service = StartService(data_repository)

        data = start_service.get_all_nomenclature
        prot = NomenclaturePrototype(data)

        filter_nomenclature = NomenclatureFilter()
        filter_nomenclature.name = "масло"
        filter_nomenclature.name_operation(OperationEnum.Like)

        # Act
        res = prot.create(filter_nomenclature)

        # Assert
        assert len(res) > 0

        for item in res:
            assert "масло" in item.name

    def test_equal(self):
        # Arrange
        data = self.start_service.get_all_nomenclature
        prot = NomenclaturePrototype(data)

        filter_nomenclature = NomenclatureFilter()
        filter_nomenclature.name = data[0].name
        filter_nomenclature.id = data[0].id

        # Act
        res = prot.create(filter_nomenclature)

        # Assert
        assert len(res) == 1
        assert res[0] == data[0]

    def test_from_json(self):
        # Arrange
        filter_raw = {
            'id': None,
            'name': {
                'value': 'масло',
                'operation': 2
            }
        }

        filter_val = self.json_helper.to_deserialize(NomenclatureFilter, filter_raw)
        data = self.start_service.get_all_nomenclature

        # Act
        prot = NomenclaturePrototype(data)
        res = prot.create(filter_val)

        # Assert
        assert len(res) > 0

        for item in res:
            assert 'масло' in item.name




