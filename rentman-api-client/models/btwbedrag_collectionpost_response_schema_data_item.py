import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BtwbedragCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class BtwbedragCollectionpostResponseSchemaDataItem:
    """ """

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    item: Union[Unset, None, str] = UNSET
    base: Union[Unset, float] = UNSET
    ledger: Union[Unset, str] = UNSET
    vatrate: Union[Unset, float] = UNSET
    vatamount: Union[Unset, float] = UNSET
    priceincl: Union[Unset, float] = UNSET
    ledgercode: Union[Unset, str] = UNSET
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
        item = self.item
        base = self.base
        ledger = self.ledger
        vatrate = self.vatrate
        vatamount = self.vatamount
        priceincl = self.priceincl
        ledgercode = self.ledgercode

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
        if item is not UNSET:
            field_dict["item"] = item
        if base is not UNSET:
            field_dict["base"] = base
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if vatrate is not UNSET:
            field_dict["vatrate"] = vatrate
        if vatamount is not UNSET:
            field_dict["vatamount"] = vatamount
        if priceincl is not UNSET:
            field_dict["priceincl"] = priceincl
        if ledgercode is not UNSET:
            field_dict["ledgercode"] = ledgercode

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

        item = d.pop("item", UNSET)

        base = d.pop("base", UNSET)

        ledger = d.pop("ledger", UNSET)

        vatrate = d.pop("vatrate", UNSET)

        vatamount = d.pop("vatamount", UNSET)

        priceincl = d.pop("priceincl", UNSET)

        ledgercode = d.pop("ledgercode", UNSET)

        btwbedrag_collectionpost_response_schema_data_item = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            item=item,
            base=base,
            ledger=ledger,
            vatrate=vatrate,
            vatamount=vatamount,
            priceincl=priceincl,
            ledgercode=ledgercode,
        )

        btwbedrag_collectionpost_response_schema_data_item.additional_properties = d
        return btwbedrag_collectionpost_response_schema_data_item

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
