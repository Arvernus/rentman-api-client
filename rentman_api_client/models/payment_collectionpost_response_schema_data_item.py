import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.payment_collectionpost_response_schema_data_item_payment_import_source import (
    PaymentCollectionpostResponseSchemaDataItemPaymentImportSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class PaymentCollectionpostResponseSchemaDataItem:
    """ """

    amount: Union[Unset, float] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    invoice: Union[Unset, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    moment: Union[Unset, datetime.datetime] = UNSET
    payment_import_source: Union[Unset, PaymentCollectionpostResponseSchemaDataItemPaymentImportSource] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        description = self.description
        displayname = self.displayname
        id = self.id
        invoice = self.invoice
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        moment: Union[Unset, str] = UNSET
        if not isinstance(self.moment, Unset):
            moment = self.moment.isoformat()

        payment_import_source: Union[Unset, str] = UNSET
        if not isinstance(self.payment_import_source, Unset):
            payment_import_source = self.payment_import_source.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if id is not UNSET:
            field_dict["id"] = id
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if modified is not UNSET:
            field_dict["modified"] = modified
        if moment is not UNSET:
            field_dict["moment"] = moment
        if payment_import_source is not UNSET:
            field_dict["payment_import_source"] = payment_import_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        description = d.pop("description", UNSET)

        displayname = d.pop("displayname", UNSET)

        id = d.pop("id", UNSET)

        invoice = d.pop("invoice", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        moment: Union[Unset, datetime.datetime] = UNSET
        _moment = d.pop("moment", UNSET)
        if not isinstance(_moment, Unset):
            moment = isoparse(_moment)

        payment_import_source: Union[Unset, PaymentCollectionpostResponseSchemaDataItemPaymentImportSource] = UNSET
        _payment_import_source = d.pop("payment_import_source", UNSET)
        if not isinstance(_payment_import_source, Unset):
            payment_import_source = PaymentCollectionpostResponseSchemaDataItemPaymentImportSource(
                _payment_import_source
            )

        payment_collectionpost_response_schema_data_item = cls(
            amount=amount,
            created=created,
            creator=creator,
            description=description,
            displayname=displayname,
            id=id,
            invoice=invoice,
            modified=modified,
            moment=moment,
            payment_import_source=payment_import_source,
        )

        payment_collectionpost_response_schema_data_item.additional_properties = d
        return payment_collectionpost_response_schema_data_item

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
