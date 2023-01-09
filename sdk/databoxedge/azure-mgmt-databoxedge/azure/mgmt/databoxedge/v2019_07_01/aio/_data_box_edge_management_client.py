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
from ..._serialization import Deserializer, Serializer
from ._configuration import DataBoxEdgeManagementClientConfiguration
from .operations import (
    AlertsOperations,
    BandwidthSchedulesOperations,
    DevicesOperations,
    JobsOperations,
    NodesOperations,
    Operations,
    OperationsStatusOperations,
    OrdersOperations,
    RolesOperations,
    SharesOperations,
    StorageAccountCredentialsOperations,
    TriggersOperations,
    UsersOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class DataBoxEdgeManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The DataBoxEdge Client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.databoxedge.v2019_07_01.aio.operations.Operations
    :ivar devices: DevicesOperations operations
    :vartype devices: azure.mgmt.databoxedge.v2019_07_01.aio.operations.DevicesOperations
    :ivar alerts: AlertsOperations operations
    :vartype alerts: azure.mgmt.databoxedge.v2019_07_01.aio.operations.AlertsOperations
    :ivar bandwidth_schedules: BandwidthSchedulesOperations operations
    :vartype bandwidth_schedules:
     azure.mgmt.databoxedge.v2019_07_01.aio.operations.BandwidthSchedulesOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: azure.mgmt.databoxedge.v2019_07_01.aio.operations.JobsOperations
    :ivar nodes: NodesOperations operations
    :vartype nodes: azure.mgmt.databoxedge.v2019_07_01.aio.operations.NodesOperations
    :ivar operations_status: OperationsStatusOperations operations
    :vartype operations_status:
     azure.mgmt.databoxedge.v2019_07_01.aio.operations.OperationsStatusOperations
    :ivar orders: OrdersOperations operations
    :vartype orders: azure.mgmt.databoxedge.v2019_07_01.aio.operations.OrdersOperations
    :ivar roles: RolesOperations operations
    :vartype roles: azure.mgmt.databoxedge.v2019_07_01.aio.operations.RolesOperations
    :ivar shares: SharesOperations operations
    :vartype shares: azure.mgmt.databoxedge.v2019_07_01.aio.operations.SharesOperations
    :ivar storage_account_credentials: StorageAccountCredentialsOperations operations
    :vartype storage_account_credentials:
     azure.mgmt.databoxedge.v2019_07_01.aio.operations.StorageAccountCredentialsOperations
    :ivar triggers: TriggersOperations operations
    :vartype triggers: azure.mgmt.databoxedge.v2019_07_01.aio.operations.TriggersOperations
    :ivar users: UsersOperations operations
    :vartype users: azure.mgmt.databoxedge.v2019_07_01.aio.operations.UsersOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription ID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2019-07-01". Note that overriding this
     default value may result in unsupported behavior.
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
        self._config = DataBoxEdgeManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.devices = DevicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.alerts = AlertsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.bandwidth_schedules = BandwidthSchedulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.jobs = JobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.nodes = NodesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations_status = OperationsStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.orders = OrdersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.roles = RolesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.shares = SharesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.storage_account_credentials = StorageAccountCredentialsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.triggers = TriggersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.users = UsersOperations(self._client, self._config, self._serialize, self._deserialize)

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

    async def __aenter__(self) -> "DataBoxEdgeManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
