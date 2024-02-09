from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.subproject_itemget_request_schema_custom import SubprojectItemgetRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubprojectItemgetRequestSchema")


@attr.s(auto_attribs=True)
class SubprojectItemgetRequestSchema:
    """ """

    asset_location_from: Union[Unset, None, str] = UNSET
    custom: Union[Unset, SubprojectItemgetRequestSchemaCustom] = UNSET
    discount_additional_costs: Union[Unset, float] = UNSET
    discount_crew: Union[Unset, float] = UNSET
    discount_fixed: Union[Unset, bool] = UNSET
    discount_fixed_amount: Union[Unset, float] = UNSET
    discount_rental: Union[Unset, float] = UNSET
    discount_sale: Union[Unset, float] = UNSET
    discount_subproject: Union[Unset, float] = UNSET
    discount_transport: Union[Unset, float] = UNSET
    fixed_price: Union[Unset, bool] = UNSET
    in_financial: Union[Unset, bool] = UNSET
    in_planning: Union[Unset, bool] = UNSET
    insurance_rate: Union[Unset, float] = UNSET
    is_template: Union[Unset, bool] = UNSET
    loc_contact: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_location_from = self.asset_location_from
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
        fixed_price = self.fixed_price
        in_financial = self.in_financial
        in_planning = self.in_planning
        insurance_rate = self.insurance_rate
        is_template = self.is_template
        loc_contact = self.loc_contact
        location = self.location
        name = self.name
        order = self.order
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_location_from is not UNSET:
            field_dict["asset_location_from"] = asset_location_from
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
        if fixed_price is not UNSET:
            field_dict["fixed_price"] = fixed_price
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
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_location_from = d.pop("asset_location_from", UNSET)

        custom: Union[Unset, SubprojectItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = SubprojectItemgetRequestSchemaCustom.from_dict(_custom)

        discount_additional_costs = d.pop("discount_additional_costs", UNSET)

        discount_crew = d.pop("discount_crew", UNSET)

        discount_fixed = d.pop("discount_fixed", UNSET)

        discount_fixed_amount = d.pop("discount_fixed_amount", UNSET)

        discount_rental = d.pop("discount_rental", UNSET)

        discount_sale = d.pop("discount_sale", UNSET)

        discount_subproject = d.pop("discount_subproject", UNSET)

        discount_transport = d.pop("discount_transport", UNSET)

        fixed_price = d.pop("fixed_price", UNSET)

        in_financial = d.pop("in_financial", UNSET)

        in_planning = d.pop("in_planning", UNSET)

        insurance_rate = d.pop("insurance_rate", UNSET)

        is_template = d.pop("is_template", UNSET)

        loc_contact = d.pop("loc_contact", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        status = d.pop("status", UNSET)

        subproject_itemget_request_schema = cls(
            asset_location_from=asset_location_from,
            custom=custom,
            discount_additional_costs=discount_additional_costs,
            discount_crew=discount_crew,
            discount_fixed=discount_fixed,
            discount_fixed_amount=discount_fixed_amount,
            discount_rental=discount_rental,
            discount_sale=discount_sale,
            discount_subproject=discount_subproject,
            discount_transport=discount_transport,
            fixed_price=fixed_price,
            in_financial=in_financial,
            in_planning=in_planning,
            insurance_rate=insurance_rate,
            is_template=is_template,
            loc_contact=loc_contact,
            location=location,
            name=name,
            order=order,
            status=status,
        )

        subproject_itemget_request_schema.additional_properties = d
        return subproject_itemget_request_schema

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
