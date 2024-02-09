import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.time_registration_itemput_request_schema_custom import TimeRegistrationItemputRequestSchemaCustom
from ..models.time_registration_itemput_request_schema_type import TimeRegistrationItemputRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeRegistrationItemputRequestSchema")


@attr.s(auto_attribs=True)
class TimeRegistrationItemputRequestSchema:
    """ """

    break_duration: Union[Unset, None, float] = UNSET
    correction_duration: Union[Unset, None, float] = UNSET
    crewmember: Union[Unset, None, str] = UNSET
    custom: Union[Unset, TimeRegistrationItemputRequestSchemaCustom] = UNSET
    distance: Union[Unset, float] = UNSET
    end: Union[Unset, None, datetime.datetime] = UNSET
    is_lunch_included: Union[Unset, bool] = UNSET
    registered_by_clocking: Union[Unset, bool] = UNSET
    remark: Union[Unset, str] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    travel_time: Union[Unset, None, float] = UNSET
    type: Union[Unset, TimeRegistrationItemputRequestSchemaType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        break_duration = self.break_duration
        correction_duration = self.correction_duration
        crewmember = self.crewmember
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        distance = self.distance
        end: Union[Unset, None, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat() if self.end else None

        is_lunch_included = self.is_lunch_included
        registered_by_clocking = self.registered_by_clocking
        remark = self.remark
        start: Union[Unset, None, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat() if self.start else None

        travel_time = self.travel_time
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if break_duration is not UNSET:
            field_dict["break_duration"] = break_duration
        if correction_duration is not UNSET:
            field_dict["correction_duration"] = correction_duration
        if crewmember is not UNSET:
            field_dict["crewmember"] = crewmember
        if custom is not UNSET:
            field_dict["custom"] = custom
        if distance is not UNSET:
            field_dict["distance"] = distance
        if end is not UNSET:
            field_dict["end"] = end
        if is_lunch_included is not UNSET:
            field_dict["is_lunch_included"] = is_lunch_included
        if registered_by_clocking is not UNSET:
            field_dict["registered_by_clocking"] = registered_by_clocking
        if remark is not UNSET:
            field_dict["remark"] = remark
        if start is not UNSET:
            field_dict["start"] = start
        if travel_time is not UNSET:
            field_dict["travel_time"] = travel_time
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        break_duration = d.pop("break_duration", UNSET)

        correction_duration = d.pop("correction_duration", UNSET)

        crewmember = d.pop("crewmember", UNSET)

        custom: Union[Unset, TimeRegistrationItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = TimeRegistrationItemputRequestSchemaCustom.from_dict(_custom)

        distance = d.pop("distance", UNSET)

        end = None
        _end = d.pop("end", UNSET)
        if _end is not None and not isinstance(_end, Unset):
            end = isoparse(_end)

        is_lunch_included = d.pop("is_lunch_included", UNSET)

        registered_by_clocking = d.pop("registered_by_clocking", UNSET)

        remark = d.pop("remark", UNSET)

        start = None
        _start = d.pop("start", UNSET)
        if _start is not None and not isinstance(_start, Unset):
            start = isoparse(_start)

        travel_time = d.pop("travel_time", UNSET)

        type: Union[Unset, TimeRegistrationItemputRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = TimeRegistrationItemputRequestSchemaType(_type)

        time_registration_itemput_request_schema = cls(
            break_duration=break_duration,
            correction_duration=correction_duration,
            crewmember=crewmember,
            custom=custom,
            distance=distance,
            end=end,
            is_lunch_included=is_lunch_included,
            registered_by_clocking=registered_by_clocking,
            remark=remark,
            start=start,
            travel_time=travel_time,
            type=type,
        )

        time_registration_itemput_request_schema.additional_properties = d
        return time_registration_itemput_request_schema

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
