from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.vehicle_itempost_request_schema_custom import VehicleItempostRequestSchemaCustom
from ..models.vehicle_itempost_request_schema_multiple import VehicleItempostRequestSchemaMultiple
from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleItempostRequestSchema")


@attr.s(auto_attribs=True)
class VehicleItempostRequestSchema:
    """ """

    cost_rate: Union[Unset, None, str] = UNSET
    custom: Union[Unset, VehicleItempostRequestSchemaCustom] = UNSET
    folder: Union[Unset, None, str] = UNSET
    height: Union[Unset, float] = UNSET
    image: Union[Unset, None, str] = UNSET
    in_planner: Union[Unset, bool] = UNSET
    inspection_date: Union[Unset, None, str] = UNSET
    length: Union[Unset, float] = UNSET
    licenseplate: Union[Unset, str] = UNSET
    multiple: Union[Unset, VehicleItempostRequestSchemaMultiple] = UNSET
    name: Union[Unset, str] = UNSET
    payload_capacity: Union[Unset, float] = UNSET
    remark: Union[Unset, str] = UNSET
    seats: Union[Unset, int] = UNSET
    surface_area: Union[Unset, str] = UNSET
    width: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_rate = self.cost_rate
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        folder = self.folder
        height = self.height
        image = self.image
        in_planner = self.in_planner
        inspection_date = self.inspection_date
        length = self.length
        licenseplate = self.licenseplate
        multiple: Union[Unset, int] = UNSET
        if not isinstance(self.multiple, Unset):
            multiple = self.multiple.value

        name = self.name
        payload_capacity = self.payload_capacity
        remark = self.remark
        seats = self.seats
        surface_area = self.surface_area
        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
        if custom is not UNSET:
            field_dict["custom"] = custom
        if folder is not UNSET:
            field_dict["folder"] = folder
        if height is not UNSET:
            field_dict["height"] = height
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
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_rate = d.pop("cost_rate", UNSET)

        custom: Union[Unset, VehicleItempostRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = VehicleItempostRequestSchemaCustom.from_dict(_custom)

        folder = d.pop("folder", UNSET)

        height = d.pop("height", UNSET)

        image = d.pop("image", UNSET)

        in_planner = d.pop("in_planner", UNSET)

        inspection_date = d.pop("inspection_date", UNSET)

        length = d.pop("length", UNSET)

        licenseplate = d.pop("licenseplate", UNSET)

        multiple: Union[Unset, VehicleItempostRequestSchemaMultiple] = UNSET
        _multiple = d.pop("multiple", UNSET)
        if not isinstance(_multiple, Unset):
            multiple = VehicleItempostRequestSchemaMultiple(_multiple)

        name = d.pop("name", UNSET)

        payload_capacity = d.pop("payload_capacity", UNSET)

        remark = d.pop("remark", UNSET)

        seats = d.pop("seats", UNSET)

        surface_area = d.pop("surface_area", UNSET)

        width = d.pop("width", UNSET)

        vehicle_itempost_request_schema = cls(
            cost_rate=cost_rate,
            custom=custom,
            folder=folder,
            height=height,
            image=image,
            in_planner=in_planner,
            inspection_date=inspection_date,
            length=length,
            licenseplate=licenseplate,
            multiple=multiple,
            name=name,
            payload_capacity=payload_capacity,
            remark=remark,
            seats=seats,
            surface_area=surface_area,
            width=width,
        )

        vehicle_itempost_request_schema.additional_properties = d
        return vehicle_itempost_request_schema

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
