import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.planningpersoneel_itemget_response_schema_data_custom import (
    PlanningpersoneelItemgetResponseSchemaDataCustom,
)
from ..models.planningpersoneel_itemget_response_schema_data_transport import (
    PlanningpersoneelItemgetResponseSchemaDataTransport,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanningpersoneelItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class PlanningpersoneelItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    cost_rate: Union[Unset, None, str] = UNSET
    function: Union[Unset, str] = UNSET
    crewmember: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    transport: Union[Unset, PlanningpersoneelItemgetResponseSchemaDataTransport] = UNSET
    remark: Union[Unset, str] = UNSET
    remark_planner: Union[Unset, str] = UNSET
    invoice_reference: Union[Unset, str] = UNSET
    project_leader: Union[Unset, bool] = UNSET
    is_visible_on_dashboard: Union[Unset, bool] = UNSET
    costs: Union[Unset, float] = UNSET
    cost_actual: Union[Unset, float] = UNSET
    hours_registered: Union[Unset, None, float] = UNSET
    hours_planned: Union[Unset, None, float] = UNSET
    cost_planned: Union[Unset, float] = UNSET
    custom: Union[Unset, PlanningpersoneelItemgetResponseSchemaDataCustom] = UNSET
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
        crewmember = self.crewmember
        visible = self.visible
        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        transport: Union[Unset, str] = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.value

        remark = self.remark
        remark_planner = self.remark_planner
        invoice_reference = self.invoice_reference
        project_leader = self.project_leader
        is_visible_on_dashboard = self.is_visible_on_dashboard
        costs = self.costs
        cost_actual = self.cost_actual
        hours_registered = self.hours_registered
        hours_planned = self.hours_planned
        cost_planned = self.cost_planned
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
        if crewmember is not UNSET:
            field_dict["crewmember"] = crewmember
        if visible is not UNSET:
            field_dict["visible"] = visible
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if transport is not UNSET:
            field_dict["transport"] = transport
        if remark is not UNSET:
            field_dict["remark"] = remark
        if remark_planner is not UNSET:
            field_dict["remark_planner"] = remark_planner
        if invoice_reference is not UNSET:
            field_dict["invoice_reference"] = invoice_reference
        if project_leader is not UNSET:
            field_dict["project_leader"] = project_leader
        if is_visible_on_dashboard is not UNSET:
            field_dict["is_visible_on_dashboard"] = is_visible_on_dashboard
        if costs is not UNSET:
            field_dict["costs"] = costs
        if cost_actual is not UNSET:
            field_dict["cost_actual"] = cost_actual
        if hours_registered is not UNSET:
            field_dict["hours_registered"] = hours_registered
        if hours_planned is not UNSET:
            field_dict["hours_planned"] = hours_planned
        if cost_planned is not UNSET:
            field_dict["cost_planned"] = cost_planned
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

        crewmember = d.pop("crewmember", UNSET)

        visible = d.pop("visible", UNSET)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        transport: Union[Unset, PlanningpersoneelItemgetResponseSchemaDataTransport] = UNSET
        _transport = d.pop("transport", UNSET)
        if not isinstance(_transport, Unset):
            transport = PlanningpersoneelItemgetResponseSchemaDataTransport(_transport)

        remark = d.pop("remark", UNSET)

        remark_planner = d.pop("remark_planner", UNSET)

        invoice_reference = d.pop("invoice_reference", UNSET)

        project_leader = d.pop("project_leader", UNSET)

        is_visible_on_dashboard = d.pop("is_visible_on_dashboard", UNSET)

        costs = d.pop("costs", UNSET)

        cost_actual = d.pop("cost_actual", UNSET)

        hours_registered = d.pop("hours_registered", UNSET)

        hours_planned = d.pop("hours_planned", UNSET)

        cost_planned = d.pop("cost_planned", UNSET)

        custom: Union[Unset, PlanningpersoneelItemgetResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = PlanningpersoneelItemgetResponseSchemaDataCustom.from_dict(_custom)

        planningpersoneel_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            cost_rate=cost_rate,
            function=function,
            crewmember=crewmember,
            visible=visible,
            planperiod_start=planperiod_start,
            planperiod_end=planperiod_end,
            transport=transport,
            remark=remark,
            remark_planner=remark_planner,
            invoice_reference=invoice_reference,
            project_leader=project_leader,
            is_visible_on_dashboard=is_visible_on_dashboard,
            costs=costs,
            cost_actual=cost_actual,
            hours_registered=hours_registered,
            hours_planned=hours_planned,
            cost_planned=cost_planned,
            custom=custom,
        )

        planningpersoneel_itemget_response_schema_data.additional_properties = d
        return planningpersoneel_itemget_response_schema_data

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
