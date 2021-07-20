# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ApiManagementClientConfiguration
from .operations import ApiOperations
from .operations import ApiRevisionOperations
from .operations import ApiReleaseOperations
from .operations import ApiOperationOperations
from .operations import ApiOperationPolicyOperations
from .operations import TagOperations
from .operations import ApiProductOperations
from .operations import ApiPolicyOperations
from .operations import ApiSchemaOperations
from .operations import ApiDiagnosticOperations
from .operations import ApiIssueOperations
from .operations import ApiIssueCommentOperations
from .operations import ApiIssueAttachmentOperations
from .operations import ApiTagDescriptionOperations
from .operations import OperationOperations
from .operations import ApiExportOperations
from .operations import ApiVersionSetOperations
from .operations import AuthorizationServerOperations
from .operations import BackendOperations
from .operations import CacheOperations
from .operations import CertificateOperations
from .operations import ContentTypeOperations
from .operations import ContentItemOperations
from .operations import DeletedServicesOperations
from .operations import ApiManagementOperationsOperations
from .operations import ApiManagementServiceSkusOperations
from .operations import ApiManagementServiceOperations
from .operations import DiagnosticOperations
from .operations import EmailTemplateOperations
from .operations import GatewayOperations
from .operations import GatewayHostnameConfigurationOperations
from .operations import GatewayApiOperations
from .operations import GatewayCertificateAuthorityOperations
from .operations import GroupOperations
from .operations import GroupUserOperations
from .operations import IdentityProviderOperations
from .operations import IssueOperations
from .operations import LoggerOperations
from .operations import NamedValueOperations
from .operations import NetworkStatusOperations
from .operations import NotificationOperations
from .operations import NotificationRecipientUserOperations
from .operations import NotificationRecipientEmailOperations
from .operations import OpenIdConnectProviderOperations
from .operations import OutboundNetworkDependenciesEndpointsOperations
from .operations import PolicyOperations
from .operations import PolicyDescriptionOperations
from .operations import PortalRevisionOperations
from .operations import PortalSettingsOperations
from .operations import SignInSettingsOperations
from .operations import SignUpSettingsOperations
from .operations import DelegationSettingsOperations
from .operations import PrivateEndpointConnectionOperations
from .operations import ProductOperations
from .operations import ProductApiOperations
from .operations import ProductGroupOperations
from .operations import ProductSubscriptionsOperations
from .operations import ProductPolicyOperations
from .operations import QuotaByCounterKeysOperations
from .operations import QuotaByPeriodKeysOperations
from .operations import RegionOperations
from .operations import ReportsOperations
from .operations import TenantSettingsOperations
from .operations import ApiManagementSkusOperations
from .operations import SubscriptionOperations
from .operations import TagResourceOperations
from .operations import TenantAccessOperations
from .operations import TenantAccessGitOperations
from .operations import TenantConfigurationOperations
from .operations import UserOperations
from .operations import UserGroupOperations
from .operations import UserSubscriptionOperations
from .operations import UserIdentitiesOperations
from .operations import UserConfirmationPasswordOperations
from .. import models


class ApiManagementClient(object):
    """ApiManagement Client.

    :ivar api: ApiOperations operations
    :vartype api: azure.mgmt.apimanagement.aio.operations.ApiOperations
    :ivar api_revision: ApiRevisionOperations operations
    :vartype api_revision: azure.mgmt.apimanagement.aio.operations.ApiRevisionOperations
    :ivar api_release: ApiReleaseOperations operations
    :vartype api_release: azure.mgmt.apimanagement.aio.operations.ApiReleaseOperations
    :ivar api_operation: ApiOperationOperations operations
    :vartype api_operation: azure.mgmt.apimanagement.aio.operations.ApiOperationOperations
    :ivar api_operation_policy: ApiOperationPolicyOperations operations
    :vartype api_operation_policy: azure.mgmt.apimanagement.aio.operations.ApiOperationPolicyOperations
    :ivar tag: TagOperations operations
    :vartype tag: azure.mgmt.apimanagement.aio.operations.TagOperations
    :ivar api_product: ApiProductOperations operations
    :vartype api_product: azure.mgmt.apimanagement.aio.operations.ApiProductOperations
    :ivar api_policy: ApiPolicyOperations operations
    :vartype api_policy: azure.mgmt.apimanagement.aio.operations.ApiPolicyOperations
    :ivar api_schema: ApiSchemaOperations operations
    :vartype api_schema: azure.mgmt.apimanagement.aio.operations.ApiSchemaOperations
    :ivar api_diagnostic: ApiDiagnosticOperations operations
    :vartype api_diagnostic: azure.mgmt.apimanagement.aio.operations.ApiDiagnosticOperations
    :ivar api_issue: ApiIssueOperations operations
    :vartype api_issue: azure.mgmt.apimanagement.aio.operations.ApiIssueOperations
    :ivar api_issue_comment: ApiIssueCommentOperations operations
    :vartype api_issue_comment: azure.mgmt.apimanagement.aio.operations.ApiIssueCommentOperations
    :ivar api_issue_attachment: ApiIssueAttachmentOperations operations
    :vartype api_issue_attachment: azure.mgmt.apimanagement.aio.operations.ApiIssueAttachmentOperations
    :ivar api_tag_description: ApiTagDescriptionOperations operations
    :vartype api_tag_description: azure.mgmt.apimanagement.aio.operations.ApiTagDescriptionOperations
    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.apimanagement.aio.operations.OperationOperations
    :ivar api_export: ApiExportOperations operations
    :vartype api_export: azure.mgmt.apimanagement.aio.operations.ApiExportOperations
    :ivar api_version_set: ApiVersionSetOperations operations
    :vartype api_version_set: azure.mgmt.apimanagement.aio.operations.ApiVersionSetOperations
    :ivar authorization_server: AuthorizationServerOperations operations
    :vartype authorization_server: azure.mgmt.apimanagement.aio.operations.AuthorizationServerOperations
    :ivar backend: BackendOperations operations
    :vartype backend: azure.mgmt.apimanagement.aio.operations.BackendOperations
    :ivar cache: CacheOperations operations
    :vartype cache: azure.mgmt.apimanagement.aio.operations.CacheOperations
    :ivar certificate: CertificateOperations operations
    :vartype certificate: azure.mgmt.apimanagement.aio.operations.CertificateOperations
    :ivar content_type: ContentTypeOperations operations
    :vartype content_type: azure.mgmt.apimanagement.aio.operations.ContentTypeOperations
    :ivar content_item: ContentItemOperations operations
    :vartype content_item: azure.mgmt.apimanagement.aio.operations.ContentItemOperations
    :ivar deleted_services: DeletedServicesOperations operations
    :vartype deleted_services: azure.mgmt.apimanagement.aio.operations.DeletedServicesOperations
    :ivar api_management_operations: ApiManagementOperationsOperations operations
    :vartype api_management_operations: azure.mgmt.apimanagement.aio.operations.ApiManagementOperationsOperations
    :ivar api_management_service_skus: ApiManagementServiceSkusOperations operations
    :vartype api_management_service_skus: azure.mgmt.apimanagement.aio.operations.ApiManagementServiceSkusOperations
    :ivar api_management_service: ApiManagementServiceOperations operations
    :vartype api_management_service: azure.mgmt.apimanagement.aio.operations.ApiManagementServiceOperations
    :ivar diagnostic: DiagnosticOperations operations
    :vartype diagnostic: azure.mgmt.apimanagement.aio.operations.DiagnosticOperations
    :ivar email_template: EmailTemplateOperations operations
    :vartype email_template: azure.mgmt.apimanagement.aio.operations.EmailTemplateOperations
    :ivar gateway: GatewayOperations operations
    :vartype gateway: azure.mgmt.apimanagement.aio.operations.GatewayOperations
    :ivar gateway_hostname_configuration: GatewayHostnameConfigurationOperations operations
    :vartype gateway_hostname_configuration: azure.mgmt.apimanagement.aio.operations.GatewayHostnameConfigurationOperations
    :ivar gateway_api: GatewayApiOperations operations
    :vartype gateway_api: azure.mgmt.apimanagement.aio.operations.GatewayApiOperations
    :ivar gateway_certificate_authority: GatewayCertificateAuthorityOperations operations
    :vartype gateway_certificate_authority: azure.mgmt.apimanagement.aio.operations.GatewayCertificateAuthorityOperations
    :ivar group: GroupOperations operations
    :vartype group: azure.mgmt.apimanagement.aio.operations.GroupOperations
    :ivar group_user: GroupUserOperations operations
    :vartype group_user: azure.mgmt.apimanagement.aio.operations.GroupUserOperations
    :ivar identity_provider: IdentityProviderOperations operations
    :vartype identity_provider: azure.mgmt.apimanagement.aio.operations.IdentityProviderOperations
    :ivar issue: IssueOperations operations
    :vartype issue: azure.mgmt.apimanagement.aio.operations.IssueOperations
    :ivar logger: LoggerOperations operations
    :vartype logger: azure.mgmt.apimanagement.aio.operations.LoggerOperations
    :ivar named_value: NamedValueOperations operations
    :vartype named_value: azure.mgmt.apimanagement.aio.operations.NamedValueOperations
    :ivar network_status: NetworkStatusOperations operations
    :vartype network_status: azure.mgmt.apimanagement.aio.operations.NetworkStatusOperations
    :ivar notification: NotificationOperations operations
    :vartype notification: azure.mgmt.apimanagement.aio.operations.NotificationOperations
    :ivar notification_recipient_user: NotificationRecipientUserOperations operations
    :vartype notification_recipient_user: azure.mgmt.apimanagement.aio.operations.NotificationRecipientUserOperations
    :ivar notification_recipient_email: NotificationRecipientEmailOperations operations
    :vartype notification_recipient_email: azure.mgmt.apimanagement.aio.operations.NotificationRecipientEmailOperations
    :ivar open_id_connect_provider: OpenIdConnectProviderOperations operations
    :vartype open_id_connect_provider: azure.mgmt.apimanagement.aio.operations.OpenIdConnectProviderOperations
    :ivar outbound_network_dependencies_endpoints: OutboundNetworkDependenciesEndpointsOperations operations
    :vartype outbound_network_dependencies_endpoints: azure.mgmt.apimanagement.aio.operations.OutboundNetworkDependenciesEndpointsOperations
    :ivar policy: PolicyOperations operations
    :vartype policy: azure.mgmt.apimanagement.aio.operations.PolicyOperations
    :ivar policy_description: PolicyDescriptionOperations operations
    :vartype policy_description: azure.mgmt.apimanagement.aio.operations.PolicyDescriptionOperations
    :ivar portal_revision: PortalRevisionOperations operations
    :vartype portal_revision: azure.mgmt.apimanagement.aio.operations.PortalRevisionOperations
    :ivar portal_settings: PortalSettingsOperations operations
    :vartype portal_settings: azure.mgmt.apimanagement.aio.operations.PortalSettingsOperations
    :ivar sign_in_settings: SignInSettingsOperations operations
    :vartype sign_in_settings: azure.mgmt.apimanagement.aio.operations.SignInSettingsOperations
    :ivar sign_up_settings: SignUpSettingsOperations operations
    :vartype sign_up_settings: azure.mgmt.apimanagement.aio.operations.SignUpSettingsOperations
    :ivar delegation_settings: DelegationSettingsOperations operations
    :vartype delegation_settings: azure.mgmt.apimanagement.aio.operations.DelegationSettingsOperations
    :ivar private_endpoint_connection: PrivateEndpointConnectionOperations operations
    :vartype private_endpoint_connection: azure.mgmt.apimanagement.aio.operations.PrivateEndpointConnectionOperations
    :ivar product: ProductOperations operations
    :vartype product: azure.mgmt.apimanagement.aio.operations.ProductOperations
    :ivar product_api: ProductApiOperations operations
    :vartype product_api: azure.mgmt.apimanagement.aio.operations.ProductApiOperations
    :ivar product_group: ProductGroupOperations operations
    :vartype product_group: azure.mgmt.apimanagement.aio.operations.ProductGroupOperations
    :ivar product_subscriptions: ProductSubscriptionsOperations operations
    :vartype product_subscriptions: azure.mgmt.apimanagement.aio.operations.ProductSubscriptionsOperations
    :ivar product_policy: ProductPolicyOperations operations
    :vartype product_policy: azure.mgmt.apimanagement.aio.operations.ProductPolicyOperations
    :ivar quota_by_counter_keys: QuotaByCounterKeysOperations operations
    :vartype quota_by_counter_keys: azure.mgmt.apimanagement.aio.operations.QuotaByCounterKeysOperations
    :ivar quota_by_period_keys: QuotaByPeriodKeysOperations operations
    :vartype quota_by_period_keys: azure.mgmt.apimanagement.aio.operations.QuotaByPeriodKeysOperations
    :ivar region: RegionOperations operations
    :vartype region: azure.mgmt.apimanagement.aio.operations.RegionOperations
    :ivar reports: ReportsOperations operations
    :vartype reports: azure.mgmt.apimanagement.aio.operations.ReportsOperations
    :ivar tenant_settings: TenantSettingsOperations operations
    :vartype tenant_settings: azure.mgmt.apimanagement.aio.operations.TenantSettingsOperations
    :ivar api_management_skus: ApiManagementSkusOperations operations
    :vartype api_management_skus: azure.mgmt.apimanagement.aio.operations.ApiManagementSkusOperations
    :ivar subscription: SubscriptionOperations operations
    :vartype subscription: azure.mgmt.apimanagement.aio.operations.SubscriptionOperations
    :ivar tag_resource: TagResourceOperations operations
    :vartype tag_resource: azure.mgmt.apimanagement.aio.operations.TagResourceOperations
    :ivar tenant_access: TenantAccessOperations operations
    :vartype tenant_access: azure.mgmt.apimanagement.aio.operations.TenantAccessOperations
    :ivar tenant_access_git: TenantAccessGitOperations operations
    :vartype tenant_access_git: azure.mgmt.apimanagement.aio.operations.TenantAccessGitOperations
    :ivar tenant_configuration: TenantConfigurationOperations operations
    :vartype tenant_configuration: azure.mgmt.apimanagement.aio.operations.TenantConfigurationOperations
    :ivar user: UserOperations operations
    :vartype user: azure.mgmt.apimanagement.aio.operations.UserOperations
    :ivar user_group: UserGroupOperations operations
    :vartype user_group: azure.mgmt.apimanagement.aio.operations.UserGroupOperations
    :ivar user_subscription: UserSubscriptionOperations operations
    :vartype user_subscription: azure.mgmt.apimanagement.aio.operations.UserSubscriptionOperations
    :ivar user_identities: UserIdentitiesOperations operations
    :vartype user_identities: azure.mgmt.apimanagement.aio.operations.UserIdentitiesOperations
    :ivar user_confirmation_password: UserConfirmationPasswordOperations operations
    :vartype user_confirmation_password: azure.mgmt.apimanagement.aio.operations.UserConfirmationPasswordOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
        self._config = ApiManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.api = ApiOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_revision = ApiRevisionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_release = ApiReleaseOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_operation = ApiOperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_operation_policy = ApiOperationPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tag = TagOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_product = ApiProductOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_policy = ApiPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_schema = ApiSchemaOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_diagnostic = ApiDiagnosticOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_issue = ApiIssueOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_issue_comment = ApiIssueCommentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_issue_attachment = ApiIssueAttachmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_tag_description = ApiTagDescriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_export = ApiExportOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_version_set = ApiVersionSetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.authorization_server = AuthorizationServerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.backend = BackendOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cache = CacheOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.certificate = CertificateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.content_type = ContentTypeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.content_item = ContentItemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deleted_services = DeletedServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_management_operations = ApiManagementOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_management_service_skus = ApiManagementServiceSkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_management_service = ApiManagementServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.diagnostic = DiagnosticOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.email_template = EmailTemplateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gateway = GatewayOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gateway_hostname_configuration = GatewayHostnameConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gateway_api = GatewayApiOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gateway_certificate_authority = GatewayCertificateAuthorityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group = GroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_user = GroupUserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.identity_provider = IdentityProviderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.issue = IssueOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.logger = LoggerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.named_value = NamedValueOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_status = NetworkStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notification = NotificationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notification_recipient_user = NotificationRecipientUserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notification_recipient_email = NotificationRecipientEmailOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.open_id_connect_provider = OpenIdConnectProviderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.outbound_network_dependencies_endpoints = OutboundNetworkDependenciesEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policy = PolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policy_description = PolicyDescriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.portal_revision = PortalRevisionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.portal_settings = PortalSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sign_in_settings = SignInSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sign_up_settings = SignUpSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.delegation_settings = DelegationSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connection = PrivateEndpointConnectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.product = ProductOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.product_api = ProductApiOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.product_group = ProductGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.product_subscriptions = ProductSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.product_policy = ProductPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.quota_by_counter_keys = QuotaByCounterKeysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.quota_by_period_keys = QuotaByPeriodKeysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.region = RegionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.reports = ReportsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tenant_settings = TenantSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_management_skus = ApiManagementSkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscription = SubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tag_resource = TagResourceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tenant_access = TenantAccessOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tenant_access_git = TenantAccessGitOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tenant_configuration = TenantConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_group = UserGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_subscription = UserSubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_identities = UserIdentitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_confirmation_password = UserConfirmationPasswordOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ApiManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
