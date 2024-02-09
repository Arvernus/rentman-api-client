from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.project_request_itemget_response_schema import ProjectRequestItemgetResponseSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: int,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Dict[str, Any]:
    url = "{}/projectrequests/{id}".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "offset": offset,
        "limit": limit,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ProjectRequestItemgetResponseSchema]:
    if response.status_code == 200:
        response_200 = ProjectRequestItemgetResponseSchema.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ProjectRequestItemgetResponseSchema]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: int,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Response[ProjectRequestItemgetResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        offset=offset,
        limit=limit,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: int,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Optional[ProjectRequestItemgetResponseSchema]:
    """ """

    return sync_detailed(
        client=client,
        id=id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: int,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Response[ProjectRequestItemgetResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        offset=offset,
        limit=limit,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: int,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Optional[ProjectRequestItemgetResponseSchema]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            offset=offset,
            limit=limit,
        )
    ).parsed
