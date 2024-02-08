from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tax_class_itemput_request_schema_type import TaxClassItemputRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxClassItemputRequestSchema")


@attr.s(auto_attribs=True)
class TaxClassItemputRequestSchema:
    """ """

    name: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    type: Union[Unset, TaxClassItemputRequestSchemaType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        code = self.code
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        type: Union[Unset, TaxClassItemputRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = TaxClassItemputRequestSchemaType(_type)

        tax_class_itemput_request_schema = cls(
            name=name,
            code=code,
            type=type,
        )

        tax_class_itemput_request_schema.additional_properties = d
        return tax_class_itemput_request_schema

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
