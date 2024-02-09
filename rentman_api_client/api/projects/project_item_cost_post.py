from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.cost_itempost_request_schema import CostItempostRequestSchema
from ...models.cost_itempost_response_schema import CostItempostResponseSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: int,
    json_body: CostItempostRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Dict[str, Any]:
    url = "{}/projects/{id}/costs".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "offset": offset,
        "limit": limit,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CostItempostResponseSchema]:
    if response.status_code == 200:
        response_200 = CostItempostResponseSchema.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CostItempostResponseSchema]:
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
    json_body: CostItempostRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Response[CostItempostResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
        offset=offset,
        limit=limit,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: int,
    json_body: CostItempostRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Optional[CostItempostResponseSchema]:
    """ """

    return sync_detailed(
        client=client,
        id=id,
        json_body=json_body,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: int,
    json_body: CostItempostRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Response[CostItempostResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
        offset=offset,
        limit=limit,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: int,
    json_body: CostItempostRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Optional[CostItempostResponseSchema]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            json_body=json_body,
            offset=offset,
            limit=limit,
        )
    ).parsed
