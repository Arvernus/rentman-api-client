import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.beschikbaarheid_itempost_request_schema_recurrence_interval_unit import (
    BeschikbaarheidItempostRequestSchemaRecurrenceIntervalUnit,
)
from ..models.beschikbaarheid_itempost_request_schema_status import BeschikbaarheidItempostRequestSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BeschikbaarheidItempostRequestSchema")


@attr.s(auto_attribs=True)
class BeschikbaarheidItempostRequestSchema:
    """ """

    last_updater: Union[Unset, None, str] = UNSET
    last_updated: Union[Unset, None, datetime.datetime] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    end: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, BeschikbaarheidItempostRequestSchemaStatus] = UNSET
    remark: Union[Unset, str] = UNSET
    recurrence_interval_unit: Union[Unset, BeschikbaarheidItempostRequestSchemaRecurrenceIntervalUnit] = UNSET
    recurrence_enddate: Union[Unset, None, str] = UNSET
    recurrence_interval: Union[Unset, int] = UNSET
    recurrent_group: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        if last_updater is not UNSET:
            field_dict["last_updater"] = last_updater
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
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

        status: Union[Unset, BeschikbaarheidItempostRequestSchemaStatus] = UNSET
        _status = d.pop("status", UNSET)
        if not isinstance(_status, Unset):
            status = BeschikbaarheidItempostRequestSchemaStatus(_status)

        remark = d.pop("remark", UNSET)

        recurrence_interval_unit: Union[Unset, BeschikbaarheidItempostRequestSchemaRecurrenceIntervalUnit] = UNSET
        _recurrence_interval_unit = d.pop("recurrence_interval_unit", UNSET)
        if not isinstance(_recurrence_interval_unit, Unset):
            recurrence_interval_unit = BeschikbaarheidItempostRequestSchemaRecurrenceIntervalUnit(
                _recurrence_interval_unit
            )

        recurrence_enddate = d.pop("recurrence_enddate", UNSET)

        recurrence_interval = d.pop("recurrence_interval", UNSET)

        recurrent_group = d.pop("recurrent_group", UNSET)

        beschikbaarheid_itempost_request_schema = cls(
            last_updater=last_updater,
            last_updated=last_updated,
            start=start,
            end=end,
            status=status,
            remark=remark,
            recurrence_interval_unit=recurrence_interval_unit,
            recurrence_enddate=recurrence_enddate,
            recurrence_interval=recurrence_interval,
            recurrent_group=recurrent_group,
        )

        beschikbaarheid_itempost_request_schema.additional_properties = d
        return beschikbaarheid_itempost_request_schema

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
