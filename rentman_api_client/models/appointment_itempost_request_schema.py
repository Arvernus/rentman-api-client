import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentItempostRequestSchema")


@attr.s(auto_attribs=True)
class AppointmentItempostRequestSchema:
    """ """

    end: datetime.datetime
    start: datetime.datetime
    color: Union[Unset, str] = UNSET
    is_plannable: Union[Unset, bool] = UNSET
    is_public: Union[Unset, bool] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        color = self.color
        is_plannable = self.is_plannable
        is_public = self.is_public
        location = self.location
        name = self.name
        remark = self.remark

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if is_plannable is not UNSET:
            field_dict["is_plannable"] = is_plannable
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if remark is not UNSET:
            field_dict["remark"] = remark

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end = isoparse(d.pop("end"))

        start = isoparse(d.pop("start"))

        color = d.pop("color", UNSET)

        is_plannable = d.pop("is_plannable", UNSET)

        is_public = d.pop("is_public", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        remark = d.pop("remark", UNSET)

        appointment_itempost_request_schema = cls(
            end=end,
            start=start,
            color=color,
            is_plannable=is_plannable,
            is_public=is_public,
            location=location,
            name=name,
            remark=remark,
        )

        appointment_itempost_request_schema.additional_properties = d
        return appointment_itempost_request_schema

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
