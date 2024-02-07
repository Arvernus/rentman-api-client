import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.contact_itempost_response_schema_data_country import ContactItempostResponseSchemaDataCountry
from ..models.contact_itempost_response_schema_data_custom import ContactItempostResponseSchemaDataCustom
from ..models.contact_itempost_response_schema_data_invoice_country import (
    ContactItempostResponseSchemaDataInvoiceCountry,
)
from ..models.contact_itempost_response_schema_data_mailing_country import (
    ContactItempostResponseSchemaDataMailingCountry,
)
from ..models.contact_itempost_response_schema_data_type import ContactItempostResponseSchemaDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactItempostResponseSchemaData")


@attr.s(auto_attribs=True)
class ContactItempostResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    folder: Union[Unset, None, str] = UNSET
    type: Union[Unset, ContactItempostResponseSchemaDataType] = UNSET
    ext_name_line: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    distance: Union[Unset, float] = UNSET
    travel_time: Union[Unset, None, float] = UNSET
    surfix: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    longitude: Union[Unset, float] = UNSET
    latitude: Union[Unset, float] = UNSET
    code: Union[Unset, str] = UNSET
    accounting_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    mailing_city: Union[Unset, str] = UNSET
    mailing_street: Union[Unset, str] = UNSET
    mailing_number: Union[Unset, str] = UNSET
    mailing_postalcode: Union[Unset, str] = UNSET
    mailing_state: Union[Unset, str] = UNSET
    mailing_country: Union[Unset, ContactItempostResponseSchemaDataMailingCountry] = UNSET
    visit_city: Union[Unset, str] = UNSET
    visit_street: Union[Unset, str] = UNSET
    visit_number: Union[Unset, str] = UNSET
    visit_postalcode: Union[Unset, str] = UNSET
    visit_state: Union[Unset, str] = UNSET
    country: Union[Unset, ContactItempostResponseSchemaDataCountry] = UNSET
    invoice_city: Union[Unset, str] = UNSET
    invoice_street: Union[Unset, str] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    invoice_postalcode: Union[Unset, str] = UNSET
    invoice_state: Union[Unset, str] = UNSET
    invoice_country: Union[Unset, ContactItempostResponseSchemaDataInvoiceCountry] = UNSET
    phone_1: Union[Unset, str] = UNSET
    phone_2: Union[Unset, str] = UNSET
    email_1: Union[Unset, str] = UNSET
    email_2: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    vat_code: Union[Unset, str] = UNSET
    fiscal_code: Union[Unset, str] = UNSET
    commerce_code: Union[Unset, str] = UNSET
    purchase_number: Union[Unset, str] = UNSET
    bic: Union[Unset, str] = UNSET
    bank_account: Union[Unset, str] = UNSET
    default_person: Union[Unset, None, str] = UNSET
    admin_contactperson: Union[Unset, None, str] = UNSET
    discount_crew: Union[Unset, float] = UNSET
    discount_transport: Union[Unset, float] = UNSET
    discount_rental: Union[Unset, float] = UNSET
    discount_sale: Union[Unset, float] = UNSET
    discount_total: Union[Unset, float] = UNSET
    projectnote: Union[Unset, str] = UNSET
    projectnote_title: Union[Unset, str] = UNSET
    contact_warning: Union[Unset, str] = UNSET
    discount_subrent: Union[Unset, float] = UNSET
    tags: Union[Unset, str] = UNSET
    custom: Union[Unset, ContactItempostResponseSchemaDataCustom] = UNSET
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
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        ext_name_line = self.ext_name_line
        firstname = self.firstname
        distance = self.distance
        travel_time = self.travel_time
        surfix = self.surfix
        surname = self.surname
        longitude = self.longitude
        latitude = self.latitude
        code = self.code
        accounting_code = self.accounting_code
        name = self.name
        gender = self.gender
        mailing_city = self.mailing_city
        mailing_street = self.mailing_street
        mailing_number = self.mailing_number
        mailing_postalcode = self.mailing_postalcode
        mailing_state = self.mailing_state
        mailing_country: Union[Unset, str] = UNSET
        if not isinstance(self.mailing_country, Unset):
            mailing_country = self.mailing_country.value

        visit_city = self.visit_city
        visit_street = self.visit_street
        visit_number = self.visit_number
        visit_postalcode = self.visit_postalcode
        visit_state = self.visit_state
        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        invoice_city = self.invoice_city
        invoice_street = self.invoice_street
        invoice_number = self.invoice_number
        invoice_postalcode = self.invoice_postalcode
        invoice_state = self.invoice_state
        invoice_country: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_country, Unset):
            invoice_country = self.invoice_country.value

        phone_1 = self.phone_1
        phone_2 = self.phone_2
        email_1 = self.email_1
        email_2 = self.email_2
        website = self.website
        vat_code = self.vat_code
        fiscal_code = self.fiscal_code
        commerce_code = self.commerce_code
        purchase_number = self.purchase_number
        bic = self.bic
        bank_account = self.bank_account
        default_person = self.default_person
        admin_contactperson = self.admin_contactperson
        discount_crew = self.discount_crew
        discount_transport = self.discount_transport
        discount_rental = self.discount_rental
        discount_sale = self.discount_sale
        discount_total = self.discount_total
        projectnote = self.projectnote
        projectnote_title = self.projectnote_title
        contact_warning = self.contact_warning
        discount_subrent = self.discount_subrent
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
        if folder is not UNSET:
            field_dict["folder"] = folder
        if type is not UNSET:
            field_dict["type"] = type
        if ext_name_line is not UNSET:
            field_dict["ext_name_line"] = ext_name_line
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if distance is not UNSET:
            field_dict["distance"] = distance
        if travel_time is not UNSET:
            field_dict["travel_time"] = travel_time
        if surfix is not UNSET:
            field_dict["surfix"] = surfix
        if surname is not UNSET:
            field_dict["surname"] = surname
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if code is not UNSET:
            field_dict["code"] = code
        if accounting_code is not UNSET:
            field_dict["accounting_code"] = accounting_code
        if name is not UNSET:
            field_dict["name"] = name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if mailing_city is not UNSET:
            field_dict["mailing_city"] = mailing_city
        if mailing_street is not UNSET:
            field_dict["mailing_street"] = mailing_street
        if mailing_number is not UNSET:
            field_dict["mailing_number"] = mailing_number
        if mailing_postalcode is not UNSET:
            field_dict["mailing_postalcode"] = mailing_postalcode
        if mailing_state is not UNSET:
            field_dict["mailing_state"] = mailing_state
        if mailing_country is not UNSET:
            field_dict["mailing_country"] = mailing_country
        if visit_city is not UNSET:
            field_dict["visit_city"] = visit_city
        if visit_street is not UNSET:
            field_dict["visit_street"] = visit_street
        if visit_number is not UNSET:
            field_dict["visit_number"] = visit_number
        if visit_postalcode is not UNSET:
            field_dict["visit_postalcode"] = visit_postalcode
        if visit_state is not UNSET:
            field_dict["visit_state"] = visit_state
        if country is not UNSET:
            field_dict["country"] = country
        if invoice_city is not UNSET:
            field_dict["invoice_city"] = invoice_city
        if invoice_street is not UNSET:
            field_dict["invoice_street"] = invoice_street
        if invoice_number is not UNSET:
            field_dict["invoice_number"] = invoice_number
        if invoice_postalcode is not UNSET:
            field_dict["invoice_postalcode"] = invoice_postalcode
        if invoice_state is not UNSET:
            field_dict["invoice_state"] = invoice_state
        if invoice_country is not UNSET:
            field_dict["invoice_country"] = invoice_country
        if phone_1 is not UNSET:
            field_dict["phone_1"] = phone_1
        if phone_2 is not UNSET:
            field_dict["phone_2"] = phone_2
        if email_1 is not UNSET:
            field_dict["email_1"] = email_1
        if email_2 is not UNSET:
            field_dict["email_2"] = email_2
        if website is not UNSET:
            field_dict["website"] = website
        if vat_code is not UNSET:
            field_dict["VAT_code"] = vat_code
        if fiscal_code is not UNSET:
            field_dict["fiscal_code"] = fiscal_code
        if commerce_code is not UNSET:
            field_dict["commerce_code"] = commerce_code
        if purchase_number is not UNSET:
            field_dict["purchase_number"] = purchase_number
        if bic is not UNSET:
            field_dict["bic"] = bic
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if default_person is not UNSET:
            field_dict["default_person"] = default_person
        if admin_contactperson is not UNSET:
            field_dict["admin_contactperson"] = admin_contactperson
        if discount_crew is not UNSET:
            field_dict["discount_crew"] = discount_crew
        if discount_transport is not UNSET:
            field_dict["discount_transport"] = discount_transport
        if discount_rental is not UNSET:
            field_dict["discount_rental"] = discount_rental
        if discount_sale is not UNSET:
            field_dict["discount_sale"] = discount_sale
        if discount_total is not UNSET:
            field_dict["discount_total"] = discount_total
        if projectnote is not UNSET:
            field_dict["projectnote"] = projectnote
        if projectnote_title is not UNSET:
            field_dict["projectnote_title"] = projectnote_title
        if contact_warning is not UNSET:
            field_dict["contact_warning"] = contact_warning
        if discount_subrent is not UNSET:
            field_dict["discount_subrent"] = discount_subrent
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

        folder = d.pop("folder", UNSET)

        type: Union[Unset, ContactItempostResponseSchemaDataType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = ContactItempostResponseSchemaDataType(_type)

        ext_name_line = d.pop("ext_name_line", UNSET)

        firstname = d.pop("firstname", UNSET)

        distance = d.pop("distance", UNSET)

        travel_time = d.pop("travel_time", UNSET)

        surfix = d.pop("surfix", UNSET)

        surname = d.pop("surname", UNSET)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        code = d.pop("code", UNSET)

        accounting_code = d.pop("accounting_code", UNSET)

        name = d.pop("name", UNSET)

        gender = d.pop("gender", UNSET)

        mailing_city = d.pop("mailing_city", UNSET)

        mailing_street = d.pop("mailing_street", UNSET)

        mailing_number = d.pop("mailing_number", UNSET)

        mailing_postalcode = d.pop("mailing_postalcode", UNSET)

        mailing_state = d.pop("mailing_state", UNSET)

        mailing_country: Union[Unset, ContactItempostResponseSchemaDataMailingCountry] = UNSET
        _mailing_country = d.pop("mailing_country", UNSET)
        if not isinstance(_mailing_country, Unset):
            mailing_country = ContactItempostResponseSchemaDataMailingCountry(_mailing_country)

        visit_city = d.pop("visit_city", UNSET)

        visit_street = d.pop("visit_street", UNSET)

        visit_number = d.pop("visit_number", UNSET)

        visit_postalcode = d.pop("visit_postalcode", UNSET)

        visit_state = d.pop("visit_state", UNSET)

        country: Union[Unset, ContactItempostResponseSchemaDataCountry] = UNSET
        _country = d.pop("country", UNSET)
        if not isinstance(_country, Unset):
            country = ContactItempostResponseSchemaDataCountry(_country)

        invoice_city = d.pop("invoice_city", UNSET)

        invoice_street = d.pop("invoice_street", UNSET)

        invoice_number = d.pop("invoice_number", UNSET)

        invoice_postalcode = d.pop("invoice_postalcode", UNSET)

        invoice_state = d.pop("invoice_state", UNSET)

        invoice_country: Union[Unset, ContactItempostResponseSchemaDataInvoiceCountry] = UNSET
        _invoice_country = d.pop("invoice_country", UNSET)
        if not isinstance(_invoice_country, Unset):
            invoice_country = ContactItempostResponseSchemaDataInvoiceCountry(_invoice_country)

        phone_1 = d.pop("phone_1", UNSET)

        phone_2 = d.pop("phone_2", UNSET)

        email_1 = d.pop("email_1", UNSET)

        email_2 = d.pop("email_2", UNSET)

        website = d.pop("website", UNSET)

        vat_code = d.pop("VAT_code", UNSET)

        fiscal_code = d.pop("fiscal_code", UNSET)

        commerce_code = d.pop("commerce_code", UNSET)

        purchase_number = d.pop("purchase_number", UNSET)

        bic = d.pop("bic", UNSET)

        bank_account = d.pop("bank_account", UNSET)

        default_person = d.pop("default_person", UNSET)

        admin_contactperson = d.pop("admin_contactperson", UNSET)

        discount_crew = d.pop("discount_crew", UNSET)

        discount_transport = d.pop("discount_transport", UNSET)

        discount_rental = d.pop("discount_rental", UNSET)

        discount_sale = d.pop("discount_sale", UNSET)

        discount_total = d.pop("discount_total", UNSET)

        projectnote = d.pop("projectnote", UNSET)

        projectnote_title = d.pop("projectnote_title", UNSET)

        contact_warning = d.pop("contact_warning", UNSET)

        discount_subrent = d.pop("discount_subrent", UNSET)

        tags = d.pop("tags", UNSET)

        custom: Union[Unset, ContactItempostResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ContactItempostResponseSchemaDataCustom.from_dict(_custom)

        contact_itempost_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            folder=folder,
            type=type,
            ext_name_line=ext_name_line,
            firstname=firstname,
            distance=distance,
            travel_time=travel_time,
            surfix=surfix,
            surname=surname,
            longitude=longitude,
            latitude=latitude,
            code=code,
            accounting_code=accounting_code,
            name=name,
            gender=gender,
            mailing_city=mailing_city,
            mailing_street=mailing_street,
            mailing_number=mailing_number,
            mailing_postalcode=mailing_postalcode,
            mailing_state=mailing_state,
            mailing_country=mailing_country,
            visit_city=visit_city,
            visit_street=visit_street,
            visit_number=visit_number,
            visit_postalcode=visit_postalcode,
            visit_state=visit_state,
            country=country,
            invoice_city=invoice_city,
            invoice_street=invoice_street,
            invoice_number=invoice_number,
            invoice_postalcode=invoice_postalcode,
            invoice_state=invoice_state,
            invoice_country=invoice_country,
            phone_1=phone_1,
            phone_2=phone_2,
            email_1=email_1,
            email_2=email_2,
            website=website,
            vat_code=vat_code,
            fiscal_code=fiscal_code,
            commerce_code=commerce_code,
            purchase_number=purchase_number,
            bic=bic,
            bank_account=bank_account,
            default_person=default_person,
            admin_contactperson=admin_contactperson,
            discount_crew=discount_crew,
            discount_transport=discount_transport,
            discount_rental=discount_rental,
            discount_sale=discount_sale,
            discount_total=discount_total,
            projectnote=projectnote,
            projectnote_title=projectnote_title,
            contact_warning=contact_warning,
            discount_subrent=discount_subrent,
            tags=tags,
            custom=custom,
        )

        contact_itempost_response_schema_data.additional_properties = d
        return contact_itempost_response_schema_data

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
