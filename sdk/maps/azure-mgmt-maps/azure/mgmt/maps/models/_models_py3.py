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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class Resource(Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
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

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AzureEntityResource(Resource):
    """The resource model definition for a Azure Resource Manager resource with an
    etag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AzureEntityResource, self).__init__(**kwargs)
        self.etag = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorAdditionalInfo(Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorResponse(Model):
    """The resource management error response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.maps.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.maps.models.ErrorAdditionalInfo]
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

    def __init__(self, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
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

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class MapsAccount(TrackedResource):
    """An Azure resource which represents access to a suite of Maps REST APIs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :ivar sku: The SKU of this account.
    :vartype sku: ~azure.mgmt.maps.models.Sku
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data: ~azure.mgmt.maps.models.SystemData
    :ivar properties: The map account properties.
    :vartype properties: ~azure.mgmt.maps.models.MapsAccountProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'readonly': True},
        'system_data': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'properties': {'key': 'properties', 'type': 'MapsAccountProperties'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(MapsAccount, self).__init__(tags=tags, location=location, **kwargs)
        self.sku = None
        self.system_data = None
        self.properties = None


class MapsAccountCreateParameters(Model):
    """Parameters used to create a new Maps Account.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The location of the resource.
    :type location: str
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). Each tag must have a key no greater than 128
     characters and value no greater than 256 characters.
    :type tags: dict[str, str]
    :param sku: Required. The SKU of this account.
    :type sku: ~azure.mgmt.maps.models.Sku
    """

    _validation = {
        'location': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, *, location: str, sku, tags=None, **kwargs) -> None:
        super(MapsAccountCreateParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.sku = sku


class MapsAccountKeys(Model):
    """The set of keys which can be used to access the Maps REST APIs. Two keys
    are provided for key rotation without interruption.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The full Azure resource identifier of the Maps Account.
    :vartype id: str
    :ivar primary_key: The primary key for accessing the Maps REST APIs.
    :vartype primary_key: str
    :ivar secondary_key: The secondary key for accessing the Maps REST APIs.
    :vartype secondary_key: str
    """

    _validation = {
        'id': {'readonly': True},
        'primary_key': {'readonly': True},
        'secondary_key': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(MapsAccountKeys, self).__init__(**kwargs)
        self.id = None
        self.primary_key = None
        self.secondary_key = None


class MapsAccountProperties(Model):
    """Additional Map account properties.

    :param x_ms_client_id: A unique identifier for the maps account
    :type x_ms_client_id: str
    """

    _attribute_map = {
        'x_ms_client_id': {'key': 'x-ms-client-id', 'type': 'str'},
    }

    def __init__(self, *, x_ms_client_id: str=None, **kwargs) -> None:
        super(MapsAccountProperties, self).__init__(**kwargs)
        self.x_ms_client_id = x_ms_client_id


class MapsAccountUpdateParameters(Model):
    """Parameters used to update an existing Maps Account.

    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict[str, str]
    :param sku: The SKU of this account.
    :type sku: ~azure.mgmt.maps.models.Sku
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, *, tags=None, sku=None, **kwargs) -> None:
        super(MapsAccountUpdateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.sku = sku


class MapsKeySpecification(Model):
    """Whether the operation refers to the primary or secondary key.

    All required parameters must be populated in order to send to Azure.

    :param key_type: Required. Whether the operation refers to the primary or
     secondary key. Possible values include: 'primary', 'secondary'
    :type key_type: str or ~azure.mgmt.maps.models.KeyType
    """

    _validation = {
        'key_type': {'required': True},
    }

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'str'},
    }

    def __init__(self, *, key_type, **kwargs) -> None:
        super(MapsKeySpecification, self).__init__(**kwargs)
        self.key_type = key_type


class MapsOperationsValueItem(Model):
    """MapsOperationsValueItem.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Operation name: {provider}/{resource}/{operation}.
    :vartype name: str
    :param display: The human-readable description of the operation.
    :type display: ~azure.mgmt.maps.models.MapsOperationsValueItemDisplay
    :ivar origin: The origin of the operation.
    :vartype origin: str
    """

    _validation = {
        'name': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'MapsOperationsValueItemDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self, *, display=None, **kwargs) -> None:
        super(MapsOperationsValueItem, self).__init__(**kwargs)
        self.name = None
        self.display = display
        self.origin = None


class MapsOperationsValueItemDisplay(Model):
    """The human-readable description of the operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: Service provider: Microsoft Maps.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed.
    :vartype resource: str
    :ivar operation: The action that users can perform, based on their
     permission level.
    :vartype operation: str
    :ivar description: The description of the operation.
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

    def __init__(self, **kwargs) -> None:
        super(MapsOperationsValueItemDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class PrivateAtlas(TrackedResource):
    """An Azure resource which represents which will provision the ability to
    create private location data.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param properties: The Private Atlas resource properties.
    :type properties: ~azure.mgmt.maps.models.PrivateAtlasProperties
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
        'properties': {'key': 'properties', 'type': 'PrivateAtlasProperties'},
    }

    def __init__(self, *, location: str, tags=None, properties=None, **kwargs) -> None:
        super(PrivateAtlas, self).__init__(tags=tags, location=location, **kwargs)
        self.properties = properties


class PrivateAtlasCreateParameters(Model):
    """Parameters used to create a new Private Atlas resource.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The location of the resource.
    :type location: str
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict[str, str]
    """

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(PrivateAtlasCreateParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags


class PrivateAtlasProperties(Model):
    """Private Atlas resource properties.

    :param provisioning_state: The state of the resource provisioning,
     terminal states: Succeeded, Failed, Canceled
    :type provisioning_state: str
    """

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(self, *, provisioning_state: str=None, **kwargs) -> None:
        super(PrivateAtlasProperties, self).__init__(**kwargs)
        self.provisioning_state = provisioning_state


class PrivateAtlasUpdateParameters(Model):
    """Parameters used to update an existing Private Atlas resource.

    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, tags=None, **kwargs) -> None:
        super(PrivateAtlasUpdateParameters, self).__init__(**kwargs)
        self.tags = tags


class ProxyResource(Resource):
    """The resource model definition for a ARM proxy resource. It will have
    everything other than required location and tags.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
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

    def __init__(self, **kwargs) -> None:
        super(ProxyResource, self).__init__(**kwargs)


class Sku(Model):
    """The SKU of the Maps Account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU, in standard format (such as
     S0).
    :type name: str
    :ivar tier: Gets the sku tier. This is based on the SKU name.
    :vartype tier: str
    """

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, *, name: str, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = None


class SystemData(Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource.
     Possible values include: 'User', 'Application', 'ManagedIdentity', 'Key'
    :type created_by_type: str or ~azure.mgmt.maps.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the
     resource. Possible values include: 'User', 'Application',
     'ManagedIdentity', 'Key'
    :type last_modified_by_type: str or ~azure.mgmt.maps.models.CreatedByType
    :param last_modified_at: The type of identity that last modified the
     resource.
    :type last_modified_at: datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(self, *, created_by: str=None, created_by_type=None, created_at=None, last_modified_by: str=None, last_modified_by_type=None, last_modified_at=None, **kwargs) -> None:
        super(SystemData, self).__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
