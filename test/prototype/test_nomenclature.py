import helper
from prototype import NomenclatureFilter, NomenclaturePrototype, OperationEnum
from service import StartService
from repository.data import DataRepository
import unittest as un

class TestNomenclaturePrototype(un.TestCase):
    def test_like(self):
        data_repository = DataRepository()
        start_service = StartService(data_repository)

        data = start_service.get_all_nomenclature
        prot = NomenclaturePrototype(data)

        filter_nomenclature = NomenclatureFilter()
        filter_nomenclature.name = "масло"
        filter_nomenclature.name_operation(OperationEnum.Like)

        res = prot.create(filter_nomenclature)

        assert len(res) > 0

        for item in res:
            assert "масло" in item.name

    def test_equal(self):
        data_repository = DataRepository()
        start_service = StartService(data_repository)

        data = start_service.get_all_nomenclature
        prot = NomenclaturePrototype(data)

        filter_nomenclature = NomenclatureFilter()
        filter_nomenclature.name =  data[0].name
        filter_nomenclature.id = data[0].id

        res = prot.create(filter_nomenclature)

        assert len(res) == 1

        assert res[0] == data[0]

    def test_from_json(self):

        filter_raw = {
            'id': None,
            'name': {
                'value': 'масло',
                'operation': 2
            }
        }

        json_helper = helper.JsonHelper()

        filter_val = json_helper.to_deserialize(NomenclatureFilter, filter_raw)

        data_repository = DataRepository()
        start_service = StartService(data_repository)

        data = start_service.get_all_nomenclature
        prot = NomenclaturePrototype(data)

        res = prot.create(filter_val)

        assert len(res) > 0

        for item in res:
            assert 'масло' in item.name




