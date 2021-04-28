# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


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
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs['location']


class Account(TrackedResource):
    """Device Update account details.

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
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~device_update.models.SystemData
    :param identity: The type of identity used for the resource.
    :type identity: ~device_update.models.Identity
    :ivar provisioning_state: Provisioning state. Possible values include: "Succeeded", "Deleted",
     "Failed", "Canceled", "Accepted", "Creating".
    :vartype provisioning_state: str or ~device_update.models.ProvisioningState
    :ivar host_name: API host name.
    :vartype host_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'host_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Account, self).__init__(**kwargs)
        self.system_data = None
        self.identity = kwargs.get('identity', None)
        self.provisioning_state = None
        self.host_name = None


class AccountList(msrest.serialization.Model):
    """List of Accounts.

    :param next_link: The link used to get the next page of Accounts list.
    :type next_link: str
    :param value: List of Accounts.
    :type value: list[~device_update.models.Account]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Account]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AccountList, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = kwargs.get('value', None)


class TagUpdate(msrest.serialization.Model):
    """Request payload used to update an existing resource's tags.

    :param tags: A set of tags. List of key value pairs that describe the resource. This will
     overwrite the existing tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TagUpdate, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class AccountUpdate(TagUpdate):
    """Request payload used to update and existing Accounts.

    :param tags: A set of tags. List of key value pairs that describe the resource. This will
     overwrite the existing tags.
    :type tags: dict[str, str]
    :param identity: The type of identity used for the resource.
    :type identity: ~device_update.models.Identity
    :param location: The geo-location where the resource lives.
    :type location: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AccountUpdate, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.location = kwargs.get('location', None)


class CheckNameAvailabilityRequest(msrest.serialization.Model):
    """The check availability request body.

    :param name: The name of the resource for which availability needs to be checked.
    :type name: str
    :param type: The resource type.
    :type type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CheckNameAvailabilityRequest, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)


class CheckNameAvailabilityResponse(msrest.serialization.Model):
    """The check availability result.

    :param name_available: Indicates if the resource name is available.
    :type name_available: bool
    :param reason: The reason why the given name is not available. Possible values include:
     "Invalid", "AlreadyExists".
    :type reason: str or ~device_update.models.CheckNameAvailabilityReason
    :param message: Detailed reason why the given name is available.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CheckNameAvailabilityResponse, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.reason = kwargs.get('reason', None)
        self.message = kwargs.get('message', None)


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
    :vartype details: list[~device_update.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~device_update.models.ErrorAdditionalInfo]
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
    :type error: ~device_update.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class Identity(msrest.serialization.Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: The identity type. Possible values include: "SystemAssigned", "None".
    :type type: str or ~device_update.models.ResourceIdentityType
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
        **kwargs
    ):
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class Instance(TrackedResource):
    """Device Update instance details.

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
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~device_update.models.SystemData
    :ivar provisioning_state: Provisioning state. Possible values include: "Succeeded", "Deleted",
     "Failed", "Canceled", "Accepted", "Creating".
    :vartype provisioning_state: str or ~device_update.models.ProvisioningState
    :ivar account_name: Parent Device Update Account name which Instance belongs to.
    :vartype account_name: str
    :param iot_hubs: List of IoT Hubs associated with the account.
    :type iot_hubs: list[~device_update.models.IotHubSettings]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'account_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'account_name': {'key': 'properties.accountName', 'type': 'str'},
        'iot_hubs': {'key': 'properties.iotHubs', 'type': '[IotHubSettings]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Instance, self).__init__(**kwargs)
        self.system_data = None
        self.provisioning_state = None
        self.account_name = None
        self.iot_hubs = kwargs.get('iot_hubs', None)


class InstanceList(msrest.serialization.Model):
    """List of Instances.

    :param next_link: The link used to get the next page of Instances list.
    :type next_link: str
    :param value: List of Instances.
    :type value: list[~device_update.models.Instance]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Instance]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InstanceList, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = kwargs.get('value', None)


class IotHubSettings(msrest.serialization.Model):
    """Device Update account integration with IoT Hub settings.

    All required parameters must be populated in order to send to Azure.

    :param resource_id: Required. IoTHub resource ID.
    :type resource_id: str
    :param io_t_hub_connection_string: IoTHub connection string.
    :type io_t_hub_connection_string: str
    :param event_hub_connection_string: EventHub connection string.
    :type event_hub_connection_string: str
    """

    _validation = {
        'resource_id': {'required': True, 'max_length': 244, 'min_length': 108},
    }

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'io_t_hub_connection_string': {'key': 'ioTHubConnectionString', 'type': 'str'},
        'event_hub_connection_string': {'key': 'eventHubConnectionString', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(IotHubSettings, self).__init__(**kwargs)
        self.resource_id = kwargs['resource_id']
        self.io_t_hub_connection_string = kwargs.get('io_t_hub_connection_string', None)
        self.event_hub_connection_string = kwargs.get('event_hub_connection_string', None)


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
    :type display: ~device_update.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Possible values include: "user",
     "system", "user,system".
    :vartype origin: str or ~device_update.models.Origin
    :ivar action_type: Enum. Indicates the action type. "Internal" refers to actions that are for
     internal only APIs. Possible values include: "Internal".
    :vartype action_type: str or ~device_update.models.ActionType
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
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.is_data_action = None
        self.display = kwargs.get('display', None)
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
    :vartype value: list[~device_update.models.Operation]
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


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or ~device_update.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or ~device_update.models.CreatedByType
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
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = kwargs.get('created_by', None)
        self.created_by_type = kwargs.get('created_by_type', None)
        self.created_at = kwargs.get('created_at', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.last_modified_by_type = kwargs.get('last_modified_by_type', None)
        self.last_modified_at = kwargs.get('last_modified_at', None)
