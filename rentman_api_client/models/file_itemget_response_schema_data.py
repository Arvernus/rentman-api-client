import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.file_itemget_response_schema_data_previewstatus import FileItemgetResponseSchemaDataPreviewstatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class FileItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    readable_name: Union[Unset, str] = UNSET
    expiration: Union[Unset, None, str] = UNSET
    size: Union[Unset, int] = UNSET
    image: Union[Unset, bool] = UNSET
    item: Union[Unset, None, str] = UNSET
    itemtype: Union[Unset, None, int] = UNSET
    description: Union[Unset, str] = UNSET
    in_documents: Union[Unset, bool] = UNSET
    in_webshop: Union[Unset, bool] = UNSET
    classified: Union[Unset, bool] = UNSET
    public: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    preview_of: Union[Unset, None, str] = UNSET
    previewstatus: Union[Unset, FileItemgetResponseSchemaDataPreviewstatus] = UNSET
    file_item: Union[Unset, int] = UNSET
    file_itemtype: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    proxy_url: Union[Unset, str] = UNSET
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
        readable_name = self.readable_name
        expiration = self.expiration
        size = self.size
        image = self.image
        item = self.item
        itemtype = self.itemtype
        description = self.description
        in_documents = self.in_documents
        in_webshop = self.in_webshop
        classified = self.classified
        public = self.public
        type = self.type
        preview_of = self.preview_of
        previewstatus: Union[Unset, bool] = UNSET
        if not isinstance(self.previewstatus, Unset):
            previewstatus = self.previewstatus.value

        file_item = self.file_item
        file_itemtype = self.file_itemtype
        path = self.path
        url = self.url
        proxy_url = self.proxy_url

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
        if readable_name is not UNSET:
            field_dict["readable_name"] = readable_name
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if size is not UNSET:
            field_dict["size"] = size
        if image is not UNSET:
            field_dict["image"] = image
        if item is not UNSET:
            field_dict["item"] = item
        if itemtype is not UNSET:
            field_dict["itemtype"] = itemtype
        if description is not UNSET:
            field_dict["description"] = description
        if in_documents is not UNSET:
            field_dict["in_documents"] = in_documents
        if in_webshop is not UNSET:
            field_dict["in_webshop"] = in_webshop
        if classified is not UNSET:
            field_dict["classified"] = classified
        if public is not UNSET:
            field_dict["public"] = public
        if type is not UNSET:
            field_dict["type"] = type
        if preview_of is not UNSET:
            field_dict["preview_of"] = preview_of
        if previewstatus is not UNSET:
            field_dict["previewstatus"] = previewstatus
        if file_item is not UNSET:
            field_dict["file_item"] = file_item
        if file_itemtype is not UNSET:
            field_dict["file_itemtype"] = file_itemtype
        if path is not UNSET:
            field_dict["path"] = path
        if url is not UNSET:
            field_dict["url"] = url
        if proxy_url is not UNSET:
            field_dict["proxy_url"] = proxy_url

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

        readable_name = d.pop("readable_name", UNSET)

        expiration = d.pop("expiration", UNSET)

        size = d.pop("size", UNSET)

        image = d.pop("image", UNSET)

        item = d.pop("item", UNSET)

        itemtype = d.pop("itemtype", UNSET)

        description = d.pop("description", UNSET)

        in_documents = d.pop("in_documents", UNSET)

        in_webshop = d.pop("in_webshop", UNSET)

        classified = d.pop("classified", UNSET)

        public = d.pop("public", UNSET)

        type = d.pop("type", UNSET)

        preview_of = d.pop("preview_of", UNSET)

        previewstatus: Union[Unset, FileItemgetResponseSchemaDataPreviewstatus] = UNSET
        _previewstatus = d.pop("previewstatus", UNSET)
        if not isinstance(_previewstatus, Unset):
            previewstatus = FileItemgetResponseSchemaDataPreviewstatus(_previewstatus)

        file_item = d.pop("file_item", UNSET)

        file_itemtype = d.pop("file_itemtype", UNSET)

        path = d.pop("path", UNSET)

        url = d.pop("url", UNSET)

        proxy_url = d.pop("proxy_url", UNSET)

        file_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            readable_name=readable_name,
            expiration=expiration,
            size=size,
            image=image,
            item=item,
            itemtype=itemtype,
            description=description,
            in_documents=in_documents,
            in_webshop=in_webshop,
            classified=classified,
            public=public,
            type=type,
            preview_of=preview_of,
            previewstatus=previewstatus,
            file_item=file_item,
            file_itemtype=file_itemtype,
            path=path,
            url=url,
            proxy_url=proxy_url,
        )

        file_itemget_response_schema_data.additional_properties = d
        return file_itemget_response_schema_data

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
