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

from ._configuration import ApplicationInsightsManagementClientConfiguration
from .operations import ApplicationInsightsManagementClientOperationsMixin
from .operations import Operations
from . import models


class ApplicationInsightsManagementClient(ApplicationInsightsManagementClientOperationsMixin, SDKClient):
    """Composite Swagger for Application Insights Management Client

    :ivar config: Configuration for client.
    :vartype config: ApplicationInsightsManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.applicationinsights.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ApplicationInsightsManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ApplicationInsightsManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-02-10-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
