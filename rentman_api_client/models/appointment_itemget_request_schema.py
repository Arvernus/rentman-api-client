import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.appointment_itemget_request_schema_recurrence_interval_unit import (
    AppointmentItemgetRequestSchemaRecurrenceIntervalUnit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentItemgetRequestSchema")


@attr.s(auto_attribs=True)
class AppointmentItemgetRequestSchema:
    """ """

    end: datetime.datetime
    start: datetime.datetime
    color: Union[Unset, str] = UNSET
    is_plannable: Union[Unset, bool] = UNSET
    is_public: Union[Unset, bool] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    recurrence_enddate: Union[Unset, None, str] = UNSET
    recurrence_group: Union[Unset, int] = UNSET
    recurrence_interval: Union[Unset, int] = UNSET
    recurrence_interval_unit: Union[Unset, AppointmentItemgetRequestSchemaRecurrenceIntervalUnit] = UNSET
    remark: Union[Unset, str] = UNSET
    synchronisation_uri: Union[Unset, str] = UNSET
    synchronization_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        color = self.color
        is_plannable = self.is_plannable
        is_public = self.is_public
        location = self.location
        name = self.name
        recurrence_enddate = self.recurrence_enddate
        recurrence_group = self.recurrence_group
        recurrence_interval = self.recurrence_interval
        recurrence_interval_unit: Union[Unset, str] = UNSET
        if not isinstance(self.recurrence_interval_unit, Unset):
            recurrence_interval_unit = self.recurrence_interval_unit.value

        remark = self.remark
        synchronisation_uri = self.synchronisation_uri
        synchronization_id = self.synchronization_id

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
        if recurrence_enddate is not UNSET:
            field_dict["recurrence_enddate"] = recurrence_enddate
        if recurrence_group is not UNSET:
            field_dict["recurrence_group"] = recurrence_group
        if recurrence_interval is not UNSET:
            field_dict["recurrence_interval"] = recurrence_interval
        if recurrence_interval_unit is not UNSET:
            field_dict["recurrence_interval_unit"] = recurrence_interval_unit
        if remark is not UNSET:
            field_dict["remark"] = remark
        if synchronisation_uri is not UNSET:
            field_dict["synchronisation_uri"] = synchronisation_uri
        if synchronization_id is not UNSET:
            field_dict["synchronization_id"] = synchronization_id

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

        recurrence_enddate = d.pop("recurrence_enddate", UNSET)

        recurrence_group = d.pop("recurrence_group", UNSET)

        recurrence_interval = d.pop("recurrence_interval", UNSET)

        recurrence_interval_unit: Union[Unset, AppointmentItemgetRequestSchemaRecurrenceIntervalUnit] = UNSET
        _recurrence_interval_unit = d.pop("recurrence_interval_unit", UNSET)
        if not isinstance(_recurrence_interval_unit, Unset):
            recurrence_interval_unit = AppointmentItemgetRequestSchemaRecurrenceIntervalUnit(_recurrence_interval_unit)

        remark = d.pop("remark", UNSET)

        synchronisation_uri = d.pop("synchronisation_uri", UNSET)

        synchronization_id = d.pop("synchronization_id", UNSET)

        appointment_itemget_request_schema = cls(
            end=end,
            start=start,
            color=color,
            is_plannable=is_plannable,
            is_public=is_public,
            location=location,
            name=name,
            recurrence_enddate=recurrence_enddate,
            recurrence_group=recurrence_group,
            recurrence_interval=recurrence_interval,
            recurrence_interval_unit=recurrence_interval_unit,
            remark=remark,
            synchronisation_uri=synchronisation_uri,
            synchronization_id=synchronization_id,
        )

        appointment_itemget_request_schema.additional_properties = d
        return appointment_itemget_request_schema

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
