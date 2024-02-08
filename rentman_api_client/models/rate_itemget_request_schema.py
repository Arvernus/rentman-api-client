from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rate_itemget_request_schema_subtype import RateItemgetRequestSchemaSubtype
from ..models.rate_itemget_request_schema_type import RateItemgetRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RateItemgetRequestSchema")


@attr.s(auto_attribs=True)
class RateItemgetRequestSchema:
    """ """

    name: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    type: Union[Unset, RateItemgetRequestSchemaType] = UNSET
    subtype: Union[Unset, RateItemgetRequestSchemaSubtype] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        archived = self.archived
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        subtype: Union[Unset, str] = UNSET
        if not isinstance(self.subtype, Unset):
            subtype = self.subtype.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if archived is not UNSET:
            field_dict["archived"] = archived
        if type is not UNSET:
            field_dict["type"] = type
        if subtype is not UNSET:
            field_dict["subtype"] = subtype

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        archived = d.pop("archived", UNSET)

        type: Union[Unset, RateItemgetRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = RateItemgetRequestSchemaType(_type)

        subtype: Union[Unset, RateItemgetRequestSchemaSubtype] = UNSET
        _subtype = d.pop("subtype", UNSET)
        if not isinstance(_subtype, Unset):
            subtype = RateItemgetRequestSchemaSubtype(_subtype)

        rate_itemget_request_schema = cls(
            name=name,
            archived=archived,
            type=type,
            subtype=subtype,
        )

        rate_itemget_request_schema.additional_properties = d
        return rate_itemget_request_schema

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
