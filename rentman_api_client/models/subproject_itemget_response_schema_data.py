import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.subproject_itemget_response_schema_data_custom import SubprojectItemgetResponseSchemaDataCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubprojectItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class SubprojectItemgetResponseSchemaData:
    """All the data about the requested items"""

    already_invoiced: Union[Unset, float] = UNSET
    asset_location_from: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    current: Union[Unset, float] = UNSET
    custom: Union[Unset, SubprojectItemgetResponseSchemaDataCustom] = UNSET
    discount_additional_costs: Union[Unset, float] = UNSET
    discount_crew: Union[Unset, float] = UNSET
    discount_fixed: Union[Unset, bool] = UNSET
    discount_fixed_amount: Union[Unset, float] = UNSET
    discount_rental: Union[Unset, float] = UNSET
    discount_sale: Union[Unset, float] = UNSET
    discount_subproject: Union[Unset, float] = UNSET
    discount_transport: Union[Unset, float] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment_period_from: Union[Unset, None, datetime.datetime] = UNSET
    equipment_period_to: Union[Unset, None, datetime.datetime] = UNSET
    fixed_price: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    in_financial: Union[Unset, bool] = UNSET
    in_planning: Union[Unset, bool] = UNSET
    insurance_rate: Union[Unset, float] = UNSET
    is_template: Union[Unset, bool] = UNSET
    loc_contact: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    power: Union[Unset, float] = UNSET
    project: Union[Unset, str] = UNSET
    project_crew_price: Union[Unset, float] = UNSET
    project_insurance_price: Union[Unset, float] = UNSET
    project_other_price: Union[Unset, float] = UNSET
    project_rental_price: Union[Unset, float] = UNSET
    project_sale_price: Union[Unset, float] = UNSET
    project_total_price: Union[Unset, float] = UNSET
    project_transport_price: Union[Unset, float] = UNSET
    purchasecosts: Union[Unset, float] = UNSET
    status: Union[Unset, str] = UNSET
    volume: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        already_invoiced = self.already_invoiced
        asset_location_from = self.asset_location_from
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        current = self.current
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        discount_additional_costs = self.discount_additional_costs
        discount_crew = self.discount_crew
        discount_fixed = self.discount_fixed
        discount_fixed_amount = self.discount_fixed_amount
        discount_rental = self.discount_rental
        discount_sale = self.discount_sale
        discount_subproject = self.discount_subproject
        discount_transport = self.discount_transport
        displayname = self.displayname
        equipment_period_from: Union[Unset, None, str] = UNSET
        if not isinstance(self.equipment_period_from, Unset):
            equipment_period_from = self.equipment_period_from.isoformat() if self.equipment_period_from else None

        equipment_period_to: Union[Unset, None, str] = UNSET
        if not isinstance(self.equipment_period_to, Unset):
            equipment_period_to = self.equipment_period_to.isoformat() if self.equipment_period_to else None

        fixed_price = self.fixed_price
        id = self.id
        in_financial = self.in_financial
        in_planning = self.in_planning
        insurance_rate = self.insurance_rate
        is_template = self.is_template
        loc_contact = self.loc_contact
        location = self.location
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        order = self.order
        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        power = self.power
        project = self.project
        project_crew_price = self.project_crew_price
        project_insurance_price = self.project_insurance_price
        project_other_price = self.project_other_price
        project_rental_price = self.project_rental_price
        project_sale_price = self.project_sale_price
        project_total_price = self.project_total_price
        project_transport_price = self.project_transport_price
        purchasecosts = self.purchasecosts
        status = self.status
        volume = self.volume
        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if already_invoiced is not UNSET:
            field_dict["already_invoiced"] = already_invoiced
        if asset_location_from is not UNSET:
            field_dict["asset_location_from"] = asset_location_from
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if current is not UNSET:
            field_dict["current"] = current
        if custom is not UNSET:
            field_dict["custom"] = custom
        if discount_additional_costs is not UNSET:
            field_dict["discount_additional_costs"] = discount_additional_costs
        if discount_crew is not UNSET:
            field_dict["discount_crew"] = discount_crew
        if discount_fixed is not UNSET:
            field_dict["discount_fixed"] = discount_fixed
        if discount_fixed_amount is not UNSET:
            field_dict["discount_fixed_amount"] = discount_fixed_amount
        if discount_rental is not UNSET:
            field_dict["discount_rental"] = discount_rental
        if discount_sale is not UNSET:
            field_dict["discount_sale"] = discount_sale
        if discount_subproject is not UNSET:
            field_dict["discount_subproject"] = discount_subproject
        if discount_transport is not UNSET:
            field_dict["discount_transport"] = discount_transport
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment_period_from is not UNSET:
            field_dict["equipment_period_from"] = equipment_period_from
        if equipment_period_to is not UNSET:
            field_dict["equipment_period_to"] = equipment_period_to
        if fixed_price is not UNSET:
            field_dict["fixed_price"] = fixed_price
        if id is not UNSET:
            field_dict["id"] = id
        if in_financial is not UNSET:
            field_dict["in_financial"] = in_financial
        if in_planning is not UNSET:
            field_dict["in_planning"] = in_planning
        if insurance_rate is not UNSET:
            field_dict["insurance_rate"] = insurance_rate
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if loc_contact is not UNSET:
            field_dict["loc_contact"] = loc_contact
        if location is not UNSET:
            field_dict["location"] = location
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if power is not UNSET:
            field_dict["power"] = power
        if project is not UNSET:
            field_dict["project"] = project
        if project_crew_price is not UNSET:
            field_dict["project_crew_price"] = project_crew_price
        if project_insurance_price is not UNSET:
            field_dict["project_insurance_price"] = project_insurance_price
        if project_other_price is not UNSET:
            field_dict["project_other_price"] = project_other_price
        if project_rental_price is not UNSET:
            field_dict["project_rental_price"] = project_rental_price
        if project_sale_price is not UNSET:
            field_dict["project_sale_price"] = project_sale_price
        if project_total_price is not UNSET:
            field_dict["project_total_price"] = project_total_price
        if project_transport_price is not UNSET:
            field_dict["project_transport_price"] = project_transport_price
        if purchasecosts is not UNSET:
            field_dict["purchasecosts"] = purchasecosts
        if status is not UNSET:
            field_dict["status"] = status
        if volume is not UNSET:
            field_dict["volume"] = volume
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        already_invoiced = d.pop("already_invoiced", UNSET)

        asset_location_from = d.pop("asset_location_from", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        current = d.pop("current", UNSET)

        custom: Union[Unset, SubprojectItemgetResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = SubprojectItemgetResponseSchemaDataCustom.from_dict(_custom)

        discount_additional_costs = d.pop("discount_additional_costs", UNSET)

        discount_crew = d.pop("discount_crew", UNSET)

        discount_fixed = d.pop("discount_fixed", UNSET)

        discount_fixed_amount = d.pop("discount_fixed_amount", UNSET)

        discount_rental = d.pop("discount_rental", UNSET)

        discount_sale = d.pop("discount_sale", UNSET)

        discount_subproject = d.pop("discount_subproject", UNSET)

        discount_transport = d.pop("discount_transport", UNSET)

        displayname = d.pop("displayname", UNSET)

        equipment_period_from = None
        _equipment_period_from = d.pop("equipment_period_from", UNSET)
        if _equipment_period_from is not None and not isinstance(_equipment_period_from, Unset):
            equipment_period_from = isoparse(_equipment_period_from)

        equipment_period_to = None
        _equipment_period_to = d.pop("equipment_period_to", UNSET)
        if _equipment_period_to is not None and not isinstance(_equipment_period_to, Unset):
            equipment_period_to = isoparse(_equipment_period_to)

        fixed_price = d.pop("fixed_price", UNSET)

        id = d.pop("id", UNSET)

        in_financial = d.pop("in_financial", UNSET)

        in_planning = d.pop("in_planning", UNSET)

        insurance_rate = d.pop("insurance_rate", UNSET)

        is_template = d.pop("is_template", UNSET)

        loc_contact = d.pop("loc_contact", UNSET)

        location = d.pop("location", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        power = d.pop("power", UNSET)

        project = d.pop("project", UNSET)

        project_crew_price = d.pop("project_crew_price", UNSET)

        project_insurance_price = d.pop("project_insurance_price", UNSET)

        project_other_price = d.pop("project_other_price", UNSET)

        project_rental_price = d.pop("project_rental_price", UNSET)

        project_sale_price = d.pop("project_sale_price", UNSET)

        project_total_price = d.pop("project_total_price", UNSET)

        project_transport_price = d.pop("project_transport_price", UNSET)

        purchasecosts = d.pop("purchasecosts", UNSET)

        status = d.pop("status", UNSET)

        volume = d.pop("volume", UNSET)

        weight = d.pop("weight", UNSET)

        subproject_itemget_response_schema_data = cls(
            already_invoiced=already_invoiced,
            asset_location_from=asset_location_from,
            created=created,
            creator=creator,
            current=current,
            custom=custom,
            discount_additional_costs=discount_additional_costs,
            discount_crew=discount_crew,
            discount_fixed=discount_fixed,
            discount_fixed_amount=discount_fixed_amount,
            discount_rental=discount_rental,
            discount_sale=discount_sale,
            discount_subproject=discount_subproject,
            discount_transport=discount_transport,
            displayname=displayname,
            equipment_period_from=equipment_period_from,
            equipment_period_to=equipment_period_to,
            fixed_price=fixed_price,
            id=id,
            in_financial=in_financial,
            in_planning=in_planning,
            insurance_rate=insurance_rate,
            is_template=is_template,
            loc_contact=loc_contact,
            location=location,
            modified=modified,
            name=name,
            order=order,
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            power=power,
            project=project,
            project_crew_price=project_crew_price,
            project_insurance_price=project_insurance_price,
            project_other_price=project_other_price,
            project_rental_price=project_rental_price,
            project_sale_price=project_sale_price,
            project_total_price=project_total_price,
            project_transport_price=project_transport_price,
            purchasecosts=purchasecosts,
            status=status,
            volume=volume,
            weight=weight,
        )

        subproject_itemget_response_schema_data.additional_properties = d
        return subproject_itemget_response_schema_data

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
