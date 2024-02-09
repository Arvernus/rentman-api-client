import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_function_group_collectionget_response_schema_data_item_planperiod_end_schedule_is_start import (
    ProjectFunctionGroupCollectiongetResponseSchemaDataItemPlanperiodEndScheduleIsStart,
)
from ..models.project_function_group_collectionget_response_schema_data_item_planperiod_start_schedule_is_start import (
    ProjectFunctionGroupCollectiongetResponseSchemaDataItemPlanperiodStartScheduleIsStart,
)
from ..models.project_function_group_collectionget_response_schema_data_item_usageperiod_end_schedule_is_start import (
    ProjectFunctionGroupCollectiongetResponseSchemaDataItemUsageperiodEndScheduleIsStart,
)
from ..models.project_function_group_collectionget_response_schema_data_item_usageperiod_start_schedule_is_start import (
    ProjectFunctionGroupCollectiongetResponseSchemaDataItemUsageperiodStartScheduleIsStart,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectFunctionGroupCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class ProjectFunctionGroupCollectiongetResponseSchemaDataItem:
    """ """

    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    duration: Union[Unset, None, float] = UNSET
    id: Union[Unset, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end_schedule_is_start: Union[
        Unset, ProjectFunctionGroupCollectiongetResponseSchemaDataItemPlanperiodEndScheduleIsStart
    ] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start_schedule_is_start: Union[
        Unset, ProjectFunctionGroupCollectiongetResponseSchemaDataItemPlanperiodStartScheduleIsStart
    ] = UNSET
    project: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    subproject: Union[Unset, str] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_end_schedule_is_start: Union[
        Unset, ProjectFunctionGroupCollectiongetResponseSchemaDataItemUsageperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_start_schedule_is_start: Union[
        Unset, ProjectFunctionGroupCollectiongetResponseSchemaDataItemUsageperiodStartScheduleIsStart
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        displayname = self.displayname
        duration = self.duration
        id = self.id
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        planperiod_end_schedule_is_start: Union[Unset, int] = UNSET
        if not isinstance(self.planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = self.planperiod_end_schedule_is_start.value

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        planperiod_start_schedule_is_start: Union[Unset, int] = UNSET
        if not isinstance(self.planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = self.planperiod_start_schedule_is_start.value

        project = self.project
        remark = self.remark
        subproject = self.subproject
        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        usageperiod_end_schedule_is_start: Union[Unset, int] = UNSET
        if not isinstance(self.usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = self.usageperiod_end_schedule_is_start.value

        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        usageperiod_start_schedule_is_start: Union[Unset, int] = UNSET
        if not isinstance(self.usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = self.usageperiod_start_schedule_is_start.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if duration is not UNSET:
            field_dict["duration"] = duration
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if planperiod_end_schedule_is_start is not UNSET:
            field_dict["planperiod_end_schedule_is_start"] = planperiod_end_schedule_is_start
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_start_schedule_is_start is not UNSET:
            field_dict["planperiod_start_schedule_is_start"] = planperiod_start_schedule_is_start
        if project is not UNSET:
            field_dict["project"] = project
        if remark is not UNSET:
            field_dict["remark"] = remark
        if subproject is not UNSET:
            field_dict["subproject"] = subproject
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
        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        duration = d.pop("duration", UNSET)

        id = d.pop("id", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        planperiod_end_schedule_is_start: Union[
            Unset, ProjectFunctionGroupCollectiongetResponseSchemaDataItemPlanperiodEndScheduleIsStart
        ] = UNSET
        _planperiod_end_schedule_is_start = d.pop("planperiod_end_schedule_is_start", UNSET)
        if not isinstance(_planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = (
                ProjectFunctionGroupCollectiongetResponseSchemaDataItemPlanperiodEndScheduleIsStart(
                    _planperiod_end_schedule_is_start
                )
            )

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_start_schedule_is_start: Union[
            Unset, ProjectFunctionGroupCollectiongetResponseSchemaDataItemPlanperiodStartScheduleIsStart
        ] = UNSET
        _planperiod_start_schedule_is_start = d.pop("planperiod_start_schedule_is_start", UNSET)
        if not isinstance(_planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = (
                ProjectFunctionGroupCollectiongetResponseSchemaDataItemPlanperiodStartScheduleIsStart(
                    _planperiod_start_schedule_is_start
                )
            )

        project = d.pop("project", UNSET)

        remark = d.pop("remark", UNSET)

        subproject = d.pop("subproject", UNSET)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        usageperiod_end_schedule_is_start: Union[
            Unset, ProjectFunctionGroupCollectiongetResponseSchemaDataItemUsageperiodEndScheduleIsStart
        ] = UNSET
        _usageperiod_end_schedule_is_start = d.pop("usageperiod_end_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = (
                ProjectFunctionGroupCollectiongetResponseSchemaDataItemUsageperiodEndScheduleIsStart(
                    _usageperiod_end_schedule_is_start
                )
            )

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        usageperiod_start_schedule_is_start: Union[
            Unset, ProjectFunctionGroupCollectiongetResponseSchemaDataItemUsageperiodStartScheduleIsStart
        ] = UNSET
        _usageperiod_start_schedule_is_start = d.pop("usageperiod_start_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = (
                ProjectFunctionGroupCollectiongetResponseSchemaDataItemUsageperiodStartScheduleIsStart(
                    _usageperiod_start_schedule_is_start
                )
            )

        project_function_group_collectionget_response_schema_data_item = cls(
            created=created,
            creator=creator,
            displayname=displayname,
            duration=duration,
            id=id,
            modified=modified,
            name=name,
            planperiod_end=planperiod_end,
            planperiod_end_schedule_is_start=planperiod_end_schedule_is_start,
            planperiod_start=planperiod_start,
            planperiod_start_schedule_is_start=planperiod_start_schedule_is_start,
            project=project,
            remark=remark,
            subproject=subproject,
            usageperiod_end=usageperiod_end,
            usageperiod_end_schedule_is_start=usageperiod_end_schedule_is_start,
            usageperiod_start=usageperiod_start,
            usageperiod_start_schedule_is_start=usageperiod_start_schedule_is_start,
        )

        project_function_group_collectionget_response_schema_data_item.additional_properties = d
        return project_function_group_collectionget_response_schema_data_item

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
