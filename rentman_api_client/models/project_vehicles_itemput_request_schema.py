import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_vehicles_itemput_request_schema_custom import ProjectVehiclesItemputRequestSchemaCustom
from ..models.project_vehicles_itemput_request_schema_transport import ProjectVehiclesItemputRequestSchemaTransport
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectVehiclesItemputRequestSchema")


@attr.s(auto_attribs=True)
class ProjectVehiclesItemputRequestSchema:
    """ """

    vehicle: str
    cost_rate: Union[Unset, None, str] = UNSET
    custom: Union[Unset, ProjectVehiclesItemputRequestSchemaCustom] = UNSET
    planningperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planningperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    remark: Union[Unset, str] = UNSET
    remark_planner: Union[Unset, str] = UNSET
    transport: Union[Unset, ProjectVehiclesItemputRequestSchemaTransport] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vehicle = self.vehicle
        cost_rate = self.cost_rate
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        planningperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planningperiod_end, Unset):
            planningperiod_end = self.planningperiod_end.isoformat() if self.planningperiod_end else None

        planningperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planningperiod_start, Unset):
            planningperiod_start = self.planningperiod_start.isoformat() if self.planningperiod_start else None

        remark = self.remark
        remark_planner = self.remark_planner
        transport: Union[Unset, str] = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vehicle": vehicle,
            }
        )
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
        if custom is not UNSET:
            field_dict["custom"] = custom
        if planningperiod_end is not UNSET:
            field_dict["planningperiod_end"] = planningperiod_end
        if planningperiod_start is not UNSET:
            field_dict["planningperiod_start"] = planningperiod_start
        if remark is not UNSET:
            field_dict["remark"] = remark
        if remark_planner is not UNSET:
            field_dict["remark_planner"] = remark_planner
        if transport is not UNSET:
            field_dict["transport"] = transport

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vehicle = d.pop("vehicle")

        cost_rate = d.pop("cost_rate", UNSET)

        custom: Union[Unset, ProjectVehiclesItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectVehiclesItemputRequestSchemaCustom.from_dict(_custom)

        planningperiod_end = None
        _planningperiod_end = d.pop("planningperiod_end", UNSET)
        if _planningperiod_end is not None and not isinstance(_planningperiod_end, Unset):
            planningperiod_end = isoparse(_planningperiod_end)

        planningperiod_start = None
        _planningperiod_start = d.pop("planningperiod_start", UNSET)
        if _planningperiod_start is not None and not isinstance(_planningperiod_start, Unset):
            planningperiod_start = isoparse(_planningperiod_start)

        remark = d.pop("remark", UNSET)

        remark_planner = d.pop("remark_planner", UNSET)

        transport: Union[Unset, ProjectVehiclesItemputRequestSchemaTransport] = UNSET
        _transport = d.pop("transport", UNSET)
        if not isinstance(_transport, Unset):
            transport = ProjectVehiclesItemputRequestSchemaTransport(_transport)

        project_vehicles_itemput_request_schema = cls(
            vehicle=vehicle,
            cost_rate=cost_rate,
            custom=custom,
            planningperiod_end=planningperiod_end,
            planningperiod_start=planningperiod_start,
            remark=remark,
            remark_planner=remark_planner,
            transport=transport,
        )

        project_vehicles_itemput_request_schema.additional_properties = d
        return project_vehicles_itemput_request_schema

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
