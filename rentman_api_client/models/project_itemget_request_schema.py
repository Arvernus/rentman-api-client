from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.project_itemget_request_schema_custom import ProjectItemgetRequestSchemaCustom
from ..models.project_itemget_request_schema_deposit_status import ProjectItemgetRequestSchemaDepositStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectItemgetRequestSchema")


@attr.s(auto_attribs=True)
class ProjectItemgetRequestSchema:
    """ """

    account_manager: Union[Unset, None, str] = UNSET
    color: Union[Unset, str] = UNSET
    conditions: Union[Unset, str] = UNSET
    cust_contact: Union[Unset, None, str] = UNSET
    custom: Union[Unset, ProjectItemgetRequestSchemaCustom] = UNSET
    customer: Union[Unset, None, str] = UNSET
    deposit_status: Union[Unset, ProjectItemgetRequestSchemaDepositStatus] = UNSET
    loc_contact: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    project_type: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    refundabledeposit: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_manager = self.account_manager
        color = self.color
        conditions = self.conditions
        cust_contact = self.cust_contact
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        customer = self.customer
        deposit_status: Union[Unset, str] = UNSET
        if not isinstance(self.deposit_status, Unset):
            deposit_status = self.deposit_status.value

        loc_contact = self.loc_contact
        location = self.location
        name = self.name
        number = self.number
        project_type = self.project_type
        reference = self.reference
        refundabledeposit = self.refundabledeposit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_manager is not UNSET:
            field_dict["account_manager"] = account_manager
        if color is not UNSET:
            field_dict["color"] = color
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if cust_contact is not UNSET:
            field_dict["cust_contact"] = cust_contact
        if custom is not UNSET:
            field_dict["custom"] = custom
        if customer is not UNSET:
            field_dict["customer"] = customer
        if deposit_status is not UNSET:
            field_dict["deposit_status"] = deposit_status
        if loc_contact is not UNSET:
            field_dict["loc_contact"] = loc_contact
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if project_type is not UNSET:
            field_dict["project_type"] = project_type
        if reference is not UNSET:
            field_dict["reference"] = reference
        if refundabledeposit is not UNSET:
            field_dict["refundabledeposit"] = refundabledeposit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_manager = d.pop("account_manager", UNSET)

        color = d.pop("color", UNSET)

        conditions = d.pop("conditions", UNSET)

        cust_contact = d.pop("cust_contact", UNSET)

        custom: Union[Unset, ProjectItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectItemgetRequestSchemaCustom.from_dict(_custom)

        customer = d.pop("customer", UNSET)

        deposit_status: Union[Unset, ProjectItemgetRequestSchemaDepositStatus] = UNSET
        _deposit_status = d.pop("deposit_status", UNSET)
        if not isinstance(_deposit_status, Unset):
            deposit_status = ProjectItemgetRequestSchemaDepositStatus(_deposit_status)

        loc_contact = d.pop("loc_contact", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        project_type = d.pop("project_type", UNSET)

        reference = d.pop("reference", UNSET)

        refundabledeposit = d.pop("refundabledeposit", UNSET)

        project_itemget_request_schema = cls(
            account_manager=account_manager,
            color=color,
            conditions=conditions,
            cust_contact=cust_contact,
            custom=custom,
            customer=customer,
            deposit_status=deposit_status,
            loc_contact=loc_contact,
            location=location,
            name=name,
            number=number,
            project_type=project_type,
            reference=reference,
            refundabledeposit=refundabledeposit,
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
