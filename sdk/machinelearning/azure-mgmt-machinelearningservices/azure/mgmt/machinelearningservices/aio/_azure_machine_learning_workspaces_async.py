# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AzureMachineLearningWorkspacesConfiguration
from .operations_async import Operations
from .operations_async import WorkspacesOperations
from .operations_async import WorkspaceFeaturesOperations
from .operations_async import UsagesOperations
from .operations_async import VirtualMachineSizesOperations
from .operations_async import QuotasOperations
from .operations_async import MachineLearningComputeOperations
from .operations_async import AzureMachineLearningWorkspacesOperationsMixin
from .operations_async import PrivateEndpointConnectionsOperations
from .operations_async import PrivateLinkResourcesOperations
from .. import models


class AzureMachineLearningWorkspaces(AzureMachineLearningWorkspacesOperationsMixin):
    """These APIs allow end users to operate on Azure Machine Learning Workspace resources.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.machinelearningservices.aio.operations_async.Operations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.machinelearningservices.aio.operations_async.WorkspacesOperations
    :ivar workspace_features: WorkspaceFeaturesOperations operations
    :vartype workspace_features: azure.mgmt.machinelearningservices.aio.operations_async.WorkspaceFeaturesOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.machinelearningservices.aio.operations_async.UsagesOperations
    :ivar virtual_machine_sizes: VirtualMachineSizesOperations operations
    :vartype virtual_machine_sizes: azure.mgmt.machinelearningservices.aio.operations_async.VirtualMachineSizesOperations
    :ivar quotas: QuotasOperations operations
    :vartype quotas: azure.mgmt.machinelearningservices.aio.operations_async.QuotasOperations
    :ivar machine_learning_compute: MachineLearningComputeOperations operations
    :vartype machine_learning_compute: azure.mgmt.machinelearningservices.aio.operations_async.MachineLearningComputeOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.machinelearningservices.aio.operations_async.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.machinelearningservices.aio.operations_async.PrivateLinkResourcesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AzureMachineLearningWorkspacesConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_features = WorkspaceFeaturesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.quotas = QuotasOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.machine_learning_compute = MachineLearningComputeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureMachineLearningWorkspaces":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
