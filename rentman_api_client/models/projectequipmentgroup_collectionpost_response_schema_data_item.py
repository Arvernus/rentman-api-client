import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectequipmentgroupCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class ProjectequipmentgroupCollectionpostResponseSchemaDataItem:
    """ """

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    subproject: Union[Unset, str] = UNSET
    additional_scanned: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    duration: Union[Unset, None, float] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    is_delayed: Union[Unset, bool] = UNSET
    order: Union[Unset, str] = UNSET
    in_price_calculation: Union[Unset, bool] = UNSET
    remark: Union[Unset, str] = UNSET
    volume: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    power: Union[Unset, float] = UNSET
    current: Union[Unset, float] = UNSET
    total_new_price: Union[Unset, float] = UNSET
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
        project = self.project
        subproject = self.subproject
        additional_scanned = self.additional_scanned
        name = self.name
        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        duration = self.duration
        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        is_delayed = self.is_delayed
        order = self.order
        in_price_calculation = self.in_price_calculation
        remark = self.remark
        volume = self.volume
        weight = self.weight
        power = self.power
        current = self.current
        total_new_price = self.total_new_price

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
        if project is not UNSET:
            field_dict["project"] = project
        if subproject is not UNSET:
            field_dict["subproject"] = subproject
        if additional_scanned is not UNSET:
            field_dict["additional_scanned"] = additional_scanned
        if name is not UNSET:
            field_dict["name"] = name
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if duration is not UNSET:
            field_dict["duration"] = duration
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if is_delayed is not UNSET:
            field_dict["is_delayed"] = is_delayed
        if order is not UNSET:
            field_dict["order"] = order
        if in_price_calculation is not UNSET:
            field_dict["in_price_calculation"] = in_price_calculation
        if remark is not UNSET:
            field_dict["remark"] = remark
        if volume is not UNSET:
            field_dict["volume"] = volume
        if weight is not UNSET:
            field_dict["weight"] = weight
        if power is not UNSET:
            field_dict["power"] = power
        if current is not UNSET:
            field_dict["current"] = current
        if total_new_price is not UNSET:
            field_dict["total_new_price"] = total_new_price

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

        project = d.pop("project", UNSET)

        subproject = d.pop("subproject", UNSET)

        additional_scanned = d.pop("additional_scanned", UNSET)

        name = d.pop("name", UNSET)

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        duration = d.pop("duration", UNSET)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        is_delayed = d.pop("is_delayed", UNSET)

        order = d.pop("order", UNSET)

        in_price_calculation = d.pop("in_price_calculation", UNSET)

        remark = d.pop("remark", UNSET)

        volume = d.pop("volume", UNSET)

        weight = d.pop("weight", UNSET)

        power = d.pop("power", UNSET)

        current = d.pop("current", UNSET)

        total_new_price = d.pop("total_new_price", UNSET)

        projectequipmentgroup_collectionpost_response_schema_data_item = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            project=project,
            subproject=subproject,
            additional_scanned=additional_scanned,
            name=name,
            usageperiod_start=usageperiod_start,
            usageperiod_end=usageperiod_end,
            duration=duration,
            planperiod_start=planperiod_start,
            planperiod_end=planperiod_end,
            is_delayed=is_delayed,
            order=order,
            in_price_calculation=in_price_calculation,
            remark=remark,
            volume=volume,
            weight=weight,
            power=power,
            current=current,
            total_new_price=total_new_price,
        )

        projectequipmentgroup_collectionpost_response_schema_data_item.additional_properties = d
        return projectequipmentgroup_collectionpost_response_schema_data_item

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
