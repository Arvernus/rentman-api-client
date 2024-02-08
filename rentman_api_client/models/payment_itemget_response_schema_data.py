import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.payment_itemget_response_schema_data_payment_import_source import (
    PaymentItemgetResponseSchemaDataPaymentImportSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class PaymentItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    invoice: Union[Unset, str] = UNSET
    moment: Union[Unset, datetime.datetime] = UNSET
    amount: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    payment_import_source: Union[Unset, PaymentItemgetResponseSchemaDataPaymentImportSource] = UNSET
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
        invoice = self.invoice
        moment: Union[Unset, str] = UNSET
        if not isinstance(self.moment, Unset):
            moment = self.moment.isoformat()

        amount = self.amount
        description = self.description
        payment_import_source: Union[Unset, str] = UNSET
        if not isinstance(self.payment_import_source, Unset):
            payment_import_source = self.payment_import_source.value

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
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if moment is not UNSET:
            field_dict["moment"] = moment
        if amount is not UNSET:
            field_dict["amount"] = amount
        if description is not UNSET:
            field_dict["description"] = description
        if payment_import_source is not UNSET:
            field_dict["payment_import_source"] = payment_import_source

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

        invoice = d.pop("invoice", UNSET)

        moment: Union[Unset, datetime.datetime] = UNSET
        _moment = d.pop("moment", UNSET)
        if not isinstance(_moment, Unset):
            moment = isoparse(_moment)

        amount = d.pop("amount", UNSET)

        description = d.pop("description", UNSET)

        payment_import_source: Union[Unset, PaymentItemgetResponseSchemaDataPaymentImportSource] = UNSET
        _payment_import_source = d.pop("payment_import_source", UNSET)
        if not isinstance(_payment_import_source, Unset):
            payment_import_source = PaymentItemgetResponseSchemaDataPaymentImportSource(_payment_import_source)

        payment_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            invoice=invoice,
            moment=moment,
            amount=amount,
            description=description,
            payment_import_source=payment_import_source,
        )

        payment_itemget_response_schema_data.additional_properties = d
        return payment_itemget_response_schema_data

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
