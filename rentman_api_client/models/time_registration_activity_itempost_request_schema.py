from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeRegistrationActivityItempostRequestSchema")


@attr.s(auto_attribs=True)
class TimeRegistrationActivityItempostRequestSchema:
    """ """

    description: Union[Unset, str] = UNSET
    duration: Union[Unset, None, float] = UNSET
    project_function: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        duration = self.duration
        project_function = self.project_function

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if project_function is not UNSET:
            field_dict["project_function"] = project_function

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        project_function = d.pop("project_function", UNSET)

        time_registration_activity_itempost_request_schema = cls(
            description=description,
            duration=duration,
            project_function=project_function,
        )

        time_registration_activity_itempost_request_schema.additional_properties = d
        return time_registration_activity_itempost_request_schema

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
