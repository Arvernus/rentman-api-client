import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.appointment_itemget_response_schema_data_recurrence_interval_unit import (
    AppointmentItemgetResponseSchemaDataRecurrenceIntervalUnit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class AppointmentItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    color: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    is_plannable: Union[Unset, bool] = UNSET
    recurrence_interval_unit: Union[Unset, AppointmentItemgetResponseSchemaDataRecurrenceIntervalUnit] = UNSET
    recurrence_enddate: Union[Unset, None, str] = UNSET
    recurrence_interval: Union[Unset, int] = UNSET
    recurrence_group: Union[Unset, int] = UNSET
    synchronization_id: Union[Unset, str] = UNSET
    synchronisation_uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        creator = self.creator
        displayname = self.displayname
        name = self.name
        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        color = self.color
        location = self.location
        remark = self.remark
        is_public = self.is_public
        is_plannable = self.is_plannable
        recurrence_interval_unit: Union[Unset, str] = UNSET
        if not isinstance(self.recurrence_interval_unit, Unset):
            recurrence_interval_unit = self.recurrence_interval_unit.value

        recurrence_enddate = self.recurrence_enddate
        recurrence_interval = self.recurrence_interval
        recurrence_group = self.recurrence_group
        synchronization_id = self.synchronization_id
        synchronisation_uri = self.synchronisation_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if name is not UNSET:
            field_dict["name"] = name
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
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
        if recurrence_interval_unit is not UNSET:
            field_dict["recurrence_interval_unit"] = recurrence_interval_unit
        if recurrence_enddate is not UNSET:
            field_dict["recurrence_enddate"] = recurrence_enddate
        if recurrence_interval is not UNSET:
            field_dict["recurrence_interval"] = recurrence_interval
        if recurrence_group is not UNSET:
            field_dict["recurrence_group"] = recurrence_group
        if synchronization_id is not UNSET:
            field_dict["synchronization_id"] = synchronization_id
        if synchronisation_uri is not UNSET:
            field_dict["synchronisation_uri"] = synchronisation_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        name = d.pop("name", UNSET)

        start: Union[Unset, datetime.datetime] = UNSET
        _start = d.pop("start", UNSET)
        if not isinstance(_start, Unset):
            start = isoparse(_start)

        end: Union[Unset, datetime.datetime] = UNSET
        _end = d.pop("end", UNSET)
        if not isinstance(_end, Unset):
            end = isoparse(_end)

        color = d.pop("color", UNSET)

        location = d.pop("location", UNSET)

        remark = d.pop("remark", UNSET)

        is_public = d.pop("is_public", UNSET)

        is_plannable = d.pop("is_plannable", UNSET)

        recurrence_interval_unit: Union[Unset, AppointmentItemgetResponseSchemaDataRecurrenceIntervalUnit] = UNSET
        _recurrence_interval_unit = d.pop("recurrence_interval_unit", UNSET)
        if not isinstance(_recurrence_interval_unit, Unset):
            recurrence_interval_unit = AppointmentItemgetResponseSchemaDataRecurrenceIntervalUnit(
                _recurrence_interval_unit
            )

        recurrence_enddate = d.pop("recurrence_enddate", UNSET)

        recurrence_interval = d.pop("recurrence_interval", UNSET)

        recurrence_group = d.pop("recurrence_group", UNSET)

        synchronization_id = d.pop("synchronization_id", UNSET)

        synchronisation_uri = d.pop("synchronisation_uri", UNSET)

        appointment_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            name=name,
            start=start,
            end=end,
            color=color,
            location=location,
            remark=remark,
            is_public=is_public,
            is_plannable=is_plannable,
            recurrence_interval_unit=recurrence_interval_unit,
            recurrence_enddate=recurrence_enddate,
            recurrence_interval=recurrence_interval,
            recurrence_group=recurrence_group,
            synchronization_id=synchronization_id,
            synchronisation_uri=synchronisation_uri,
        )

        appointment_itemget_response_schema_data.additional_properties = d
        return appointment_itemget_response_schema_data

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
