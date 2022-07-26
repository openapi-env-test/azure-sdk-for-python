# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class DataSource(_serialization.Model):
    """Data source object contains configuration to collect telemetry and one or more sinks to send that telemetry data to.

    All required parameters must be populated in order to send to Azure.

    :ivar kind: Datasource kind. Required. Known values are: "PerformanceCounter", "ETWProviders",
     and "WindowsEventLogs".
    :vartype kind: str or ~$(python-base-namespace).v2018_06_01_preview.models.DataSourceKind
    :ivar configuration: Required.
    :vartype configuration:
     ~$(python-base-namespace).v2018_06_01_preview.models.DataSourceConfiguration
    :ivar sinks: Required.
    :vartype sinks: list[~$(python-base-namespace).v2018_06_01_preview.models.SinkConfiguration]
    """

    _validation = {
        "kind": {"required": True},
        "configuration": {"required": True},
        "sinks": {"required": True},
    }

    _attribute_map = {
        "kind": {"key": "kind", "type": "str"},
        "configuration": {"key": "configuration", "type": "DataSourceConfiguration"},
        "sinks": {"key": "sinks", "type": "[SinkConfiguration]"},
    }

    def __init__(
        self,
        *,
        kind: Union[str, "_models.DataSourceKind"],
        configuration: "_models.DataSourceConfiguration",
        sinks: List["_models.SinkConfiguration"],
        **kwargs
    ):
        """
        :keyword kind: Datasource kind. Required. Known values are: "PerformanceCounter",
         "ETWProviders", and "WindowsEventLogs".
        :paramtype kind: str or ~$(python-base-namespace).v2018_06_01_preview.models.DataSourceKind
        :keyword configuration: Required.
        :paramtype configuration:
         ~$(python-base-namespace).v2018_06_01_preview.models.DataSourceConfiguration
        :keyword sinks: Required.
        :paramtype sinks: list[~$(python-base-namespace).v2018_06_01_preview.models.SinkConfiguration]
        """
        super().__init__(**kwargs)
        self.kind = kind
        self.configuration = configuration
        self.sinks = sinks


class DataSourceConfiguration(_serialization.Model):
    """DataSourceConfiguration.

    :ivar providers: ETW providers configuration.
    :vartype providers:
     list[~$(python-base-namespace).v2018_06_01_preview.models.EtwProviderConfiguration]
    :ivar perf_counters: Performance counter configuration.
    :vartype perf_counters:
     list[~$(python-base-namespace).v2018_06_01_preview.models.PerformanceCounterConfiguration]
    :ivar event_logs: Windows event logs configuration.
    :vartype event_logs:
     list[~$(python-base-namespace).v2018_06_01_preview.models.EventLogConfiguration]
    """

    _attribute_map = {
        "providers": {"key": "providers", "type": "[EtwProviderConfiguration]"},
        "perf_counters": {"key": "perfCounters", "type": "[PerformanceCounterConfiguration]"},
        "event_logs": {"key": "eventLogs", "type": "[EventLogConfiguration]"},
    }

    def __init__(
        self,
        *,
        providers: Optional[List["_models.EtwProviderConfiguration"]] = None,
        perf_counters: Optional[List["_models.PerformanceCounterConfiguration"]] = None,
        event_logs: Optional[List["_models.EventLogConfiguration"]] = None,
        **kwargs
    ):
        """
        :keyword providers: ETW providers configuration.
        :paramtype providers:
         list[~$(python-base-namespace).v2018_06_01_preview.models.EtwProviderConfiguration]
        :keyword perf_counters: Performance counter configuration.
        :paramtype perf_counters:
         list[~$(python-base-namespace).v2018_06_01_preview.models.PerformanceCounterConfiguration]
        :keyword event_logs: Windows event logs configuration.
        :paramtype event_logs:
         list[~$(python-base-namespace).v2018_06_01_preview.models.EventLogConfiguration]
        """
        super().__init__(**kwargs)
        self.providers = providers
        self.perf_counters = perf_counters
        self.event_logs = event_logs


class ErrorResponse(_serialization.Model):
    """Describes the format of Error response.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, code: Optional[str] = None, message: Optional[str] = None, **kwargs):
        """
        :keyword code: Error code.
        :paramtype code: str
        :keyword message: Error message indicating why the operation failed.
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message


class EtwEventConfiguration(_serialization.Model):
    """EtwEventConfiguration.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar id: Required.
    :vartype id: int
    :ivar filter:
    :vartype filter: str
    """

    _validation = {
        "name": {"required": True},
        "id": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "id": {"key": "id", "type": "int"},
        "filter": {"key": "filter", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: str,
        id: int,  # pylint: disable=redefined-builtin
        filter: Optional[str] = None,  # pylint: disable=redefined-builtin
        **kwargs
    ):
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword id: Required.
        :paramtype id: int
        :keyword filter:
        :paramtype filter: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.id = id
        self.filter = filter


class EtwProviderConfiguration(_serialization.Model):
    """EtwProviderConfiguration.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Required.
    :vartype id: str
    :ivar events: Required.
    :vartype events:
     list[~$(python-base-namespace).v2018_06_01_preview.models.EtwEventConfiguration]
    """

    _validation = {
        "id": {"required": True},
        "events": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "events": {"key": "events", "type": "[EtwEventConfiguration]"},
    }

    def __init__(
        self, *, id: str, events: List["_models.EtwEventConfiguration"], **kwargs  # pylint: disable=redefined-builtin
    ):
        """
        :keyword id: Required.
        :paramtype id: str
        :keyword events: Required.
        :paramtype events:
         list[~$(python-base-namespace).v2018_06_01_preview.models.EtwEventConfiguration]
        """
        super().__init__(**kwargs)
        self.id = id
        self.events = events


class EventLogConfiguration(_serialization.Model):
    """EventLogConfiguration.

    All required parameters must be populated in order to send to Azure.

    :ivar log_name: Required.
    :vartype log_name: str
    :ivar filter:
    :vartype filter: str
    """

    _validation = {
        "log_name": {"required": True},
    }

    _attribute_map = {
        "log_name": {"key": "logName", "type": "str"},
        "filter": {"key": "filter", "type": "str"},
    }

    def __init__(self, *, log_name: str, filter: Optional[str] = None, **kwargs):  # pylint: disable=redefined-builtin
        """
        :keyword log_name: Required.
        :paramtype log_name: str
        :keyword filter:
        :paramtype filter: str
        """
        super().__init__(**kwargs)
        self.log_name = log_name
        self.filter = filter


class GuestDiagnosticSettingsAssociationList(_serialization.Model):
    """A list of guest diagnostic settings association.

    :ivar value: The list of guest diagnostic settings association.
    :vartype value:
     list[~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource]
    :ivar next_link: Provides the link to retrieve the next set of elements.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[GuestDiagnosticSettingsAssociationResource]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.GuestDiagnosticSettingsAssociationResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: The list of guest diagnostic settings association.
        :paramtype value:
         list[~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource]
        :keyword next_link: Provides the link to retrieve the next set of elements.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class Resource(_serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs):
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class GuestDiagnosticSettingsAssociationResource(Resource):
    """Virtual machine guest diagnostic settings resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar guest_diagnostic_settings_name: The guest diagnostic settings name. Required.
    :vartype guest_diagnostic_settings_name: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
        "guest_diagnostic_settings_name": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "guest_diagnostic_settings_name": {"key": "properties.guestDiagnosticSettingsName", "type": "str"},
    }

    def __init__(
        self, *, location: str, guest_diagnostic_settings_name: str, tags: Optional[Dict[str, str]] = None, **kwargs
    ):
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword guest_diagnostic_settings_name: The guest diagnostic settings name. Required.
        :paramtype guest_diagnostic_settings_name: str
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.guest_diagnostic_settings_name = guest_diagnostic_settings_name


class GuestDiagnosticSettingsAssociationResourcePatch(_serialization.Model):
    """Guest diagnostic setting resource for patch operations.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar guest_diagnostic_settings_name: The guest diagnostic settings name.
    :vartype guest_diagnostic_settings_name: str
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "guest_diagnostic_settings_name": {"key": "properties.guestDiagnosticSettingsName", "type": "str"},
    }

    def __init__(
        self, *, tags: Optional[Dict[str, str]] = None, guest_diagnostic_settings_name: Optional[str] = None, **kwargs
    ):
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword guest_diagnostic_settings_name: The guest diagnostic settings name.
        :paramtype guest_diagnostic_settings_name: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.guest_diagnostic_settings_name = guest_diagnostic_settings_name


class GuestDiagnosticSettingsList(_serialization.Model):
    """A list of guest diagnostic settings.

    :ivar value: The list of guest diagnostic settings.
    :vartype value:
     list[~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsResource]
    :ivar next_link: Provides the link to retrieve the next set of elements.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[GuestDiagnosticSettingsResource]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.GuestDiagnosticSettingsResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: The list of guest diagnostic settings.
        :paramtype value:
         list[~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsResource]
        :keyword next_link: Provides the link to retrieve the next set of elements.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class GuestDiagnosticSettingsPatchResource(_serialization.Model):
    """An diagnostic settings object for the body of patch operations.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar os_type: Operating system type for the configuration. Known values are: "Windows" and
     "Linux".
    :vartype os_type: str or
     ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsOsType
    :ivar data_sources: the array of data source object which are configured to collect and send
     data.
    :vartype data_sources: list[~$(python-base-namespace).v2018_06_01_preview.models.DataSource]
    :ivar proxy_setting:
    :vartype proxy_setting: str
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "os_type": {"key": "properties.osType", "type": "str"},
        "data_sources": {"key": "properties.dataSources", "type": "[DataSource]"},
        "proxy_setting": {"key": "properties.proxySetting", "type": "str"},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        os_type: Optional[Union[str, "_models.GuestDiagnosticSettingsOsType"]] = None,
        data_sources: Optional[List["_models.DataSource"]] = None,
        proxy_setting: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword os_type: Operating system type for the configuration. Known values are: "Windows" and
         "Linux".
        :paramtype os_type: str or
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsOsType
        :keyword data_sources: the array of data source object which are configured to collect and send
         data.
        :paramtype data_sources: list[~$(python-base-namespace).v2018_06_01_preview.models.DataSource]
        :keyword proxy_setting:
        :paramtype proxy_setting: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.os_type = os_type
        self.data_sources = data_sources
        self.proxy_setting = proxy_setting


class GuestDiagnosticSettingsResource(Resource):
    """Virtual machine guest diagnostics settings resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar os_type: Operating system type for the configuration. Known values are: "Windows" and
     "Linux".
    :vartype os_type: str or
     ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsOsType
    :ivar data_sources: the array of data source object which are configured to collect and send
     data.
    :vartype data_sources: list[~$(python-base-namespace).v2018_06_01_preview.models.DataSource]
    :ivar proxy_setting:
    :vartype proxy_setting: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "os_type": {"key": "properties.osType", "type": "str"},
        "data_sources": {"key": "properties.dataSources", "type": "[DataSource]"},
        "proxy_setting": {"key": "properties.proxySetting", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        os_type: Optional[Union[str, "_models.GuestDiagnosticSettingsOsType"]] = None,
        data_sources: Optional[List["_models.DataSource"]] = None,
        proxy_setting: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword os_type: Operating system type for the configuration. Known values are: "Windows" and
         "Linux".
        :paramtype os_type: str or
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsOsType
        :keyword data_sources: the array of data source object which are configured to collect and send
         data.
        :paramtype data_sources: list[~$(python-base-namespace).v2018_06_01_preview.models.DataSource]
        :keyword proxy_setting:
        :paramtype proxy_setting: str
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.os_type = os_type
        self.data_sources = data_sources
        self.proxy_setting = proxy_setting


class PerformanceCounterConfiguration(_serialization.Model):
    """PerformanceCounterConfiguration.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar sampling_period: Required.
    :vartype sampling_period: str
    :ivar instance:
    :vartype instance: str
    """

    _validation = {
        "name": {"required": True},
        "sampling_period": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "sampling_period": {"key": "samplingPeriod", "type": "str"},
        "instance": {"key": "instance", "type": "str"},
    }

    def __init__(self, *, name: str, sampling_period: str, instance: Optional[str] = None, **kwargs):
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword sampling_period: Required.
        :paramtype sampling_period: str
        :keyword instance:
        :paramtype instance: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.sampling_period = sampling_period
        self.instance = instance


class SinkConfiguration(_serialization.Model):
    """SinkConfiguration.

    All required parameters must be populated in order to send to Azure.

    :ivar kind: Required. Known values are: "EventHub", "ApplicationInsights", and "LogAnalytics".
    :vartype kind: str or
     ~$(python-base-namespace).v2018_06_01_preview.models.SinkConfigurationKind
    """

    _validation = {
        "kind": {"required": True},
    }

    _attribute_map = {
        "kind": {"key": "kind", "type": "str"},
    }

    def __init__(self, *, kind: Union[str, "_models.SinkConfigurationKind"], **kwargs):
        """
        :keyword kind: Required. Known values are: "EventHub", "ApplicationInsights", and
         "LogAnalytics".
        :paramtype kind: str or
         ~$(python-base-namespace).v2018_06_01_preview.models.SinkConfigurationKind
        """
        super().__init__(**kwargs)
        self.kind = kind
