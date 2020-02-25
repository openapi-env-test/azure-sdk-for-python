# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AzureMachineLearningWorkspacesConfiguration
from .operations import AzureMachineLearningWorkspacesOperationsMixin
from .operations import Operations
from .operations import WorkspacesOperations
from .operations import WorkspaceFeaturesOperations
from .operations import UsagesOperations
from .operations import VirtualMachineSizesOperations
from .operations import QuotasOperations
from .operations import MachineLearningComputeOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from . import models


class AzureMachineLearningWorkspaces(AzureMachineLearningWorkspacesOperationsMixin, SDKClient):
    """These APIs allow end users to operate on Azure Machine Learning Workspace resources.

    :ivar config: Configuration for client.
    :vartype config: AzureMachineLearningWorkspacesConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.machinelearningservices.operations.Operations
    :ivar workspaces: Workspaces operations
    :vartype workspaces: azure.mgmt.machinelearningservices.operations.WorkspacesOperations
    :ivar workspace_features: WorkspaceFeatures operations
    :vartype workspace_features: azure.mgmt.machinelearningservices.operations.WorkspaceFeaturesOperations
    :ivar usages: Usages operations
    :vartype usages: azure.mgmt.machinelearningservices.operations.UsagesOperations
    :ivar virtual_machine_sizes: VirtualMachineSizes operations
    :vartype virtual_machine_sizes: azure.mgmt.machinelearningservices.operations.VirtualMachineSizesOperations
    :ivar quotas: Quotas operations
    :vartype quotas: azure.mgmt.machinelearningservices.operations.QuotasOperations
    :ivar machine_learning_compute: MachineLearningCompute operations
    :vartype machine_learning_compute: azure.mgmt.machinelearningservices.operations.MachineLearningComputeOperations
    :ivar private_endpoint_connections: PrivateEndpointConnections operations
    :vartype private_endpoint_connections: azure.mgmt.machinelearningservices.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResources operations
    :vartype private_link_resources: azure.mgmt.machinelearningservices.operations.PrivateLinkResourcesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AzureMachineLearningWorkspacesConfiguration(credentials, subscription_id, base_url)
        super(AzureMachineLearningWorkspaces, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-02-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_features = WorkspaceFeaturesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.quotas = QuotasOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.machine_learning_compute = MachineLearningComputeOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
