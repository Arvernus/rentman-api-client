import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.contactperson_collectionpost_response_schema_data_item_country import (
    ContactpersonCollectionpostResponseSchemaDataItemCountry,
)
from ..models.contactperson_collectionpost_response_schema_data_item_custom import (
    ContactpersonCollectionpostResponseSchemaDataItemCustom,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactpersonCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class ContactpersonCollectionpostResponseSchemaDataItem:
    """ """

    city: Union[Unset, str] = UNSET
    contact: Union[Unset, str] = UNSET
    country: Union[Unset, ContactpersonCollectionpostResponseSchemaDataItemCountry] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    custom: Union[Unset, ContactpersonCollectionpostResponseSchemaDataItemCustom] = UNSET
    displayname: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    lastname: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    mobilephone: Union[Unset, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    number: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    postalcode: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    tags: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city
        contact = self.contact
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        displayname = self.displayname
        email = self.email
        firstname = self.firstname
        function = self.function
        id = self.id
        lastname = self.lastname
        middle_name = self.middle_name
        mobilephone = self.mobilephone
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        number = self.number
        phone = self.phone
        postalcode = self.postalcode
        state = self.state
        street = self.street
        tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if contact is not UNSET:
            field_dict["contact"] = contact
        if country is not UNSET:
            field_dict["country"] = country
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if custom is not UNSET:
            field_dict["custom"] = custom
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if email is not UNSET:
            field_dict["email"] = email
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if function is not UNSET:
            field_dict["function"] = function
        if id is not UNSET:
            field_dict["id"] = id
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if mobilephone is not UNSET:
            field_dict["mobilephone"] = mobilephone
        if modified is not UNSET:
            field_dict["modified"] = modified
        if number is not UNSET:
            field_dict["number"] = number
        if phone is not UNSET:
            field_dict["phone"] = phone
        if postalcode is not UNSET:
            field_dict["postalcode"] = postalcode
        if state is not UNSET:
            field_dict["state"] = state
        if street is not UNSET:
            field_dict["street"] = street
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city", UNSET)

        contact = d.pop("contact", UNSET)

        country: Union[Unset, ContactpersonCollectionpostResponseSchemaDataItemCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = ContactpersonCollectionpostResponseSchemaDataItemCountry(_country)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        custom: Union[Unset, ContactpersonCollectionpostResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ContactpersonCollectionpostResponseSchemaDataItemCustom.from_dict(_custom)

        displayname = d.pop("displayname", UNSET)

        email = d.pop("email", UNSET)

        firstname = d.pop("firstname", UNSET)

        function = d.pop("function", UNSET)

        id = d.pop("id", UNSET)

        lastname = d.pop("lastname", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        mobilephone = d.pop("mobilephone", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        number = d.pop("number", UNSET)

        phone = d.pop("phone", UNSET)

        postalcode = d.pop("postalcode", UNSET)

        state = d.pop("state", UNSET)

        street = d.pop("street", UNSET)

        tags = d.pop("tags", UNSET)

        contactperson_collectionpost_response_schema_data_item = cls(
            city=city,
            contact=contact,
            country=country,
            created=created,
            creator=creator,
            custom=custom,
            displayname=displayname,
            email=email,
            firstname=firstname,
            function=function,
            id=id,
            lastname=lastname,
            middle_name=middle_name,
            mobilephone=mobilephone,
            modified=modified,
            number=number,
            phone=phone,
            postalcode=postalcode,
            state=state,
            street=street,
            tags=tags,
        )

        contactperson_collectionpost_response_schema_data_item.additional_properties = d
        return contactperson_collectionpost_response_schema_data_item

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
