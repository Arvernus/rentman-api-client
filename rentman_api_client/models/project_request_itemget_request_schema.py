import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_request_itemget_request_schema_source import ProjectRequestItemgetRequestSchemaSource
from ..models.project_request_itemget_request_schema_status import ProjectRequestItemgetRequestSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectRequestItemgetRequestSchema")


@attr.s(auto_attribs=True)
class ProjectRequestItemgetRequestSchema:
    """ """

    planperiod_end: datetime.datetime
    planperiod_start: datetime.datetime
    linked_contact: Union[Unset, None, str] = UNSET
    contact_mailing_number: Union[Unset, str] = UNSET
    contact_mailing_country: Union[Unset, str] = UNSET
    contact_name: Union[Unset, str] = UNSET
    contact_mailing_postalcode: Union[Unset, str] = UNSET
    contact_mailing_city: Union[Unset, str] = UNSET
    contact_mailing_street: Union[Unset, str] = UNSET
    linked_contact_person: Union[Unset, None, str] = UNSET
    contact_person_lastname: Union[Unset, str] = UNSET
    contact_person_email: Union[Unset, str] = UNSET
    contact_person_middle_name: Union[Unset, str] = UNSET
    contact_person_first_name: Union[Unset, str] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    language: Union[Unset, str] = UNSET
    in_: Union[Unset, None, datetime.datetime] = UNSET
    out: Union[Unset, None, datetime.datetime] = UNSET
    linked_location: Union[Unset, None, str] = UNSET
    location_mailing_number: Union[Unset, str] = UNSET
    location_mailing_country: Union[Unset, str] = UNSET
    location_name: Union[Unset, str] = UNSET
    location_mailing_postalcode: Union[Unset, str] = UNSET
    location_mailing_city: Union[Unset, str] = UNSET
    location_mailing_street: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    external_reference: Union[Unset, int] = UNSET
    remark: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    linked_project: Union[Unset, None, str] = UNSET
    source: Union[Unset, ProjectRequestItemgetRequestSchemaSource] = UNSET
    status: Union[Unset, ProjectRequestItemgetRequestSchemaStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        planperiod_end = self.planperiod_end.isoformat()

        planperiod_start = self.planperiod_start.isoformat()

        linked_contact = self.linked_contact
        contact_mailing_number = self.contact_mailing_number
        contact_mailing_country = self.contact_mailing_country
        contact_name = self.contact_name
        contact_mailing_postalcode = self.contact_mailing_postalcode
        contact_mailing_city = self.contact_mailing_city
        contact_mailing_street = self.contact_mailing_street
        linked_contact_person = self.linked_contact_person
        contact_person_lastname = self.contact_person_lastname
        contact_person_email = self.contact_person_email
        contact_person_middle_name = self.contact_person_middle_name
        contact_person_first_name = self.contact_person_first_name
        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        language = self.language
        in_: Union[Unset, None, str] = UNSET
        if not isinstance(self.in_, Unset):
            in_ = self.in_.isoformat() if self.in_ else None

        out: Union[Unset, None, str] = UNSET
        if not isinstance(self.out, Unset):
            out = self.out.isoformat() if self.out else None

        linked_location = self.linked_location
        location_mailing_number = self.location_mailing_number
        location_mailing_country = self.location_mailing_country
        location_name = self.location_name
        location_mailing_postalcode = self.location_mailing_postalcode
        location_mailing_city = self.location_mailing_city
        location_mailing_street = self.location_mailing_street
        name = self.name
        external_reference = self.external_reference
        remark = self.remark
        price = self.price
        linked_project = self.linked_project
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "planperiod_end": planperiod_end,
                "planperiod_start": planperiod_start,
            }
        )
        if linked_contact is not UNSET:
            field_dict["linked_contact"] = linked_contact
        if contact_mailing_number is not UNSET:
            field_dict["contact_mailing_number"] = contact_mailing_number
        if contact_mailing_country is not UNSET:
            field_dict["contact_mailing_country"] = contact_mailing_country
        if contact_name is not UNSET:
            field_dict["contact_name"] = contact_name
        if contact_mailing_postalcode is not UNSET:
            field_dict["contact_mailing_postalcode"] = contact_mailing_postalcode
        if contact_mailing_city is not UNSET:
            field_dict["contact_mailing_city"] = contact_mailing_city
        if contact_mailing_street is not UNSET:
            field_dict["contact_mailing_street"] = contact_mailing_street
        if linked_contact_person is not UNSET:
            field_dict["linked_contact_person"] = linked_contact_person
        if contact_person_lastname is not UNSET:
            field_dict["contact_person_lastname"] = contact_person_lastname
        if contact_person_email is not UNSET:
            field_dict["contact_person_email"] = contact_person_email
        if contact_person_middle_name is not UNSET:
            field_dict["contact_person_middle_name"] = contact_person_middle_name
        if contact_person_first_name is not UNSET:
            field_dict["contact_person_first_name"] = contact_person_first_name
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start
        if language is not UNSET:
            field_dict["language"] = language
        if in_ is not UNSET:
            field_dict["in"] = in_
        if out is not UNSET:
            field_dict["out"] = out
        if linked_location is not UNSET:
            field_dict["linked_location"] = linked_location
        if location_mailing_number is not UNSET:
            field_dict["location_mailing_number"] = location_mailing_number
        if location_mailing_country is not UNSET:
            field_dict["location_mailing_country"] = location_mailing_country
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if location_mailing_postalcode is not UNSET:
            field_dict["location_mailing_postalcode"] = location_mailing_postalcode
        if location_mailing_city is not UNSET:
            field_dict["location_mailing_city"] = location_mailing_city
        if location_mailing_street is not UNSET:
            field_dict["location_mailing_street"] = location_mailing_street
        if name is not UNSET:
            field_dict["name"] = name
        if external_reference is not UNSET:
            field_dict["external_reference"] = external_reference
        if remark is not UNSET:
            field_dict["remark"] = remark
        if price is not UNSET:
            field_dict["price"] = price
        if linked_project is not UNSET:
            field_dict["linked_project"] = linked_project
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        planperiod_end = isoparse(d.pop("planperiod_end"))

        planperiod_start = isoparse(d.pop("planperiod_start"))

        linked_contact = d.pop("linked_contact", UNSET)

        contact_mailing_number = d.pop("contact_mailing_number", UNSET)

        contact_mailing_country = d.pop("contact_mailing_country", UNSET)

        contact_name = d.pop("contact_name", UNSET)

        contact_mailing_postalcode = d.pop("contact_mailing_postalcode", UNSET)

        contact_mailing_city = d.pop("contact_mailing_city", UNSET)

        contact_mailing_street = d.pop("contact_mailing_street", UNSET)

        linked_contact_person = d.pop("linked_contact_person", UNSET)

        contact_person_lastname = d.pop("contact_person_lastname", UNSET)

        contact_person_email = d.pop("contact_person_email", UNSET)

        contact_person_middle_name = d.pop("contact_person_middle_name", UNSET)

        contact_person_first_name = d.pop("contact_person_first_name", UNSET)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        language = d.pop("language", UNSET)

        in_ = None
        _in_ = d.pop("in", UNSET)
        if _in_ is not None and not isinstance(_in_, Unset):
            in_ = isoparse(_in_)

        out = None
        _out = d.pop("out", UNSET)
        if _out is not None and not isinstance(_out, Unset):
            out = isoparse(_out)

        linked_location = d.pop("linked_location", UNSET)

        location_mailing_number = d.pop("location_mailing_number", UNSET)

        location_mailing_country = d.pop("location_mailing_country", UNSET)

        location_name = d.pop("location_name", UNSET)

        location_mailing_postalcode = d.pop("location_mailing_postalcode", UNSET)

        location_mailing_city = d.pop("location_mailing_city", UNSET)

        location_mailing_street = d.pop("location_mailing_street", UNSET)

        name = d.pop("name", UNSET)

        external_reference = d.pop("external_reference", UNSET)

        remark = d.pop("remark", UNSET)

        price = d.pop("price", UNSET)

        linked_project = d.pop("linked_project", UNSET)

        source: Union[Unset, ProjectRequestItemgetRequestSchemaSource] = UNSET
        _source = d.pop("source", UNSET)
        if not isinstance(_source, Unset):
            source = ProjectRequestItemgetRequestSchemaSource(_source)

        status: Union[Unset, ProjectRequestItemgetRequestSchemaStatus] = UNSET
        _status = d.pop("status", UNSET)
        if not isinstance(_status, Unset):
            status = ProjectRequestItemgetRequestSchemaStatus(_status)

        project_request_itemget_request_schema = cls(
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            linked_contact=linked_contact,
            contact_mailing_number=contact_mailing_number,
            contact_mailing_country=contact_mailing_country,
            contact_name=contact_name,
            contact_mailing_postalcode=contact_mailing_postalcode,
            contact_mailing_city=contact_mailing_city,
            contact_mailing_street=contact_mailing_street,
            linked_contact_person=linked_contact_person,
            contact_person_lastname=contact_person_lastname,
            contact_person_email=contact_person_email,
            contact_person_middle_name=contact_person_middle_name,
            contact_person_first_name=contact_person_first_name,
            usageperiod_end=usageperiod_end,
            usageperiod_start=usageperiod_start,
            language=language,
            in_=in_,
            out=out,
            linked_location=linked_location,
            location_mailing_number=location_mailing_number,
            location_mailing_country=location_mailing_country,
            location_name=location_name,
            location_mailing_postalcode=location_mailing_postalcode,
            location_mailing_city=location_mailing_city,
            location_mailing_street=location_mailing_street,
            name=name,
            external_reference=external_reference,
            remark=remark,
            price=price,
            linked_project=linked_project,
            source=source,
            status=status,
        )

        project_request_itemget_request_schema.additional_properties = d
        return project_request_itemget_request_schema

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
