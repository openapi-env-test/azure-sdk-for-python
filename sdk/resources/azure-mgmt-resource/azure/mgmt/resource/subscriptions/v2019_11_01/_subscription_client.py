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

from ._configuration import SubscriptionClientConfiguration
from .operations import Operations
from .operations import SubscriptionsOperations
from .operations import TenantsOperations
from . import models


class SubscriptionClient(SDKClient):
    """All resource groups and resources exist within subscriptions. These operation enable you get information about your subscriptions and tenants. A tenant is a dedicated instance of Azure Active Directory (Azure AD) for your organization.

    :ivar config: Configuration for client.
    :vartype config: SubscriptionClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.resource.subscriptions.v2019_11_01.operations.Operations
    :ivar subscriptions: Subscriptions operations
    :vartype subscriptions: azure.mgmt.resource.subscriptions.v2019_11_01.operations.SubscriptionsOperations
    :ivar tenants: Tenants operations
    :vartype tenants: azure.mgmt.resource.subscriptions.v2019_11_01.operations.TenantsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = SubscriptionClientConfiguration(credentials, base_url)
        super(SubscriptionClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-11-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscriptions = SubscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tenants = TenantsOperations(
            self._client, self.config, self._serialize, self._deserialize)
