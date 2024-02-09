from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.vehicle_collectionget_response_schema import VehicleCollectiongetResponseSchema
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/vehicles".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[VehicleCollectiongetResponseSchema]:
    if response.status_code == 200:
        response_200 = VehicleCollectiongetResponseSchema.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[VehicleCollectiongetResponseSchema]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[VehicleCollectiongetResponseSchema]:
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
) -> Optional[VehicleCollectiongetResponseSchema]:
    """ """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[VehicleCollectiongetResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[VehicleCollectiongetResponseSchema]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
