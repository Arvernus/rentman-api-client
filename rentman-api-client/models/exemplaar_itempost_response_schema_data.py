import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.exemplaar_itempost_response_schema_data_custom import ExemplaarItempostResponseSchemaDataCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExemplaarItempostResponseSchemaData")


@attr.s(auto_attribs=True)
class ExemplaarItempostResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    purchasedate: Union[Unset, None, str] = UNSET
    depreciation_monthly: Union[Unset, float] = UNSET
    book_value: Union[Unset, float] = UNSET
    purchase_costs: Union[Unset, float] = UNSET
    active: Union[Unset, bool] = UNSET
    remark: Union[Unset, str] = UNSET
    ref: Union[Unset, str] = UNSET
    asset_location: Union[Unset, None, str] = UNSET
    current_book_value: Union[Unset, float] = UNSET
    next_inspection: Union[Unset, None, str] = UNSET
    qrcodes: Union[Unset, str] = UNSET
    tags: Union[Unset, str] = UNSET
    custom: Union[Unset, ExemplaarItempostResponseSchemaDataCustom] = UNSET
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
        equipment = self.equipment
        serial = self.serial
        purchasedate = self.purchasedate
        depreciation_monthly = self.depreciation_monthly
        book_value = self.book_value
        purchase_costs = self.purchase_costs
        active = self.active
        remark = self.remark
        ref = self.ref
        asset_location = self.asset_location
        current_book_value = self.current_book_value
        next_inspection = self.next_inspection
        qrcodes = self.qrcodes
        tags = self.tags
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

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
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if serial is not UNSET:
            field_dict["serial"] = serial
        if purchasedate is not UNSET:
            field_dict["purchasedate"] = purchasedate
        if depreciation_monthly is not UNSET:
            field_dict["depreciation_monthly"] = depreciation_monthly
        if book_value is not UNSET:
            field_dict["book_value"] = book_value
        if purchase_costs is not UNSET:
            field_dict["purchase_costs"] = purchase_costs
        if active is not UNSET:
            field_dict["active"] = active
        if remark is not UNSET:
            field_dict["remark"] = remark
        if ref is not UNSET:
            field_dict["ref"] = ref
        if asset_location is not UNSET:
            field_dict["asset_location"] = asset_location
        if current_book_value is not UNSET:
            field_dict["current_book_value"] = current_book_value
        if next_inspection is not UNSET:
            field_dict["next_inspection"] = next_inspection
        if qrcodes is not UNSET:
            field_dict["qrcodes"] = qrcodes
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom is not UNSET:
            field_dict["custom"] = custom

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

        equipment = d.pop("equipment", UNSET)

        serial = d.pop("serial", UNSET)

        purchasedate = d.pop("purchasedate", UNSET)

        depreciation_monthly = d.pop("depreciation_monthly", UNSET)

        book_value = d.pop("book_value", UNSET)

        purchase_costs = d.pop("purchase_costs", UNSET)

        active = d.pop("active", UNSET)

        remark = d.pop("remark", UNSET)

        ref = d.pop("ref", UNSET)

        asset_location = d.pop("asset_location", UNSET)

        current_book_value = d.pop("current_book_value", UNSET)

        next_inspection = d.pop("next_inspection", UNSET)

        qrcodes = d.pop("qrcodes", UNSET)

        tags = d.pop("tags", UNSET)

        custom: Union[Unset, ExemplaarItempostResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ExemplaarItempostResponseSchemaDataCustom.from_dict(_custom)

        exemplaar_itempost_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            equipment=equipment,
            serial=serial,
            purchasedate=purchasedate,
            depreciation_monthly=depreciation_monthly,
            book_value=book_value,
            purchase_costs=purchase_costs,
            active=active,
            remark=remark,
            ref=ref,
            asset_location=asset_location,
            current_book_value=current_book_value,
            next_inspection=next_inspection,
            qrcodes=qrcodes,
            tags=tags,
            custom=custom,
        )

        exemplaar_itempost_response_schema_data.additional_properties = d
        return exemplaar_itempost_response_schema_data

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
