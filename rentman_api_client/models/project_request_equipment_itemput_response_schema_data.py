import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectRequestEquipmentItemputResponseSchemaData")


@attr.s(auto_attribs=True)
class ProjectRequestEquipmentItemputResponseSchemaData:
    """All the data about the requested items"""

    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    discount: Union[Unset, float] = UNSET
    displayname: Union[Unset, str] = UNSET
    external_remark: Union[Unset, str] = UNSET
    factor: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_comment: Union[Unset, bool] = UNSET
    is_kit: Union[Unset, bool] = UNSET
    linked_equipment: Union[Unset, None, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    project_request: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    unit_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        discount = self.discount
        displayname = self.displayname
        external_remark = self.external_remark
        factor = self.factor
        id = self.id
        is_comment = self.is_comment
        is_kit = self.is_kit
        linked_equipment = self.linked_equipment
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        order = self.order
        parent = self.parent
        project_request = self.project_request
        quantity = self.quantity
        quantity_total = self.quantity_total
        unit_price = self.unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if discount is not UNSET:
            field_dict["discount"] = discount
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if external_remark is not UNSET:
            field_dict["external_remark"] = external_remark
        if factor is not UNSET:
            field_dict["factor"] = factor
        if id is not UNSET:
            field_dict["id"] = id
        if is_comment is not UNSET:
            field_dict["is_comment"] = is_comment
        if is_kit is not UNSET:
            field_dict["is_kit"] = is_kit
        if linked_equipment is not UNSET:
            field_dict["linked_equipment"] = linked_equipment
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if parent is not UNSET:
            field_dict["parent"] = parent
        if project_request is not UNSET:
            field_dict["project_request"] = project_request
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_total is not UNSET:
            field_dict["quantity_total"] = quantity_total
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        discount = d.pop("discount", UNSET)

        displayname = d.pop("displayname", UNSET)

        external_remark = d.pop("external_remark", UNSET)

        factor = d.pop("factor", UNSET)

        id = d.pop("id", UNSET)

        is_comment = d.pop("is_comment", UNSET)

        is_kit = d.pop("is_kit", UNSET)

        linked_equipment = d.pop("linked_equipment", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        parent = d.pop("parent", UNSET)

        project_request = d.pop("project_request", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_total = d.pop("quantity_total", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        project_request_equipment_itemput_response_schema_data = cls(
            created=created,
            creator=creator,
            discount=discount,
            displayname=displayname,
            external_remark=external_remark,
            factor=factor,
            id=id,
            is_comment=is_comment,
            is_kit=is_kit,
            linked_equipment=linked_equipment,
            modified=modified,
            name=name,
            order=order,
            parent=parent,
            project_request=project_request,
            quantity=quantity,
            quantity_total=quantity_total,
            unit_price=unit_price,
        )

        project_request_equipment_itemput_response_schema_data.additional_properties = d
        return project_request_equipment_itemput_response_schema_data

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
