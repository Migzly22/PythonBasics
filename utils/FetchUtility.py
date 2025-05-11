import httpx
from box import Box
import asyncio
from typing import Optional, Dict, Any

"""Standardized objectified response format """
class FetchUtility:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def _create_response(
        self,
        *,
        success: bool,
        code: int,
        result: Optional[Any] = None,
        error: Optional[Any] = None
    ) -> Dict[str, Any]:
        """Standardized response format"""
        return Box({
            "success": success,
            "code": code,
            "result": result,
            "error": str(error) if error else None
        })

    async def _request(
        self,
        method: str,
        *,
        url: str,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        payload: Optional[Dict] = None,
    ) -> Box:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                    json=payload,
                    timeout=self.timeout
                )
                response.raise_for_status()

                try:
                    data = response.json()
                except ValueError:
                    data = response.text

                return self._create_response(
                    success=True,
                    code=response.status_code,
                    result=data
                )

            except httpx.HTTPStatusError as e:
                error_response  = self._create_response(
                    success=False,
                    code=e.response.status_code,
                    error=f"HTTP error: {e}"
                )
                
                raise Exception(error_response) from e
            
            except httpx.RequestError as e:
                error_response  = self._create_response(
                    success=False,
                    code=500,
                    error=f"Request failed: {e}"
                )
                raise Exception(error_response) from e
            
            except Exception as e:
                error_response  = self._create_response(
                    success=False,
                    code=500,
                    error=f"Unexpected error: {e}"
                )
                raise Exception(error_response) from e

    # Public methods
    async def get(self, url: str, *, params=None, headers=None) -> Box:
        return await self._request("GET", url=url, params=params, headers=headers)

    async def post(self, url: str, *, params=None, headers=None, payload=None) -> Box:
        return await self._request("POST", url=url, params=params, headers=headers, payload=payload)

    async def put(self, url: str, *, params=None, headers=None, payload=None) ->Box:
        return await self._request("PUT", url=url, params=params, headers=headers, payload=payload)

    async def delete(self, url: str, *, params=None, headers=None) -> Box:
        return await self._request("DELETE", url=url, params=params, headers=headers)

# Class Instantiation
pyFetch = FetchUtility(timeout=5)