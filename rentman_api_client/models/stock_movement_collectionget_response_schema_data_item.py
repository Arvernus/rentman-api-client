import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.stock_movement_collectionget_response_schema_data_item_type import (
    StockMovementCollectiongetResponseSchemaDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StockMovementCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class StockMovementCollectiongetResponseSchemaDataItem:
    """ """

    amount: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    date: Union[Unset, None, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    projectequipment: Union[Unset, None, str] = UNSET
    stock_location: Union[Unset, None, str] = UNSET
    type: Union[Unset, StockMovementCollectiongetResponseSchemaDataItemType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        date: Union[Unset, None, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat() if self.date else None

        description = self.description
        details = self.details
        displayname = self.displayname
        equipment = self.equipment
        id = self.id
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        projectequipment = self.projectequipment
        stock_location = self.stock_location
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if details is not UNSET:
            field_dict["details"] = details
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if projectequipment is not UNSET:
            field_dict["projectequipment"] = projectequipment
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if type is not UNSET:
            field_dict["type"] = type

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

        date = None
        _date = d.pop("date", UNSET)
        if _date is not None and not isinstance(_date, Unset):
            date = isoparse(_date)

        description = d.pop("description", UNSET)

        details = d.pop("details", UNSET)

        displayname = d.pop("displayname", UNSET)

        equipment = d.pop("equipment", UNSET)

        id = d.pop("id", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        projectequipment = d.pop("projectequipment", UNSET)

        stock_location = d.pop("stock_location", UNSET)

        type: Union[Unset, StockMovementCollectiongetResponseSchemaDataItemType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = StockMovementCollectiongetResponseSchemaDataItemType(_type)

        stock_movement_collectionget_response_schema_data_item = cls(
            amount=amount,
            created=created,
            creator=creator,
            date=date,
            description=description,
            details=details,
            displayname=displayname,
            equipment=equipment,
            id=id,
            modified=modified,
            projectequipment=projectequipment,
            stock_location=stock_location,
            type=type,
        )

        stock_movement_collectionget_response_schema_data_item.additional_properties = d
        return stock_movement_collectionget_response_schema_data_item

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
