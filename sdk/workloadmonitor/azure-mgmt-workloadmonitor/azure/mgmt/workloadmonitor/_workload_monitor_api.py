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

from ._configuration import WorkloadMonitorAPIConfiguration
from .operations import Operations
from .operations import HealthMonitorsOperations
from . import models


class WorkloadMonitorAPI(SDKClient):
    """Workload Monitor API

    :ivar config: Configuration for client.
    :vartype config: WorkloadMonitorAPIConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.workloadmonitor.operations.Operations
    :ivar health_monitors: HealthMonitors operations
    :vartype health_monitors: azure.mgmt.workloadmonitor.operations.HealthMonitorsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = WorkloadMonitorAPIConfiguration(credentials, base_url)
        super(WorkloadMonitorAPI, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-01-13-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.health_monitors = HealthMonitorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
