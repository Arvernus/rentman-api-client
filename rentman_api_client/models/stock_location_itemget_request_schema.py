from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.stock_location_itemget_request_schema_country import StockLocationItemgetRequestSchemaCountry
from ..models.stock_location_itemget_request_schema_type import StockLocationItemgetRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StockLocationItemgetRequestSchema")


@attr.s(auto_attribs=True)
class StockLocationItemgetRequestSchema:
    """ """

    active: Union[Unset, bool] = UNSET
    city: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    country: Union[Unset, StockLocationItemgetRequestSchemaCountry] = UNSET
    house_number: Union[Unset, str] = UNSET
    in_archive: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    state_province: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    type: Union[Unset, StockLocationItemgetRequestSchemaType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        city = self.city
        color = self.color
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        house_number = self.house_number
        in_archive = self.in_archive
        name = self.name
        postal_code = self.postal_code
        state_province = self.state_province
        street = self.street
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if city is not UNSET:
            field_dict["city"] = city
        if color is not UNSET:
            field_dict["color"] = color
        if country is not UNSET:
            field_dict["country"] = country
        if house_number is not UNSET:
            field_dict["house_number"] = house_number
        if in_archive is not UNSET:
            field_dict["in_archive"] = in_archive
        if name is not UNSET:
            field_dict["name"] = name
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if state_province is not UNSET:
            field_dict["state_province"] = state_province
        if street is not UNSET:
            field_dict["street"] = street
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active", UNSET)

        city = d.pop("city", UNSET)

        color = d.pop("color", UNSET)

        country: Union[Unset, StockLocationItemgetRequestSchemaCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = StockLocationItemgetRequestSchemaCountry(_country)

        house_number = d.pop("house_number", UNSET)

        in_archive = d.pop("in_archive", UNSET)

        name = d.pop("name", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        state_province = d.pop("state_province", UNSET)

        street = d.pop("street", UNSET)

        type: Union[Unset, StockLocationItemgetRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = StockLocationItemgetRequestSchemaType(_type)

        stock_location_itemget_request_schema = cls(
            active=active,
            city=city,
            color=color,
            country=country,
            house_number=house_number,
            in_archive=in_archive,
            name=name,
            postal_code=postal_code,
            state_province=state_province,
            street=street,
            type=type,
        )

        stock_location_itemget_request_schema.additional_properties = d
        return stock_location_itemget_request_schema

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
