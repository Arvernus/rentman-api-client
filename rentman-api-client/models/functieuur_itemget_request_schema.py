from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FunctieuurItemgetRequestSchema")


@attr.s(auto_attribs=True)
class FunctieuurItemgetRequestSchema:
    """ """

    project_function: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    duration: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_function = self.project_function
        description = self.description
        duration = self.duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_function is not UNSET:
            field_dict["project_function"] = project_function
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_function = d.pop("project_function", UNSET)

        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        functieuur_itemget_request_schema = cls(
            project_function=project_function,
            description=description,
            duration=duration,
        )

        functieuur_itemget_request_schema.additional_properties = d
        return functieuur_itemget_request_schema

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
