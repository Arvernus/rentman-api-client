import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_collectionget_response_schema_data_item_custom import (
    ProjectCollectiongetResponseSchemaDataItemCustom,
)
from ..models.project_collectionget_response_schema_data_item_deposit_status import (
    ProjectCollectiongetResponseSchemaDataItemDepositStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class ProjectCollectiongetResponseSchemaDataItem:
    """ """

    account_manager: Union[Unset, None, str] = UNSET
    already_invoiced: Union[Unset, float] = UNSET
    color: Union[Unset, str] = UNSET
    conditions: Union[Unset, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    current: Union[Unset, float] = UNSET
    cust_contact: Union[Unset, None, str] = UNSET
    custom: Union[Unset, ProjectCollectiongetResponseSchemaDataItemCustom] = UNSET
    customer: Union[Unset, None, str] = UNSET
    deposit_status: Union[Unset, ProjectCollectiongetResponseSchemaDataItemDepositStatus] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment_period_from: Union[Unset, None, datetime.datetime] = UNSET
    equipment_period_to: Union[Unset, None, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    loc_contact: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    power: Union[Unset, float] = UNSET
    project_type: Union[Unset, str] = UNSET
    purchasecosts: Union[Unset, float] = UNSET
    reference: Union[Unset, str] = UNSET
    refundabledeposit: Union[Unset, float] = UNSET
    tags: Union[Unset, str] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    volume: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_manager = self.account_manager
        already_invoiced = self.already_invoiced
        color = self.color
        conditions = self.conditions
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        current = self.current
        cust_contact = self.cust_contact
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        customer = self.customer
        deposit_status: Union[Unset, str] = UNSET
        if not isinstance(self.deposit_status, Unset):
            deposit_status = self.deposit_status.value

        displayname = self.displayname
        equipment_period_from: Union[Unset, None, str] = UNSET
        if not isinstance(self.equipment_period_from, Unset):
            equipment_period_from = self.equipment_period_from.isoformat() if self.equipment_period_from else None

        equipment_period_to: Union[Unset, None, str] = UNSET
        if not isinstance(self.equipment_period_to, Unset):
            equipment_period_to = self.equipment_period_to.isoformat() if self.equipment_period_to else None

        id = self.id
        loc_contact = self.loc_contact
        location = self.location
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

        power = self.power
        project_type = self.project_type
        purchasecosts = self.purchasecosts
        reference = self.reference
        refundabledeposit = self.refundabledeposit
        tags = self.tags
        usageperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_end, Unset):
            usageperiod_end = self.usageperiod_end.isoformat() if self.usageperiod_end else None

        usageperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.usageperiod_start, Unset):
            usageperiod_start = self.usageperiod_start.isoformat() if self.usageperiod_start else None

        volume = self.volume
        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_manager is not UNSET:
            field_dict["account_manager"] = account_manager
        if already_invoiced is not UNSET:
            field_dict["already_invoiced"] = already_invoiced
        if color is not UNSET:
            field_dict["color"] = color
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if current is not UNSET:
            field_dict["current"] = current
        if cust_contact is not UNSET:
            field_dict["cust_contact"] = cust_contact
        if custom is not UNSET:
            field_dict["custom"] = custom
        if customer is not UNSET:
            field_dict["customer"] = customer
        if deposit_status is not UNSET:
            field_dict["deposit_status"] = deposit_status
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment_period_from is not UNSET:
            field_dict["equipment_period_from"] = equipment_period_from
        if equipment_period_to is not UNSET:
            field_dict["equipment_period_to"] = equipment_period_to
        if id is not UNSET:
            field_dict["id"] = id
        if loc_contact is not UNSET:
            field_dict["loc_contact"] = loc_contact
        if location is not UNSET:
            field_dict["location"] = location
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
        if power is not UNSET:
            field_dict["power"] = power
        if project_type is not UNSET:
            field_dict["project_type"] = project_type
        if purchasecosts is not UNSET:
            field_dict["purchasecosts"] = purchasecosts
        if reference is not UNSET:
            field_dict["reference"] = reference
        if refundabledeposit is not UNSET:
            field_dict["refundabledeposit"] = refundabledeposit
        if tags is not UNSET:
            field_dict["tags"] = tags
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start
        if volume is not UNSET:
            field_dict["volume"] = volume
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_manager = d.pop("account_manager", UNSET)

        already_invoiced = d.pop("already_invoiced", UNSET)

        color = d.pop("color", UNSET)

        conditions = d.pop("conditions", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        current = d.pop("current", UNSET)

        cust_contact = d.pop("cust_contact", UNSET)

        custom: Union[Unset, ProjectCollectiongetResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectCollectiongetResponseSchemaDataItemCustom.from_dict(_custom)

        customer = d.pop("customer", UNSET)

        deposit_status: Union[Unset, ProjectCollectiongetResponseSchemaDataItemDepositStatus] = UNSET
        _deposit_status = d.pop("deposit_status", UNSET)
        if not isinstance(_deposit_status, Unset):
            deposit_status = ProjectCollectiongetResponseSchemaDataItemDepositStatus(_deposit_status)

        displayname = d.pop("displayname", UNSET)

        equipment_period_from = None
        _equipment_period_from = d.pop("equipment_period_from", UNSET)
        if _equipment_period_from is not None and not isinstance(_equipment_period_from, Unset):
            equipment_period_from = isoparse(_equipment_period_from)

        equipment_period_to = None
        _equipment_period_to = d.pop("equipment_period_to", UNSET)
        if _equipment_period_to is not None and not isinstance(_equipment_period_to, Unset):
            equipment_period_to = isoparse(_equipment_period_to)

        id = d.pop("id", UNSET)

        loc_contact = d.pop("loc_contact", UNSET)

        location = d.pop("location", UNSET)

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

        power = d.pop("power", UNSET)

        project_type = d.pop("project_type", UNSET)

        purchasecosts = d.pop("purchasecosts", UNSET)

        reference = d.pop("reference", UNSET)

        refundabledeposit = d.pop("refundabledeposit", UNSET)

        tags = d.pop("tags", UNSET)

        usageperiod_end = None
        _usageperiod_end = d.pop("usageperiod_end", UNSET)
        if _usageperiod_end is not None and not isinstance(_usageperiod_end, Unset):
            usageperiod_end = isoparse(_usageperiod_end)

        usageperiod_start = None
        _usageperiod_start = d.pop("usageperiod_start", UNSET)
        if _usageperiod_start is not None and not isinstance(_usageperiod_start, Unset):
            usageperiod_start = isoparse(_usageperiod_start)

        volume = d.pop("volume", UNSET)

        weight = d.pop("weight", UNSET)

        project_collectionget_response_schema_data_item = cls(
            account_manager=account_manager,
            already_invoiced=already_invoiced,
            color=color,
            conditions=conditions,
            created=created,
            creator=creator,
            current=current,
            cust_contact=cust_contact,
            custom=custom,
            customer=customer,
            deposit_status=deposit_status,
            displayname=displayname,
            equipment_period_from=equipment_period_from,
            equipment_period_to=equipment_period_to,
            id=id,
            loc_contact=loc_contact,
            location=location,
            modified=modified,
            name=name,
            number=number,
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            power=power,
            project_type=project_type,
            purchasecosts=purchasecosts,
            reference=reference,
            refundabledeposit=refundabledeposit,
            tags=tags,
            usageperiod_end=usageperiod_end,
            usageperiod_start=usageperiod_start,
            volume=volume,
            weight=weight,
        )

        project_collectionget_response_schema_data_item.additional_properties = d
        return project_collectionget_response_schema_data_item

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
