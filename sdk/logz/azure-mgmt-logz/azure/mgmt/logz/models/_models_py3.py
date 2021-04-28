# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._microsoft_logz_enums import *


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: str
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~microsoft_logz.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~microsoft_logz.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :param error: The error object.
    :type error: ~microsoft_logz.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDetail"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class FilteringTag(msrest.serialization.Model):
    """The definition of a filtering tag. Filtering tags are used for capturing resources and include/exclude them from being monitored.

    :param name: The name (also known as the key) of the tag.
    :type name: str
    :param value: The value of the tag.
    :type value: str
    :param action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.
     Possible values include: "Include", "Exclude".
    :type action: str or ~microsoft_logz.models.TagAction
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'action': {'key': 'action', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        value: Optional[str] = None,
        action: Optional[Union[str, "TagAction"]] = None,
        **kwargs
    ):
        super(FilteringTag, self).__init__(**kwargs)
        self.name = name
        self.value = value
        self.action = action


class IdentityProperties(msrest.serialization.Model):
    """IdentityProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The identity ID.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type:  Possible values include: "SystemAssigned", "UserAssigned".
    :type type: str or ~microsoft_logz.models.ManagedIdentityTypes
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[Union[str, "ManagedIdentityTypes"]] = None,
        **kwargs
    ):
        super(IdentityProperties, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class LogRules(msrest.serialization.Model):
    """Set of rules for sending logs for the Monitor resource.

    :param send_aad_logs: Flag specifying if AAD logs should be sent for the Monitor resource.
    :type send_aad_logs: bool
    :param send_subscription_logs: Flag specifying if subscription logs should be sent for the
     Monitor resource.
    :type send_subscription_logs: bool
    :param send_activity_logs: Flag specifying if activity logs from Azure resources should be sent
     for the Monitor resource.
    :type send_activity_logs: bool
    :param filtering_tags: List of filtering tags to be used for capturing logs. This only takes
     effect if SendActivityLogs flag is enabled. If empty, all resources will be captured. If only
     Exclude action is specified, the rules will apply to the list of all available resources. If
     Include actions are specified, the rules will only include resources with the associated tags.
    :type filtering_tags: list[~microsoft_logz.models.FilteringTag]
    """

    _attribute_map = {
        'send_aad_logs': {'key': 'sendAadLogs', 'type': 'bool'},
        'send_subscription_logs': {'key': 'sendSubscriptionLogs', 'type': 'bool'},
        'send_activity_logs': {'key': 'sendActivityLogs', 'type': 'bool'},
        'filtering_tags': {'key': 'filteringTags', 'type': '[FilteringTag]'},
    }

    def __init__(
        self,
        *,
        send_aad_logs: Optional[bool] = None,
        send_subscription_logs: Optional[bool] = None,
        send_activity_logs: Optional[bool] = None,
        filtering_tags: Optional[List["FilteringTag"]] = None,
        **kwargs
    ):
        super(LogRules, self).__init__(**kwargs)
        self.send_aad_logs = send_aad_logs
        self.send_subscription_logs = send_subscription_logs
        self.send_activity_logs = send_activity_logs
        self.filtering_tags = filtering_tags


class LogzMonitorResource(msrest.serialization.Model):
    """LogzMonitorResource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: ARM id of the monitor resource.
    :vartype id: str
    :ivar system_data: The system metadata relating to this resource.
    :vartype system_data: ~microsoft_logz.models.SystemData
    :ivar name: Name of the monitor resource.
    :vartype name: str
    :ivar type: The type of the monitor resource.
    :vartype type: str
    :param properties: Properties specific to the monitor resource.
    :type properties: ~microsoft_logz.models.MonitorProperties
    :param identity:
    :type identity: ~microsoft_logz.models.IdentityProperties
    :param tags: A set of tags. Dictionary of :code:`<string>`.
    :type tags: dict[str, str]
    :param location: Required.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'system_data': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'MonitorProperties'},
        'identity': {'key': 'identity', 'type': 'IdentityProperties'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        properties: Optional["MonitorProperties"] = None,
        identity: Optional["IdentityProperties"] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(LogzMonitorResource, self).__init__(**kwargs)
        self.id = None
        self.system_data = None
        self.name = None
        self.type = None
        self.properties = properties
        self.identity = identity
        self.tags = tags
        self.location = location


class LogzMonitorResourceListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_logz.models.LogzMonitorResource]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[LogzMonitorResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["LogzMonitorResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(LogzMonitorResourceListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class LogzMonitorResourceUpdateParameters(msrest.serialization.Model):
    """The parameters for a PATCH request to a monitor resource.

    :param properties: The set of properties that can be update in a PATCH request to a monitor
     resource.
    :type properties: ~microsoft_logz.models.MonitorUpdateProperties
    :param tags: A set of tags. The new tags of the monitor resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'MonitorUpdateProperties'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        properties: Optional["MonitorUpdateProperties"] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(LogzMonitorResourceUpdateParameters, self).__init__(**kwargs)
        self.properties = properties
        self.tags = tags


class LogzOrganizationProperties(msrest.serialization.Model):
    """LogzOrganizationProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param company_name: Name of the Logz organization.
    :type company_name: str
    :ivar id: Id of the Logz organization.
    :vartype id: str
    :param enterprise_app_id: The Id of the Enterprise App used for Single sign on.
    :type enterprise_app_id: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'company_name': {'key': 'companyName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'enterprise_app_id': {'key': 'enterpriseAppId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        company_name: Optional[str] = None,
        enterprise_app_id: Optional[str] = None,
        **kwargs
    ):
        super(LogzOrganizationProperties, self).__init__(**kwargs)
        self.company_name = company_name
        self.id = None
        self.enterprise_app_id = enterprise_app_id


class LogzSingleSignOnProperties(msrest.serialization.Model):
    """LogzSingleSignOnProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param single_sign_on_state: Various states of the SSO resource. Possible values include:
     "Initial", "Enable", "Disable", "Existing".
    :type single_sign_on_state: str or ~microsoft_logz.models.SingleSignOnStates
    :param enterprise_app_id: The Id of the Enterprise App used for Single sign-on.
    :type enterprise_app_id: str
    :param single_sign_on_url: The login URL specific to this Logz Organization.
    :type single_sign_on_url: str
    :ivar provisioning_state:  Possible values include: "Accepted", "Creating", "Updating",
     "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", "NotSpecified".
    :vartype provisioning_state: str or ~microsoft_logz.models.ProvisioningState
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'single_sign_on_state': {'key': 'singleSignOnState', 'type': 'str'},
        'enterprise_app_id': {'key': 'enterpriseAppId', 'type': 'str'},
        'single_sign_on_url': {'key': 'singleSignOnUrl', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        single_sign_on_state: Optional[Union[str, "SingleSignOnStates"]] = None,
        enterprise_app_id: Optional[str] = None,
        single_sign_on_url: Optional[str] = None,
        **kwargs
    ):
        super(LogzSingleSignOnProperties, self).__init__(**kwargs)
        self.single_sign_on_state = single_sign_on_state
        self.enterprise_app_id = enterprise_app_id
        self.single_sign_on_url = single_sign_on_url
        self.provisioning_state = None


class LogzSingleSignOnResource(msrest.serialization.Model):
    """LogzSingleSignOnResource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM id of the resource.
    :vartype id: str
    :ivar name: Name of the configuration.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~microsoft_logz.models.SystemData
    :param properties:
    :type properties: ~microsoft_logz.models.LogzSingleSignOnProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'properties': {'key': 'properties', 'type': 'LogzSingleSignOnProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["LogzSingleSignOnProperties"] = None,
        **kwargs
    ):
        super(LogzSingleSignOnResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None
        self.properties = properties


class LogzSingleSignOnResourceListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_logz.models.LogzSingleSignOnResource]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[LogzSingleSignOnResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["LogzSingleSignOnResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(LogzSingleSignOnResourceListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class MonitoredResource(msrest.serialization.Model):
    """The properties of a resource currently being monitored by the Logz monitor resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param id: The ARM id of the resource.
    :type id: str
    :param sending_metrics: Flag indicating if resource is sending metrics to Logz.
    :type sending_metrics: bool
    :param reason_for_metrics_status: Reason for why the resource is sending metrics (or why it is
     not sending).
    :type reason_for_metrics_status: str
    :param sending_logs: Flag indicating if resource is sending logs to Logz.
    :type sending_logs: bool
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~microsoft_logz.models.SystemData
    :param reason_for_logs_status: Reason for why the resource is sending logs (or why it is not
     sending).
    :type reason_for_logs_status: str
    """

    _validation = {
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'sending_metrics': {'key': 'sendingMetrics', 'type': 'bool'},
        'reason_for_metrics_status': {'key': 'reasonForMetricsStatus', 'type': 'str'},
        'sending_logs': {'key': 'sendingLogs', 'type': 'bool'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'reason_for_logs_status': {'key': 'reasonForLogsStatus', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        sending_metrics: Optional[bool] = None,
        reason_for_metrics_status: Optional[str] = None,
        sending_logs: Optional[bool] = None,
        reason_for_logs_status: Optional[str] = None,
        **kwargs
    ):
        super(MonitoredResource, self).__init__(**kwargs)
        self.id = id
        self.sending_metrics = sending_metrics
        self.reason_for_metrics_status = reason_for_metrics_status
        self.sending_logs = sending_logs
        self.system_data = None
        self.reason_for_logs_status = reason_for_logs_status


class MonitoredResourceListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_logz.models.MonitoredResource]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MonitoredResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MonitoredResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(MonitoredResourceListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class MonitoringTagRules(msrest.serialization.Model):
    """Capture logs and metrics of Azure resources based on ARM tags.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the rule set.
    :vartype name: str
    :ivar id: The id of the rule set.
    :vartype id: str
    :ivar type: The type of the rule set.
    :vartype type: str
    :ivar system_data: The system metadata relating to this resource.
    :vartype system_data: ~microsoft_logz.models.SystemData
    :param properties: Definition of the properties for a TagRules resource.
    :type properties: ~microsoft_logz.models.MonitoringTagRulesProperties
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'properties': {'key': 'properties', 'type': 'MonitoringTagRulesProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["MonitoringTagRulesProperties"] = None,
        **kwargs
    ):
        super(MonitoringTagRules, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.type = None
        self.system_data = None
        self.properties = properties


class MonitoringTagRulesListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_logz.models.MonitoringTagRules]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MonitoringTagRules]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MonitoringTagRules"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(MonitoringTagRulesListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class MonitoringTagRulesProperties(msrest.serialization.Model):
    """Definition of the properties for a TagRules resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param log_rules: Set of rules for sending logs for the Monitor resource.
    :type log_rules: ~microsoft_logz.models.LogRules
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~microsoft_logz.models.SystemData
    """

    _validation = {
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'log_rules': {'key': 'logRules', 'type': 'LogRules'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        *,
        log_rules: Optional["LogRules"] = None,
        **kwargs
    ):
        super(MonitoringTagRulesProperties, self).__init__(**kwargs)
        self.log_rules = log_rules
        self.system_data = None


class MonitorProperties(msrest.serialization.Model):
    """Properties specific to the monitor resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provisioning_state:  Possible values include: "Accepted", "Creating", "Updating",
     "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", "NotSpecified".
    :vartype provisioning_state: str or ~microsoft_logz.models.ProvisioningState
    :param monitoring_status: Flag specifying if the resource monitoring is enabled or disabled.
     Possible values include: "Enabled", "Disabled".
    :type monitoring_status: str or ~microsoft_logz.models.MonitoringStatus
    :param marketplace_subscription_status: Flag specifying the Marketplace Subscription Status of
     the resource. If payment is not made in time, the resource will go in Suspended state. Possible
     values include: "Active", "Suspended".
    :type marketplace_subscription_status: str or
     ~microsoft_logz.models.MarketplaceSubscriptionStatus
    :param logz_organization_properties:
    :type logz_organization_properties: ~microsoft_logz.models.LogzOrganizationProperties
    :param user_info:
    :type user_info: ~microsoft_logz.models.UserInfo
    :param plan_data:
    :type plan_data: ~microsoft_logz.models.PlanData
    :ivar liftr_resource_category:  Possible values include: "Unknown", "MonitorLogs".
    :vartype liftr_resource_category: str or ~microsoft_logz.models.LiftrResourceCategories
    :ivar liftr_resource_preference: The priority of the resource.
    :vartype liftr_resource_preference: int
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'liftr_resource_category': {'readonly': True},
        'liftr_resource_preference': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'monitoring_status': {'key': 'monitoringStatus', 'type': 'str'},
        'marketplace_subscription_status': {'key': 'marketplaceSubscriptionStatus', 'type': 'str'},
        'logz_organization_properties': {'key': 'logzOrganizationProperties', 'type': 'LogzOrganizationProperties'},
        'user_info': {'key': 'userInfo', 'type': 'UserInfo'},
        'plan_data': {'key': 'planData', 'type': 'PlanData'},
        'liftr_resource_category': {'key': 'liftrResourceCategory', 'type': 'str'},
        'liftr_resource_preference': {'key': 'liftrResourcePreference', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        monitoring_status: Optional[Union[str, "MonitoringStatus"]] = None,
        marketplace_subscription_status: Optional[Union[str, "MarketplaceSubscriptionStatus"]] = None,
        logz_organization_properties: Optional["LogzOrganizationProperties"] = None,
        user_info: Optional["UserInfo"] = None,
        plan_data: Optional["PlanData"] = None,
        **kwargs
    ):
        super(MonitorProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.monitoring_status = monitoring_status
        self.marketplace_subscription_status = marketplace_subscription_status
        self.logz_organization_properties = logz_organization_properties
        self.user_info = user_info
        self.plan_data = plan_data
        self.liftr_resource_category = None
        self.liftr_resource_preference = None


class MonitorUpdateProperties(msrest.serialization.Model):
    """The set of properties that can be update in a PATCH request to a monitor resource.

    :param monitoring_status: Flag specifying if the resource monitoring is enabled or disabled.
     Possible values include: "Enabled", "Disabled".
    :type monitoring_status: str or ~microsoft_logz.models.MonitoringStatus
    """

    _attribute_map = {
        'monitoring_status': {'key': 'monitoringStatus', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        monitoring_status: Optional[Union[str, "MonitoringStatus"]] = None,
        **kwargs
    ):
        super(MonitorUpdateProperties, self).__init__(**kwargs)
        self.monitoring_status = monitoring_status


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider, i.e., Microsoft.Logz.
    :type provider: str
    :param resource: Type on which the operation is performed, e.g., 'monitors'.
    :type resource: str
    :param operation: Operation type, e.g., read, write, delete, etc.
    :type operation: str
    :param description: Description of the operation, e.g., 'Write monitors'.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationListResult(msrest.serialization.Model):
    """Result of GET request to list the Microsoft.Logz operations.

    :param value: List of operations supported by the Microsoft.Logz provider.
    :type value: list[~microsoft_logz.models.OperationResult]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationResult]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["OperationResult"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class OperationResult(msrest.serialization.Model):
    """A Microsoft.Logz REST API operation.

    :param name: Operation name, i.e., {provider}/{resource}/{operation}.
    :type name: str
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: bool
    :param display: The object that represents the operation.
    :type display: ~microsoft_logz.models.OperationDisplay
    :param origin: Origin of the operation.
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        is_data_action: Optional[bool] = None,
        display: Optional["OperationDisplay"] = None,
        origin: Optional[str] = None,
        **kwargs
    ):
        super(OperationResult, self).__init__(**kwargs)
        self.name = name
        self.is_data_action = is_data_action
        self.display = display
        self.origin = origin


class PlanData(msrest.serialization.Model):
    """PlanData.

    :param usage_type: different usage type like PAYG/COMMITTED. this could be enum.
    :type usage_type: str
    :param billing_cycle: different billing cycles like MONTHLY/WEEKLY. this could be enum.
    :type billing_cycle: str
    :param plan_details: plan id as published by Logz.
    :type plan_details: str
    :param effective_date: date when plan was applied.
    :type effective_date: ~datetime.datetime
    """

    _validation = {
        'usage_type': {'max_length': 50, 'min_length': 0},
        'billing_cycle': {'max_length': 50, 'min_length': 0},
        'plan_details': {'max_length': 50, 'min_length': 0},
    }

    _attribute_map = {
        'usage_type': {'key': 'usageType', 'type': 'str'},
        'billing_cycle': {'key': 'billingCycle', 'type': 'str'},
        'plan_details': {'key': 'planDetails', 'type': 'str'},
        'effective_date': {'key': 'effectiveDate', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        usage_type: Optional[str] = None,
        billing_cycle: Optional[str] = None,
        plan_details: Optional[str] = None,
        effective_date: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(PlanData, self).__init__(**kwargs)
        self.usage_type = usage_type
        self.billing_cycle = billing_cycle
        self.plan_details = plan_details
        self.effective_date = effective_date


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or ~microsoft_logz.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or ~microsoft_logz.models.CreatedByType
    :param last_modified_at: The timestamp of resource last modification (UTC).
    :type last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at


class UserInfo(msrest.serialization.Model):
    """UserInfo.

    :param first_name: First Name of the user.
    :type first_name: str
    :param last_name: Last Name of the user.
    :type last_name: str
    :param email_address: Email of the user used by Logz for contacting them if needed.
    :type email_address: str
    :param phone_number: Phone number of the user used by Logz for contacting them if needed.
    :type phone_number: str
    """

    _validation = {
        'first_name': {'max_length': 50, 'min_length': 0},
        'last_name': {'max_length': 50, 'min_length': 0},
        'email_address': {'pattern': r'^[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}$'},
        'phone_number': {'max_length': 40, 'min_length': 0},
    }

    _attribute_map = {
        'first_name': {'key': 'firstName', 'type': 'str'},
        'last_name': {'key': 'lastName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        **kwargs
    ):
        super(UserInfo, self).__init__(**kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
