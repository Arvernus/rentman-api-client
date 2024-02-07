from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.project_itemget_request_schema_custom import ProjectItemgetRequestSchemaCustom
from ..models.project_itemget_request_schema_deposit_status import ProjectItemgetRequestSchemaDepositStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectItemgetRequestSchema")


@attr.s(auto_attribs=True)
class ProjectItemgetRequestSchema:
    """ """

    location: Union[Unset, None, str] = UNSET
    refundabledeposit: Union[Unset, float] = UNSET
    deposit_status: Union[Unset, ProjectItemgetRequestSchemaDepositStatus] = UNSET
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
    custom: Union[Unset, ProjectItemgetRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location = d.pop("location", UNSET)

        refundabledeposit = d.pop("refundabledeposit", UNSET)

        deposit_status: Union[Unset, ProjectItemgetRequestSchemaDepositStatus] = UNSET
        _deposit_status = d.pop("deposit_status", UNSET)
        if not isinstance(_deposit_status, Unset):
            deposit_status = ProjectItemgetRequestSchemaDepositStatus(_deposit_status)

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

        custom: Union[Unset, ProjectItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectItemgetRequestSchemaCustom.from_dict(_custom)

        project_itemget_request_schema = cls(
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
            custom=custom,
        )

        project_itemget_request_schema.additional_properties = d
        return project_itemget_request_schema

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
