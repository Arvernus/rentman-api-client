import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.contactperson_itemput_response_schema_data_country import ContactpersonItemputResponseSchemaDataCountry
from ..models.contactperson_itemput_response_schema_data_custom import ContactpersonItemputResponseSchemaDataCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactpersonItemputResponseSchemaData")


@attr.s(auto_attribs=True)
class ContactpersonItemputResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    contact: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    lastname: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    postalcode: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, ContactpersonItemputResponseSchemaDataCountry] = UNSET
    mobilephone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    tags: Union[Unset, str] = UNSET
    custom: Union[Unset, ContactpersonItemputResponseSchemaDataCustom] = UNSET
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
        contact = self.contact
        firstname = self.firstname
        middle_name = self.middle_name
        lastname = self.lastname
        function = self.function
        phone = self.phone
        street = self.street
        number = self.number
        postalcode = self.postalcode
        city = self.city
        state = self.state
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        mobilephone = self.mobilephone
        email = self.email
        tags = self.tags
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
        if contact is not UNSET:
            field_dict["contact"] = contact
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if function is not UNSET:
            field_dict["function"] = function
        if phone is not UNSET:
            field_dict["phone"] = phone
        if street is not UNSET:
            field_dict["street"] = street
        if number is not UNSET:
            field_dict["number"] = number
        if postalcode is not UNSET:
            field_dict["postalcode"] = postalcode
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if mobilephone is not UNSET:
            field_dict["mobilephone"] = mobilephone
        if email is not UNSET:
            field_dict["email"] = email
        if tags is not UNSET:
            field_dict["tags"] = tags
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

        contact = d.pop("contact", UNSET)

        firstname = d.pop("firstname", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        lastname = d.pop("lastname", UNSET)

        function = d.pop("function", UNSET)

        phone = d.pop("phone", UNSET)

        street = d.pop("street", UNSET)

        number = d.pop("number", UNSET)

        postalcode = d.pop("postalcode", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country: Union[Unset, ContactpersonItemputResponseSchemaDataCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = ContactpersonItemputResponseSchemaDataCountry(_country)

        mobilephone = d.pop("mobilephone", UNSET)

        email = d.pop("email", UNSET)

        tags = d.pop("tags", UNSET)

        custom: Union[Unset, ContactpersonItemputResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ContactpersonItemputResponseSchemaDataCustom.from_dict(_custom)

        contactperson_itemput_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            contact=contact,
            firstname=firstname,
            middle_name=middle_name,
            lastname=lastname,
            function=function,
            phone=phone,
            street=street,
            number=number,
            postalcode=postalcode,
            city=city,
            state=state,
            country=country,
            mobilephone=mobilephone,
            email=email,
            tags=tags,
            custom=custom,
        )

        contactperson_itemput_response_schema_data.additional_properties = d
        return contactperson_itemput_response_schema_data

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
