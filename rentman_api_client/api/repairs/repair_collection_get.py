from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.repair_collectionget_response_schema import RepairCollectiongetResponseSchema
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repairs".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RepairCollectiongetResponseSchema]:
    if response.status_code == 200:
        response_200 = RepairCollectiongetResponseSchema.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RepairCollectiongetResponseSchema]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[RepairCollectiongetResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[RepairCollectiongetResponseSchema]:
    """ """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[RepairCollectiongetResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[RepairCollectiongetResponseSchema]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed