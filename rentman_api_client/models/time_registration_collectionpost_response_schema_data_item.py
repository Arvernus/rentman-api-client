import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.time_registration_collectionpost_response_schema_data_item_custom import (
    TimeRegistrationCollectionpostResponseSchemaDataItemCustom,
)
from ..models.time_registration_collectionpost_response_schema_data_item_type import (
    TimeRegistrationCollectionpostResponseSchemaDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeRegistrationCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class TimeRegistrationCollectionpostResponseSchemaDataItem:
    """ """

    break_duration: Union[Unset, None, float] = UNSET
    correction_duration: Union[Unset, None, float] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    crewmember: Union[Unset, None, str] = UNSET
    custom: Union[Unset, TimeRegistrationCollectionpostResponseSchemaDataItemCustom] = UNSET
    displayname: Union[Unset, str] = UNSET
    distance: Union[Unset, float] = UNSET
    end: Union[Unset, None, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    is_lunch_included: Union[Unset, bool] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    registered_by_clocking: Union[Unset, bool] = UNSET
    remark: Union[Unset, str] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    travel_time: Union[Unset, None, float] = UNSET
    type: Union[Unset, TimeRegistrationCollectionpostResponseSchemaDataItemType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        break_duration = self.break_duration
        correction_duration = self.correction_duration
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        crewmember = self.crewmember
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        displayname = self.displayname
        distance = self.distance
        end: Union[Unset, None, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat() if self.end else None

        id = self.id
        is_lunch_included = self.is_lunch_included
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

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
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if crewmember is not UNSET:
            field_dict["crewmember"] = crewmember
        if custom is not UNSET:
            field_dict["custom"] = custom
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if distance is not UNSET:
            field_dict["distance"] = distance
        if end is not UNSET:
            field_dict["end"] = end
        if id is not UNSET:
            field_dict["id"] = id
        if is_lunch_included is not UNSET:
            field_dict["is_lunch_included"] = is_lunch_included
        if modified is not UNSET:
            field_dict["modified"] = modified
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

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        crewmember = d.pop("crewmember", UNSET)

        custom: Union[Unset, TimeRegistrationCollectionpostResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = TimeRegistrationCollectionpostResponseSchemaDataItemCustom.from_dict(_custom)

        displayname = d.pop("displayname", UNSET)

        distance = d.pop("distance", UNSET)

        end = None
        _end = d.pop("end", UNSET)
        if _end is not None and not isinstance(_end, Unset):
            end = isoparse(_end)

        id = d.pop("id", UNSET)

        is_lunch_included = d.pop("is_lunch_included", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        registered_by_clocking = d.pop("registered_by_clocking", UNSET)

        remark = d.pop("remark", UNSET)

        start = None
        _start = d.pop("start", UNSET)
        if _start is not None and not isinstance(_start, Unset):
            start = isoparse(_start)

        travel_time = d.pop("travel_time", UNSET)

        type: Union[Unset, TimeRegistrationCollectionpostResponseSchemaDataItemType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = TimeRegistrationCollectionpostResponseSchemaDataItemType(_type)

        time_registration_collectionpost_response_schema_data_item = cls(
            break_duration=break_duration,
            correction_duration=correction_duration,
            created=created,
            creator=creator,
            crewmember=crewmember,
            custom=custom,
            displayname=displayname,
            distance=distance,
            end=end,
            id=id,
            is_lunch_included=is_lunch_included,
            modified=modified,
            registered_by_clocking=registered_by_clocking,
            remark=remark,
            start=start,
            travel_time=travel_time,
            type=type,
        )

        time_registration_collectionpost_response_schema_data_item.additional_properties = d
        return time_registration_collectionpost_response_schema_data_item

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
