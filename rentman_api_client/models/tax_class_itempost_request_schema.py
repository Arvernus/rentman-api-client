from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tax_class_itempost_request_schema_type import TaxClassItempostRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxClassItempostRequestSchema")


@attr.s(auto_attribs=True)
class TaxClassItempostRequestSchema:
    """ """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, TaxClassItempostRequestSchemaType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        type: Union[Unset, TaxClassItempostRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = TaxClassItempostRequestSchemaType(_type)

        tax_class_itempost_request_schema = cls(
            code=code,
            name=name,
            type=type,
        )

        tax_class_itempost_request_schema.additional_properties = d
        return tax_class_itempost_request_schema

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
