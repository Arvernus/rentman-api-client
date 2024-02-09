from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.contactperson_itempost_request_schema_country import ContactpersonItempostRequestSchemaCountry
from ..models.contactperson_itempost_request_schema_custom import ContactpersonItempostRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactpersonItempostRequestSchema")


@attr.s(auto_attribs=True)
class ContactpersonItempostRequestSchema:
    """ """

    city: Union[Unset, str] = UNSET
    country: Union[Unset, ContactpersonItempostRequestSchemaCountry] = UNSET
    custom: Union[Unset, ContactpersonItempostRequestSchemaCustom] = UNSET
    email: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    lastname: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    mobilephone: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    postalcode: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        email = self.email
        firstname = self.firstname
        function = self.function
        lastname = self.lastname
        middle_name = self.middle_name
        mobilephone = self.mobilephone
        number = self.number
        phone = self.phone
        postalcode = self.postalcode
        state = self.state
        street = self.street

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if custom is not UNSET:
            field_dict["custom"] = custom
        if email is not UNSET:
            field_dict["email"] = email
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if function is not UNSET:
            field_dict["function"] = function
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if mobilephone is not UNSET:
            field_dict["mobilephone"] = mobilephone
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city", UNSET)

        country: Union[Unset, ContactpersonItempostRequestSchemaCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = ContactpersonItempostRequestSchemaCountry(_country)

        custom: Union[Unset, ContactpersonItempostRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ContactpersonItempostRequestSchemaCustom.from_dict(_custom)

        email = d.pop("email", UNSET)

        firstname = d.pop("firstname", UNSET)

        function = d.pop("function", UNSET)

        lastname = d.pop("lastname", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        mobilephone = d.pop("mobilephone", UNSET)

        number = d.pop("number", UNSET)

        phone = d.pop("phone", UNSET)

        postalcode = d.pop("postalcode", UNSET)

        state = d.pop("state", UNSET)

        street = d.pop("street", UNSET)

        contactperson_itempost_request_schema = cls(
            city=city,
            country=country,
            custom=custom,
            email=email,
            firstname=firstname,
            function=function,
            lastname=lastname,
            middle_name=middle_name,
            mobilephone=mobilephone,
            number=number,
            phone=phone,
            postalcode=postalcode,
            state=state,
            street=street,
        )

        contactperson_itempost_request_schema.additional_properties = d
        return contactperson_itempost_request_schema

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
