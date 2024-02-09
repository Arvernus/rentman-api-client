import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.projectcrew_itemput_request_schema_custom import ProjectcrewItemputRequestSchemaCustom
from ..models.projectcrew_itemput_request_schema_transport import ProjectcrewItemputRequestSchemaTransport
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectcrewItemputRequestSchema")


@attr.s(auto_attribs=True)
class ProjectcrewItemputRequestSchema:
    """ """

    crewmember: str
    cost_rate: Union[Unset, None, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    transport: Union[Unset, ProjectcrewItemputRequestSchemaTransport] = UNSET
    remark: Union[Unset, str] = UNSET
    remark_planner: Union[Unset, str] = UNSET
    invoice_reference: Union[Unset, str] = UNSET
    project_leader: Union[Unset, bool] = UNSET
    is_visible_on_dashboard: Union[Unset, bool] = UNSET
    custom: Union[Unset, ProjectcrewItemputRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        crewmember = self.crewmember
        cost_rate = self.cost_rate
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
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "crewmember": crewmember,
            }
        )
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
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
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        crewmember = d.pop("crewmember")

        cost_rate = d.pop("cost_rate", UNSET)

        visible = d.pop("visible", UNSET)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        transport: Union[Unset, ProjectcrewItemputRequestSchemaTransport] = UNSET
        _transport = d.pop("transport", UNSET)
        if not isinstance(_transport, Unset):
            transport = ProjectcrewItemputRequestSchemaTransport(_transport)

        remark = d.pop("remark", UNSET)

        remark_planner = d.pop("remark_planner", UNSET)

        invoice_reference = d.pop("invoice_reference", UNSET)

        project_leader = d.pop("project_leader", UNSET)

        is_visible_on_dashboard = d.pop("is_visible_on_dashboard", UNSET)

        custom: Union[Unset, ProjectcrewItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectcrewItemputRequestSchemaCustom.from_dict(_custom)

        projectcrew_itemput_request_schema = cls(
            crewmember=crewmember,
            cost_rate=cost_rate,
            visible=visible,
            planperiod_start=planperiod_start,
            planperiod_end=planperiod_end,
            transport=transport,
            remark=remark,
            remark_planner=remark_planner,
            invoice_reference=invoice_reference,
            project_leader=project_leader,
            is_visible_on_dashboard=is_visible_on_dashboard,
            custom=custom,
        )

        projectcrew_itemput_request_schema.additional_properties = d
        return projectcrew_itemput_request_schema

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
