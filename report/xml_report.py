from .base import BaseReporter
from xml.etree.ElementTree import Element, tostring, SubElement


class XmlReporter(BaseReporter):

    def __init__(self):
        super().__init__()

    def report(self, data) -> str:
        root = Element("root")

        class_name = self._get_main_class_name(data)

        if not isinstance(data, list):
            data = [data]

        for i, item in enumerate(data):
            object_element = SubElement(root, f"{class_name}_{i}")
            dict_elem = self._to_serializable(item)
            self._dict_to_xml(dict_elem, object_element)

        return tostring(root, encoding='unicode', xml_declaration=True)

    def _dict_to_xml(self, d: dict, parent: Element):
        for key, value in d.items():
            child = SubElement(parent, key)
            if isinstance(value, dict):
                self._dict_to_xml(value, child)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    dict_elem = self._to_serializable(item)
                    if isinstance(dict_elem, dict):
                        self._dict_to_xml(dict_elem, child)
                    else:
                        sub_child = SubElement(child, f"{key}_{i}")
                        sub_child.text = item
            else:
                child.text = str(value)


    def _set_value_to_parent(self, parent, value):
        if isinstance(value, list):
            for idx, item in enumerate(value):
                item_element = SubElement(parent, f'item{idx}')
                self._set_value_to_parent(item_element, item)
        elif isinstance(value, dict):
            for k, v in value.items():
                sub_element = SubElement(parent, k)
                self._set_value_to_parent(sub_element, v)
        else:
            parent.text = str(value)