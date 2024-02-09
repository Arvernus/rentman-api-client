import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.subrental_collectionput_response_schema_data_item_custom import (
    SubrentalCollectionputResponseSchemaDataItemCustom,
)
from ..models.subrental_collectionput_response_schema_data_item_type import (
    SubrentalCollectionputResponseSchemaDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubrentalCollectionputResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class SubrentalCollectionputResponseSchemaDataItem:
    """ """

    accountmanager: Union[Unset, None, str] = UNSET
    asset_location_from: Union[Unset, None, str] = UNSET
    asset_location_to: Union[Unset, None, str] = UNSET
    auto_update_costs: Union[Unset, bool] = UNSET
    contactperson: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    custom: Union[Unset, SubrentalCollectionputResponseSchemaDataItemCustom] = UNSET
    delivery_in: Union[Unset, None, datetime.datetime] = UNSET
    delivery_out: Union[Unset, None, datetime.datetime] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment_cost: Union[Unset, float] = UNSET
    extra_cost: Union[Unset, float] = UNSET
    id: Union[Unset, int] = UNSET
    is_internal: Union[Unset, bool] = UNSET
    location: Union[Unset, None, str] = UNSET
    location_contact: Union[Unset, None, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    price: Union[Unset, float] = UNSET
    reference: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    sent: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    supplier: Union[Unset, None, str] = UNSET
    supplier_project: Union[Unset, None, str] = UNSET
    tags: Union[Unset, str] = UNSET
    type: Union[Unset, SubrentalCollectionputResponseSchemaDataItemType] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accountmanager = self.accountmanager
        asset_location_from = self.asset_location_from
        asset_location_to = self.asset_location_to
        auto_update_costs = self.auto_update_costs
        contactperson = self.contactperson
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        delivery_in: Union[Unset, None, str] = UNSET
        if not isinstance(self.delivery_in, Unset):
            delivery_in = self.delivery_in.isoformat() if self.delivery_in else None

        delivery_out: Union[Unset, None, str] = UNSET
        if not isinstance(self.delivery_out, Unset):
            delivery_out = self.delivery_out.isoformat() if self.delivery_out else None

        displayname = self.displayname
        equipment_cost = self.equipment_cost
        extra_cost = self.extra_cost
        id = self.id
        is_internal = self.is_internal
        location = self.location
        location_contact = self.location_contact
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        number = self.number
        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        price = self.price
        reference = self.reference
        remark = self.remark
        sent: Union[Unset, None, str] = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.isoformat() if self.sent else None

        status = self.status
        supplier = self.supplier
        supplier_project = self.supplier_project
        tags = self.tags
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accountmanager is not UNSET:
            field_dict["accountmanager"] = accountmanager
        if asset_location_from is not UNSET:
            field_dict["asset_location_from"] = asset_location_from
        if asset_location_to is not UNSET:
            field_dict["asset_location_to"] = asset_location_to
        if auto_update_costs is not UNSET:
            field_dict["auto_update_costs"] = auto_update_costs
        if contactperson is not UNSET:
            field_dict["contactperson"] = contactperson
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if custom is not UNSET:
            field_dict["custom"] = custom
        if delivery_in is not UNSET:
            field_dict["delivery_in"] = delivery_in
        if delivery_out is not UNSET:
            field_dict["delivery_out"] = delivery_out
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment_cost is not UNSET:
            field_dict["equipment_cost"] = equipment_cost
        if extra_cost is not UNSET:
            field_dict["extra_cost"] = extra_cost
        if id is not UNSET:
            field_dict["id"] = id
        if is_internal is not UNSET:
            field_dict["is_internal"] = is_internal
        if location is not UNSET:
            field_dict["location"] = location
        if location_contact is not UNSET:
            field_dict["location_contact"] = location_contact
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if price is not UNSET:
            field_dict["price"] = price
        if reference is not UNSET:
            field_dict["reference"] = reference
        if remark is not UNSET:
            field_dict["remark"] = remark
        if sent is not UNSET:
            field_dict["sent"] = sent
        if status is not UNSET:
            field_dict["status"] = status
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if supplier_project is not UNSET:
            field_dict["supplier_project"] = supplier_project
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type is not UNSET:
            field_dict["type"] = type
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accountmanager = d.pop("accountmanager", UNSET)

        asset_location_from = d.pop("asset_location_from", UNSET)

        asset_location_to = d.pop("asset_location_to", UNSET)

        auto_update_costs = d.pop("auto_update_costs", UNSET)

        contactperson = d.pop("contactperson", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        custom: Union[Unset, SubrentalCollectionputResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = SubrentalCollectionputResponseSchemaDataItemCustom.from_dict(_custom)

        delivery_in = None
        _delivery_in = d.pop("delivery_in", UNSET)
        if _delivery_in is not None and not isinstance(_delivery_in, Unset):
            delivery_in = isoparse(_delivery_in)

        delivery_out = None
        _delivery_out = d.pop("delivery_out", UNSET)
        if _delivery_out is not None and not isinstance(_delivery_out, Unset):
            delivery_out = isoparse(_delivery_out)

        displayname = d.pop("displayname", UNSET)

        equipment_cost = d.pop("equipment_cost", UNSET)

        extra_cost = d.pop("extra_cost", UNSET)

        id = d.pop("id", UNSET)

        is_internal = d.pop("is_internal", UNSET)

        location = d.pop("location", UNSET)

        location_contact = d.pop("location_contact", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        price = d.pop("price", UNSET)

        reference = d.pop("reference", UNSET)

        remark = d.pop("remark", UNSET)

        sent = None
        _sent = d.pop("sent", UNSET)
        if _sent is not None and not isinstance(_sent, Unset):
            sent = isoparse(_sent)

        status = d.pop("status", UNSET)

        supplier = d.pop("supplier", UNSET)

        supplier_project = d.pop("supplier_project", UNSET)

        tags = d.pop("tags", UNSET)

        type: Union[Unset, SubrentalCollectionputResponseSchemaDataItemType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = SubrentalCollectionputResponseSchemaDataItemType(_type)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        subrental_collectionput_response_schema_data_item = cls(
            accountmanager=accountmanager,
            asset_location_from=asset_location_from,
            asset_location_to=asset_location_to,
            auto_update_costs=auto_update_costs,
            contactperson=contactperson,
            created=created,
            creator=creator,
            custom=custom,
            delivery_in=delivery_in,
            delivery_out=delivery_out,
            displayname=displayname,
            equipment_cost=equipment_cost,
            extra_cost=extra_cost,
            id=id,
            is_internal=is_internal,
            location=location,
            location_contact=location_contact,
            modified=modified,
            name=name,
            number=number,
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            price=price,
            reference=reference,
            remark=remark,
            sent=sent,
            status=status,
            supplier=supplier,
            supplier_project=supplier_project,
            tags=tags,
            type=type,
            usageperiod_end=usageperiod_end,
            usageperiod_start=usageperiod_start,
        )

        subrental_collectionput_response_schema_data_item.additional_properties = d
        return subrental_collectionput_response_schema_data_item

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
