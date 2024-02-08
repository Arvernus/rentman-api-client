import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_itemget_response_schema_data_custom import ProjectItemgetResponseSchemaDataCustom
from ..models.project_itemget_response_schema_data_deposit_status import ProjectItemgetResponseSchemaDataDepositStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class ProjectItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    refundabledeposit: Union[Unset, float] = UNSET
    deposit_status: Union[Unset, ProjectItemgetResponseSchemaDataDepositStatus] = UNSET
    customer: Union[Unset, None, str] = UNSET
    loc_contact: Union[Unset, None, str] = UNSET
    cust_contact: Union[Unset, None, str] = UNSET
    project_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    account_manager: Union[Unset, None, str] = UNSET
    color: Union[Unset, str] = UNSET
    conditions: Union[Unset, str] = UNSET
    project_total_price: Union[Unset, float] = UNSET
    project_rental_price: Union[Unset, float] = UNSET
    project_sale_price: Union[Unset, float] = UNSET
    project_crew_price: Union[Unset, float] = UNSET
    project_transport_price: Union[Unset, float] = UNSET
    project_other_price: Union[Unset, float] = UNSET
    project_insurance_price: Union[Unset, float] = UNSET
    already_invoiced: Union[Unset, float] = UNSET
    tags: Union[Unset, str] = UNSET
    usageperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    usageperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    volume: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    power: Union[Unset, float] = UNSET
    current: Union[Unset, float] = UNSET
    equipment_period_from: Union[Unset, None, datetime.datetime] = UNSET
    equipment_period_to: Union[Unset, None, datetime.datetime] = UNSET
    purchasecosts: Union[Unset, float] = UNSET
    custom: Union[Unset, ProjectItemgetResponseSchemaDataCustom] = UNSET
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
        location = self.location
        refundabledeposit = self.refundabledeposit
        deposit_status: Union[Unset, str] = UNSET
        if not isinstance(self.deposit_status, Unset):
            deposit_status = self.deposit_status.value

        customer = self.customer
        loc_contact = self.loc_contact
        cust_contact = self.cust_contact
        project_type = self.project_type
        name = self.name
        reference = self.reference
        number = self.number
        account_manager = self.account_manager
        color = self.color
        conditions = self.conditions
        project_total_price = self.project_total_price
        project_rental_price = self.project_rental_price
        project_sale_price = self.project_sale_price
        project_crew_price = self.project_crew_price
        project_transport_price = self.project_transport_price
        project_other_price = self.project_other_price
        project_insurance_price = self.project_insurance_price
        already_invoiced = self.already_invoiced
        tags = self.tags
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

        volume = self.volume
        weight = self.weight
        power = self.power
        current = self.current
        equipment_period_from: Union[Unset, None, str] = UNSET
        if not isinstance(self.equipment_period_from, Unset):
            equipment_period_from = self.equipment_period_from.isoformat() if self.equipment_period_from else None

        equipment_period_to: Union[Unset, None, str] = UNSET
        if not isinstance(self.equipment_period_to, Unset):
            equipment_period_to = self.equipment_period_to.isoformat() if self.equipment_period_to else None

        purchasecosts = self.purchasecosts
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
        if location is not UNSET:
            field_dict["location"] = location
        if refundabledeposit is not UNSET:
            field_dict["refundabledeposit"] = refundabledeposit
        if deposit_status is not UNSET:
            field_dict["deposit_status"] = deposit_status
        if customer is not UNSET:
            field_dict["customer"] = customer
        if loc_contact is not UNSET:
            field_dict["loc_contact"] = loc_contact
        if cust_contact is not UNSET:
            field_dict["cust_contact"] = cust_contact
        if project_type is not UNSET:
            field_dict["project_type"] = project_type
        if name is not UNSET:
            field_dict["name"] = name
        if reference is not UNSET:
            field_dict["reference"] = reference
        if number is not UNSET:
            field_dict["number"] = number
        if account_manager is not UNSET:
            field_dict["account_manager"] = account_manager
        if color is not UNSET:
            field_dict["color"] = color
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if project_total_price is not UNSET:
            field_dict["project_total_price"] = project_total_price
        if project_rental_price is not UNSET:
            field_dict["project_rental_price"] = project_rental_price
        if project_sale_price is not UNSET:
            field_dict["project_sale_price"] = project_sale_price
        if project_crew_price is not UNSET:
            field_dict["project_crew_price"] = project_crew_price
        if project_transport_price is not UNSET:
            field_dict["project_transport_price"] = project_transport_price
        if project_other_price is not UNSET:
            field_dict["project_other_price"] = project_other_price
        if project_insurance_price is not UNSET:
            field_dict["project_insurance_price"] = project_insurance_price
        if already_invoiced is not UNSET:
            field_dict["already_invoiced"] = already_invoiced
        if tags is not UNSET:
            field_dict["tags"] = tags
        if usageperiod_start is not UNSET:
            field_dict["usageperiod_start"] = usageperiod_start
        if usageperiod_end is not UNSET:
            field_dict["usageperiod_end"] = usageperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if volume is not UNSET:
            field_dict["volume"] = volume
        if weight is not UNSET:
            field_dict["weight"] = weight
        if power is not UNSET:
            field_dict["power"] = power
        if current is not UNSET:
            field_dict["current"] = current
        if equipment_period_from is not UNSET:
            field_dict["equipment_period_from"] = equipment_period_from
        if equipment_period_to is not UNSET:
            field_dict["equipment_period_to"] = equipment_period_to
        if purchasecosts is not UNSET:
            field_dict["purchasecosts"] = purchasecosts
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

        location = d.pop("location", UNSET)

        refundabledeposit = d.pop("refundabledeposit", UNSET)

        deposit_status: Union[Unset, ProjectItemgetResponseSchemaDataDepositStatus] = UNSET
        _deposit_status = d.pop("deposit_status", UNSET)
        if not isinstance(_deposit_status, Unset):
            deposit_status = ProjectItemgetResponseSchemaDataDepositStatus(_deposit_status)

        customer = d.pop("customer", UNSET)

        loc_contact = d.pop("loc_contact", UNSET)

        cust_contact = d.pop("cust_contact", UNSET)

        project_type = d.pop("project_type", UNSET)

        name = d.pop("name", UNSET)

        reference = d.pop("reference", UNSET)

        number = d.pop("number", UNSET)

        account_manager = d.pop("account_manager", UNSET)

        color = d.pop("color", UNSET)

        conditions = d.pop("conditions", UNSET)

        project_total_price = d.pop("project_total_price", UNSET)

        project_rental_price = d.pop("project_rental_price", UNSET)

        project_sale_price = d.pop("project_sale_price", UNSET)

        project_crew_price = d.pop("project_crew_price", UNSET)

        project_transport_price = d.pop("project_transport_price", UNSET)

        project_other_price = d.pop("project_other_price", UNSET)

        project_insurance_price = d.pop("project_insurance_price", UNSET)

        already_invoiced = d.pop("already_invoiced", UNSET)

        tags = d.pop("tags", UNSET)

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

        volume = d.pop("volume", UNSET)

        weight = d.pop("weight", UNSET)

        power = d.pop("power", UNSET)

        current = d.pop("current", UNSET)

        equipment_period_from = None
        _equipment_period_from = d.pop("equipment_period_from", UNSET)
        if _equipment_period_from is not None and not isinstance(_equipment_period_from, Unset):
            equipment_period_from = isoparse(_equipment_period_from)

        equipment_period_to = None
        _equipment_period_to = d.pop("equipment_period_to", UNSET)
        if _equipment_period_to is not None and not isinstance(_equipment_period_to, Unset):
            equipment_period_to = isoparse(_equipment_period_to)

        purchasecosts = d.pop("purchasecosts", UNSET)

        custom: Union[Unset, ProjectItemgetResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectItemgetResponseSchemaDataCustom.from_dict(_custom)

        project_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            location=location,
            refundabledeposit=refundabledeposit,
            deposit_status=deposit_status,
            customer=customer,
            loc_contact=loc_contact,
            cust_contact=cust_contact,
            project_type=project_type,
            name=name,
            reference=reference,
            number=number,
            account_manager=account_manager,
            color=color,
            conditions=conditions,
            project_total_price=project_total_price,
            project_rental_price=project_rental_price,
            project_sale_price=project_sale_price,
            project_crew_price=project_crew_price,
            project_transport_price=project_transport_price,
            project_other_price=project_other_price,
            project_insurance_price=project_insurance_price,
            already_invoiced=already_invoiced,
            tags=tags,
            usageperiod_start=usageperiod_start,
            usageperiod_end=usageperiod_end,
            planperiod_start=planperiod_start,
            planperiod_end=planperiod_end,
            volume=volume,
            weight=weight,
            power=power,
            current=current,
            equipment_period_from=equipment_period_from,
            equipment_period_to=equipment_period_to,
            purchasecosts=purchasecosts,
            custom=custom,
        )

        project_itemget_response_schema_data.additional_properties = d
        return project_itemget_response_schema_data

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
