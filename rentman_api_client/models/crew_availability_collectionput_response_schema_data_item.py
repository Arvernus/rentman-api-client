import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.crew_availability_collectionput_response_schema_data_item_recurrence_interval_unit import (
    CrewAvailabilityCollectionputResponseSchemaDataItemRecurrenceIntervalUnit,
)
from ..models.crew_availability_collectionput_response_schema_data_item_status import (
    CrewAvailabilityCollectionputResponseSchemaDataItemStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CrewAvailabilityCollectionputResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class CrewAvailabilityCollectionputResponseSchemaDataItem:
    """ """

    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    crewmember: Union[Unset, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    end: Union[Unset, None, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    last_updated: Union[Unset, None, datetime.datetime] = UNSET
    last_updater: Union[Unset, None, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    recurrence_enddate: Union[Unset, None, str] = UNSET
    recurrence_interval: Union[Unset, int] = UNSET
    recurrence_interval_unit: Union[
        Unset, CrewAvailabilityCollectionputResponseSchemaDataItemRecurrenceIntervalUnit
    ] = UNSET
    recurrent_group: Union[Unset, int] = UNSET
    remark: Union[Unset, str] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, CrewAvailabilityCollectionputResponseSchemaDataItemStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        crewmember = self.crewmember
        displayname = self.displayname
        end: Union[Unset, None, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat() if self.end else None

        id = self.id
        last_updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat() if self.last_updated else None

        last_updater = self.last_updater
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        recurrence_enddate = self.recurrence_enddate
        recurrence_interval = self.recurrence_interval
        recurrence_interval_unit: Union[Unset, str] = UNSET
        if not isinstance(self.recurrence_interval_unit, Unset):
            recurrence_interval_unit = self.recurrence_interval_unit.value

        recurrent_group = self.recurrent_group
        remark = self.remark
        start: Union[Unset, None, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat() if self.start else None

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if crewmember is not UNSET:
            field_dict["crewmember"] = crewmember
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if end is not UNSET:
            field_dict["end"] = end
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if last_updater is not UNSET:
            field_dict["last_updater"] = last_updater
        if modified is not UNSET:
            field_dict["modified"] = modified
        if recurrence_enddate is not UNSET:
            field_dict["recurrence_enddate"] = recurrence_enddate
        if recurrence_interval is not UNSET:
            field_dict["recurrence_interval"] = recurrence_interval
        if recurrence_interval_unit is not UNSET:
            field_dict["recurrence_interval_unit"] = recurrence_interval_unit
        if recurrent_group is not UNSET:
            field_dict["recurrent_group"] = recurrent_group
        if remark is not UNSET:
            field_dict["remark"] = remark
        if start is not UNSET:
            field_dict["start"] = start
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        crewmember = d.pop("crewmember", UNSET)

        displayname = d.pop("displayname", UNSET)

        end = None
        _end = d.pop("end", UNSET)
        if _end is not None and not isinstance(_end, Unset):
            end = isoparse(_end)

        id = d.pop("id", UNSET)

        last_updated = None
        _last_updated = d.pop("last_updated", UNSET)
        if _last_updated is not None and not isinstance(_last_updated, Unset):
            last_updated = isoparse(_last_updated)

        last_updater = d.pop("last_updater", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        recurrence_enddate = d.pop("recurrence_enddate", UNSET)

        recurrence_interval = d.pop("recurrence_interval", UNSET)

        recurrence_interval_unit: Union[
            Unset, CrewAvailabilityCollectionputResponseSchemaDataItemRecurrenceIntervalUnit
        ] = UNSET
        _recurrence_interval_unit = d.pop("recurrence_interval_unit", UNSET)
        if not isinstance(_recurrence_interval_unit, Unset):
            recurrence_interval_unit = CrewAvailabilityCollectionputResponseSchemaDataItemRecurrenceIntervalUnit(
                _recurrence_interval_unit
            )

        recurrent_group = d.pop("recurrent_group", UNSET)

        remark = d.pop("remark", UNSET)

        start = None
        _start = d.pop("start", UNSET)
        if _start is not None and not isinstance(_start, Unset):
            start = isoparse(_start)

        status: Union[Unset, CrewAvailabilityCollectionputResponseSchemaDataItemStatus] = UNSET
        _status = d.pop("status", UNSET)
        if not isinstance(_status, Unset):
            status = CrewAvailabilityCollectionputResponseSchemaDataItemStatus(_status)

        crew_availability_collectionput_response_schema_data_item = cls(
            created=created,
            creator=creator,
            crewmember=crewmember,
            displayname=displayname,
            end=end,
            id=id,
            last_updated=last_updated,
            last_updater=last_updater,
            modified=modified,
            recurrence_enddate=recurrence_enddate,
            recurrence_interval=recurrence_interval,
            recurrence_interval_unit=recurrence_interval_unit,
            recurrent_group=recurrent_group,
            remark=remark,
            start=start,
            status=status,
        )

        crew_availability_collectionput_response_schema_data_item.additional_properties = d
        return crew_availability_collectionput_response_schema_data_item

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
