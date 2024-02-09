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

    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    custom: Union[Unset, CostItempostResponseSchemaDataCustom] = UNSET
    displayname: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    inkoopprijs: Union[Unset, float] = UNSET
    is_template: Union[Unset, bool] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    project: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    subproject: Union[Unset, str] = UNSET
    taxclass: Union[Unset, None, str] = UNSET
    verkoopprijs: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        displayname = self.displayname
        id = self.id
        inkoopprijs = self.inkoopprijs
        is_template = self.is_template
        ledger = self.ledger
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        price = self.price
        project = self.project
        remark = self.remark
        subproject = self.subproject
        taxclass = self.taxclass
        verkoopprijs = self.verkoopprijs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if custom is not UNSET:
            field_dict["custom"] = custom
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if id is not UNSET:
            field_dict["id"] = id
        if inkoopprijs is not UNSET:
            field_dict["inkoopprijs"] = inkoopprijs
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if project is not UNSET:
            field_dict["project"] = project
        if remark is not UNSET:
            field_dict["remark"] = remark
        if subproject is not UNSET:
            field_dict["subproject"] = subproject
        if taxclass is not UNSET:
            field_dict["taxclass"] = taxclass
        if verkoopprijs is not UNSET:
            field_dict["verkoopprijs"] = verkoopprijs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        custom: Union[Unset, CostItempostResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = CostItempostResponseSchemaDataCustom.from_dict(_custom)

        displayname = d.pop("displayname", UNSET)

        id = d.pop("id", UNSET)

        inkoopprijs = d.pop("inkoopprijs", UNSET)

        is_template = d.pop("is_template", UNSET)

        ledger = d.pop("ledger", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        project = d.pop("project", UNSET)

        remark = d.pop("remark", UNSET)

        subproject = d.pop("subproject", UNSET)

        taxclass = d.pop("taxclass", UNSET)

        verkoopprijs = d.pop("verkoopprijs", UNSET)

        cost_itempost_response_schema_data = cls(
            created=created,
            creator=creator,
            custom=custom,
            displayname=displayname,
            id=id,
            inkoopprijs=inkoopprijs,
            is_template=is_template,
            ledger=ledger,
            modified=modified,
            name=name,
            price=price,
            project=project,
            remark=remark,
            subproject=subproject,
            taxclass=taxclass,
            verkoopprijs=verkoopprijs,
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
