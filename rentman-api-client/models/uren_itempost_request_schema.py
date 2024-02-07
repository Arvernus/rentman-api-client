import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.uren_itempost_request_schema_custom import UrenItempostRequestSchemaCustom
from ..models.uren_itempost_request_schema_type import UrenItempostRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UrenItempostRequestSchema")


@attr.s(auto_attribs=True)
class UrenItempostRequestSchema:
    """ """

    crewmember: Union[Unset, None, str] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    end: Union[Unset, None, datetime.datetime] = UNSET
    distance: Union[Unset, float] = UNSET
    is_lunch_included: Union[Unset, bool] = UNSET
    type: Union[Unset, UrenItempostRequestSchemaType] = UNSET
    break_duration: Union[Unset, None, float] = UNSET
    travel_time: Union[Unset, None, float] = UNSET
    correction_duration: Union[Unset, None, float] = UNSET
    registered_by_clocking: Union[Unset, bool] = UNSET
    remark: Union[Unset, str] = UNSET
    custom: Union[Unset, UrenItempostRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        crewmember = self.crewmember
        start: Union[Unset, None, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat() if self.start else None

        end: Union[Unset, None, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat() if self.end else None

        distance = self.distance
        is_lunch_included = self.is_lunch_included
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        break_duration = self.break_duration
        travel_time = self.travel_time
        correction_duration = self.correction_duration
        registered_by_clocking = self.registered_by_clocking
        remark = self.remark
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crewmember is not UNSET:
            field_dict["crewmember"] = crewmember
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if distance is not UNSET:
            field_dict["distance"] = distance
        if is_lunch_included is not UNSET:
            field_dict["is_lunch_included"] = is_lunch_included
        if type is not UNSET:
            field_dict["type"] = type
        if break_duration is not UNSET:
            field_dict["break_duration"] = break_duration
        if travel_time is not UNSET:
            field_dict["travel_time"] = travel_time
        if correction_duration is not UNSET:
            field_dict["correction_duration"] = correction_duration
        if registered_by_clocking is not UNSET:
            field_dict["registered_by_clocking"] = registered_by_clocking
        if remark is not UNSET:
            field_dict["remark"] = remark
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        crewmember = d.pop("crewmember", UNSET)

        start = None
        _start = d.pop("start", UNSET)
        if _start is not None and not isinstance(_start, Unset):
            start = isoparse(_start)

        end = None
        _end = d.pop("end", UNSET)
        if _end is not None and not isinstance(_end, Unset):
            end = isoparse(_end)

        distance = d.pop("distance", UNSET)

        is_lunch_included = d.pop("is_lunch_included", UNSET)

        type: Union[Unset, UrenItempostRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = UrenItempostRequestSchemaType(_type)

        break_duration = d.pop("break_duration", UNSET)

        travel_time = d.pop("travel_time", UNSET)

        correction_duration = d.pop("correction_duration", UNSET)

        registered_by_clocking = d.pop("registered_by_clocking", UNSET)

        remark = d.pop("remark", UNSET)

        custom: Union[Unset, UrenItempostRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = UrenItempostRequestSchemaCustom.from_dict(_custom)

        uren_itempost_request_schema = cls(
            crewmember=crewmember,
            start=start,
            end=end,
            distance=distance,
            is_lunch_included=is_lunch_included,
            type=type,
            break_duration=break_duration,
            travel_time=travel_time,
            correction_duration=correction_duration,
            registered_by_clocking=registered_by_clocking,
            remark=remark,
            custom=custom,
        )

        uren_itempost_request_schema.additional_properties = d
        return uren_itempost_request_schema

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
