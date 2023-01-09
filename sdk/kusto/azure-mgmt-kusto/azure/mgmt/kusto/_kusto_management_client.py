# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from ._configuration import KustoManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    AttachedDatabaseConfigurationsOperations,
    ClusterPrincipalAssignmentsOperations,
    ClustersOperations,
    DataConnectionsOperations,
    DatabasePrincipalAssignmentsOperations,
    DatabasesOperations,
    ManagedPrivateEndpointsOperations,
    Operations,
    OperationsResultsLocationOperations,
    OperationsResultsOperations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    ScriptsOperations,
    SkusOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class KustoManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The Azure Kusto management API provides a RESTful set of web services that interact with Azure
    Kusto services to manage your clusters and databases. The API enables you to create, update,
    and delete clusters and databases.

    :ivar clusters: ClustersOperations operations
    :vartype clusters: azure.mgmt.kusto.operations.ClustersOperations
    :ivar cluster_principal_assignments: ClusterPrincipalAssignmentsOperations operations
    :vartype cluster_principal_assignments:
     azure.mgmt.kusto.operations.ClusterPrincipalAssignmentsOperations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.kusto.operations.SkusOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: azure.mgmt.kusto.operations.DatabasesOperations
    :ivar attached_database_configurations: AttachedDatabaseConfigurationsOperations operations
    :vartype attached_database_configurations:
     azure.mgmt.kusto.operations.AttachedDatabaseConfigurationsOperations
    :ivar managed_private_endpoints: ManagedPrivateEndpointsOperations operations
    :vartype managed_private_endpoints:
     azure.mgmt.kusto.operations.ManagedPrivateEndpointsOperations
    :ivar database_principal_assignments: DatabasePrincipalAssignmentsOperations operations
    :vartype database_principal_assignments:
     azure.mgmt.kusto.operations.DatabasePrincipalAssignmentsOperations
    :ivar scripts: ScriptsOperations operations
    :vartype scripts: azure.mgmt.kusto.operations.ScriptsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.kusto.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.kusto.operations.PrivateLinkResourcesOperations
    :ivar data_connections: DataConnectionsOperations operations
    :vartype data_connections: azure.mgmt.kusto.operations.DataConnectionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.kusto.operations.Operations
    :ivar operations_results: OperationsResultsOperations operations
    :vartype operations_results: azure.mgmt.kusto.operations.OperationsResultsOperations
    :ivar operations_results_location: OperationsResultsLocationOperations operations
    :vartype operations_results_location:
     azure.mgmt.kusto.operations.OperationsResultsLocationOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-11-11". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = KustoManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.clusters = ClustersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.cluster_principal_assignments = ClusterPrincipalAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.skus = SkusOperations(self._client, self._config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.attached_database_configurations = AttachedDatabaseConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.managed_private_endpoints = ManagedPrivateEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.database_principal_assignments = DatabasePrincipalAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.scripts = ScriptsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_connections = DataConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.operations_results = OperationsResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations_results_location = OperationsResultsLocationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "KustoManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details) -> None:
        self._client.__exit__(*exc_details)
