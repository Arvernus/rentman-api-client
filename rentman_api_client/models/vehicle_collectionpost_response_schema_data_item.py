import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.vehicle_collectionpost_response_schema_data_item_custom import (
    VehicleCollectionpostResponseSchemaDataItemCustom,
)
from ..models.vehicle_collectionpost_response_schema_data_item_multiple import (
    VehicleCollectionpostResponseSchemaDataItemMultiple,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class VehicleCollectionpostResponseSchemaDataItem:
    """ """

    cost_rate: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    custom: Union[Unset, VehicleCollectionpostResponseSchemaDataItemCustom] = UNSET
    displayname: Union[Unset, str] = UNSET
    distance_cost: Union[Unset, float] = UNSET
    fixed_cost: Union[Unset, float] = UNSET
    folder: Union[Unset, None, str] = UNSET
    height: Union[Unset, float] = UNSET
    id: Union[Unset, int] = UNSET
    image: Union[Unset, None, str] = UNSET
    in_planner: Union[Unset, bool] = UNSET
    inspection_date: Union[Unset, None, str] = UNSET
    length: Union[Unset, float] = UNSET
    licenseplate: Union[Unset, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    multiple: Union[Unset, VehicleCollectionpostResponseSchemaDataItemMultiple] = UNSET
    name: Union[Unset, str] = UNSET
    payload_capacity: Union[Unset, float] = UNSET
    remark: Union[Unset, str] = UNSET
    seats: Union[Unset, int] = UNSET
    surface_area: Union[Unset, str] = UNSET
    tags: Union[Unset, str] = UNSET
    width: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_rate = self.cost_rate
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        displayname = self.displayname
        distance_cost = self.distance_cost
        fixed_cost = self.fixed_cost
        folder = self.folder
        height = self.height
        id = self.id
        image = self.image
        in_planner = self.in_planner
        inspection_date = self.inspection_date
        length = self.length
        licenseplate = self.licenseplate
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        multiple: Union[Unset, int] = UNSET
        if not isinstance(self.multiple, Unset):
            multiple = self.multiple.value

        name = self.name
        payload_capacity = self.payload_capacity
        remark = self.remark
        seats = self.seats
        surface_area = self.surface_area
        tags = self.tags
        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if custom is not UNSET:
            field_dict["custom"] = custom
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if distance_cost is not UNSET:
            field_dict["distance_cost"] = distance_cost
        if fixed_cost is not UNSET:
            field_dict["fixed_cost"] = fixed_cost
        if folder is not UNSET:
            field_dict["folder"] = folder
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if in_planner is not UNSET:
            field_dict["in_planner"] = in_planner
        if inspection_date is not UNSET:
            field_dict["inspection_date"] = inspection_date
        if length is not UNSET:
            field_dict["length"] = length
        if licenseplate is not UNSET:
            field_dict["licenseplate"] = licenseplate
        if modified is not UNSET:
            field_dict["modified"] = modified
        if multiple is not UNSET:
            field_dict["multiple"] = multiple
        if name is not UNSET:
            field_dict["name"] = name
        if payload_capacity is not UNSET:
            field_dict["payload_capacity"] = payload_capacity
        if remark is not UNSET:
            field_dict["remark"] = remark
        if seats is not UNSET:
            field_dict["seats"] = seats
        if surface_area is not UNSET:
            field_dict["surface_area"] = surface_area
        if tags is not UNSET:
            field_dict["tags"] = tags
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_rate = d.pop("cost_rate", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        custom: Union[Unset, VehicleCollectionpostResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = VehicleCollectionpostResponseSchemaDataItemCustom.from_dict(_custom)

        displayname = d.pop("displayname", UNSET)

        distance_cost = d.pop("distance_cost", UNSET)

        fixed_cost = d.pop("fixed_cost", UNSET)

        folder = d.pop("folder", UNSET)

        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        in_planner = d.pop("in_planner", UNSET)

        inspection_date = d.pop("inspection_date", UNSET)

        length = d.pop("length", UNSET)

        licenseplate = d.pop("licenseplate", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        multiple: Union[Unset, VehicleCollectionpostResponseSchemaDataItemMultiple] = UNSET
        _multiple = d.pop("multiple", UNSET)
        if not isinstance(_multiple, Unset):
            multiple = VehicleCollectionpostResponseSchemaDataItemMultiple(_multiple)

        name = d.pop("name", UNSET)

        payload_capacity = d.pop("payload_capacity", UNSET)

        remark = d.pop("remark", UNSET)

        seats = d.pop("seats", UNSET)

        surface_area = d.pop("surface_area", UNSET)

        tags = d.pop("tags", UNSET)

        width = d.pop("width", UNSET)

        vehicle_collectionpost_response_schema_data_item = cls(
            cost_rate=cost_rate,
            created=created,
            creator=creator,
            custom=custom,
            displayname=displayname,
            distance_cost=distance_cost,
            fixed_cost=fixed_cost,
            folder=folder,
            height=height,
            id=id,
            image=image,
            in_planner=in_planner,
            inspection_date=inspection_date,
            length=length,
            licenseplate=licenseplate,
            modified=modified,
            multiple=multiple,
            name=name,
            payload_capacity=payload_capacity,
            remark=remark,
            seats=seats,
            surface_area=surface_area,
            tags=tags,
            width=width,
        )

        vehicle_collectionpost_response_schema_data_item.additional_properties = d
        return vehicle_collectionpost_response_schema_data_item

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
