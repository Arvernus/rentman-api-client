import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectRequestEquipmentCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class ProjectRequestEquipmentCollectionpostResponseSchemaDataItem:
    """ """

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    is_comment: Union[Unset, bool] = UNSET
    is_kit: Union[Unset, bool] = UNSET
    discount: Union[Unset, float] = UNSET
    linked_equipment: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    external_remark: Union[Unset, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    project_request: Union[Unset, str] = UNSET
    factor: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
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
        quantity = self.quantity
        quantity_total = self.quantity_total
        is_comment = self.is_comment
        is_kit = self.is_kit
        discount = self.discount
        linked_equipment = self.linked_equipment
        name = self.name
        external_remark = self.external_remark
        parent = self.parent
        unit_price = self.unit_price
        project_request = self.project_request
        factor = self.factor
        order = self.order

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
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_total is not UNSET:
            field_dict["quantity_total"] = quantity_total
        if is_comment is not UNSET:
            field_dict["is_comment"] = is_comment
        if is_kit is not UNSET:
            field_dict["is_kit"] = is_kit
        if discount is not UNSET:
            field_dict["discount"] = discount
        if linked_equipment is not UNSET:
            field_dict["linked_equipment"] = linked_equipment
        if name is not UNSET:
            field_dict["name"] = name
        if external_remark is not UNSET:
            field_dict["external_remark"] = external_remark
        if parent is not UNSET:
            field_dict["parent"] = parent
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if project_request is not UNSET:
            field_dict["project_request"] = project_request
        if factor is not UNSET:
            field_dict["factor"] = factor
        if order is not UNSET:
            field_dict["order"] = order

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

        quantity = d.pop("quantity", UNSET)

        quantity_total = d.pop("quantity_total", UNSET)

        is_comment = d.pop("is_comment", UNSET)

        is_kit = d.pop("is_kit", UNSET)

        discount = d.pop("discount", UNSET)

        linked_equipment = d.pop("linked_equipment", UNSET)

        name = d.pop("name", UNSET)

        external_remark = d.pop("external_remark", UNSET)

        parent = d.pop("parent", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        project_request = d.pop("project_request", UNSET)

        factor = d.pop("factor", UNSET)

        order = d.pop("order", UNSET)

        project_request_equipment_collectionpost_response_schema_data_item = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            quantity=quantity,
            quantity_total=quantity_total,
            is_comment=is_comment,
            is_kit=is_kit,
            discount=discount,
            linked_equipment=linked_equipment,
            name=name,
            external_remark=external_remark,
            parent=parent,
            unit_price=unit_price,
            project_request=project_request,
            factor=factor,
            order=order,
        )

        project_request_equipment_collectionpost_response_schema_data_item.additional_properties = d
        return project_request_equipment_collectionpost_response_schema_data_item

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
