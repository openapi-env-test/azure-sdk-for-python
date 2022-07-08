# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from ._configuration import DemoNewServiceClientConfiguration
from .operations import DeviceManagementOperations, DeviceUpdateOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

    from azure.core.credentials_async import AsyncTokenCredential

class DemoNewServiceClient:  # pylint: disable=client-accepts-api-version-keyword
    """Device Update for IoT Hub is an Azure service that enables customers to publish update for
    their IoT devices to the cloud, and then deploy that update to their devices (approve updates
    to groups of devices managed and provisioned in IoT Hub). It leverages the proven security and
    reliability of the Windows Update platform, optimized for IoT devices. It works globally and
    knows when and how to update devices, enabling customers to focus on their business goals and
    let Device Update for IoT Hub handle the updates.

    :ivar device_update: DeviceUpdateOperations operations
    :vartype device_update: azure.newservice.demo.aio.operations.DeviceUpdateOperations
    :ivar device_management: DeviceManagementOperations operations
    :vartype device_management: azure.newservice.demo.aio.operations.DeviceManagementOperations
    :param endpoint: Account endpoint. Required.
    :type endpoint: str
    :param instance_id: Account instance identifier. Required.
    :type instance_id: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword api_version: Api Version. Default value is "2022-07-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        endpoint: str,
        instance_id: str,
        credential: "AsyncTokenCredential",
        **kwargs: Any
    ) -> None:
        _endpoint = 'https://{endpoint}'
        self._config = DemoNewServiceClientConfiguration(endpoint=endpoint, instance_id=instance_id, credential=credential, **kwargs)
        self._client = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.device_update = DeviceUpdateOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.device_management = DeviceManagementOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DemoNewServiceClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
