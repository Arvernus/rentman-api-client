import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.projectfunctiongroup_itemget_request_schema_planperiod_end_schedule_is_start import (
    ProjectfunctiongroupItemgetRequestSchemaPlanperiodEndScheduleIsStart,
)
from ..models.projectfunctiongroup_itemget_request_schema_planperiod_start_schedule_is_start import (
    ProjectfunctiongroupItemgetRequestSchemaPlanperiodStartScheduleIsStart,
)
from ..models.projectfunctiongroup_itemget_request_schema_usageperiod_end_schedule_is_start import (
    ProjectfunctiongroupItemgetRequestSchemaUsageperiodEndScheduleIsStart,
)
from ..models.projectfunctiongroup_itemget_request_schema_usageperiod_start_schedule_is_start import (
    ProjectfunctiongroupItemgetRequestSchemaUsageperiodStartScheduleIsStart,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectfunctiongroupItemgetRequestSchema")


@attr.s(auto_attribs=True)
class ProjectfunctiongroupItemgetRequestSchema:
    """ """

    subproject: str
    name: Union[Unset, str] = UNSET
    duration: Union[Unset, None, float] = UNSET
    planperiod_start_schedule_is_start: Union[
        Unset, ProjectfunctiongroupItemgetRequestSchemaPlanperiodStartScheduleIsStart
    ] = UNSET
    usageperiod_start_schedule_is_start: Union[
        Unset, ProjectfunctiongroupItemgetRequestSchemaUsageperiodStartScheduleIsStart
    ] = UNSET
    planperiod_end_schedule_is_start: Union[
        Unset, ProjectfunctiongroupItemgetRequestSchemaPlanperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_end_schedule_is_start: Union[
        Unset, ProjectfunctiongroupItemgetRequestSchemaUsageperiodEndScheduleIsStart
    ] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    remark: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subproject = self.subproject
        name = self.name
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
        field_dict.update(
            {
                "subproject": subproject,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
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
        subproject = d.pop("subproject")

        name = d.pop("name", UNSET)

        duration = d.pop("duration", UNSET)

        planperiod_start_schedule_is_start: Union[
            Unset, ProjectfunctiongroupItemgetRequestSchemaPlanperiodStartScheduleIsStart
        ] = UNSET
        _planperiod_start_schedule_is_start = d.pop("planperiod_start_schedule_is_start", UNSET)
        if not isinstance(_planperiod_start_schedule_is_start, Unset):
            planperiod_start_schedule_is_start = ProjectfunctiongroupItemgetRequestSchemaPlanperiodStartScheduleIsStart(
                _planperiod_start_schedule_is_start
            )

        usageperiod_start_schedule_is_start: Union[
            Unset, ProjectfunctiongroupItemgetRequestSchemaUsageperiodStartScheduleIsStart
        ] = UNSET
        _usageperiod_start_schedule_is_start = d.pop("usageperiod_start_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_start_schedule_is_start, Unset):
            usageperiod_start_schedule_is_start = (
                ProjectfunctiongroupItemgetRequestSchemaUsageperiodStartScheduleIsStart(
                    _usageperiod_start_schedule_is_start
                )
            )

        planperiod_end_schedule_is_start: Union[
            Unset, ProjectfunctiongroupItemgetRequestSchemaPlanperiodEndScheduleIsStart
        ] = UNSET
        _planperiod_end_schedule_is_start = d.pop("planperiod_end_schedule_is_start", UNSET)
        if not isinstance(_planperiod_end_schedule_is_start, Unset):
            planperiod_end_schedule_is_start = ProjectfunctiongroupItemgetRequestSchemaPlanperiodEndScheduleIsStart(
                _planperiod_end_schedule_is_start
            )

        usageperiod_end_schedule_is_start: Union[
            Unset, ProjectfunctiongroupItemgetRequestSchemaUsageperiodEndScheduleIsStart
        ] = UNSET
        _usageperiod_end_schedule_is_start = d.pop("usageperiod_end_schedule_is_start", UNSET)
        if not isinstance(_usageperiod_end_schedule_is_start, Unset):
            usageperiod_end_schedule_is_start = ProjectfunctiongroupItemgetRequestSchemaUsageperiodEndScheduleIsStart(
                _usageperiod_end_schedule_is_start
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

        projectfunctiongroup_itemget_request_schema = cls(
            subproject=subproject,
            name=name,
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

        projectfunctiongroup_itemget_request_schema.additional_properties = d
        return projectfunctiongroup_itemget_request_schema

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
