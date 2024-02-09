import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.vehicle_itemget_response_schema_data_custom import VehicleItemgetResponseSchemaDataCustom
from ..models.vehicle_itemget_response_schema_data_multiple import VehicleItemgetResponseSchemaDataMultiple
from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class VehicleItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    folder: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    cost_rate: Union[Unset, None, str] = UNSET
    in_planner: Union[Unset, bool] = UNSET
    height: Union[Unset, float] = UNSET
    length: Union[Unset, float] = UNSET
    width: Union[Unset, float] = UNSET
    seats: Union[Unset, int] = UNSET
    inspection_date: Union[Unset, None, str] = UNSET
    licenseplate: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    payload_capacity: Union[Unset, float] = UNSET
    surface_area: Union[Unset, str] = UNSET
    multiple: Union[Unset, VehicleItemgetResponseSchemaDataMultiple] = UNSET
    image: Union[Unset, None, str] = UNSET
    tags: Union[Unset, str] = UNSET
    distance_cost: Union[Unset, float] = UNSET
    fixed_cost: Union[Unset, float] = UNSET
    custom: Union[Unset, VehicleItemgetResponseSchemaDataCustom] = UNSET
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
        folder = self.folder
        name = self.name
        cost_rate = self.cost_rate
        in_planner = self.in_planner
        height = self.height
        length = self.length
        width = self.width
        seats = self.seats
        inspection_date = self.inspection_date
        licenseplate = self.licenseplate
        remark = self.remark
        payload_capacity = self.payload_capacity
        surface_area = self.surface_area
        multiple: Union[Unset, int] = UNSET
        if not isinstance(self.multiple, Unset):
            multiple = self.multiple.value

        image = self.image
        tags = self.tags
        distance_cost = self.distance_cost
        fixed_cost = self.fixed_cost
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
        if folder is not UNSET:
            field_dict["folder"] = folder
        if name is not UNSET:
            field_dict["name"] = name
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
        if in_planner is not UNSET:
            field_dict["in_planner"] = in_planner
        if height is not UNSET:
            field_dict["height"] = height
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if seats is not UNSET:
            field_dict["seats"] = seats
        if inspection_date is not UNSET:
            field_dict["inspection_date"] = inspection_date
        if licenseplate is not UNSET:
            field_dict["licenseplate"] = licenseplate
        if remark is not UNSET:
            field_dict["remark"] = remark
        if payload_capacity is not UNSET:
            field_dict["payload_capacity"] = payload_capacity
        if surface_area is not UNSET:
            field_dict["surface_area"] = surface_area
        if multiple is not UNSET:
            field_dict["multiple"] = multiple
        if image is not UNSET:
            field_dict["image"] = image
        if tags is not UNSET:
            field_dict["tags"] = tags
        if distance_cost is not UNSET:
            field_dict["distance_cost"] = distance_cost
        if fixed_cost is not UNSET:
            field_dict["fixed_cost"] = fixed_cost
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

        folder = d.pop("folder", UNSET)

        name = d.pop("name", UNSET)

        cost_rate = d.pop("cost_rate", UNSET)

        in_planner = d.pop("in_planner", UNSET)

        height = d.pop("height", UNSET)

        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        seats = d.pop("seats", UNSET)

        inspection_date = d.pop("inspection_date", UNSET)

        licenseplate = d.pop("licenseplate", UNSET)

        remark = d.pop("remark", UNSET)

        payload_capacity = d.pop("payload_capacity", UNSET)

        surface_area = d.pop("surface_area", UNSET)

        multiple: Union[Unset, VehicleItemgetResponseSchemaDataMultiple] = UNSET
        _multiple = d.pop("multiple", UNSET)
        if not isinstance(_multiple, Unset):
            multiple = VehicleItemgetResponseSchemaDataMultiple(_multiple)

        image = d.pop("image", UNSET)

        tags = d.pop("tags", UNSET)

        distance_cost = d.pop("distance_cost", UNSET)

        fixed_cost = d.pop("fixed_cost", UNSET)

        custom: Union[Unset, VehicleItemgetResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = VehicleItemgetResponseSchemaDataCustom.from_dict(_custom)

        vehicle_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            folder=folder,
            name=name,
            cost_rate=cost_rate,
            in_planner=in_planner,
            height=height,
            length=length,
            width=width,
            seats=seats,
            inspection_date=inspection_date,
            licenseplate=licenseplate,
            remark=remark,
            payload_capacity=payload_capacity,
            surface_area=surface_area,
            multiple=multiple,
            image=image,
            tags=tags,
            distance_cost=distance_cost,
            fixed_cost=fixed_cost,
            custom=custom,
        )

        vehicle_itemget_response_schema_data.additional_properties = d
        return vehicle_itemget_response_schema_data

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
