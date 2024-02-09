import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceLinesItempostResponseSchemaData")


@attr.s(auto_attribs=True)
class InvoiceLinesItempostResponseSchemaData:
    """All the data about the requested items"""

    base: Union[Unset, float] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    item: Union[Unset, None, str] = UNSET
    ledger: Union[Unset, str] = UNSET
    ledgercode: Union[Unset, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    priceincl: Union[Unset, float] = UNSET
    vatamount: Union[Unset, float] = UNSET
    vatrate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base = self.base
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        displayname = self.displayname
        id = self.id
        item = self.item
        ledger = self.ledger
        ledgercode = self.ledgercode
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        priceincl = self.priceincl
        vatamount = self.vatamount
        vatrate = self.vatrate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base is not UNSET:
            field_dict["base"] = base
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if id is not UNSET:
            field_dict["id"] = id
        if item is not UNSET:
            field_dict["item"] = item
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if ledgercode is not UNSET:
            field_dict["ledgercode"] = ledgercode
        if modified is not UNSET:
            field_dict["modified"] = modified
        if priceincl is not UNSET:
            field_dict["priceincl"] = priceincl
        if vatamount is not UNSET:
            field_dict["vatamount"] = vatamount
        if vatrate is not UNSET:
            field_dict["vatrate"] = vatrate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base = d.pop("base", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        id = d.pop("id", UNSET)

        item = d.pop("item", UNSET)

        ledger = d.pop("ledger", UNSET)

        ledgercode = d.pop("ledgercode", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        priceincl = d.pop("priceincl", UNSET)

        vatamount = d.pop("vatamount", UNSET)

        vatrate = d.pop("vatrate", UNSET)

        invoice_lines_itempost_response_schema_data = cls(
            base=base,
            created=created,
            creator=creator,
            displayname=displayname,
            id=id,
            item=item,
            ledger=ledger,
            ledgercode=ledgercode,
            modified=modified,
            priceincl=priceincl,
            vatamount=vatamount,
            vatrate=vatrate,
        )

        invoice_lines_itempost_response_schema_data.additional_properties = d
        return invoice_lines_itempost_response_schema_data

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
