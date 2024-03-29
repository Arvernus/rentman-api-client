import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_crew_collectionpost_response_schema_data_item_custom import (
    ProjectCrewCollectionpostResponseSchemaDataItemCustom,
)
from ..models.project_crew_collectionpost_response_schema_data_item_transport import (
    ProjectCrewCollectionpostResponseSchemaDataItemTransport,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectCrewCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class ProjectCrewCollectionpostResponseSchemaDataItem:
    """ """

    cost_actual: Union[Unset, float] = UNSET
    cost_planned: Union[Unset, float] = UNSET
    cost_rate: Union[Unset, None, str] = UNSET
    costs: Union[Unset, float] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    crewmember: Union[Unset, str] = UNSET
    custom: Union[Unset, ProjectCrewCollectionpostResponseSchemaDataItemCustom] = UNSET
    displayname: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    hours_planned: Union[Unset, None, float] = UNSET
    hours_registered: Union[Unset, None, float] = UNSET
    id: Union[Unset, int] = UNSET
    invoice_reference: Union[Unset, str] = UNSET
    is_visible_on_dashboard: Union[Unset, bool] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    project_leader: Union[Unset, bool] = UNSET
    remark: Union[Unset, str] = UNSET
    remark_planner: Union[Unset, str] = UNSET
    transport: Union[Unset, ProjectCrewCollectionpostResponseSchemaDataItemTransport] = UNSET
    visible: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_actual = self.cost_actual
        cost_planned = self.cost_planned
        cost_rate = self.cost_rate
        costs = self.costs
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        crewmember = self.crewmember
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        displayname = self.displayname
        function = self.function
        hours_planned = self.hours_planned
        hours_registered = self.hours_registered
        id = self.id
        invoice_reference = self.invoice_reference
        is_visible_on_dashboard = self.is_visible_on_dashboard
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        project_leader = self.project_leader
        remark = self.remark
        remark_planner = self.remark_planner
        transport: Union[Unset, str] = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.value

        visible = self.visible

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_actual is not UNSET:
            field_dict["cost_actual"] = cost_actual
        if cost_planned is not UNSET:
            field_dict["cost_planned"] = cost_planned
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
        if costs is not UNSET:
            field_dict["costs"] = costs
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if crewmember is not UNSET:
            field_dict["crewmember"] = crewmember
        if custom is not UNSET:
            field_dict["custom"] = custom
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if function is not UNSET:
            field_dict["function"] = function
        if hours_planned is not UNSET:
            field_dict["hours_planned"] = hours_planned
        if hours_registered is not UNSET:
            field_dict["hours_registered"] = hours_registered
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_reference is not UNSET:
            field_dict["invoice_reference"] = invoice_reference
        if is_visible_on_dashboard is not UNSET:
            field_dict["is_visible_on_dashboard"] = is_visible_on_dashboard
        if modified is not UNSET:
            field_dict["modified"] = modified
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if project_leader is not UNSET:
            field_dict["project_leader"] = project_leader
        if remark is not UNSET:
            field_dict["remark"] = remark
        if remark_planner is not UNSET:
            field_dict["remark_planner"] = remark_planner
        if transport is not UNSET:
            field_dict["transport"] = transport
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_actual = d.pop("cost_actual", UNSET)

        cost_planned = d.pop("cost_planned", UNSET)

        cost_rate = d.pop("cost_rate", UNSET)

        costs = d.pop("costs", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        crewmember = d.pop("crewmember", UNSET)

        custom: Union[Unset, ProjectCrewCollectionpostResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectCrewCollectionpostResponseSchemaDataItemCustom.from_dict(_custom)

        displayname = d.pop("displayname", UNSET)

        function = d.pop("function", UNSET)

        hours_planned = d.pop("hours_planned", UNSET)

        hours_registered = d.pop("hours_registered", UNSET)

        id = d.pop("id", UNSET)

        invoice_reference = d.pop("invoice_reference", UNSET)

        is_visible_on_dashboard = d.pop("is_visible_on_dashboard", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        project_leader = d.pop("project_leader", UNSET)

        remark = d.pop("remark", UNSET)

        remark_planner = d.pop("remark_planner", UNSET)

        transport: Union[Unset, ProjectCrewCollectionpostResponseSchemaDataItemTransport] = UNSET
        _transport = d.pop("transport", UNSET)
        if not isinstance(_transport, Unset):
            transport = ProjectCrewCollectionpostResponseSchemaDataItemTransport(_transport)

        visible = d.pop("visible", UNSET)

        project_crew_collectionpost_response_schema_data_item = cls(
            cost_actual=cost_actual,
            cost_planned=cost_planned,
            cost_rate=cost_rate,
            costs=costs,
            created=created,
            creator=creator,
            crewmember=crewmember,
            custom=custom,
            displayname=displayname,
            function=function,
            hours_planned=hours_planned,
            hours_registered=hours_registered,
            id=id,
            invoice_reference=invoice_reference,
            is_visible_on_dashboard=is_visible_on_dashboard,
            modified=modified,
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            project_leader=project_leader,
            remark=remark,
            remark_planner=remark_planner,
            transport=transport,
            visible=visible,
        )

        project_crew_collectionpost_response_schema_data_item.additional_properties = d
        return project_crew_collectionpost_response_schema_data_item

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
