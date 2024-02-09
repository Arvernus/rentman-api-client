import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.file_itemput_response_schema_data_previewstatus import FileItemputResponseSchemaDataPreviewstatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileItemputResponseSchemaData")


@attr.s(auto_attribs=True)
class FileItemputResponseSchemaData:
    """All the data about the requested items"""

    classified: Union[Unset, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    expiration: Union[Unset, None, str] = UNSET
    file_item: Union[Unset, int] = UNSET
    file_itemtype: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    image: Union[Unset, bool] = UNSET
    in_documents: Union[Unset, bool] = UNSET
    in_webshop: Union[Unset, bool] = UNSET
    item: Union[Unset, None, str] = UNSET
    itemtype: Union[Unset, None, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    path: Union[Unset, str] = UNSET
    preview_of: Union[Unset, None, str] = UNSET
    previewstatus: Union[Unset, FileItemputResponseSchemaDataPreviewstatus] = UNSET
    proxy_url: Union[Unset, str] = UNSET
    public: Union[Unset, bool] = UNSET
    readable_name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        classified = self.classified
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        description = self.description
        displayname = self.displayname
        expiration = self.expiration
        file_item = self.file_item
        file_itemtype = self.file_itemtype
        id = self.id
        image = self.image
        in_documents = self.in_documents
        in_webshop = self.in_webshop
        item = self.item
        itemtype = self.itemtype
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        path = self.path
        preview_of = self.preview_of
        previewstatus: Union[Unset, bool] = UNSET
        if not isinstance(self.previewstatus, Unset):
            previewstatus = self.previewstatus.value

        proxy_url = self.proxy_url
        public = self.public
        readable_name = self.readable_name
        size = self.size
        type = self.type
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classified is not UNSET:
            field_dict["classified"] = classified
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if file_item is not UNSET:
            field_dict["file_item"] = file_item
        if file_itemtype is not UNSET:
            field_dict["file_itemtype"] = file_itemtype
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if in_documents is not UNSET:
            field_dict["in_documents"] = in_documents
        if in_webshop is not UNSET:
            field_dict["in_webshop"] = in_webshop
        if item is not UNSET:
            field_dict["item"] = item
        if itemtype is not UNSET:
            field_dict["itemtype"] = itemtype
        if modified is not UNSET:
            field_dict["modified"] = modified
        if path is not UNSET:
            field_dict["path"] = path
        if preview_of is not UNSET:
            field_dict["preview_of"] = preview_of
        if previewstatus is not UNSET:
            field_dict["previewstatus"] = previewstatus
        if proxy_url is not UNSET:
            field_dict["proxy_url"] = proxy_url
        if public is not UNSET:
            field_dict["public"] = public
        if readable_name is not UNSET:
            field_dict["readable_name"] = readable_name
        if size is not UNSET:
            field_dict["size"] = size
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        classified = d.pop("classified", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        description = d.pop("description", UNSET)

        displayname = d.pop("displayname", UNSET)

        expiration = d.pop("expiration", UNSET)

        file_item = d.pop("file_item", UNSET)

        file_itemtype = d.pop("file_itemtype", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        in_documents = d.pop("in_documents", UNSET)

        in_webshop = d.pop("in_webshop", UNSET)

        item = d.pop("item", UNSET)

        itemtype = d.pop("itemtype", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        path = d.pop("path", UNSET)

        preview_of = d.pop("preview_of", UNSET)

        previewstatus: Union[Unset, FileItemputResponseSchemaDataPreviewstatus] = UNSET
        _previewstatus = d.pop("previewstatus", UNSET)
        if not isinstance(_previewstatus, Unset):
            previewstatus = FileItemputResponseSchemaDataPreviewstatus(_previewstatus)

        proxy_url = d.pop("proxy_url", UNSET)

        public = d.pop("public", UNSET)

        readable_name = d.pop("readable_name", UNSET)

        size = d.pop("size", UNSET)

        type = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        file_itemput_response_schema_data = cls(
            classified=classified,
            created=created,
            creator=creator,
            description=description,
            displayname=displayname,
            expiration=expiration,
            file_item=file_item,
            file_itemtype=file_itemtype,
            id=id,
            image=image,
            in_documents=in_documents,
            in_webshop=in_webshop,
            item=item,
            itemtype=itemtype,
            modified=modified,
            path=path,
            preview_of=preview_of,
            previewstatus=previewstatus,
            proxy_url=proxy_url,
            public=public,
            readable_name=readable_name,
            size=size,
            type=type,
            url=url,
        )

        file_itemput_response_schema_data.additional_properties = d
        return file_itemput_response_schema_data

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
