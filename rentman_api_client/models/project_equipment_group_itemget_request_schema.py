import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectEquipmentGroupItemgetRequestSchema")


@attr.s(auto_attribs=True)
class ProjectEquipmentGroupItemgetRequestSchema:
    """ """

    subproject: str
    additional_scanned: Union[Unset, bool] = UNSET
    duration: Union[Unset, None, float] = UNSET
    in_price_calculation: Union[Unset, bool] = UNSET
    is_delayed: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    remark: Union[Unset, str] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subproject = self.subproject
        additional_scanned = self.additional_scanned
        duration = self.duration
        in_price_calculation = self.in_price_calculation
        is_delayed = self.is_delayed
        name = self.name
        order = self.order
        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        remark = self.remark
        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subproject": subproject,
            }
        )
        if additional_scanned is not UNSET:
            field_dict["additional_scanned"] = additional_scanned
        if duration is not UNSET:
            field_dict["duration"] = duration
        if in_price_calculation is not UNSET:
            field_dict["in_price_calculation"] = in_price_calculation
        if is_delayed is not UNSET:
            field_dict["is_delayed"] = is_delayed
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if remark is not UNSET:
            field_dict["remark"] = remark
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subproject = d.pop("subproject")

        additional_scanned = d.pop("additional_scanned", UNSET)

        duration = d.pop("duration", UNSET)

        in_price_calculation = d.pop("in_price_calculation", UNSET)

        is_delayed = d.pop("is_delayed", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        remark = d.pop("remark", UNSET)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        project_equipment_group_itemget_request_schema = cls(
            subproject=subproject,
            additional_scanned=additional_scanned,
            duration=duration,
            in_price_calculation=in_price_calculation,
            is_delayed=is_delayed,
            name=name,
            order=order,
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            remark=remark,
            usageperiod_end=usageperiod_end,
            usageperiod_start=usageperiod_start,
        )

        project_equipment_group_itemget_request_schema.additional_properties = d
        return project_equipment_group_itemget_request_schema

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
