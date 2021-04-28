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

from ._communication_service_management_client_enums import *


class CommunicationServiceKeys(msrest.serialization.Model):
    """A class representing the access keys of a CommunicationService.

    :param primary_key: The primary access key.
    :type primary_key: str
    :param secondary_key: The secondary access key.
    :type secondary_key: str
    :param primary_connection_string: CommunicationService connection string constructed via the
     primaryKey.
    :type primary_connection_string: str
    :param secondary_connection_string: CommunicationService connection string constructed via the
     secondaryKey.
    :type secondary_connection_string: str
    """

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'primary_connection_string': {'key': 'primaryConnectionString', 'type': 'str'},
        'secondary_connection_string': {'key': 'secondaryConnectionString', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        primary_key: Optional[str] = None,
        secondary_key: Optional[str] = None,
        primary_connection_string: Optional[str] = None,
        secondary_connection_string: Optional[str] = None,
        **kwargs
    ):
        super(CommunicationServiceKeys, self).__init__(**kwargs)
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.primary_connection_string = primary_connection_string
        self.secondary_connection_string = secondary_connection_string


class TaggedResource(msrest.serialization.Model):
    """An ARM resource with that can accept tags.

    :param tags: A set of tags. Tags of the service which is a list of key value pairs that
     describe the resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TaggedResource, self).__init__(**kwargs)
        self.tags = tags


class LocationResource(msrest.serialization.Model):
    """An ARM resource with its own location (not a global or an inherited location).

    :param location: The Azure location where the CommunicationService is running.
    :type location: str
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        **kwargs
    ):
        super(LocationResource, self).__init__(**kwargs)
        self.location = location


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


class CommunicationServiceResource(Resource, LocationResource, TaggedResource):
    """A class representing a CommunicationService resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param tags: A set of tags. Tags of the service which is a list of key value pairs that
     describe the resource.
    :type tags: dict[str, str]
    :param location: The Azure location where the CommunicationService is running.
    :type location: str
    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~communication_service_management_client.models.SystemData
    :ivar provisioning_state: Provisioning state of the resource. Possible values include:
     "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting",
     "Moving".
    :vartype provisioning_state: str or
     ~communication_service_management_client.models.ProvisioningState
    :ivar host_name: FQDN of the CommunicationService instance.
    :vartype host_name: str
    :param data_location: The location where the communication service stores its data at rest.
    :type data_location: str
    :ivar notification_hub_id: Resource ID of an Azure Notification Hub linked to this resource.
    :vartype notification_hub_id: str
    :ivar version: Version of the CommunicationService resource. Probably you need the same or
     higher version of client SDKs.
    :vartype version: str
    :ivar immutable_resource_id: The immutable resource Id of the communication service.
    :vartype immutable_resource_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'host_name': {'readonly': True},
        'notification_hub_id': {'readonly': True},
        'version': {'readonly': True},
        'immutable_resource_id': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'data_location': {'key': 'properties.dataLocation', 'type': 'str'},
        'notification_hub_id': {'key': 'properties.notificationHubId', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'immutable_resource_id': {'key': 'properties.immutableResourceId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        data_location: Optional[str] = None,
        **kwargs
    ):
        super(CommunicationServiceResource, self).__init__(location=location, tags=tags, **kwargs)
        self.tags = tags
        self.location = location
        self.system_data = None
        self.provisioning_state = None
        self.host_name = None
        self.data_location = data_location
        self.notification_hub_id = None
        self.version = None
        self.immutable_resource_id = None
        self.tags = tags
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None
        self.provisioning_state = None
        self.host_name = None
        self.data_location = data_location
        self.notification_hub_id = None
        self.version = None
        self.immutable_resource_id = None
        self.location = location
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None
        self.provisioning_state = None
        self.host_name = None
        self.data_location = data_location
        self.notification_hub_id = None
        self.version = None
        self.immutable_resource_id = None


class CommunicationServiceResourceList(msrest.serialization.Model):
    """Object that includes an array of CommunicationServices and a possible link for next set.

    :param value: List of CommunicationService.
    :type value: list[~communication_service_management_client.models.CommunicationServiceResource]
    :param next_link: The URL the client should use to fetch the next page (per server side
     paging).
     It's null for now, added for future use.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CommunicationServiceResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["CommunicationServiceResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(CommunicationServiceResourceList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


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
    :vartype details: list[~communication_service_management_client.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~communication_service_management_client.models.ErrorAdditionalInfo]
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
    :type error: ~communication_service_management_client.models.ErrorDetail
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


class LinkedNotificationHub(msrest.serialization.Model):
    """A notification hub that has been linked to the communication service.

    :param resource_id: The resource ID of the notification hub.
    :type resource_id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        resource_id: Optional[str] = None,
        **kwargs
    ):
        super(LinkedNotificationHub, self).__init__(**kwargs)
        self.resource_id = resource_id


class LinkNotificationHubParameters(msrest.serialization.Model):
    """Description of an Azure Notification Hub to link to the communication service.

    All required parameters must be populated in order to send to Azure.

    :param resource_id: Required. The resource ID of the notification hub.
    :type resource_id: str
    :param connection_string: Required. Connection string for the notification hub.
    :type connection_string: str
    """

    _validation = {
        'resource_id': {'required': True},
        'connection_string': {'required': True},
    }

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'connection_string': {'key': 'connectionString', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        resource_id: str,
        connection_string: str,
        **kwargs
    ):
        super(LinkNotificationHubParameters, self).__init__(**kwargs)
        self.resource_id = resource_id
        self.connection_string = connection_string


class NameAvailability(msrest.serialization.Model):
    """Result of the request to check name availability. It contains a flag and possible reason of failure.

    :param name_available: Indicates whether the name is available or not.
    :type name_available: bool
    :param reason: The reason of the availability. Required if name is not available.
    :type reason: str
    :param message: The message of the operation.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name_available: Optional[bool] = None,
        reason: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(NameAvailability, self).__init__(**kwargs)
        self.name_available = name_available
        self.reason = reason
        self.message = message


class NameAvailabilityParameters(msrest.serialization.Model):
    """Data POST-ed to the nameAvailability action.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The resource type. Should be always
     "Microsoft.Communication/CommunicationServices".
    :type type: str
    :param name: Required. The CommunicationService name to validate.
     e.g."my-CommunicationService-name-here".
    :type name: str
    """

    _validation = {
        'type': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: str,
        name: str,
        **kwargs
    ):
        super(NameAvailabilityParameters, self).__init__(**kwargs)
        self.type = type
        self.name = name


class Operation(msrest.serialization.Model):
    """Details of a REST API operation, returned from the Resource Provider Operations API.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action".
    :vartype name: str
    :ivar is_data_action: Whether the operation applies to data-plane. This is "true" for
     data-plane operations and "false" for ARM/control-plane operations.
    :vartype is_data_action: bool
    :param display: Localized display information for this particular operation.
    :type display: ~communication_service_management_client.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Possible values include: "user",
     "system", "user,system".
    :vartype origin: str or ~communication_service_management_client.models.Origin
    :ivar action_type: Enum. Indicates the action type. "Internal" refers to actions that are for
     internal only APIs. Possible values include: "Internal".
    :vartype action_type: str or ~communication_service_management_client.models.ActionType
    """

    _validation = {
        'name': {'readonly': True},
        'is_data_action': {'readonly': True},
        'origin': {'readonly': True},
        'action_type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'action_type': {'key': 'actionType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.is_data_action = None
        self.display = display
        self.origin = None
        self.action_type = None


class OperationDisplay(msrest.serialization.Model):
    """Localized display information for this particular operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: The localized friendly form of the resource provider name, e.g. "Microsoft
     Monitoring Insights" or "Microsoft Compute".
    :vartype provider: str
    :ivar resource: The localized friendly name of the resource type related to this operation.
     E.g. "Virtual Machines" or "Job Schedule Collections".
    :vartype resource: str
    :ivar operation: The concise, localized friendly name for the operation; suitable for
     dropdowns. E.g. "Create or Update Virtual Machine", "Restart Virtual Machine".
    :vartype operation: str
    :ivar description: The short, localized friendly description of the operation; suitable for
     tool tips and detailed views.
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationListResult(msrest.serialization.Model):
    """A list of REST API operations supported by an Azure Resource Provider. It contains an URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of operations supported by the resource provider.
    :vartype value: list[~communication_service_management_client.models.Operation]
    :ivar next_link: URL to get the next set of operation list results (if there are any).
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class OperationStatus(msrest.serialization.Model):
    """The current status of an async operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified ID for the operation status.
    :vartype id: str
    :ivar status: Provisioning state of the resource. Possible values include: "Succeeded",
     "Failed", "Canceled", "Creating", "Deleting", "Moving".
    :vartype status: str or ~communication_service_management_client.models.Status
    :ivar start_time: The start time of the operation.
    :vartype start_time: ~datetime.datetime
    :ivar end_time: The end time of the operation.
    :vartype end_time: ~datetime.datetime
    :ivar percent_complete: Percent of the operation that is complete.
    :vartype percent_complete: float
    :param error: The error object.
    :type error: ~communication_service_management_client.models.ErrorDetail
    """

    _validation = {
        'id': {'readonly': True},
        'status': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'percent_complete': {'readonly': True, 'maximum': 100, 'minimum': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'percent_complete': {'key': 'percentComplete', 'type': 'float'},
        'error': {'key': 'error.error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDetail"] = None,
        **kwargs
    ):
        super(OperationStatus, self).__init__(**kwargs)
        self.id = None
        self.status = None
        self.start_time = None
        self.end_time = None
        self.percent_complete = None
        self.error = error


class RegenerateKeyParameters(msrest.serialization.Model):
    """Parameters describes the request to regenerate access keys.

    :param key_type: The keyType to regenerate. Must be either 'primary' or
     'secondary'(case-insensitive). Possible values include: "Primary", "Secondary".
    :type key_type: str or ~communication_service_management_client.models.KeyType
    """

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        key_type: Optional[Union[str, "KeyType"]] = None,
        **kwargs
    ):
        super(RegenerateKeyParameters, self).__init__(**kwargs)
        self.key_type = key_type


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or ~communication_service_management_client.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or
     ~communication_service_management_client.models.CreatedByType
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
