from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.person_itemget_request_schema_country import PersonItemgetRequestSchemaCountry
from ..models.person_itemget_request_schema_custom import PersonItemgetRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonItemgetRequestSchema")


@attr.s(auto_attribs=True)
class PersonItemgetRequestSchema:
    """ """

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
    country: Union[Unset, PersonItemgetRequestSchemaCountry] = UNSET
    mobilephone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    custom: Union[Unset, PersonItemgetRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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

        country: Union[Unset, PersonItemgetRequestSchemaCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = PersonItemgetRequestSchemaCountry(_country)

        mobilephone = d.pop("mobilephone", UNSET)

        email = d.pop("email", UNSET)

        custom: Union[Unset, PersonItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = PersonItemgetRequestSchemaCustom.from_dict(_custom)

        person_itemget_request_schema = cls(
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
            custom=custom,
        )

        person_itemget_request_schema.additional_properties = d
        return person_itemget_request_schema

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
