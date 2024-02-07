import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.beschikbaarheid_collectionget_response_schema_data_item_recurrence_interval_unit import (
    BeschikbaarheidCollectiongetResponseSchemaDataItemRecurrenceIntervalUnit,
)
from ..models.beschikbaarheid_collectionget_response_schema_data_item_status import (
    BeschikbaarheidCollectiongetResponseSchemaDataItemStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BeschikbaarheidCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class BeschikbaarheidCollectiongetResponseSchemaDataItem:
    """ """

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    last_updater: Union[Unset, None, str] = UNSET
    last_updated: Union[Unset, None, datetime.datetime] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    end: Union[Unset, None, datetime.datetime] = UNSET
    crewmember: Union[Unset, str] = UNSET
    status: Union[Unset, BeschikbaarheidCollectiongetResponseSchemaDataItemStatus] = UNSET
    remark: Union[Unset, str] = UNSET
    recurrence_interval_unit: Union[
        Unset, BeschikbaarheidCollectiongetResponseSchemaDataItemRecurrenceIntervalUnit
    ] = UNSET
    recurrence_enddate: Union[Unset, None, str] = UNSET
    recurrence_interval: Union[Unset, int] = UNSET
    recurrent_group: Union[Unset, int] = UNSET
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
        last_updater = self.last_updater
        last_updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat() if self.last_updated else None

        start: Union[Unset, None, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat() if self.start else None

        end: Union[Unset, None, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat() if self.end else None

        crewmember = self.crewmember
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        remark = self.remark
        recurrence_interval_unit: Union[Unset, str] = UNSET
        if not isinstance(self.recurrence_interval_unit, Unset):
            recurrence_interval_unit = self.recurrence_interval_unit.value

        recurrence_enddate = self.recurrence_enddate
        recurrence_interval = self.recurrence_interval
        recurrent_group = self.recurrent_group

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
        if last_updater is not UNSET:
            field_dict["last_updater"] = last_updater
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if crewmember is not UNSET:
            field_dict["crewmember"] = crewmember
        if status is not UNSET:
            field_dict["status"] = status
        if remark is not UNSET:
            field_dict["remark"] = remark
        if recurrence_interval_unit is not UNSET:
            field_dict["recurrence_interval_unit"] = recurrence_interval_unit
        if recurrence_enddate is not UNSET:
            field_dict["recurrence_enddate"] = recurrence_enddate
        if recurrence_interval is not UNSET:
            field_dict["recurrence_interval"] = recurrence_interval
        if recurrent_group is not UNSET:
            field_dict["recurrent_group"] = recurrent_group

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

        last_updater = d.pop("last_updater", UNSET)

        last_updated = None
        _last_updated = d.pop("last_updated", UNSET)
        if _last_updated is not None and not isinstance(_last_updated, Unset):
            last_updated = isoparse(_last_updated)

        start = None
        _start = d.pop("start", UNSET)
        if _start is not None and not isinstance(_start, Unset):
            start = isoparse(_start)

        end = None
        _end = d.pop("end", UNSET)
        if _end is not None and not isinstance(_end, Unset):
            end = isoparse(_end)

        crewmember = d.pop("crewmember", UNSET)

        status: Union[Unset, BeschikbaarheidCollectiongetResponseSchemaDataItemStatus] = UNSET
        _status = d.pop("status", UNSET)
        if not isinstance(_status, Unset):
            status = BeschikbaarheidCollectiongetResponseSchemaDataItemStatus(_status)

        remark = d.pop("remark", UNSET)

        recurrence_interval_unit: Union[
            Unset, BeschikbaarheidCollectiongetResponseSchemaDataItemRecurrenceIntervalUnit
        ] = UNSET
        _recurrence_interval_unit = d.pop("recurrence_interval_unit", UNSET)
        if not isinstance(_recurrence_interval_unit, Unset):
            recurrence_interval_unit = BeschikbaarheidCollectiongetResponseSchemaDataItemRecurrenceIntervalUnit(
                _recurrence_interval_unit
            )

        recurrence_enddate = d.pop("recurrence_enddate", UNSET)

        recurrence_interval = d.pop("recurrence_interval", UNSET)

        recurrent_group = d.pop("recurrent_group", UNSET)

        beschikbaarheid_collectionget_response_schema_data_item = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            last_updater=last_updater,
            last_updated=last_updated,
            start=start,
            end=end,
            crewmember=crewmember,
            status=status,
            remark=remark,
            recurrence_interval_unit=recurrence_interval_unit,
            recurrence_enddate=recurrence_enddate,
            recurrence_interval=recurrence_interval,
            recurrent_group=recurrent_group,
        )

        beschikbaarheid_collectionget_response_schema_data_item.additional_properties = d
        return beschikbaarheid_collectionget_response_schema_data_item

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
