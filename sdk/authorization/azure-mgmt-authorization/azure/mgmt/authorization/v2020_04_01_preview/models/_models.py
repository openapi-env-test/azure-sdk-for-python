# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


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
    :vartype details: list[~azure.mgmt.authorization.v2020_04_01_preview.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.authorization.v2020_04_01_preview.models.ErrorAdditionalInfo]
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
    :type error: ~azure.mgmt.authorization.v2020_04_01_preview.models.ErrorDetail
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


class RoleAssignment(msrest.serialization.Model):
    """Role Assignments.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The role assignment ID.
    :vartype id: str
    :ivar name: The role assignment name.
    :vartype name: str
    :ivar type: The role assignment type.
    :vartype type: str
    :param scope: The role assignment scope.
    :type scope: str
    :param role_definition_id: The role definition ID.
    :type role_definition_id: str
    :param principal_id: The principal ID.
    :type principal_id: str
    :param principal_type: The principal type of the assigned principal ID. Possible values
     include: "User", "Group", "ServicePrincipal", "Unknown", "DirectoryRoleTemplate",
     "ForeignGroup", "Application", "MSI", "DirectoryObjectOrGroup", "Everyone".
    :type principal_type: str or ~azure.mgmt.authorization.v2020_04_01_preview.models.PrincipalType
    :param can_delegate: The Delegation flag for the role assignment.
    :type can_delegate: bool
    :param description: Description of role assignment.
    :type description: str
    :param condition: The conditions on the role assignment. This limits the resources it can be
     assigned to. e.g.:
     @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName]
     StringEqualsIgnoreCase 'foo_storage_container'.
    :type condition: str
    :param condition_version: Version of the condition. Currently accepted value is '2.0'.
    :type condition_version: str
    :param created_on: Time it was created.
    :type created_on: ~datetime.datetime
    :param updated_on: Time it was updated.
    :type updated_on: ~datetime.datetime
    :param created_by: Id of the user who created the assignment.
    :type created_by: str
    :param updated_by: Id of the user who updated the assignment.
    :type updated_by: str
    :param delegated_managed_identity_resource_id: Id of the delegated managed identity resource.
    :type delegated_managed_identity_resource_id: str
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
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'role_definition_id': {'key': 'properties.roleDefinitionId', 'type': 'str'},
        'principal_id': {'key': 'properties.principalId', 'type': 'str'},
        'principal_type': {'key': 'properties.principalType', 'type': 'str'},
        'can_delegate': {'key': 'properties.canDelegate', 'type': 'bool'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'condition': {'key': 'properties.condition', 'type': 'str'},
        'condition_version': {'key': 'properties.conditionVersion', 'type': 'str'},
        'created_on': {'key': 'properties.createdOn', 'type': 'iso-8601'},
        'updated_on': {'key': 'properties.updatedOn', 'type': 'iso-8601'},
        'created_by': {'key': 'properties.createdBy', 'type': 'str'},
        'updated_by': {'key': 'properties.updatedBy', 'type': 'str'},
        'delegated_managed_identity_resource_id': {'key': 'properties.delegatedManagedIdentityResourceId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignment, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.scope = kwargs.get('scope', None)
        self.role_definition_id = kwargs.get('role_definition_id', None)
        self.principal_id = kwargs.get('principal_id', None)
        self.principal_type = kwargs.get('principal_type', None)
        self.can_delegate = kwargs.get('can_delegate', None)
        self.description = kwargs.get('description', None)
        self.condition = kwargs.get('condition', None)
        self.condition_version = kwargs.get('condition_version', None)
        self.created_on = kwargs.get('created_on', None)
        self.updated_on = kwargs.get('updated_on', None)
        self.created_by = kwargs.get('created_by', None)
        self.updated_by = kwargs.get('updated_by', None)
        self.delegated_managed_identity_resource_id = kwargs.get('delegated_managed_identity_resource_id', None)


class RoleAssignmentCreateParameters(msrest.serialization.Model):
    """Role assignment create parameters.

    All required parameters must be populated in order to send to Azure.

    :param role_definition_id: Required. The role definition ID used in the role assignment.
    :type role_definition_id: str
    :param principal_id: Required. The principal ID assigned to the role. This maps to the ID
     inside the Active Directory. It can point to a user, service principal, or security group.
    :type principal_id: str
    :param principal_type: The principal type of the assigned principal ID. Possible values
     include: "User", "Group", "ServicePrincipal", "Unknown", "DirectoryRoleTemplate",
     "ForeignGroup", "Application", "MSI", "DirectoryObjectOrGroup", "Everyone".
    :type principal_type: str or ~azure.mgmt.authorization.v2020_04_01_preview.models.PrincipalType
    :param can_delegate: The delegation flag used for creating a role assignment.
    :type can_delegate: bool
    :param description: Description of role assignment.
    :type description: str
    :param condition: The conditions on the role assignment. This limits the resources it can be
     assigned to. e.g.:
     @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName]
     StringEqualsIgnoreCase 'foo_storage_container'.
    :type condition: str
    :param condition_version: Version of the condition. Currently accepted value is '2.0'.
    :type condition_version: str
    :param delegated_managed_identity_resource_id: Id of the delegated managed identity resource.
    :type delegated_managed_identity_resource_id: str
    """

    _validation = {
        'role_definition_id': {'required': True},
        'principal_id': {'required': True},
    }

    _attribute_map = {
        'role_definition_id': {'key': 'properties.roleDefinitionId', 'type': 'str'},
        'principal_id': {'key': 'properties.principalId', 'type': 'str'},
        'principal_type': {'key': 'properties.principalType', 'type': 'str'},
        'can_delegate': {'key': 'properties.canDelegate', 'type': 'bool'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'condition': {'key': 'properties.condition', 'type': 'str'},
        'condition_version': {'key': 'properties.conditionVersion', 'type': 'str'},
        'delegated_managed_identity_resource_id': {'key': 'properties.delegatedManagedIdentityResourceId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentCreateParameters, self).__init__(**kwargs)
        self.role_definition_id = kwargs['role_definition_id']
        self.principal_id = kwargs['principal_id']
        self.principal_type = kwargs.get('principal_type', None)
        self.can_delegate = kwargs.get('can_delegate', None)
        self.description = kwargs.get('description', None)
        self.condition = kwargs.get('condition', None)
        self.condition_version = kwargs.get('condition_version', None)
        self.delegated_managed_identity_resource_id = kwargs.get('delegated_managed_identity_resource_id', None)


class RoleAssignmentFilter(msrest.serialization.Model):
    """Role Assignments filter.

    :param principal_id: Returns role assignment of the specific principal.
    :type principal_id: str
    :param can_delegate: The Delegation flag for the role assignment.
    :type can_delegate: bool
    """

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'can_delegate': {'key': 'canDelegate', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentFilter, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)
        self.can_delegate = kwargs.get('can_delegate', None)


class RoleAssignmentListResult(msrest.serialization.Model):
    """Role assignment list operation result.

    :param value: Role assignment list.
    :type value: list[~azure.mgmt.authorization.v2020_04_01_preview.models.RoleAssignment]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[RoleAssignment]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)
