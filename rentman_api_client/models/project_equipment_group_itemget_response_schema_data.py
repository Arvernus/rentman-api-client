import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectEquipmentGroupItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class ProjectEquipmentGroupItemgetResponseSchemaData:
    """All the data about the requested items"""

    additional_scanned: Union[Unset, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    current: Union[Unset, float] = UNSET
    displayname: Union[Unset, str] = UNSET
    duration: Union[Unset, None, float] = UNSET
    id: Union[Unset, int] = UNSET
    in_price_calculation: Union[Unset, bool] = UNSET
    is_delayed: Union[Unset, bool] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    power: Union[Unset, float] = UNSET
    project: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    subproject: Union[Unset, str] = UNSET
    total_new_price: Union[Unset, float] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    volume: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additional_scanned = self.additional_scanned
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        current = self.current
        displayname = self.displayname
        duration = self.duration
        id = self.id
        in_price_calculation = self.in_price_calculation
        is_delayed = self.is_delayed
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        order = self.order
        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        power = self.power
        project = self.project
        remark = self.remark
        subproject = self.subproject
        total_new_price = self.total_new_price
        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        volume = self.volume
        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_scanned is not UNSET:
            field_dict["additional_scanned"] = additional_scanned
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if current is not UNSET:
            field_dict["current"] = current
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if duration is not UNSET:
            field_dict["duration"] = duration
        if id is not UNSET:
            field_dict["id"] = id
        if in_price_calculation is not UNSET:
            field_dict["in_price_calculation"] = in_price_calculation
        if is_delayed is not UNSET:
            field_dict["is_delayed"] = is_delayed
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if power is not UNSET:
            field_dict["power"] = power
        if project is not UNSET:
            field_dict["project"] = project
        if remark is not UNSET:
            field_dict["remark"] = remark
        if subproject is not UNSET:
            field_dict["subproject"] = subproject
        if total_new_price is not UNSET:
            field_dict["total_new_price"] = total_new_price
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start
        if volume is not UNSET:
            field_dict["volume"] = volume
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        additional_scanned = d.pop("additional_scanned", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        current = d.pop("current", UNSET)

        displayname = d.pop("displayname", UNSET)

        duration = d.pop("duration", UNSET)

        id = d.pop("id", UNSET)

        in_price_calculation = d.pop("in_price_calculation", UNSET)

        is_delayed = d.pop("is_delayed", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        power = d.pop("power", UNSET)

        project = d.pop("project", UNSET)

        remark = d.pop("remark", UNSET)

        subproject = d.pop("subproject", UNSET)

        total_new_price = d.pop("total_new_price", UNSET)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        volume = d.pop("volume", UNSET)

        weight = d.pop("weight", UNSET)

        project_equipment_group_itemget_response_schema_data = cls(
            additional_scanned=additional_scanned,
            created=created,
            creator=creator,
            current=current,
            displayname=displayname,
            duration=duration,
            id=id,
            in_price_calculation=in_price_calculation,
            is_delayed=is_delayed,
            modified=modified,
            name=name,
            order=order,
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            power=power,
            project=project,
            remark=remark,
            subproject=subproject,
            total_new_price=total_new_price,
            usageperiod_end=usageperiod_end,
            usageperiod_start=usageperiod_start,
            volume=volume,
            weight=weight,
        )

        project_equipment_group_itemget_response_schema_data.additional_properties = d
        return project_equipment_group_itemget_response_schema_data

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
