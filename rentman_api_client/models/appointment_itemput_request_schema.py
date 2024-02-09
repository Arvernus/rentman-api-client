import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentItemputRequestSchema")


@attr.s(auto_attribs=True)
class AppointmentItemputRequestSchema:
    """ """

    start: datetime.datetime
    end: datetime.datetime
    name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    is_plannable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.isoformat()

        end = self.end.isoformat()

        name = self.name
        color = self.color
        location = self.location
        remark = self.remark
        is_public = self.is_public
        is_plannable = self.is_plannable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if color is not UNSET:
            field_dict["color"] = color
        if location is not UNSET:
            field_dict["location"] = location
        if remark is not UNSET:
            field_dict["remark"] = remark
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if is_plannable is not UNSET:
            field_dict["is_plannable"] = is_plannable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        name = d.pop("name", UNSET)

        color = d.pop("color", UNSET)

        location = d.pop("location", UNSET)

        remark = d.pop("remark", UNSET)

        is_public = d.pop("is_public", UNSET)

        is_plannable = d.pop("is_plannable", UNSET)

        appointment_itemput_request_schema = cls(
            start=start,
            end=end,
            name=name,
            color=color,
            location=location,
            remark=remark,
            is_public=is_public,
            is_plannable=is_plannable,
        )

        appointment_itemput_request_schema.additional_properties = d
        return appointment_itemput_request_schema

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
