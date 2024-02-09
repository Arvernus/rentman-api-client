from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuoteItempostRequestSchema")


@attr.s(auto_attribs=True)
class QuoteItempostRequestSchema:
    """ """

    contact: Union[Unset, None, str] = UNSET
    customer: Union[Unset, None, str] = UNSET
    date: Union[Unset, None, str] = UNSET
    expiration_date: Union[Unset, None, str] = UNSET
    filename: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    show_tax: Union[Unset, bool] = UNSET
    subject: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact = self.contact
        customer = self.customer
        date = self.date
        expiration_date = self.expiration_date
        filename = self.filename
        number = self.number
        show_tax = self.show_tax
        subject = self.subject
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if customer is not UNSET:
            field_dict["customer"] = customer
        if date is not UNSET:
            field_dict["date"] = date
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if filename is not UNSET:
            field_dict["filename"] = filename
        if number is not UNSET:
            field_dict["number"] = number
        if show_tax is not UNSET:
            field_dict["show_tax"] = show_tax
        if subject is not UNSET:
            field_dict["subject"] = subject
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact = d.pop("contact", UNSET)

        customer = d.pop("customer", UNSET)

        date = d.pop("date", UNSET)

        expiration_date = d.pop("expiration_date", UNSET)

        filename = d.pop("filename", UNSET)

        number = d.pop("number", UNSET)

        show_tax = d.pop("show_tax", UNSET)

        subject = d.pop("subject", UNSET)

        version = d.pop("version", UNSET)

        quote_itempost_request_schema = cls(
            contact=contact,
            customer=customer,
            date=date,
            expiration_date=expiration_date,
            filename=filename,
            number=number,
            show_tax=show_tax,
            subject=subject,
            version=version,
        )

        quote_itempost_request_schema.additional_properties = d
        return quote_itempost_request_schema

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
