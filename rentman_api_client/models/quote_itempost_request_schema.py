from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuoteItempostRequestSchema")


@attr.s(auto_attribs=True)
class QuoteItempostRequestSchema:
    """ """

    number: Union[Unset, str] = UNSET
    customer: Union[Unset, None, str] = UNSET
    contact: Union[Unset, None, str] = UNSET
    date: Union[Unset, None, str] = UNSET
    expiration_date: Union[Unset, None, str] = UNSET
    version: Union[Unset, int] = UNSET
    subject: Union[Unset, str] = UNSET
    show_tax: Union[Unset, bool] = UNSET
    filename: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        customer = self.customer
        contact = self.contact
        date = self.date
        expiration_date = self.expiration_date
        version = self.version
        subject = self.subject
        show_tax = self.show_tax
        filename = self.filename

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if customer is not UNSET:
            field_dict["customer"] = customer
        if contact is not UNSET:
            field_dict["contact"] = contact
        if date is not UNSET:
            field_dict["date"] = date
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if version is not UNSET:
            field_dict["version"] = version
        if subject is not UNSET:
            field_dict["subject"] = subject
        if show_tax is not UNSET:
            field_dict["show_tax"] = show_tax
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        customer = d.pop("customer", UNSET)

        contact = d.pop("contact", UNSET)

        date = d.pop("date", UNSET)

        expiration_date = d.pop("expiration_date", UNSET)

        version = d.pop("version", UNSET)

        subject = d.pop("subject", UNSET)

        show_tax = d.pop("show_tax", UNSET)

        filename = d.pop("filename", UNSET)

        quote_itempost_request_schema = cls(
            number=number,
            customer=customer,
            contact=contact,
            date=date,
            expiration_date=expiration_date,
            version=version,
            subject=subject,
            show_tax=show_tax,
            filename=filename,
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
