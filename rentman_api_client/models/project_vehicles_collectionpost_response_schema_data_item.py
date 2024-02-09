import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_vehicles_collectionpost_response_schema_data_item_custom import (
    ProjectVehiclesCollectionpostResponseSchemaDataItemCustom,
)
from ..models.project_vehicles_collectionpost_response_schema_data_item_transport import (
    ProjectVehiclesCollectionpostResponseSchemaDataItemTransport,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectVehiclesCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class ProjectVehiclesCollectionpostResponseSchemaDataItem:
    """ """

    cost_rate: Union[Unset, None, str] = UNSET
    costs: Union[Unset, float] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    custom: Union[Unset, ProjectVehiclesCollectionpostResponseSchemaDataItemCustom] = UNSET
    displayname: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    planningperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planningperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    remark: Union[Unset, str] = UNSET
    remark_planner: Union[Unset, str] = UNSET
    transport: Union[Unset, ProjectVehiclesCollectionpostResponseSchemaDataItemTransport] = UNSET
    vehicle: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_rate = self.cost_rate
        costs = self.costs
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        displayname = self.displayname
        function = self.function
        id = self.id
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

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

        vehicle = self.vehicle

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
        if costs is not UNSET:
            field_dict["costs"] = costs
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if custom is not UNSET:
            field_dict["custom"] = custom
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if function is not UNSET:
            field_dict["function"] = function
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
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
        if vehicle is not UNSET:
            field_dict["vehicle"] = vehicle

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_rate = d.pop("cost_rate", UNSET)

        costs = d.pop("costs", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        custom: Union[Unset, ProjectVehiclesCollectionpostResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectVehiclesCollectionpostResponseSchemaDataItemCustom.from_dict(_custom)

        displayname = d.pop("displayname", UNSET)

        function = d.pop("function", UNSET)

        id = d.pop("id", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

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

        transport: Union[Unset, ProjectVehiclesCollectionpostResponseSchemaDataItemTransport] = UNSET
        _transport = d.pop("transport", UNSET)
        if not isinstance(_transport, Unset):
            transport = ProjectVehiclesCollectionpostResponseSchemaDataItemTransport(_transport)

        vehicle = d.pop("vehicle", UNSET)

        project_vehicles_collectionpost_response_schema_data_item = cls(
            cost_rate=cost_rate,
            costs=costs,
            created=created,
            creator=creator,
            custom=custom,
            displayname=displayname,
            function=function,
            id=id,
            modified=modified,
            planningperiod_end=planningperiod_end,
            planningperiod_start=planningperiod_start,
            remark=remark,
            remark_planner=remark_planner,
            transport=transport,
            vehicle=vehicle,
        )

        project_vehicles_collectionpost_response_schema_data_item.additional_properties = d
        return project_vehicles_collectionpost_response_schema_data_item

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
