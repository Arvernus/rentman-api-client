from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.projecttype_itempost_request_schema_type import ProjecttypeItempostRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjecttypeItempostRequestSchema")


@attr.s(auto_attribs=True)
class ProjecttypeItempostRequestSchema:
    """ """

    name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    type: Union[Unset, ProjecttypeItempostRequestSchemaType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        color = self.color
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if color is not UNSET:
            field_dict["color"] = color
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        color = d.pop("color", UNSET)

        type: Union[Unset, ProjecttypeItempostRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = ProjecttypeItempostRequestSchemaType(_type)

        projecttype_itempost_request_schema = cls(
            name=name,
            color=color,
            type=type,
        )

        projecttype_itempost_request_schema.additional_properties = d
        return projecttype_itempost_request_schema

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
