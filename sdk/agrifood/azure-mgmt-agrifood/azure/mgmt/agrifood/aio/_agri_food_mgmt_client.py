# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import AgriFoodMgmtClientConfiguration
from .operations import (
    CheckNameAvailabilityOperations,
    DataConnectorsOperations,
    DataManagerForAgricultureExtensionsOperations,
    DataManagerForAgricultureResourcesOperations,
    ExtensionsOperations,
    OperationResultsOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    SolutionsDiscoverabilityOperations,
    SolutionsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class AgriFoodMgmtClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """APIs documentation for Microsoft Azure Data Manager for Agriculture Service.

    :ivar check_name_availability: CheckNameAvailabilityOperations operations
    :vartype check_name_availability:
     azure.mgmt.agrifood.aio.operations.CheckNameAvailabilityOperations
    :ivar data_connectors: DataConnectorsOperations operations
    :vartype data_connectors: azure.mgmt.agrifood.aio.operations.DataConnectorsOperations
    :ivar data_manager_for_agriculture_extensions: DataManagerForAgricultureExtensionsOperations
     operations
    :vartype data_manager_for_agriculture_extensions:
     azure.mgmt.agrifood.aio.operations.DataManagerForAgricultureExtensionsOperations
    :ivar data_manager_for_agriculture_resources: DataManagerForAgricultureResourcesOperations
     operations
    :vartype data_manager_for_agriculture_resources:
     azure.mgmt.agrifood.aio.operations.DataManagerForAgricultureResourcesOperations
    :ivar operation_results: OperationResultsOperations operations
    :vartype operation_results: azure.mgmt.agrifood.aio.operations.OperationResultsOperations
    :ivar extensions: ExtensionsOperations operations
    :vartype extensions: azure.mgmt.agrifood.aio.operations.ExtensionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.agrifood.aio.operations.Operations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.agrifood.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.agrifood.aio.operations.PrivateLinkResourcesOperations
    :ivar solutions: SolutionsOperations operations
    :vartype solutions: azure.mgmt.agrifood.aio.operations.SolutionsOperations
    :ivar solutions_discoverability: SolutionsDiscoverabilityOperations operations
    :vartype solutions_discoverability:
     azure.mgmt.agrifood.aio.operations.SolutionsDiscoverabilityOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. The value must be an UUID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-06-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AgriFoodMgmtClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_connectors = DataConnectorsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_manager_for_agriculture_extensions = DataManagerForAgricultureExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_manager_for_agriculture_resources = DataManagerForAgricultureResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operation_results = OperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.extensions = ExtensionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.solutions = SolutionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.solutions_discoverability = SolutionsDiscoverabilityOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AgriFoodMgmtClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
