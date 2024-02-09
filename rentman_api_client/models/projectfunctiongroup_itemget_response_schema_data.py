import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.projectfunctiongroup_itemget_response_schema_data_planperiod_end_schedule_is_start import (
    ProjectfunctiongroupItemgetResponseSchemaDataPlanperiodEndScheduleIsStart,
)
from ..models.projectfunctiongroup_itemget_response_schema_data_planperiod_start_schedule_is_start import (
    ProjectfunctiongroupItemgetResponseSchemaDataPlanperiodStartScheduleIsStart,
)
from ..models.projectfunctiongroup_itemget_response_schema_data_usageperiod_end_schedule_is_start import (
    ProjectfunctiongroupItemgetResponseSchemaDataUsageperiodEndScheduleIsStart,
)
from ..models.projectfunctiongroup_itemget_response_schema_data_usageperiod_start_schedule_is_start import (
    ProjectfunctiongroupItemgetResponseSchemaDataUsageperiodStartScheduleIsStart,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectfunctiongroupItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class ProjectfunctiongroupItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    subproject: Union[Unset, str] = UNSET
    duration: Union[Unset, None, float] = UNSET
    planperiod_start_schedule_is_start: Union[
        Unset, ProjectfunctiongroupItemgetResponseSchemaDataPlanperiodStartScheduleIsStart
    ] = UNSET
    usageperiod_start_schedule_is_start: Union[
        Unset, ProjectfunctiongroupItemgetResponseSchemaDataUsageperiodStartScheduleIsStart
    ] = UNSET
    planperiod_end_schedule_is_start: Union[
        Unset, ProjectfunctiongroupItemgetResponseSchemaDataPlanperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_end_schedule_is_start: Union[
        Unset, ProjectfunctiongroupItemgetResponseSchemaDataUsageperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    remark: Union[Unset, str] = UNSET
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
        name = self.name
        project = self.project
        subproject = self.subproject
        duration = self.duration
        planperiod_start_schedule_is_start: Union[Unset, int] = UNSET
        if not isinstance(self.planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = self.planperiod_start_schedule_is_start.value

        usageperiod_start_schedule_is_start: Union[Unset, int] = UNSET
        if not isinstance(self.usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = self.usageperiod_start_schedule_is_start.value

        planperiod_end_schedule_is_start: Union[Unset, int] = UNSET
        if not isinstance(self.planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = self.planperiod_end_schedule_is_start.value

        usageperiod_end_schedule_is_start: Union[Unset, int] = UNSET
        if not isinstance(self.usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = self.usageperiod_end_schedule_is_start.value

        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        remark = self.remark

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
        if name is not UNSET:
            field_dict["name"] = name
        if project is not UNSET:
            field_dict["project"] = project
        if subproject is not UNSET:
            field_dict["subproject"] = subproject
        if duration is not UNSET:
            field_dict["duration"] = duration
        if planperiod_start_schedule_is_start is not UNSET:
            field_dict["planperiod_start_schedule_is_start"] = planperiod_start_schedule_is_start
        if usageperiod_start_schedule_is_start is not UNSET:
            field_dict["usageperiod_start_schedule_is_start"] = usageperiod_start_schedule_is_start
        if planperiod_end_schedule_is_start is not UNSET:
            field_dict["planperiod_end_schedule_is_start"] = planperiod_end_schedule_is_start
        if usageperiod_end_schedule_is_start is not UNSET:
            field_dict["usageperiod_end_schedule_is_start"] = usageperiod_end_schedule_is_start
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if remark is not UNSET:
            field_dict["remark"] = remark

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

        name = d.pop("name", UNSET)

        project = d.pop("project", UNSET)

        subproject = d.pop("subproject", UNSET)

        duration = d.pop("duration", UNSET)

        planperiod_start_schedule_is_start: Union[
            Unset, ProjectfunctiongroupItemgetResponseSchemaDataPlanperiodStartScheduleIsStart
        ] = UNSET
        _planperiod_start_schedule_is_start = d.pop("planperiod_start_schedule_is_start", UNSET)
        if not isinstance(_planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = (
                ProjectfunctiongroupItemgetResponseSchemaDataPlanperiodStartScheduleIsStart(
                    _planperiod_start_schedule_is_start
                )
            )

        usageperiod_start_schedule_is_start: Union[
            Unset, ProjectfunctiongroupItemgetResponseSchemaDataUsageperiodStartScheduleIsStart
        ] = UNSET
        _usageperiod_start_schedule_is_start = d.pop("usageperiod_start_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = (
                ProjectfunctiongroupItemgetResponseSchemaDataUsageperiodStartScheduleIsStart(
                    _usageperiod_start_schedule_is_start
                )
            )

        planperiod_end_schedule_is_start: Union[
            Unset, ProjectfunctiongroupItemgetResponseSchemaDataPlanperiodEndScheduleIsStart
        ] = UNSET
        _planperiod_end_schedule_is_start = d.pop("planperiod_end_schedule_is_start", UNSET)
        if not isinstance(_planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = (
                ProjectfunctiongroupItemgetResponseSchemaDataPlanperiodEndScheduleIsStart(
                    _planperiod_end_schedule_is_start
                )
            )

        usageperiod_end_schedule_is_start: Union[
            Unset, ProjectfunctiongroupItemgetResponseSchemaDataUsageperiodEndScheduleIsStart
        ] = UNSET
        _usageperiod_end_schedule_is_start = d.pop("usageperiod_end_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = (
                ProjectfunctiongroupItemgetResponseSchemaDataUsageperiodEndScheduleIsStart(
                    _usageperiod_end_schedule_is_start
                )
            )

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

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

        remark = d.pop("remark", UNSET)

        projectfunctiongroup_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            name=name,
            project=project,
            subproject=subproject,
            duration=duration,
            planperiod_start_schedule_is_start=planperiod_start_schedule_is_start,
            usageperiod_start_schedule_is_start=usageperiod_start_schedule_is_start,
            planperiod_end_schedule_is_start=planperiod_end_schedule_is_start,
            usageperiod_end_schedule_is_start=usageperiod_end_schedule_is_start,
            usageperiod_start=usageperiod_start,
            usageperiod_end=usageperiod_end,
            planperiod_start=planperiod_start,
            planperiod_end=planperiod_end,
            remark=remark,
        )

        projectfunctiongroup_itemget_response_schema_data.additional_properties = d
        return projectfunctiongroup_itemget_response_schema_data

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
