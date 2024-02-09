import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.projectfunction_itemget_request_schema_custom import ProjectfunctionItemgetRequestSchemaCustom
from ..models.projectfunction_itemget_request_schema_planperiod_end_schedule_is_start import (
    ProjectfunctionItemgetRequestSchemaPlanperiodEndScheduleIsStart,
)
from ..models.projectfunction_itemget_request_schema_planperiod_start_schedule_is_start import (
    ProjectfunctionItemgetRequestSchemaPlanperiodStartScheduleIsStart,
)
from ..models.projectfunction_itemget_request_schema_type import ProjectfunctionItemgetRequestSchemaType
from ..models.projectfunction_itemget_request_schema_usageperiod_end_schedule_is_start import (
    ProjectfunctionItemgetRequestSchemaUsageperiodEndScheduleIsStart,
)
from ..models.projectfunction_itemget_request_schema_usageperiod_start_schedule_is_start import (
    ProjectfunctionItemgetRequestSchemaUsageperiodStartScheduleIsStart,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectfunctionItemgetRequestSchema")


@attr.s(auto_attribs=True)
class ProjectfunctionItemgetRequestSchema:
    """ """

    cost_rate: str
    price_rate: str
    subproject: str
    is_template: Union[Unset, bool] = UNSET
    group: Union[Unset, None, str] = UNSET
    name_external: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    travel_time_before: Union[Unset, None, float] = UNSET
    travel_time_after: Union[Unset, None, float] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start_schedule_is_start: Union[
        Unset, ProjectfunctionItemgetRequestSchemaPlanperiodStartScheduleIsStart
    ] = UNSET
    usageperiod_start_schedule_is_start: Union[
        Unset, ProjectfunctionItemgetRequestSchemaUsageperiodStartScheduleIsStart
    ] = UNSET
    planperiod_end_schedule_is_start: Union[
        Unset, ProjectfunctionItemgetRequestSchemaPlanperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_end_schedule_is_start: Union[
        Unset, ProjectfunctionItemgetRequestSchemaUsageperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    type: Union[Unset, ProjectfunctionItemgetRequestSchemaType] = UNSET
    duration: Union[Unset, None, float] = UNSET
    amount: Union[Unset, int] = UNSET
    break_: Union[Unset, None, float] = UNSET
    distance: Union[Unset, float] = UNSET
    twoway: Union[Unset, bool] = UNSET
    taxclass: Union[Unset, None, str] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    order: Union[Unset, str] = UNSET
    remark_client: Union[Unset, str] = UNSET
    remark_planner: Union[Unset, str] = UNSET
    remark_crew: Union[Unset, str] = UNSET
    in_financial: Union[Unset, bool] = UNSET
    in_planning: Union[Unset, bool] = UNSET
    is_plannable: Union[Unset, bool] = UNSET
    custom: Union[Unset, ProjectfunctionItemgetRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_rate = self.cost_rate
        price_rate = self.price_rate
        subproject = self.subproject
        is_template = self.is_template
        group = self.group
        name_external = self.name_external
        name = self.name
        travel_time_before = self.travel_time_before
        travel_time_after = self.travel_time_after
        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        planperiod_start_schedule_is_start: Union[Unset, str] = UNSET
        if not isinstance(self.planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = self.planperiod_start_schedule_is_start.value

        usageperiod_start_schedule_is_start: Union[Unset, str] = UNSET
        if not isinstance(self.usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = self.usageperiod_start_schedule_is_start.value

        planperiod_end_schedule_is_start: Union[Unset, str] = UNSET
        if not isinstance(self.planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = self.planperiod_end_schedule_is_start.value

        usageperiod_end_schedule_is_start: Union[Unset, str] = UNSET
        if not isinstance(self.usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = self.usageperiod_end_schedule_is_start.value

        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        duration = self.duration
        amount = self.amount
        break_ = self.break_
        distance = self.distance
        twoway = self.twoway
        taxclass = self.taxclass
        ledger = self.ledger
        order = self.order
        remark_client = self.remark_client
        remark_planner = self.remark_planner
        remark_crew = self.remark_crew
        in_financial = self.in_financial
        in_planning = self.in_planning
        is_plannable = self.is_plannable
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost_rate": cost_rate,
                "price_rate": price_rate,
                "subproject": subproject,
            }
        )
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if group is not UNSET:
            field_dict["group"] = group
        if name_external is not UNSET:
            field_dict["name_external"] = name_external
        if name is not UNSET:
            field_dict["name"] = name
        if travel_time_before is not UNSET:
            field_dict["travel_time_before"] = travel_time_before
        if travel_time_after is not UNSET:
            field_dict["travel_time_after"] = travel_time_after
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start
        if planperiod_start_schedule_is_start is not UNSET:
            field_dict["planperiod_start_schedule_is_start"] = planperiod_start_schedule_is_start
        if usageperiod_start_schedule_is_start is not UNSET:
            field_dict["usageperiod_start_schedule_is_start"] = usageperiod_start_schedule_is_start
        if planperiod_end_schedule_is_start is not UNSET:
            field_dict["planperiod_end_schedule_is_start"] = planperiod_end_schedule_is_start
        if usageperiod_end_schedule_is_start is not UNSET:
            field_dict["usageperiod_end_schedule_is_start"] = usageperiod_end_schedule_is_start
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if type is not UNSET:
            field_dict["type"] = type
        if duration is not UNSET:
            field_dict["duration"] = duration
        if amount is not UNSET:
            field_dict["amount"] = amount
        if break_ is not UNSET:
            field_dict["break"] = break_
        if distance is not UNSET:
            field_dict["distance"] = distance
        if twoway is not UNSET:
            field_dict["twoway"] = twoway
        if taxclass is not UNSET:
            field_dict["taxclass"] = taxclass
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if order is not UNSET:
            field_dict["order"] = order
        if remark_client is not UNSET:
            field_dict["remark_client"] = remark_client
        if remark_planner is not UNSET:
            field_dict["remark_planner"] = remark_planner
        if remark_crew is not UNSET:
            field_dict["remark_crew"] = remark_crew
        if in_financial is not UNSET:
            field_dict["in_financial"] = in_financial
        if in_planning is not UNSET:
            field_dict["in_planning"] = in_planning
        if is_plannable is not UNSET:
            field_dict["is_plannable"] = is_plannable
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_rate = d.pop("cost_rate")

        price_rate = d.pop("price_rate")

        subproject = d.pop("subproject")

        is_template = d.pop("is_template", UNSET)

        group = d.pop("group", UNSET)

        name_external = d.pop("name_external", UNSET)

        name = d.pop("name", UNSET)

        travel_time_before = d.pop("travel_time_before", UNSET)

        travel_time_after = d.pop("travel_time_after", UNSET)

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        planperiod_start_schedule_is_start: Union[
            Unset, ProjectfunctionItemgetRequestSchemaPlanperiodStartScheduleIsStart
        ] = UNSET
        _planperiod_start_schedule_is_start = d.pop("planperiod_start_schedule_is_start", UNSET)
        if not isinstance(_planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = ProjectfunctionItemgetRequestSchemaPlanperiodStartScheduleIsStart(
                _planperiod_start_schedule_is_start
            )

        usageperiod_start_schedule_is_start: Union[
            Unset, ProjectfunctionItemgetRequestSchemaUsageperiodStartScheduleIsStart
        ] = UNSET
        _usageperiod_start_schedule_is_start = d.pop("usageperiod_start_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = ProjectfunctionItemgetRequestSchemaUsageperiodStartScheduleIsStart(
                _usageperiod_start_schedule_is_start
            )

        planperiod_end_schedule_is_start: Union[
            Unset, ProjectfunctionItemgetRequestSchemaPlanperiodEndScheduleIsStart
        ] = UNSET
        _planperiod_end_schedule_is_start = d.pop("planperiod_end_schedule_is_start", UNSET)
        if not isinstance(_planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = ProjectfunctionItemgetRequestSchemaPlanperiodEndScheduleIsStart(
                _planperiod_end_schedule_is_start
            )

        usageperiod_end_schedule_is_start: Union[
            Unset, ProjectfunctionItemgetRequestSchemaUsageperiodEndScheduleIsStart
        ] = UNSET
        _usageperiod_end_schedule_is_start = d.pop("usageperiod_end_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = ProjectfunctionItemgetRequestSchemaUsageperiodEndScheduleIsStart(
                _usageperiod_end_schedule_is_start
            )

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        type: Union[Unset, ProjectfunctionItemgetRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = ProjectfunctionItemgetRequestSchemaType(_type)

        duration = d.pop("duration", UNSET)

        amount = d.pop("amount", UNSET)

        break_ = d.pop("break", UNSET)

        distance = d.pop("distance", UNSET)

        twoway = d.pop("twoway", UNSET)

        taxclass = d.pop("taxclass", UNSET)

        ledger = d.pop("ledger", UNSET)

        order = d.pop("order", UNSET)

        remark_client = d.pop("remark_client", UNSET)

        remark_planner = d.pop("remark_planner", UNSET)

        remark_crew = d.pop("remark_crew", UNSET)

        in_financial = d.pop("in_financial", UNSET)

        in_planning = d.pop("in_planning", UNSET)

        is_plannable = d.pop("is_plannable", UNSET)

        custom: Union[Unset, ProjectfunctionItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectfunctionItemgetRequestSchemaCustom.from_dict(_custom)

        projectfunction_itemget_request_schema = cls(
            cost_rate=cost_rate,
            price_rate=price_rate,
            subproject=subproject,
            is_template=is_template,
            group=group,
            name_external=name_external,
            name=name,
            travel_time_before=travel_time_before,
            travel_time_after=travel_time_after,
            usageperiod_start=usageperiod_start,
            planperiod_start_schedule_is_start=planperiod_start_schedule_is_start,
            usageperiod_start_schedule_is_start=usageperiod_start_schedule_is_start,
            planperiod_end_schedule_is_start=planperiod_end_schedule_is_start,
            usageperiod_end_schedule_is_start=usageperiod_end_schedule_is_start,
            usageperiod_end=usageperiod_end,
            planperiod_start=planperiod_start,
            planperiod_end=planperiod_end,
            type=type,
            duration=duration,
            amount=amount,
            break_=break_,
            distance=distance,
            twoway=twoway,
            taxclass=taxclass,
            ledger=ledger,
            order=order,
            remark_client=remark_client,
            remark_planner=remark_planner,
            remark_crew=remark_crew,
            in_financial=in_financial,
            in_planning=in_planning,
            is_plannable=is_plannable,
            custom=custom,
        )

        projectfunction_itemget_request_schema.additional_properties = d
        return projectfunction_itemget_request_schema

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
