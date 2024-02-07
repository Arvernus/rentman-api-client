import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.planningtransport_collectionpost_response_schema_data_item_custom import (
    PlanningtransportCollectionpostResponseSchemaDataItemCustom,
)
from ..models.planningtransport_collectionpost_response_schema_data_item_transport import (
    PlanningtransportCollectionpostResponseSchemaDataItemTransport,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanningtransportCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class PlanningtransportCollectionpostResponseSchemaDataItem:
    """ """

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    cost_rate: Union[Unset, None, str] = UNSET
    function: Union[Unset, str] = UNSET
    transport: Union[Unset, PlanningtransportCollectionpostResponseSchemaDataItemTransport] = UNSET
    vehicle: Union[Unset, str] = UNSET
    planningperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planningperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    remark: Union[Unset, str] = UNSET
    remark_planner: Union[Unset, str] = UNSET
    costs: Union[Unset, float] = UNSET
    custom: Union[Unset, PlanningtransportCollectionpostResponseSchemaDataItemCustom] = UNSET
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
        cost_rate = self.cost_rate
        function = self.function
        transport: Union[Unset, str] = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.value

        vehicle = self.vehicle
        planningperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planningperiod_start, Unset):
            planningperiod_start = self.planningperiod_start.isoformat() if self.planningperiod_start else None

        planningperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planningperiod_end, Unset):
            planningperiod_end = self.planningperiod_end.isoformat() if self.planningperiod_end else None

        remark = self.remark
        remark_planner = self.remark_planner
        costs = self.costs
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

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
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
        if function is not UNSET:
            field_dict["function"] = function
        if transport is not UNSET:
            field_dict["transport"] = transport
        if vehicle is not UNSET:
            field_dict["vehicle"] = vehicle
        if planningperiod_start is not UNSET:
            field_dict["planningperiod_start"] = planningperiod_start
        if planningperiod_end is not UNSET:
            field_dict["planningperiod_end"] = planningperiod_end
        if remark is not UNSET:
            field_dict["remark"] = remark
        if remark_planner is not UNSET:
            field_dict["remark_planner"] = remark_planner
        if costs is not UNSET:
            field_dict["costs"] = costs
        if custom is not UNSET:
            field_dict["custom"] = custom

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

        cost_rate = d.pop("cost_rate", UNSET)

        function = d.pop("function", UNSET)

        transport: Union[Unset, PlanningtransportCollectionpostResponseSchemaDataItemTransport] = UNSET
        _transport = d.pop("transport", UNSET)
        if not isinstance(_transport, Unset):
            transport = PlanningtransportCollectionpostResponseSchemaDataItemTransport(_transport)

        vehicle = d.pop("vehicle", UNSET)

        planningperiod_start = None
        _planningperiod_start = d.pop("planningperiod_start", UNSET)
        if _planningperiod_start is not None and not isinstance(_planningperiod_start, Unset):
            planningperiod_start = isoparse(_planningperiod_start)

        planningperiod_end = None
        _planningperiod_end = d.pop("planningperiod_end", UNSET)
        if _planningperiod_end is not None and not isinstance(_planningperiod_end, Unset):
            planningperiod_end = isoparse(_planningperiod_end)

        remark = d.pop("remark", UNSET)

        remark_planner = d.pop("remark_planner", UNSET)

        costs = d.pop("costs", UNSET)

        custom: Union[Unset, PlanningtransportCollectionpostResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = PlanningtransportCollectionpostResponseSchemaDataItemCustom.from_dict(_custom)

        planningtransport_collectionpost_response_schema_data_item = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            cost_rate=cost_rate,
            function=function,
            transport=transport,
            vehicle=vehicle,
            planningperiod_start=planningperiod_start,
            planningperiod_end=planningperiod_end,
            remark=remark,
            remark_planner=remark_planner,
            costs=costs,
            custom=custom,
        )

        planningtransport_collectionpost_response_schema_data_item.additional_properties = d
        return planningtransport_collectionpost_response_schema_data_item

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
