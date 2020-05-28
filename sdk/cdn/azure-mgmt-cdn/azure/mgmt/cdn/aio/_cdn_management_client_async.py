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

from ._configuration_async import CdnManagementClientConfiguration
from .operations_async import ProfilesOperations
from .operations_async import EndpointsOperations
from .operations_async import OriginsOperations
from .operations_async import CustomDomainsOperations
from .operations_async import CdnManagementClientOperationsMixin
from .operations_async import ResourceUsageOperations
from .operations_async import Operations
from .operations_async import EdgeNodesOperations
from .operations_async import PoliciesOperations
from .operations_async import ManagedRuleSetsOperations
from .. import models


class CdnManagementClient(CdnManagementClientOperationsMixin):
    """Cdn Management Client.

    :ivar profiles: ProfilesOperations operations
    :vartype profiles: azure.mgmt.cdn.aio.operations_async.ProfilesOperations
    :ivar endpoints: EndpointsOperations operations
    :vartype endpoints: azure.mgmt.cdn.aio.operations_async.EndpointsOperations
    :ivar origins: OriginsOperations operations
    :vartype origins: azure.mgmt.cdn.aio.operations_async.OriginsOperations
    :ivar custom_domains: CustomDomainsOperations operations
    :vartype custom_domains: azure.mgmt.cdn.aio.operations_async.CustomDomainsOperations
    :ivar resource_usage: ResourceUsageOperations operations
    :vartype resource_usage: azure.mgmt.cdn.aio.operations_async.ResourceUsageOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.cdn.aio.operations_async.Operations
    :ivar edge_nodes: EdgeNodesOperations operations
    :vartype edge_nodes: azure.mgmt.cdn.aio.operations_async.EdgeNodesOperations
    :ivar policies: PoliciesOperations operations
    :vartype policies: azure.mgmt.cdn.aio.operations_async.PoliciesOperations
    :ivar managed_rule_sets: ManagedRuleSetsOperations operations
    :vartype managed_rule_sets: azure.mgmt.cdn.aio.operations_async.ManagedRuleSetsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Azure Subscription ID.
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
        self._config = CdnManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.profiles = ProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.endpoints = EndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.origins = OriginsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.custom_domains = CustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_usage = ResourceUsageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.edge_nodes = EdgeNodesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.managed_rule_sets = ManagedRuleSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "CdnManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
