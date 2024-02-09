from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.crew_itemput_request_schema_country import CrewItemputRequestSchemaCountry
from ..models.crew_itemput_request_schema_custom import CrewItemputRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="CrewItemputRequestSchema")


@attr.s(auto_attribs=True)
class CrewItemputRequestSchema:
    """ """

    active: Union[Unset, bool] = UNSET
    addressline_2: Union[Unset, str] = UNSET
    avatar: Union[Unset, None, str] = UNSET
    bank: Union[Unset, str] = UNSET
    birthdate: Union[Unset, None, str] = UNSET
    city: Union[Unset, str] = UNSET
    coc_code: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    contract: Union[Unset, str] = UNSET
    contract_date: Union[Unset, None, str] = UNSET
    country: Union[Unset, CrewItemputRequestSchemaCountry] = UNSET
    custom: Union[Unset, CrewItemputRequestSchemaCustom] = UNSET
    driving_license: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    emergency_contact: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    folder: Union[Unset, None, str] = UNSET
    housenumber: Union[Unset, str] = UNSET
    lastname: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    passport_number: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    vat_code: Union[Unset, str] = UNSET
    vt_fullname: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        addressline_2 = self.addressline_2
        avatar = self.avatar
        bank = self.bank
        birthdate = self.birthdate
        city = self.city
        coc_code = self.coc_code
        company_name = self.company_name
        contract = self.contract
        contract_date = self.contract_date
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        driving_license = self.driving_license
        email = self.email
        emergency_contact = self.emergency_contact
        firstname = self.firstname
        folder = self.folder
        housenumber = self.housenumber
        lastname = self.lastname
        middle_name = self.middle_name
        passport_number = self.passport_number
        phone = self.phone
        postal_code = self.postal_code
        remark = self.remark
        state = self.state
        street = self.street
        vat_code = self.vat_code
        vt_fullname = self.vt_fullname

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if addressline_2 is not UNSET:
            field_dict["addressline2"] = addressline_2
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if bank is not UNSET:
            field_dict["bank"] = bank
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if city is not UNSET:
            field_dict["city"] = city
        if coc_code is not UNSET:
            field_dict["coc_code"] = coc_code
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if contract is not UNSET:
            field_dict["contract"] = contract
        if contract_date is not UNSET:
            field_dict["contract_date"] = contract_date
        if country is not UNSET:
            field_dict["country"] = country
        if custom is not UNSET:
            field_dict["custom"] = custom
        if driving_license is not UNSET:
            field_dict["driving_license"] = driving_license
        if email is not UNSET:
            field_dict["email"] = email
        if emergency_contact is not UNSET:
            field_dict["emergency_contact"] = emergency_contact
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if folder is not UNSET:
            field_dict["folder"] = folder
        if housenumber is not UNSET:
            field_dict["housenumber"] = housenumber
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if passport_number is not UNSET:
            field_dict["passport_number"] = passport_number
        if phone is not UNSET:
            field_dict["phone"] = phone
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if remark is not UNSET:
            field_dict["remark"] = remark
        if state is not UNSET:
            field_dict["state"] = state
        if street is not UNSET:
            field_dict["street"] = street
        if vat_code is not UNSET:
            field_dict["vat_code"] = vat_code
        if vt_fullname is not UNSET:
            field_dict["vt_fullname"] = vt_fullname

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active", UNSET)

        addressline_2 = d.pop("addressline2", UNSET)

        avatar = d.pop("avatar", UNSET)

        bank = d.pop("bank", UNSET)

        birthdate = d.pop("birthdate", UNSET)

        city = d.pop("city", UNSET)

        coc_code = d.pop("coc_code", UNSET)

        company_name = d.pop("company_name", UNSET)

        contract = d.pop("contract", UNSET)

        contract_date = d.pop("contract_date", UNSET)

        country: Union[Unset, CrewItemputRequestSchemaCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = CrewItemputRequestSchemaCountry(_country)

        custom: Union[Unset, CrewItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = CrewItemputRequestSchemaCustom.from_dict(_custom)

        driving_license = d.pop("driving_license", UNSET)

        email = d.pop("email", UNSET)

        emergency_contact = d.pop("emergency_contact", UNSET)

        firstname = d.pop("firstname", UNSET)

        folder = d.pop("folder", UNSET)

        housenumber = d.pop("housenumber", UNSET)

        lastname = d.pop("lastname", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        passport_number = d.pop("passport_number", UNSET)

        phone = d.pop("phone", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        remark = d.pop("remark", UNSET)

        state = d.pop("state", UNSET)

        street = d.pop("street", UNSET)

        vat_code = d.pop("vat_code", UNSET)

        vt_fullname = d.pop("vt_fullname", UNSET)

        crew_itemput_request_schema = cls(
            active=active,
            addressline_2=addressline_2,
            avatar=avatar,
            bank=bank,
            birthdate=birthdate,
            city=city,
            coc_code=coc_code,
            company_name=company_name,
            contract=contract,
            contract_date=contract_date,
            country=country,
            custom=custom,
            driving_license=driving_license,
            email=email,
            emergency_contact=emergency_contact,
            firstname=firstname,
            folder=folder,
            housenumber=housenumber,
            lastname=lastname,
            middle_name=middle_name,
            passport_number=passport_number,
            phone=phone,
            postal_code=postal_code,
            remark=remark,
            state=state,
            street=street,
            vat_code=vat_code,
            vt_fullname=vt_fullname,
        )

        crew_itemput_request_schema.additional_properties = d
        return crew_itemput_request_schema

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
