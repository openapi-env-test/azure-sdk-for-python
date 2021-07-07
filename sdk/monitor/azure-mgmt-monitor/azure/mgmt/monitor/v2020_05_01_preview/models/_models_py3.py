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

from ._monitor_management_client_enums import *


class Action(msrest.serialization.Model):
    """Actions to invoke when the alert fires.

    :param action_group_id: Action Group resource Id to invoke when the alert fires.
    :type action_group_id: str
    :param web_hook_properties: The properties of a webhook object.
    :type web_hook_properties: dict[str, str]
    """

    _attribute_map = {
        'action_group_id': {'key': 'actionGroupId', 'type': 'str'},
        'web_hook_properties': {'key': 'webHookProperties', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        action_group_id: Optional[str] = None,
        web_hook_properties: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Action, self).__init__(**kwargs)
        self.action_group_id = action_group_id
        self.web_hook_properties = web_hook_properties


class Condition(msrest.serialization.Model):
    """A condition of the scheduled query rule.

    All required parameters must be populated in order to send to Azure.

    :param query: Log query alert.
    :type query: str
    :param time_aggregation: Required. Aggregation type. Possible values include: "Count",
     "Average", "Minimum", "Maximum", "Total".
    :type time_aggregation: str or
     ~$(python-base-namespace).v2020_05_01_preview.models.TimeAggregation
    :param metric_measure_column: The column containing the metric measure number.
    :type metric_measure_column: str
    :param resource_id_column: The column containing the resource id. The content of the column
     must be a uri formatted as resource id.
    :type resource_id_column: str
    :param dimensions: List of Dimensions conditions.
    :type dimensions: list[~$(python-base-namespace).v2020_05_01_preview.models.Dimension]
    :param operator: Required. The criteria operator. Possible values include: "Equals",
     "GreaterThan", "GreaterThanOrEqual", "LessThan", "LessThanOrEqual".
    :type operator: str or ~$(python-base-namespace).v2020_05_01_preview.models.ConditionOperator
    :param threshold: Required. the criteria threshold value that activates the alert.
    :type threshold: float
    :param failing_periods: The minimum number of violations required within the selected lookback
     time window required to raise an alert.
    :type failing_periods:
     ~$(python-base-namespace).v2020_05_01_preview.models.ConditionFailingPeriods
    """

    _validation = {
        'time_aggregation': {'required': True},
        'operator': {'required': True},
        'threshold': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'time_aggregation': {'key': 'timeAggregation', 'type': 'str'},
        'metric_measure_column': {'key': 'metricMeasureColumn', 'type': 'str'},
        'resource_id_column': {'key': 'resourceIdColumn', 'type': 'str'},
        'dimensions': {'key': 'dimensions', 'type': '[Dimension]'},
        'operator': {'key': 'operator', 'type': 'str'},
        'threshold': {'key': 'threshold', 'type': 'float'},
        'failing_periods': {'key': 'failingPeriods', 'type': 'ConditionFailingPeriods'},
    }

    def __init__(
        self,
        *,
        time_aggregation: Union[str, "TimeAggregation"],
        operator: Union[str, "ConditionOperator"],
        threshold: float,
        query: Optional[str] = None,
        metric_measure_column: Optional[str] = None,
        resource_id_column: Optional[str] = None,
        dimensions: Optional[List["Dimension"]] = None,
        failing_periods: Optional["ConditionFailingPeriods"] = None,
        **kwargs
    ):
        super(Condition, self).__init__(**kwargs)
        self.query = query
        self.time_aggregation = time_aggregation
        self.metric_measure_column = metric_measure_column
        self.resource_id_column = resource_id_column
        self.dimensions = dimensions
        self.operator = operator
        self.threshold = threshold
        self.failing_periods = failing_periods


class ConditionFailingPeriods(msrest.serialization.Model):
    """The minimum number of violations required within the selected lookback time window required to raise an alert.

    :param number_of_evaluation_periods: The number of aggregated lookback points. The lookback
     time window is calculated based on the aggregation granularity (windowSize) and the selected
     number of aggregated points. Default value is 1.
    :type number_of_evaluation_periods: long
    :param min_failing_periods_to_alert: The number of violations to trigger an alert. Should be
     smaller or equal to numberOfEvaluationPeriods. Default value is 1.
    :type min_failing_periods_to_alert: long
    """

    _attribute_map = {
        'number_of_evaluation_periods': {'key': 'numberOfEvaluationPeriods', 'type': 'long'},
        'min_failing_periods_to_alert': {'key': 'minFailingPeriodsToAlert', 'type': 'long'},
    }

    def __init__(
        self,
        *,
        number_of_evaluation_periods: Optional[int] = 1,
        min_failing_periods_to_alert: Optional[int] = 1,
        **kwargs
    ):
        super(ConditionFailingPeriods, self).__init__(**kwargs)
        self.number_of_evaluation_periods = number_of_evaluation_periods
        self.min_failing_periods_to_alert = min_failing_periods_to_alert


class Dimension(msrest.serialization.Model):
    """Dimension splitting and filtering definition.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the dimension.
    :type name: str
    :param operator: Required. Operator for dimension values. Possible values include: "Include",
     "Exclude".
    :type operator: str or ~$(python-base-namespace).v2020_05_01_preview.models.DimensionOperator
    :param values: Required. List of dimension values.
    :type values: list[str]
    """

    _validation = {
        'name': {'required': True},
        'operator': {'required': True},
        'values': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        name: str,
        operator: Union[str, "DimensionOperator"],
        values: List[str],
        **kwargs
    ):
        super(Dimension, self).__init__(**kwargs)
        self.name = name
        self.operator = operator
        self.values = values


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorContract(msrest.serialization.Model):
    """Describes the format of Error response.

    :param error: The error details.
    :type error: ~$(python-base-namespace).v2020_05_01_preview.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorResponse"] = None,
        **kwargs
    ):
        super(ErrorContract, self).__init__(**kwargs)
        self.error = error


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~$(python-base-namespace).v2020_05_01_preview.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~$(python-base-namespace).v2020_05_01_preview.models.ErrorAdditionalInfo]
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
        'details': {'key': 'details', 'type': '[ErrorResponse]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class ScheduledQueryRuleCriteria(msrest.serialization.Model):
    """The rule criteria that defines the conditions of the scheduled query rule.

    :param all_of: A list of conditions to evaluate against the specified scopes.
    :type all_of: list[~$(python-base-namespace).v2020_05_01_preview.models.Condition]
    """

    _attribute_map = {
        'all_of': {'key': 'allOf', 'type': '[Condition]'},
    }

    def __init__(
        self,
        *,
        all_of: Optional[List["Condition"]] = None,
        **kwargs
    ):
        super(ScheduledQueryRuleCriteria, self).__init__(**kwargs)
        self.all_of = all_of


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class ScheduledQueryRuleResource(TrackedResource):
    """The scheduled query rule resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :ivar kind: Metadata used by portal/tooling/etc to render different UX experiences for
     resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported,
     the resource provider must validate and persist this value.
    :vartype kind: str
    :ivar etag: The etag field is *not* required. If it is provided in the response body, it must
     also be provided as a header per the normal etag convention.  Entity tags are used for
     comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in
     the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range
     (section 14.27) header fields.
    :vartype etag: str
    :ivar created_with_api_version: The api-version used when creating this alert rule.
    :vartype created_with_api_version: str
    :ivar is_legacy_log_analytics_rule: True if alert rule is legacy Log Analytic rule.
    :vartype is_legacy_log_analytics_rule: bool
    :param description: The description of the scheduled query rule.
    :type description: str
    :param display_name: The display name of the alert rule.
    :type display_name: str
    :param severity: Severity of the alert. Should be an integer between [0-4]. Value of 0 is
     severest. Possible values include: 0, 1, 2, 3, 4.
    :type severity: str or ~$(python-base-namespace).v2020_05_01_preview.models.AlertSeverity
    :param enabled: The flag which indicates whether this scheduled query rule is enabled. Value
     should be true or false.
    :type enabled: bool
    :param scopes: The list of resource id's that this scheduled query rule is scoped to.
    :type scopes: list[str]
    :param evaluation_frequency: How often the scheduled query rule is evaluated represented in ISO
     8601 duration format.
    :type evaluation_frequency: ~datetime.timedelta
    :param window_size: The period of time (in ISO 8601 duration format) on which the Alert query
     will be executed (bin size).
    :type window_size: ~datetime.timedelta
    :param override_query_time_range: If specified then overrides the query time range (default is
     WindowSize*NumberOfEvaluationPeriods).
    :type override_query_time_range: ~datetime.timedelta
    :param target_resource_types: List of resource type of the target resource(s) on which the
     alert is created/updated. For example if the scope is a resource group and targetResourceTypes
     is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual
     machine in the resource group which meet the alert criteria.
    :type target_resource_types: list[str]
    :param criteria: The rule criteria that defines the conditions of the scheduled query rule.
    :type criteria: ~$(python-base-namespace).v2020_05_01_preview.models.ScheduledQueryRuleCriteria
    :param mute_actions_duration: Mute actions for the chosen period of time (in ISO 8601 duration
     format) after the alert is fired.
    :type mute_actions_duration: ~datetime.timedelta
    :param actions:
    :type actions: list[~$(python-base-namespace).v2020_05_01_preview.models.Action]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'kind': {'readonly': True},
        'etag': {'readonly': True},
        'created_with_api_version': {'readonly': True},
        'is_legacy_log_analytics_rule': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'created_with_api_version': {'key': 'properties.createdWithApiVersion', 'type': 'str'},
        'is_legacy_log_analytics_rule': {'key': 'properties.isLegacyLogAnalyticsRule', 'type': 'bool'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'float'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'scopes': {'key': 'properties.scopes', 'type': '[str]'},
        'evaluation_frequency': {'key': 'properties.evaluationFrequency', 'type': 'duration'},
        'window_size': {'key': 'properties.windowSize', 'type': 'duration'},
        'override_query_time_range': {'key': 'properties.overrideQueryTimeRange', 'type': 'duration'},
        'target_resource_types': {'key': 'properties.targetResourceTypes', 'type': '[str]'},
        'criteria': {'key': 'properties.criteria', 'type': 'ScheduledQueryRuleCriteria'},
        'mute_actions_duration': {'key': 'properties.muteActionsDuration', 'type': 'duration'},
        'actions': {'key': 'properties.actions', 'type': '[Action]'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        severity: Optional[Union[float, "AlertSeverity"]] = None,
        enabled: Optional[bool] = None,
        scopes: Optional[List[str]] = None,
        evaluation_frequency: Optional[datetime.timedelta] = None,
        window_size: Optional[datetime.timedelta] = None,
        override_query_time_range: Optional[datetime.timedelta] = None,
        target_resource_types: Optional[List[str]] = None,
        criteria: Optional["ScheduledQueryRuleCriteria"] = None,
        mute_actions_duration: Optional[datetime.timedelta] = None,
        actions: Optional[List["Action"]] = None,
        **kwargs
    ):
        super(ScheduledQueryRuleResource, self).__init__(tags=tags, location=location, **kwargs)
        self.kind = None
        self.etag = None
        self.created_with_api_version = None
        self.is_legacy_log_analytics_rule = None
        self.description = description
        self.display_name = display_name
        self.severity = severity
        self.enabled = enabled
        self.scopes = scopes
        self.evaluation_frequency = evaluation_frequency
        self.window_size = window_size
        self.override_query_time_range = override_query_time_range
        self.target_resource_types = target_resource_types
        self.criteria = criteria
        self.mute_actions_duration = mute_actions_duration
        self.actions = actions


class ScheduledQueryRuleResourceCollection(msrest.serialization.Model):
    """Represents a collection of scheduled query rule resources.

    :param value: The values for the scheduled query rule resources.
    :type value:
     list[~$(python-base-namespace).v2020_05_01_preview.models.ScheduledQueryRuleResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ScheduledQueryRuleResource]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ScheduledQueryRuleResource"]] = None,
        **kwargs
    ):
        super(ScheduledQueryRuleResourceCollection, self).__init__(**kwargs)
        self.value = value


class ScheduledQueryRuleResourcePatch(msrest.serialization.Model):
    """The scheduled query rule resource for patch operations.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :ivar created_with_api_version: The api-version used when creating this alert rule.
    :vartype created_with_api_version: str
    :ivar is_legacy_log_analytics_rule: True if alert rule is legacy Log Analytic rule.
    :vartype is_legacy_log_analytics_rule: bool
    :param description: The description of the scheduled query rule.
    :type description: str
    :param display_name: The display name of the alert rule.
    :type display_name: str
    :param severity: Severity of the alert. Should be an integer between [0-4]. Value of 0 is
     severest. Possible values include: 0, 1, 2, 3, 4.
    :type severity: str or ~$(python-base-namespace).v2020_05_01_preview.models.AlertSeverity
    :param enabled: The flag which indicates whether this scheduled query rule is enabled. Value
     should be true or false.
    :type enabled: bool
    :param scopes: The list of resource id's that this scheduled query rule is scoped to.
    :type scopes: list[str]
    :param evaluation_frequency: How often the scheduled query rule is evaluated represented in ISO
     8601 duration format.
    :type evaluation_frequency: ~datetime.timedelta
    :param window_size: The period of time (in ISO 8601 duration format) on which the Alert query
     will be executed (bin size).
    :type window_size: ~datetime.timedelta
    :param override_query_time_range: If specified then overrides the query time range (default is
     WindowSize*NumberOfEvaluationPeriods).
    :type override_query_time_range: ~datetime.timedelta
    :param target_resource_types: List of resource type of the target resource(s) on which the
     alert is created/updated. For example if the scope is a resource group and targetResourceTypes
     is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual
     machine in the resource group which meet the alert criteria.
    :type target_resource_types: list[str]
    :param criteria: The rule criteria that defines the conditions of the scheduled query rule.
    :type criteria: ~$(python-base-namespace).v2020_05_01_preview.models.ScheduledQueryRuleCriteria
    :param mute_actions_duration: Mute actions for the chosen period of time (in ISO 8601 duration
     format) after the alert is fired.
    :type mute_actions_duration: ~datetime.timedelta
    :param actions:
    :type actions: list[~$(python-base-namespace).v2020_05_01_preview.models.Action]
    """

    _validation = {
        'created_with_api_version': {'readonly': True},
        'is_legacy_log_analytics_rule': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'created_with_api_version': {'key': 'properties.createdWithApiVersion', 'type': 'str'},
        'is_legacy_log_analytics_rule': {'key': 'properties.isLegacyLogAnalyticsRule', 'type': 'bool'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'float'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'scopes': {'key': 'properties.scopes', 'type': '[str]'},
        'evaluation_frequency': {'key': 'properties.evaluationFrequency', 'type': 'duration'},
        'window_size': {'key': 'properties.windowSize', 'type': 'duration'},
        'override_query_time_range': {'key': 'properties.overrideQueryTimeRange', 'type': 'duration'},
        'target_resource_types': {'key': 'properties.targetResourceTypes', 'type': '[str]'},
        'criteria': {'key': 'properties.criteria', 'type': 'ScheduledQueryRuleCriteria'},
        'mute_actions_duration': {'key': 'properties.muteActionsDuration', 'type': 'duration'},
        'actions': {'key': 'properties.actions', 'type': '[Action]'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        severity: Optional[Union[float, "AlertSeverity"]] = None,
        enabled: Optional[bool] = None,
        scopes: Optional[List[str]] = None,
        evaluation_frequency: Optional[datetime.timedelta] = None,
        window_size: Optional[datetime.timedelta] = None,
        override_query_time_range: Optional[datetime.timedelta] = None,
        target_resource_types: Optional[List[str]] = None,
        criteria: Optional["ScheduledQueryRuleCriteria"] = None,
        mute_actions_duration: Optional[datetime.timedelta] = None,
        actions: Optional[List["Action"]] = None,
        **kwargs
    ):
        super(ScheduledQueryRuleResourcePatch, self).__init__(**kwargs)
        self.tags = tags
        self.created_with_api_version = None
        self.is_legacy_log_analytics_rule = None
        self.description = description
        self.display_name = display_name
        self.severity = severity
        self.enabled = enabled
        self.scopes = scopes
        self.evaluation_frequency = evaluation_frequency
        self.window_size = window_size
        self.override_query_time_range = override_query_time_range
        self.target_resource_types = target_resource_types
        self.criteria = criteria
        self.mute_actions_duration = mute_actions_duration
        self.actions = actions
