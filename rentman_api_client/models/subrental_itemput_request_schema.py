import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.subrental_itemput_request_schema_custom import SubrentalItemputRequestSchemaCustom
from ..models.subrental_itemput_request_schema_type import SubrentalItemputRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubrentalItemputRequestSchema")


@attr.s(auto_attribs=True)
class SubrentalItemputRequestSchema:
    """ """

    name: Union[Unset, str] = UNSET
    accountmanager: Union[Unset, None, str] = UNSET
    reference: Union[Unset, str] = UNSET
    supplier: Union[Unset, None, str] = UNSET
    number: Union[Unset, str] = UNSET
    contactperson: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    location_contact: Union[Unset, None, str] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    delivery_in: Union[Unset, None, datetime.datetime] = UNSET
    delivery_out: Union[Unset, None, datetime.datetime] = UNSET
    equipment_cost: Union[Unset, float] = UNSET
    price: Union[Unset, float] = UNSET
    extra_cost: Union[Unset, float] = UNSET
    auto_update_costs: Union[Unset, bool] = UNSET
    remark: Union[Unset, str] = UNSET
    type: Union[Unset, SubrentalItemputRequestSchemaType] = UNSET
    status: Union[Unset, str] = UNSET
    sent: Union[Unset, None, datetime.datetime] = UNSET
    asset_location_to: Union[Unset, None, str] = UNSET
    asset_location_from: Union[Unset, None, str] = UNSET
    is_internal: Union[Unset, bool] = UNSET
    supplier_project: Union[Unset, None, str] = UNSET
    custom: Union[Unset, SubrentalItemputRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        accountmanager = self.accountmanager
        reference = self.reference
        supplier = self.supplier
        number = self.number
        contactperson = self.contactperson
        location = self.location
        location_contact = self.location_contact
        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        delivery_in: Union[Unset, None, str] = UNSET
        if not isinstance(self.delivery_in, Unset):
            delivery_in = self.delivery_in.isoformat() if self.delivery_in else None

        delivery_out: Union[Unset, None, str] = UNSET
        if not isinstance(self.delivery_out, Unset):
            delivery_out = self.delivery_out.isoformat() if self.delivery_out else None

        equipment_cost = self.equipment_cost
        price = self.price
        extra_cost = self.extra_cost
        auto_update_costs = self.auto_update_costs
        remark = self.remark
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status = self.status
        sent: Union[Unset, None, str] = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.isoformat() if self.sent else None

        asset_location_to = self.asset_location_to
        asset_location_from = self.asset_location_from
        is_internal = self.is_internal
        supplier_project = self.supplier_project
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if accountmanager is not UNSET:
            field_dict["accountmanager"] = accountmanager
        if reference is not UNSET:
            field_dict["reference"] = reference
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if number is not UNSET:
            field_dict["number"] = number
        if contactperson is not UNSET:
            field_dict["contactperson"] = contactperson
        if location is not UNSET:
            field_dict["location"] = location
        if location_contact is not UNSET:
            field_dict["location_contact"] = location_contact
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if delivery_in is not UNSET:
            field_dict["delivery_in"] = delivery_in
        if delivery_out is not UNSET:
            field_dict["delivery_out"] = delivery_out
        if equipment_cost is not UNSET:
            field_dict["equipment_cost"] = equipment_cost
        if price is not UNSET:
            field_dict["price"] = price
        if extra_cost is not UNSET:
            field_dict["extra_cost"] = extra_cost
        if auto_update_costs is not UNSET:
            field_dict["auto_update_costs"] = auto_update_costs
        if remark is not UNSET:
            field_dict["remark"] = remark
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if sent is not UNSET:
            field_dict["sent"] = sent
        if asset_location_to is not UNSET:
            field_dict["asset_location_to"] = asset_location_to
        if asset_location_from is not UNSET:
            field_dict["asset_location_from"] = asset_location_from
        if is_internal is not UNSET:
            field_dict["is_internal"] = is_internal
        if supplier_project is not UNSET:
            field_dict["supplier_project"] = supplier_project
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        accountmanager = d.pop("accountmanager", UNSET)

        reference = d.pop("reference", UNSET)

        supplier = d.pop("supplier", UNSET)

        number = d.pop("number", UNSET)

        contactperson = d.pop("contactperson", UNSET)

        location = d.pop("location", UNSET)

        location_contact = d.pop("location_contact", UNSET)

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        delivery_in = None
        _delivery_in = d.pop("delivery_in", UNSET)
        if _delivery_in is not None and not isinstance(_delivery_in, Unset):
            delivery_in = isoparse(_delivery_in)

        delivery_out = None
        _delivery_out = d.pop("delivery_out", UNSET)
        if _delivery_out is not None and not isinstance(_delivery_out, Unset):
            delivery_out = isoparse(_delivery_out)

        equipment_cost = d.pop("equipment_cost", UNSET)

        price = d.pop("price", UNSET)

        extra_cost = d.pop("extra_cost", UNSET)

        auto_update_costs = d.pop("auto_update_costs", UNSET)

        remark = d.pop("remark", UNSET)

        type: Union[Unset, SubrentalItemputRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = SubrentalItemputRequestSchemaType(_type)

        status = d.pop("status", UNSET)

        sent = None
        _sent = d.pop("sent", UNSET)
        if _sent is not None and not isinstance(_sent, Unset):
            sent = isoparse(_sent)

        asset_location_to = d.pop("asset_location_to", UNSET)

        asset_location_from = d.pop("asset_location_from", UNSET)

        is_internal = d.pop("is_internal", UNSET)

        supplier_project = d.pop("supplier_project", UNSET)

        custom: Union[Unset, SubrentalItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = SubrentalItemputRequestSchemaCustom.from_dict(_custom)

        subrental_itemput_request_schema = cls(
            name=name,
            accountmanager=accountmanager,
            reference=reference,
            supplier=supplier,
            number=number,
            contactperson=contactperson,
            location=location,
            location_contact=location_contact,
            usageperiod_start=usageperiod_start,
            usageperiod_end=usageperiod_end,
            planperiod_start=planperiod_start,
            planperiod_end=planperiod_end,
            delivery_in=delivery_in,
            delivery_out=delivery_out,
            equipment_cost=equipment_cost,
            price=price,
            extra_cost=extra_cost,
            auto_update_costs=auto_update_costs,
            remark=remark,
            type=type,
            status=status,
            sent=sent,
            asset_location_to=asset_location_to,
            asset_location_from=asset_location_from,
            is_internal=is_internal,
            supplier_project=supplier_project,
            custom=custom,
        )

        subrental_itemput_request_schema.additional_properties = d
        return subrental_itemput_request_schema

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