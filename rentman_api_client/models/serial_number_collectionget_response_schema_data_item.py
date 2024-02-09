import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.serial_number_collectionget_response_schema_data_item_custom import (
    SerialNumberCollectiongetResponseSchemaDataItemCustom,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SerialNumberCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class SerialNumberCollectiongetResponseSchemaDataItem:
    """ """

    active: Union[Unset, bool] = UNSET
    asset_location: Union[Unset, None, str] = UNSET
    book_value: Union[Unset, float] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    current_book_value: Union[Unset, float] = UNSET
    custom: Union[Unset, SerialNumberCollectiongetResponseSchemaDataItemCustom] = UNSET
    depreciation_monthly: Union[Unset, float] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    next_inspection: Union[Unset, None, str] = UNSET
    purchase_costs: Union[Unset, float] = UNSET
    purchasedate: Union[Unset, None, str] = UNSET
    qrcodes: Union[Unset, str] = UNSET
    ref: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    tags: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        asset_location = self.asset_location
        book_value = self.book_value
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        current_book_value = self.current_book_value
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        depreciation_monthly = self.depreciation_monthly
        displayname = self.displayname
        equipment = self.equipment
        id = self.id
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        next_inspection = self.next_inspection
        purchase_costs = self.purchase_costs
        purchasedate = self.purchasedate
        qrcodes = self.qrcodes
        ref = self.ref
        remark = self.remark
        serial = self.serial
        tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if asset_location is not UNSET:
            field_dict["asset_location"] = asset_location
        if book_value is not UNSET:
            field_dict["book_value"] = book_value
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if current_book_value is not UNSET:
            field_dict["current_book_value"] = current_book_value
        if custom is not UNSET:
            field_dict["custom"] = custom
        if depreciation_monthly is not UNSET:
            field_dict["depreciation_monthly"] = depreciation_monthly
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if next_inspection is not UNSET:
            field_dict["next_inspection"] = next_inspection
        if purchase_costs is not UNSET:
            field_dict["purchase_costs"] = purchase_costs
        if purchasedate is not UNSET:
            field_dict["purchasedate"] = purchasedate
        if qrcodes is not UNSET:
            field_dict["qrcodes"] = qrcodes
        if ref is not UNSET:
            field_dict["ref"] = ref
        if remark is not UNSET:
            field_dict["remark"] = remark
        if serial is not UNSET:
            field_dict["serial"] = serial
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active", UNSET)

        asset_location = d.pop("asset_location", UNSET)

        book_value = d.pop("book_value", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        current_book_value = d.pop("current_book_value", UNSET)

        custom: Union[Unset, SerialNumberCollectiongetResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = SerialNumberCollectiongetResponseSchemaDataItemCustom.from_dict(_custom)

        depreciation_monthly = d.pop("depreciation_monthly", UNSET)

        displayname = d.pop("displayname", UNSET)

        equipment = d.pop("equipment", UNSET)

        id = d.pop("id", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        next_inspection = d.pop("next_inspection", UNSET)

        purchase_costs = d.pop("purchase_costs", UNSET)

        purchasedate = d.pop("purchasedate", UNSET)

        qrcodes = d.pop("qrcodes", UNSET)

        ref = d.pop("ref", UNSET)

        remark = d.pop("remark", UNSET)

        serial = d.pop("serial", UNSET)

        tags = d.pop("tags", UNSET)

        serial_number_collectionget_response_schema_data_item = cls(
            active=active,
            asset_location=asset_location,
            book_value=book_value,
            created=created,
            creator=creator,
            current_book_value=current_book_value,
            custom=custom,
            depreciation_monthly=depreciation_monthly,
            displayname=displayname,
            equipment=equipment,
            id=id,
            modified=modified,
            next_inspection=next_inspection,
            purchase_costs=purchase_costs,
            purchasedate=purchasedate,
            qrcodes=qrcodes,
            ref=ref,
            remark=remark,
            serial=serial,
            tags=tags,
        )

        serial_number_collectionget_response_schema_data_item.additional_properties = d
        return serial_number_collectionget_response_schema_data_item

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
