from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.stocklocation_itemput_request_schema_country import StocklocationItemputRequestSchemaCountry
from ..models.stocklocation_itemput_request_schema_type import StocklocationItemputRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StocklocationItemputRequestSchema")


@attr.s(auto_attribs=True)
class StocklocationItemputRequestSchema:
    """ """

    name: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    house_number: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    state_province: Union[Unset, str] = UNSET
    country: Union[Unset, StocklocationItemputRequestSchemaCountry] = UNSET
    active: Union[Unset, bool] = UNSET
    type: Union[Unset, StocklocationItemputRequestSchemaType] = UNSET
    color: Union[Unset, str] = UNSET
    in_archive: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        city = self.city
        street = self.street
        house_number = self.house_number
        postal_code = self.postal_code
        state_province = self.state_province
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        active = self.active
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        color = self.color
        in_archive = self.in_archive

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if city is not UNSET:
            field_dict["city"] = city
        if street is not UNSET:
            field_dict["street"] = street
        if house_number is not UNSET:
            field_dict["house_number"] = house_number
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if state_province is not UNSET:
            field_dict["state_province"] = state_province
        if country is not UNSET:
            field_dict["country"] = country
        if active is not UNSET:
            field_dict["active"] = active
        if type is not UNSET:
            field_dict["type"] = type
        if color is not UNSET:
            field_dict["color"] = color
        if in_archive is not UNSET:
            field_dict["in_archive"] = in_archive

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        city = d.pop("city", UNSET)

        street = d.pop("street", UNSET)

        house_number = d.pop("house_number", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        state_province = d.pop("state_province", UNSET)

        country: Union[Unset, StocklocationItemputRequestSchemaCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = StocklocationItemputRequestSchemaCountry(_country)

        active = d.pop("active", UNSET)

        type: Union[Unset, StocklocationItemputRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = StocklocationItemputRequestSchemaType(_type)

        color = d.pop("color", UNSET)

        in_archive = d.pop("in_archive", UNSET)

        stocklocation_itemput_request_schema = cls(
            name=name,
            city=city,
            street=street,
            house_number=house_number,
            postal_code=postal_code,
            state_province=state_province,
            country=country,
            active=active,
            type=type,
            color=color,
            in_archive=in_archive,
        )

        stocklocation_itemput_request_schema.additional_properties = d
        return stocklocation_itemput_request_schema

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
