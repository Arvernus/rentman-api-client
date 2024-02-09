import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_function_collectionget_response_schema_data_item_custom import (
    ProjectFunctionCollectiongetResponseSchemaDataItemCustom,
)
from ..models.project_function_collectionget_response_schema_data_item_planperiod_end_schedule_is_start import (
    ProjectFunctionCollectiongetResponseSchemaDataItemPlanperiodEndScheduleIsStart,
)
from ..models.project_function_collectionget_response_schema_data_item_planperiod_start_schedule_is_start import (
    ProjectFunctionCollectiongetResponseSchemaDataItemPlanperiodStartScheduleIsStart,
)
from ..models.project_function_collectionget_response_schema_data_item_type import (
    ProjectFunctionCollectiongetResponseSchemaDataItemType,
)
from ..models.project_function_collectionget_response_schema_data_item_usageperiod_end_schedule_is_start import (
    ProjectFunctionCollectiongetResponseSchemaDataItemUsageperiodEndScheduleIsStart,
)
from ..models.project_function_collectionget_response_schema_data_item_usageperiod_start_schedule_is_start import (
    ProjectFunctionCollectiongetResponseSchemaDataItemUsageperiodStartScheduleIsStart,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectFunctionCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class ProjectFunctionCollectiongetResponseSchemaDataItem:
    """ """

    amount: Union[Unset, int] = UNSET
    break_: Union[Unset, None, float] = UNSET
    cost_rate: Union[Unset, str] = UNSET
    costs_fixed: Union[Unset, float] = UNSET
    costs_total: Union[Unset, float] = UNSET
    costs_variable: Union[Unset, float] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    custom: Union[Unset, ProjectFunctionCollectiongetResponseSchemaDataItemCustom] = UNSET
    displayname: Union[Unset, str] = UNSET
    distance: Union[Unset, float] = UNSET
    duration: Union[Unset, None, float] = UNSET
    group: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    in_financial: Union[Unset, bool] = UNSET
    in_planning: Union[Unset, bool] = UNSET
    is_plannable: Union[Unset, bool] = UNSET
    is_template: Union[Unset, bool] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    name_external: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end_schedule_is_start: Union[
        Unset, ProjectFunctionCollectiongetResponseSchemaDataItemPlanperiodEndScheduleIsStart
    ] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start_schedule_is_start: Union[
        Unset, ProjectFunctionCollectiongetResponseSchemaDataItemPlanperiodStartScheduleIsStart
    ] = UNSET
    price_fixed: Union[Unset, float] = UNSET
    price_rate: Union[Unset, str] = UNSET
    price_total: Union[Unset, float] = UNSET
    price_variable: Union[Unset, float] = UNSET
    project: Union[Unset, str] = UNSET
    remark_client: Union[Unset, str] = UNSET
    remark_crew: Union[Unset, str] = UNSET
    remark_planner: Union[Unset, str] = UNSET
    subproject: Union[Unset, str] = UNSET
    tags: Union[Unset, str] = UNSET
    taxclass: Union[Unset, None, str] = UNSET
    travel_time_after: Union[Unset, None, float] = UNSET
    travel_time_before: Union[Unset, None, float] = UNSET
    twoway: Union[Unset, bool] = UNSET
    type: Union[Unset, ProjectFunctionCollectiongetResponseSchemaDataItemType] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_end_schedule_is_start: Union[
        Unset, ProjectFunctionCollectiongetResponseSchemaDataItemUsageperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_start_schedule_is_start: Union[
        Unset, ProjectFunctionCollectiongetResponseSchemaDataItemUsageperiodStartScheduleIsStart
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        break_ = self.break_
        cost_rate = self.cost_rate
        costs_fixed = self.costs_fixed
        costs_total = self.costs_total
        costs_variable = self.costs_variable
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        displayname = self.displayname
        distance = self.distance
        duration = self.duration
        group = self.group
        id = self.id
        in_financial = self.in_financial
        in_planning = self.in_planning
        is_plannable = self.is_plannable
        is_template = self.is_template
        ledger = self.ledger
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

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

        price_fixed = self.price_fixed
        price_rate = self.price_rate
        price_total = self.price_total
        price_variable = self.price_variable
        project = self.project
        remark_client = self.remark_client
        remark_crew = self.remark_crew
        remark_planner = self.remark_planner
        subproject = self.subproject
        tags = self.tags
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
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if break_ is not UNSET:
            field_dict["break"] = break_
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
        if costs_fixed is not UNSET:
            field_dict["costs_fixed"] = costs_fixed
        if costs_total is not UNSET:
            field_dict["costs_total"] = costs_total
        if costs_variable is not UNSET:
            field_dict["costs_variable"] = costs_variable
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if custom is not UNSET:
            field_dict["custom"] = custom
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if distance is not UNSET:
            field_dict["distance"] = distance
        if duration is not UNSET:
            field_dict["duration"] = duration
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
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
        if modified is not UNSET:
            field_dict["modified"] = modified
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
        if price_fixed is not UNSET:
            field_dict["price_fixed"] = price_fixed
        if price_rate is not UNSET:
            field_dict["price_rate"] = price_rate
        if price_total is not UNSET:
            field_dict["price_total"] = price_total
        if price_variable is not UNSET:
            field_dict["price_variable"] = price_variable
        if project is not UNSET:
            field_dict["project"] = project
        if remark_client is not UNSET:
            field_dict["remark_client"] = remark_client
        if remark_crew is not UNSET:
            field_dict["remark_crew"] = remark_crew
        if remark_planner is not UNSET:
            field_dict["remark_planner"] = remark_planner
        if subproject is not UNSET:
            field_dict["subproject"] = subproject
        if tags is not UNSET:
            field_dict["tags"] = tags
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
        amount = d.pop("amount", UNSET)

        break_ = d.pop("break", UNSET)

        cost_rate = d.pop("cost_rate", UNSET)

        costs_fixed = d.pop("costs_fixed", UNSET)

        costs_total = d.pop("costs_total", UNSET)

        costs_variable = d.pop("costs_variable", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        custom: Union[Unset, ProjectFunctionCollectiongetResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectFunctionCollectiongetResponseSchemaDataItemCustom.from_dict(_custom)

        displayname = d.pop("displayname", UNSET)

        distance = d.pop("distance", UNSET)

        duration = d.pop("duration", UNSET)

        group = d.pop("group", UNSET)

        id = d.pop("id", UNSET)

        in_financial = d.pop("in_financial", UNSET)

        in_planning = d.pop("in_planning", UNSET)

        is_plannable = d.pop("is_plannable", UNSET)

        is_template = d.pop("is_template", UNSET)

        ledger = d.pop("ledger", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        name_external = d.pop("name_external", UNSET)

        order = d.pop("order", UNSET)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        planperiod_end_schedule_is_start: Union[
            Unset, ProjectFunctionCollectiongetResponseSchemaDataItemPlanperiodEndScheduleIsStart
        ] = UNSET
        _planperiod_end_schedule_is_start = d.pop("planperiod_end_schedule_is_start", UNSET)
        if not isinstance(_planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = (
                ProjectFunctionCollectiongetResponseSchemaDataItemPlanperiodEndScheduleIsStart(
                    _planperiod_end_schedule_is_start
                )
            )

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_start_schedule_is_start: Union[
            Unset, ProjectFunctionCollectiongetResponseSchemaDataItemPlanperiodStartScheduleIsStart
        ] = UNSET
        _planperiod_start_schedule_is_start = d.pop("planperiod_start_schedule_is_start", UNSET)
        if not isinstance(_planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = (
                ProjectFunctionCollectiongetResponseSchemaDataItemPlanperiodStartScheduleIsStart(
                    _planperiod_start_schedule_is_start
                )
            )

        price_fixed = d.pop("price_fixed", UNSET)

        price_rate = d.pop("price_rate", UNSET)

        price_total = d.pop("price_total", UNSET)

        price_variable = d.pop("price_variable", UNSET)

        project = d.pop("project", UNSET)

        remark_client = d.pop("remark_client", UNSET)

        remark_crew = d.pop("remark_crew", UNSET)

        remark_planner = d.pop("remark_planner", UNSET)

        subproject = d.pop("subproject", UNSET)

        tags = d.pop("tags", UNSET)

        taxclass = d.pop("taxclass", UNSET)

        travel_time_after = d.pop("travel_time_after", UNSET)

        travel_time_before = d.pop("travel_time_before", UNSET)

        twoway = d.pop("twoway", UNSET)

        type: Union[Unset, ProjectFunctionCollectiongetResponseSchemaDataItemType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = ProjectFunctionCollectiongetResponseSchemaDataItemType(_type)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        usageperiod_end_schedule_is_start: Union[
            Unset, ProjectFunctionCollectiongetResponseSchemaDataItemUsageperiodEndScheduleIsStart
        ] = UNSET
        _usageperiod_end_schedule_is_start = d.pop("usageperiod_end_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = (
                ProjectFunctionCollectiongetResponseSchemaDataItemUsageperiodEndScheduleIsStart(
                    _usageperiod_end_schedule_is_start
                )
            )

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        usageperiod_start_schedule_is_start: Union[
            Unset, ProjectFunctionCollectiongetResponseSchemaDataItemUsageperiodStartScheduleIsStart
        ] = UNSET
        _usageperiod_start_schedule_is_start = d.pop("usageperiod_start_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = (
                ProjectFunctionCollectiongetResponseSchemaDataItemUsageperiodStartScheduleIsStart(
                    _usageperiod_start_schedule_is_start
                )
            )

        project_function_collectionget_response_schema_data_item = cls(
            amount=amount,
            break_=break_,
            cost_rate=cost_rate,
            costs_fixed=costs_fixed,
            costs_total=costs_total,
            costs_variable=costs_variable,
            created=created,
            creator=creator,
            custom=custom,
            displayname=displayname,
            distance=distance,
            duration=duration,
            group=group,
            id=id,
            in_financial=in_financial,
            in_planning=in_planning,
            is_plannable=is_plannable,
            is_template=is_template,
            ledger=ledger,
            modified=modified,
            name=name,
            name_external=name_external,
            order=order,
            planperiod_end=planperiod_end,
            planperiod_end_schedule_is_start=planperiod_end_schedule_is_start,
            planperiod_start=planperiod_start,
            planperiod_start_schedule_is_start=planperiod_start_schedule_is_start,
            price_fixed=price_fixed,
            price_rate=price_rate,
            price_total=price_total,
            price_variable=price_variable,
            project=project,
            remark_client=remark_client,
            remark_crew=remark_crew,
            remark_planner=remark_planner,
            subproject=subproject,
            tags=tags,
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

        project_function_collectionget_response_schema_data_item.additional_properties = d
        return project_function_collectionget_response_schema_data_item

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
