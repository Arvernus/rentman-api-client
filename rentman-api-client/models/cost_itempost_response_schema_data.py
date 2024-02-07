import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cost_itempost_response_schema_data_custom import CostItempostResponseSchemaDataCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="CostItempostResponseSchemaData")


@attr.s(auto_attribs=True)
class CostItempostResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    subproject: Union[Unset, str] = UNSET
    is_template: Union[Unset, bool] = UNSET
    taxclass: Union[Unset, None, str] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    verkoopprijs: Union[Unset, float] = UNSET
    inkoopprijs: Union[Unset, float] = UNSET
    price: Union[Unset, float] = UNSET
    custom: Union[Unset, CostItempostResponseSchemaDataCustom] = UNSET
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
        name = self.name
        remark = self.remark
        project = self.project
        subproject = self.subproject
        is_template = self.is_template
        taxclass = self.taxclass
        ledger = self.ledger
        verkoopprijs = self.verkoopprijs
        inkoopprijs = self.inkoopprijs
        price = self.price
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
        if name is not UNSET:
            field_dict["name"] = name
        if remark is not UNSET:
            field_dict["remark"] = remark
        if project is not UNSET:
            field_dict["project"] = project
        if subproject is not UNSET:
            field_dict["subproject"] = subproject
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if taxclass is not UNSET:
            field_dict["taxclass"] = taxclass
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if verkoopprijs is not UNSET:
            field_dict["verkoopprijs"] = verkoopprijs
        if inkoopprijs is not UNSET:
            field_dict["inkoopprijs"] = inkoopprijs
        if price is not UNSET:
            field_dict["price"] = price
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

        name = d.pop("name", UNSET)

        remark = d.pop("remark", UNSET)

        project = d.pop("project", UNSET)

        subproject = d.pop("subproject", UNSET)

        is_template = d.pop("is_template", UNSET)

        taxclass = d.pop("taxclass", UNSET)

        ledger = d.pop("ledger", UNSET)

        verkoopprijs = d.pop("verkoopprijs", UNSET)

        inkoopprijs = d.pop("inkoopprijs", UNSET)

        price = d.pop("price", UNSET)

        custom: Union[Unset, CostItempostResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = CostItempostResponseSchemaDataCustom.from_dict(_custom)

        cost_itempost_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            name=name,
            remark=remark,
            project=project,
            subproject=subproject,
            is_template=is_template,
            taxclass=taxclass,
            ledger=ledger,
            verkoopprijs=verkoopprijs,
            inkoopprijs=inkoopprijs,
            price=price,
            custom=custom,
        )

        cost_itempost_response_schema_data.additional_properties = d
        return cost_itempost_response_schema_data

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
