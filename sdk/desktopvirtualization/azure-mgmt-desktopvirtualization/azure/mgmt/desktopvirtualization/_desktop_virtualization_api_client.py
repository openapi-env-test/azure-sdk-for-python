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

from . import models
from ._configuration import DesktopVirtualizationAPIClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    ApplicationGroupsOperations,
    ApplicationsOperations,
    DesktopsOperations,
    HostPoolsOperations,
    MSIXPackagesOperations,
    MsixImagesOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    ScalingPlanPooledSchedulesOperations,
    ScalingPlansOperations,
    SessionHostsOperations,
    StartMenuItemsOperations,
    UserSessionsOperations,
    WorkspacesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class DesktopVirtualizationAPIClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """DesktopVirtualizationAPIClient.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.desktopvirtualization.operations.Operations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.desktopvirtualization.operations.WorkspacesOperations
    :ivar scaling_plans: ScalingPlansOperations operations
    :vartype scaling_plans: azure.mgmt.desktopvirtualization.operations.ScalingPlansOperations
    :ivar scaling_plan_pooled_schedules: ScalingPlanPooledSchedulesOperations operations
    :vartype scaling_plan_pooled_schedules:
     azure.mgmt.desktopvirtualization.operations.ScalingPlanPooledSchedulesOperations
    :ivar application_groups: ApplicationGroupsOperations operations
    :vartype application_groups:
     azure.mgmt.desktopvirtualization.operations.ApplicationGroupsOperations
    :ivar start_menu_items: StartMenuItemsOperations operations
    :vartype start_menu_items: azure.mgmt.desktopvirtualization.operations.StartMenuItemsOperations
    :ivar applications: ApplicationsOperations operations
    :vartype applications: azure.mgmt.desktopvirtualization.operations.ApplicationsOperations
    :ivar desktops: DesktopsOperations operations
    :vartype desktops: azure.mgmt.desktopvirtualization.operations.DesktopsOperations
    :ivar host_pools: HostPoolsOperations operations
    :vartype host_pools: azure.mgmt.desktopvirtualization.operations.HostPoolsOperations
    :ivar user_sessions: UserSessionsOperations operations
    :vartype user_sessions: azure.mgmt.desktopvirtualization.operations.UserSessionsOperations
    :ivar session_hosts: SessionHostsOperations operations
    :vartype session_hosts: azure.mgmt.desktopvirtualization.operations.SessionHostsOperations
    :ivar msix_packages: MSIXPackagesOperations operations
    :vartype msix_packages: azure.mgmt.desktopvirtualization.operations.MSIXPackagesOperations
    :ivar msix_images: MsixImagesOperations operations
    :vartype msix_images: azure.mgmt.desktopvirtualization.operations.MsixImagesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.desktopvirtualization.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.desktopvirtualization.operations.PrivateLinkResourcesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-07-05-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = DesktopVirtualizationAPIClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.scaling_plans = ScalingPlansOperations(self._client, self._config, self._serialize, self._deserialize)
        self.scaling_plan_pooled_schedules = ScalingPlanPooledSchedulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.application_groups = ApplicationGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.start_menu_items = StartMenuItemsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.applications = ApplicationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.desktops = DesktopsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.host_pools = HostPoolsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.user_sessions = UserSessionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.session_hosts = SessionHostsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.msix_packages = MSIXPackagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.msix_images = MsixImagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
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

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DesktopVirtualizationAPIClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
