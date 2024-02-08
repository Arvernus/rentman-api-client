import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.functie_itemget_response_schema_data_custom import FunctieItemgetResponseSchemaDataCustom
from ..models.functie_itemget_response_schema_data_planperiod_end_schedule_is_start import (
    FunctieItemgetResponseSchemaDataPlanperiodEndScheduleIsStart,
)
from ..models.functie_itemget_response_schema_data_planperiod_start_schedule_is_start import (
    FunctieItemgetResponseSchemaDataPlanperiodStartScheduleIsStart,
)
from ..models.functie_itemget_response_schema_data_type import FunctieItemgetResponseSchemaDataType
from ..models.functie_itemget_response_schema_data_usageperiod_end_schedule_is_start import (
    FunctieItemgetResponseSchemaDataUsageperiodEndScheduleIsStart,
)
from ..models.functie_itemget_response_schema_data_usageperiod_start_schedule_is_start import (
    FunctieItemgetResponseSchemaDataUsageperiodStartScheduleIsStart,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FunctieItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class FunctieItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    cost_rate: Union[Unset, str] = UNSET
    price_rate: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    subproject: Union[Unset, str] = UNSET
    is_template: Union[Unset, bool] = UNSET
    group: Union[Unset, None, str] = UNSET
    name_external: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    travel_time_before: Union[Unset, None, float] = UNSET
    travel_time_after: Union[Unset, None, float] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start_schedule_is_start: Union[
        Unset, FunctieItemgetResponseSchemaDataPlanperiodStartScheduleIsStart
    ] = UNSET
    usageperiod_start_schedule_is_start: Union[
        Unset, FunctieItemgetResponseSchemaDataUsageperiodStartScheduleIsStart
    ] = UNSET
    planperiod_end_schedule_is_start: Union[Unset, FunctieItemgetResponseSchemaDataPlanperiodEndScheduleIsStart] = UNSET
    usageperiod_end_schedule_is_start: Union[
        Unset, FunctieItemgetResponseSchemaDataUsageperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    type: Union[Unset, FunctieItemgetResponseSchemaDataType] = UNSET
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
    price_fixed: Union[Unset, float] = UNSET
    price_variable: Union[Unset, float] = UNSET
    costs_fixed: Union[Unset, float] = UNSET
    costs_variable: Union[Unset, float] = UNSET
    price_total: Union[Unset, float] = UNSET
    costs_total: Union[Unset, float] = UNSET
    tags: Union[Unset, str] = UNSET
    custom: Union[Unset, FunctieItemgetResponseSchemaDataCustom] = UNSET
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
        price_rate = self.price_rate
        project = self.project
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
        price_fixed = self.price_fixed
        price_variable = self.price_variable
        costs_fixed = self.costs_fixed
        costs_variable = self.costs_variable
        price_total = self.price_total
        costs_total = self.costs_total
        tags = self.tags
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
        if price_rate is not UNSET:
            field_dict["price_rate"] = price_rate
        if project is not UNSET:
            field_dict["project"] = project
        if subproject is not UNSET:
            field_dict["subproject"] = subproject
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
        if price_fixed is not UNSET:
            field_dict["price_fixed"] = price_fixed
        if price_variable is not UNSET:
            field_dict["price_variable"] = price_variable
        if costs_fixed is not UNSET:
            field_dict["costs_fixed"] = costs_fixed
        if costs_variable is not UNSET:
            field_dict["costs_variable"] = costs_variable
        if price_total is not UNSET:
            field_dict["price_total"] = price_total
        if costs_total is not UNSET:
            field_dict["costs_total"] = costs_total
        if tags is not UNSET:
            field_dict["tags"] = tags
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

        price_rate = d.pop("price_rate", UNSET)

        project = d.pop("project", UNSET)

        subproject = d.pop("subproject", UNSET)

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
            Unset, FunctieItemgetResponseSchemaDataPlanperiodStartScheduleIsStart
        ] = UNSET
        _planperiod_start_schedule_is_start = d.pop("planperiod_start_schedule_is_start", UNSET)
        if not isinstance(_planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = FunctieItemgetResponseSchemaDataPlanperiodStartScheduleIsStart(
                _planperiod_start_schedule_is_start
            )

        usageperiod_start_schedule_is_start: Union[
            Unset, FunctieItemgetResponseSchemaDataUsageperiodStartScheduleIsStart
        ] = UNSET
        _usageperiod_start_schedule_is_start = d.pop("usageperiod_start_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = FunctieItemgetResponseSchemaDataUsageperiodStartScheduleIsStart(
                _usageperiod_start_schedule_is_start
            )

        planperiod_end_schedule_is_start: Union[
            Unset, FunctieItemgetResponseSchemaDataPlanperiodEndScheduleIsStart
        ] = UNSET
        _planperiod_end_schedule_is_start = d.pop("planperiod_end_schedule_is_start", UNSET)
        if not isinstance(_planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = FunctieItemgetResponseSchemaDataPlanperiodEndScheduleIsStart(
                _planperiod_end_schedule_is_start
            )

        usageperiod_end_schedule_is_start: Union[
            Unset, FunctieItemgetResponseSchemaDataUsageperiodEndScheduleIsStart
        ] = UNSET
        _usageperiod_end_schedule_is_start = d.pop("usageperiod_end_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = FunctieItemgetResponseSchemaDataUsageperiodEndScheduleIsStart(
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

        type: Union[Unset, FunctieItemgetResponseSchemaDataType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = FunctieItemgetResponseSchemaDataType(_type)

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

        price_fixed = d.pop("price_fixed", UNSET)

        price_variable = d.pop("price_variable", UNSET)

        costs_fixed = d.pop("costs_fixed", UNSET)

        costs_variable = d.pop("costs_variable", UNSET)

        price_total = d.pop("price_total", UNSET)

        costs_total = d.pop("costs_total", UNSET)

        tags = d.pop("tags", UNSET)

        custom: Union[Unset, FunctieItemgetResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = FunctieItemgetResponseSchemaDataCustom.from_dict(_custom)

        functie_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            cost_rate=cost_rate,
            price_rate=price_rate,
            project=project,
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
            price_fixed=price_fixed,
            price_variable=price_variable,
            costs_fixed=costs_fixed,
            costs_variable=costs_variable,
            price_total=price_total,
            costs_total=costs_total,
            tags=tags,
            custom=custom,
        )

        functie_itemget_response_schema_data.additional_properties = d
        return functie_itemget_response_schema_data

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
