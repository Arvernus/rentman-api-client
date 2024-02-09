import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stockmovement_collectionget_response_schema_data_item_type import (
    StockmovementCollectiongetResponseSchemaDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StockmovementCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class StockmovementCollectiongetResponseSchemaDataItem:
    """ """

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    equipment: Union[Unset, str] = UNSET
    projectequipment: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    date: Union[Unset, None, datetime.datetime] = UNSET
    type: Union[Unset, StockmovementCollectiongetResponseSchemaDataItemType] = UNSET
    stock_location: Union[Unset, None, str] = UNSET
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
        amount = self.amount
        equipment = self.equipment
        projectequipment = self.projectequipment
        description = self.description
        details = self.details
        date: Union[Unset, None, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat() if self.date else None

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        stock_location = self.stock_location

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
        if amount is not UNSET:
            field_dict["amount"] = amount
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if projectequipment is not UNSET:
            field_dict["projectequipment"] = projectequipment
        if description is not UNSET:
            field_dict["description"] = description
        if details is not UNSET:
            field_dict["details"] = details
        if date is not UNSET:
            field_dict["date"] = date
        if type is not UNSET:
            field_dict["type"] = type
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location

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

        amount = d.pop("amount", UNSET)

        equipment = d.pop("equipment", UNSET)

        projectequipment = d.pop("projectequipment", UNSET)

        description = d.pop("description", UNSET)

        details = d.pop("details", UNSET)

        date = None
        _date = d.pop("date", UNSET)
        if _date is not None and not isinstance(_date, Unset):
            date = isoparse(_date)

        type: Union[Unset, StockmovementCollectiongetResponseSchemaDataItemType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = StockmovementCollectiongetResponseSchemaDataItemType(_type)

        stock_location = d.pop("stock_location", UNSET)

        stockmovement_collectionget_response_schema_data_item = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            amount=amount,
            equipment=equipment,
            projectequipment=projectequipment,
            description=description,
            details=details,
            date=date,
            type=type,
            stock_location=stock_location,
        )

        stockmovement_collectionget_response_schema_data_item.additional_properties = d
        return stockmovement_collectionget_response_schema_data_item

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
