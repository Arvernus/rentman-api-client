import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_function_itemget_request_schema_custom import ProjectFunctionItemgetRequestSchemaCustom
from ..models.project_function_itemget_request_schema_planperiod_end_schedule_is_start import (
    ProjectFunctionItemgetRequestSchemaPlanperiodEndScheduleIsStart,
)
from ..models.project_function_itemget_request_schema_planperiod_start_schedule_is_start import (
    ProjectFunctionItemgetRequestSchemaPlanperiodStartScheduleIsStart,
)
from ..models.project_function_itemget_request_schema_type import ProjectFunctionItemgetRequestSchemaType
from ..models.project_function_itemget_request_schema_usageperiod_end_schedule_is_start import (
    ProjectFunctionItemgetRequestSchemaUsageperiodEndScheduleIsStart,
)
from ..models.project_function_itemget_request_schema_usageperiod_start_schedule_is_start import (
    ProjectFunctionItemgetRequestSchemaUsageperiodStartScheduleIsStart,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectFunctionItemgetRequestSchema")


@attr.s(auto_attribs=True)
class ProjectFunctionItemgetRequestSchema:
    """ """

    cost_rate: str
    price_rate: str
    subproject: str
    amount: Union[Unset, int] = UNSET
    break_: Union[Unset, None, float] = UNSET
    custom: Union[Unset, ProjectFunctionItemgetRequestSchemaCustom] = UNSET
    distance: Union[Unset, float] = UNSET
    duration: Union[Unset, None, float] = UNSET
    group: Union[Unset, None, str] = UNSET
    in_financial: Union[Unset, bool] = UNSET
    in_planning: Union[Unset, bool] = UNSET
    is_plannable: Union[Unset, bool] = UNSET
    is_template: Union[Unset, bool] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    name_external: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end_schedule_is_start: Union[
        Unset, ProjectFunctionItemgetRequestSchemaPlanperiodEndScheduleIsStart
    ] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start_schedule_is_start: Union[
        Unset, ProjectFunctionItemgetRequestSchemaPlanperiodStartScheduleIsStart
    ] = UNSET
    remark_client: Union[Unset, str] = UNSET
    remark_crew: Union[Unset, str] = UNSET
    remark_planner: Union[Unset, str] = UNSET
    taxclass: Union[Unset, None, str] = UNSET
    travel_time_after: Union[Unset, None, float] = UNSET
    travel_time_before: Union[Unset, None, float] = UNSET
    twoway: Union[Unset, bool] = UNSET
    type: Union[Unset, ProjectFunctionItemgetRequestSchemaType] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_end_schedule_is_start: Union[
        Unset, ProjectFunctionItemgetRequestSchemaUsageperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_start_schedule_is_start: Union[
        Unset, ProjectFunctionItemgetRequestSchemaUsageperiodStartScheduleIsStart
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_rate = self.cost_rate
        price_rate = self.price_rate
        subproject = self.subproject
        amount = self.amount
        break_ = self.break_
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        distance = self.distance
        duration = self.duration
        group = self.group
        in_financial = self.in_financial
        in_planning = self.in_planning
        is_plannable = self.is_plannable
        is_template = self.is_template
        ledger = self.ledger
        name = self.name
        name_external = self.name_external
        order = self.order
        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        planperiod_end_schedule_is_start: Union[Unset, str] = UNSET
        if not isinstance(self.planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = self.planperiod_end_schedule_is_start.value

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        planperiod_start_schedule_is_start: Union[Unset, str] = UNSET
        if not isinstance(self.planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = self.planperiod_start_schedule_is_start.value

        remark_client = self.remark_client
        remark_crew = self.remark_crew
        remark_planner = self.remark_planner
        taxclass = self.taxclass
        travel_time_after = self.travel_time_after
        travel_time_before = self.travel_time_before
        twoway = self.twoway
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        usageperiod_end_schedule_is_start: Union[Unset, str] = UNSET
        if not isinstance(self.usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = self.usageperiod_end_schedule_is_start.value

        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        usageperiod_start_schedule_is_start: Union[Unset, str] = UNSET
        if not isinstance(self.usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = self.usageperiod_start_schedule_is_start.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost_rate": cost_rate,
                "price_rate": price_rate,
                "subproject": subproject,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if break_ is not UNSET:
            field_dict["break"] = break_
        if custom is not UNSET:
            field_dict["custom"] = custom
        if distance is not UNSET:
            field_dict["distance"] = distance
        if duration is not UNSET:
            field_dict["duration"] = duration
        if group is not UNSET:
            field_dict["group"] = group
        if in_financial is not UNSET:
            field_dict["in_financial"] = in_financial
        if in_planning is not UNSET:
            field_dict["in_planning"] = in_planning
        if is_plannable is not UNSET:
            field_dict["is_plannable"] = is_plannable
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if name is not UNSET:
            field_dict["name"] = name
        if name_external is not UNSET:
            field_dict["name_external"] = name_external
        if order is not UNSET:
            field_dict["order"] = order
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if planperiod_end_schedule_is_start is not UNSET:
            field_dict["planperiod_end_schedule_is_start"] = planperiod_end_schedule_is_start
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_start_schedule_is_start is not UNSET:
            field_dict["planperiod_start_schedule_is_start"] = planperiod_start_schedule_is_start
        if remark_client is not UNSET:
            field_dict["remark_client"] = remark_client
        if remark_crew is not UNSET:
            field_dict["remark_crew"] = remark_crew
        if remark_planner is not UNSET:
            field_dict["remark_planner"] = remark_planner
        if taxclass is not UNSET:
            field_dict["taxclass"] = taxclass
        if travel_time_after is not UNSET:
            field_dict["travel_time_after"] = travel_time_after
        if travel_time_before is not UNSET:
            field_dict["travel_time_before"] = travel_time_before
        if twoway is not UNSET:
            field_dict["twoway"] = twoway
        if type is not UNSET:
            field_dict["type"] = type
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if usageperiod_end_schedule_is_start is not UNSET:
            field_dict["usageperiod_end_schedule_is_start"] = usageperiod_end_schedule_is_start
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start
        if usageperiod_start_schedule_is_start is not UNSET:
            field_dict["usageperiod_start_schedule_is_start"] = usageperiod_start_schedule_is_start

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_rate = d.pop("cost_rate")

        price_rate = d.pop("price_rate")

        subproject = d.pop("subproject")

        amount = d.pop("amount", UNSET)

        break_ = d.pop("break", UNSET)

        custom: Union[Unset, ProjectFunctionItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectFunctionItemgetRequestSchemaCustom.from_dict(_custom)

        distance = d.pop("distance", UNSET)

        duration = d.pop("duration", UNSET)

        group = d.pop("group", UNSET)

        in_financial = d.pop("in_financial", UNSET)

        in_planning = d.pop("in_planning", UNSET)

        is_plannable = d.pop("is_plannable", UNSET)

        is_template = d.pop("is_template", UNSET)

        ledger = d.pop("ledger", UNSET)

        name = d.pop("name", UNSET)

        name_external = d.pop("name_external", UNSET)

        order = d.pop("order", UNSET)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        planperiod_end_schedule_is_start: Union[
            Unset, ProjectFunctionItemgetRequestSchemaPlanperiodEndScheduleIsStart
        ] = UNSET
        _planperiod_end_schedule_is_start = d.pop("planperiod_end_schedule_is_start", UNSET)
        if not isinstance(_planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = ProjectFunctionItemgetRequestSchemaPlanperiodEndScheduleIsStart(
                _planperiod_end_schedule_is_start
            )

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_start_schedule_is_start: Union[
            Unset, ProjectFunctionItemgetRequestSchemaPlanperiodStartScheduleIsStart
        ] = UNSET
        _planperiod_start_schedule_is_start = d.pop("planperiod_start_schedule_is_start", UNSET)
        if not isinstance(_planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = ProjectFunctionItemgetRequestSchemaPlanperiodStartScheduleIsStart(
                _planperiod_start_schedule_is_start
            )

        remark_client = d.pop("remark_client", UNSET)

        remark_crew = d.pop("remark_crew", UNSET)

        remark_planner = d.pop("remark_planner", UNSET)

        taxclass = d.pop("taxclass", UNSET)

        travel_time_after = d.pop("travel_time_after", UNSET)

        travel_time_before = d.pop("travel_time_before", UNSET)

        twoway = d.pop("twoway", UNSET)

        type: Union[Unset, ProjectFunctionItemgetRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = ProjectFunctionItemgetRequestSchemaType(_type)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        usageperiod_end_schedule_is_start: Union[
            Unset, ProjectFunctionItemgetRequestSchemaUsageperiodEndScheduleIsStart
        ] = UNSET
        _usageperiod_end_schedule_is_start = d.pop("usageperiod_end_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = ProjectFunctionItemgetRequestSchemaUsageperiodEndScheduleIsStart(
                _usageperiod_end_schedule_is_start
            )

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        usageperiod_start_schedule_is_start: Union[
            Unset, ProjectFunctionItemgetRequestSchemaUsageperiodStartScheduleIsStart
        ] = UNSET
        _usageperiod_start_schedule_is_start = d.pop("usageperiod_start_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = ProjectFunctionItemgetRequestSchemaUsageperiodStartScheduleIsStart(
                _usageperiod_start_schedule_is_start
            )

        project_function_itemget_request_schema = cls(
            cost_rate=cost_rate,
            price_rate=price_rate,
            subproject=subproject,
            amount=amount,
            break_=break_,
            custom=custom,
            distance=distance,
            duration=duration,
            group=group,
            in_financial=in_financial,
            in_planning=in_planning,
            is_plannable=is_plannable,
            is_template=is_template,
            ledger=ledger,
            name=name,
            name_external=name_external,
            order=order,
            planperiod_end=planperiod_end,
            planperiod_end_schedule_is_start=planperiod_end_schedule_is_start,
            planperiod_start=planperiod_start,
            planperiod_start_schedule_is_start=planperiod_start_schedule_is_start,
            remark_client=remark_client,
            remark_crew=remark_crew,
            remark_planner=remark_planner,
            taxclass=taxclass,
            travel_time_after=travel_time_after,
            travel_time_before=travel_time_before,
            twoway=twoway,
            type=type,
            usageperiod_end=usageperiod_end,
            usageperiod_end_schedule_is_start=usageperiod_end_schedule_is_start,
            usageperiod_start=usageperiod_start,
            usageperiod_start_schedule_is_start=usageperiod_start_schedule_is_start,
        )

        project_function_itemget_request_schema.additional_properties = d
        return project_function_itemget_request_schema

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
