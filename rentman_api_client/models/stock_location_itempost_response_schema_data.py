import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stock_location_itempost_response_schema_data_country import StockLocationItempostResponseSchemaDataCountry
from ..models.stock_location_itempost_response_schema_data_type import StockLocationItempostResponseSchemaDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StockLocationItempostResponseSchemaData")


@attr.s(auto_attribs=True)
class StockLocationItempostResponseSchemaData:
    """All the data about the requested items"""

    active: Union[Unset, bool] = UNSET
    city: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    country: Union[Unset, StockLocationItempostResponseSchemaDataCountry] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    house_number: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    in_archive: Union[Unset, bool] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    state_province: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    type: Union[Unset, StockLocationItempostResponseSchemaDataType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        city = self.city
        color = self.color
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        displayname = self.displayname
        house_number = self.house_number
        id = self.id
        in_archive = self.in_archive
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

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
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if house_number is not UNSET:
            field_dict["house_number"] = house_number
        if id is not UNSET:
            field_dict["id"] = id
        if in_archive is not UNSET:
            field_dict["in_archive"] = in_archive
        if modified is not UNSET:
            field_dict["modified"] = modified
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

        country: Union[Unset, StockLocationItempostResponseSchemaDataCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = StockLocationItempostResponseSchemaDataCountry(_country)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        house_number = d.pop("house_number", UNSET)

        id = d.pop("id", UNSET)

        in_archive = d.pop("in_archive", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        state_province = d.pop("state_province", UNSET)

        street = d.pop("street", UNSET)

        type: Union[Unset, StockLocationItempostResponseSchemaDataType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = StockLocationItempostResponseSchemaDataType(_type)

        stock_location_itempost_response_schema_data = cls(
            active=active,
            city=city,
            color=color,
            country=country,
            created=created,
            creator=creator,
            displayname=displayname,
            house_number=house_number,
            id=id,
            in_archive=in_archive,
            modified=modified,
            name=name,
            postal_code=postal_code,
            state_province=state_province,
            street=street,
            type=type,
        )

        stock_location_itempost_response_schema_data.additional_properties = d
        return stock_location_itempost_response_schema_data

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
