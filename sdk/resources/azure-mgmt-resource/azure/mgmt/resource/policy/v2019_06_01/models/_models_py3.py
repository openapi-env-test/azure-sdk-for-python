# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class ErrorResponse(_serialization.Model):
    """Error response indicates Azure Resource Manager is not able to process the incoming request. The reason is provided in the error message.

    :ivar http_status: Http status code.
    :vartype http_status: str
    :ivar error_code: Error code.
    :vartype error_code: str
    :ivar error_message: Error message indicating why the operation failed.
    :vartype error_message: str
    """

    _attribute_map = {
        "http_status": {"key": "httpStatus", "type": "str"},
        "error_code": {"key": "errorCode", "type": "str"},
        "error_message": {"key": "errorMessage", "type": "str"},
    }

    def __init__(
        self,
        *,
        http_status: Optional[str] = None,
        error_code: Optional[str] = None,
        error_message: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword http_status: Http status code.
        :paramtype http_status: str
        :keyword error_code: Error code.
        :paramtype error_code: str
        :keyword error_message: Error message indicating why the operation failed.
        :paramtype error_message: str
        """
        super().__init__(**kwargs)
        self.http_status = http_status
        self.error_code = error_code
        self.error_message = error_message


class Identity(_serialization.Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of the resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the resource identity.
    :vartype tenant_id: str
    :ivar type: The identity type. Known values are: "SystemAssigned" and "None".
    :vartype type: str or ~azure.mgmt.resource.policy.v2019_06_01.models.ResourceIdentityType
    """

    _validation = {
        "principal_id": {"readonly": True},
        "tenant_id": {"readonly": True},
    }

    _attribute_map = {
        "principal_id": {"key": "principalId", "type": "str"},
        "tenant_id": {"key": "tenantId", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, *, type: Optional[Union[str, "_models.ResourceIdentityType"]] = None, **kwargs):
        """
        :keyword type: The identity type. Known values are: "SystemAssigned" and "None".
        :paramtype type: str or ~azure.mgmt.resource.policy.v2019_06_01.models.ResourceIdentityType
        """
        super().__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class PolicyAssignment(_serialization.Model):  # pylint: disable=too-many-instance-attributes
    """The policy assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy assignment.
    :vartype id: str
    :ivar type: The type of the policy assignment.
    :vartype type: str
    :ivar name: The name of the policy assignment.
    :vartype name: str
    :ivar sku: The policy sku. This property is optional, obsolete, and will be ignored.
    :vartype sku: ~azure.mgmt.resource.policy.v2019_06_01.models.PolicySku
    :ivar location: The location of the policy assignment. Only required when utilizing managed
     identity.
    :vartype location: str
    :ivar identity: The managed identity associated with the policy assignment.
    :vartype identity: ~azure.mgmt.resource.policy.v2019_06_01.models.Identity
    :ivar display_name: The display name of the policy assignment.
    :vartype display_name: str
    :ivar policy_definition_id: The ID of the policy definition or policy set definition being
     assigned.
    :vartype policy_definition_id: str
    :ivar scope: The scope for the policy assignment.
    :vartype scope: str
    :ivar not_scopes: The policy's excluded scopes.
    :vartype not_scopes: list[str]
    :ivar parameters: Required if a parameter is used in policy rule.
    :vartype parameters: JSON
    :ivar description: This message will be part of response in case of policy violation.
    :vartype description: str
    :ivar metadata: The policy assignment metadata.
    :vartype metadata: JSON
    :ivar enforcement_mode: The policy assignment enforcement mode. Possible values are Default and
     DoNotEnforce. Known values are: "Default" and "DoNotEnforce".
    :vartype enforcement_mode: str or
     ~azure.mgmt.resource.policy.v2019_06_01.models.EnforcementMode
    """

    _validation = {
        "id": {"readonly": True},
        "type": {"readonly": True},
        "name": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "sku": {"key": "sku", "type": "PolicySku"},
        "location": {"key": "location", "type": "str"},
        "identity": {"key": "identity", "type": "Identity"},
        "display_name": {"key": "properties.displayName", "type": "str"},
        "policy_definition_id": {"key": "properties.policyDefinitionId", "type": "str"},
        "scope": {"key": "properties.scope", "type": "str"},
        "not_scopes": {"key": "properties.notScopes", "type": "[str]"},
        "parameters": {"key": "properties.parameters", "type": "object"},
        "description": {"key": "properties.description", "type": "str"},
        "metadata": {"key": "properties.metadata", "type": "object"},
        "enforcement_mode": {"key": "properties.enforcementMode", "type": "str"},
    }

    def __init__(
        self,
        *,
        sku: Optional["_models.PolicySku"] = None,
        location: Optional[str] = None,
        identity: Optional["_models.Identity"] = None,
        display_name: Optional[str] = None,
        policy_definition_id: Optional[str] = None,
        scope: Optional[str] = None,
        not_scopes: Optional[List[str]] = None,
        parameters: Optional[JSON] = None,
        description: Optional[str] = None,
        metadata: Optional[JSON] = None,
        enforcement_mode: Optional[Union[str, "_models.EnforcementMode"]] = None,
        **kwargs
    ):
        """
        :keyword sku: The policy sku. This property is optional, obsolete, and will be ignored.
        :paramtype sku: ~azure.mgmt.resource.policy.v2019_06_01.models.PolicySku
        :keyword location: The location of the policy assignment. Only required when utilizing managed
         identity.
        :paramtype location: str
        :keyword identity: The managed identity associated with the policy assignment.
        :paramtype identity: ~azure.mgmt.resource.policy.v2019_06_01.models.Identity
        :keyword display_name: The display name of the policy assignment.
        :paramtype display_name: str
        :keyword policy_definition_id: The ID of the policy definition or policy set definition being
         assigned.
        :paramtype policy_definition_id: str
        :keyword scope: The scope for the policy assignment.
        :paramtype scope: str
        :keyword not_scopes: The policy's excluded scopes.
        :paramtype not_scopes: list[str]
        :keyword parameters: Required if a parameter is used in policy rule.
        :paramtype parameters: JSON
        :keyword description: This message will be part of response in case of policy violation.
        :paramtype description: str
        :keyword metadata: The policy assignment metadata.
        :paramtype metadata: JSON
        :keyword enforcement_mode: The policy assignment enforcement mode. Possible values are Default
         and DoNotEnforce. Known values are: "Default" and "DoNotEnforce".
        :paramtype enforcement_mode: str or
         ~azure.mgmt.resource.policy.v2019_06_01.models.EnforcementMode
        """
        super().__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.sku = sku
        self.location = location
        self.identity = identity
        self.display_name = display_name
        self.policy_definition_id = policy_definition_id
        self.scope = scope
        self.not_scopes = not_scopes
        self.parameters = parameters
        self.description = description
        self.metadata = metadata
        self.enforcement_mode = enforcement_mode


class PolicyAssignmentListResult(_serialization.Model):
    """List of policy assignments.

    :ivar value: An array of policy assignments.
    :vartype value: list[~azure.mgmt.resource.policy.v2019_06_01.models.PolicyAssignment]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[PolicyAssignment]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.PolicyAssignment"]] = None, next_link: Optional[str] = None, **kwargs
    ):
        """
        :keyword value: An array of policy assignments.
        :paramtype value: list[~azure.mgmt.resource.policy.v2019_06_01.models.PolicyAssignment]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PolicyDefinition(_serialization.Model):
    """The policy definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy definition.
    :vartype id: str
    :ivar name: The name of the policy definition.
    :vartype name: str
    :ivar type: The type of the resource (Microsoft.Authorization/policyDefinitions).
    :vartype type: str
    :ivar policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
     and Custom. Known values are: "NotSpecified", "BuiltIn", and "Custom".
    :vartype policy_type: str or ~azure.mgmt.resource.policy.v2019_06_01.models.PolicyType
    :ivar mode: The policy definition mode. Some examples are All, Indexed,
     Microsoft.KeyVault.Data.
    :vartype mode: str
    :ivar display_name: The display name of the policy definition.
    :vartype display_name: str
    :ivar description: The policy definition description.
    :vartype description: str
    :ivar policy_rule: The policy rule.
    :vartype policy_rule: JSON
    :ivar metadata: The policy definition metadata.
    :vartype metadata: JSON
    :ivar parameters: Required if a parameter is used in policy rule.
    :vartype parameters: JSON
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "policy_type": {"key": "properties.policyType", "type": "str"},
        "mode": {"key": "properties.mode", "type": "str"},
        "display_name": {"key": "properties.displayName", "type": "str"},
        "description": {"key": "properties.description", "type": "str"},
        "policy_rule": {"key": "properties.policyRule", "type": "object"},
        "metadata": {"key": "properties.metadata", "type": "object"},
        "parameters": {"key": "properties.parameters", "type": "object"},
    }

    def __init__(
        self,
        *,
        policy_type: Optional[Union[str, "_models.PolicyType"]] = None,
        mode: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        policy_rule: Optional[JSON] = None,
        metadata: Optional[JSON] = None,
        parameters: Optional[JSON] = None,
        **kwargs
    ):
        """
        :keyword policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
         and Custom. Known values are: "NotSpecified", "BuiltIn", and "Custom".
        :paramtype policy_type: str or ~azure.mgmt.resource.policy.v2019_06_01.models.PolicyType
        :keyword mode: The policy definition mode. Some examples are All, Indexed,
         Microsoft.KeyVault.Data.
        :paramtype mode: str
        :keyword display_name: The display name of the policy definition.
        :paramtype display_name: str
        :keyword description: The policy definition description.
        :paramtype description: str
        :keyword policy_rule: The policy rule.
        :paramtype policy_rule: JSON
        :keyword metadata: The policy definition metadata.
        :paramtype metadata: JSON
        :keyword parameters: Required if a parameter is used in policy rule.
        :paramtype parameters: JSON
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.policy_type = policy_type
        self.mode = mode
        self.display_name = display_name
        self.description = description
        self.policy_rule = policy_rule
        self.metadata = metadata
        self.parameters = parameters


class PolicyDefinitionListResult(_serialization.Model):
    """List of policy definitions.

    :ivar value: An array of policy definitions.
    :vartype value: list[~azure.mgmt.resource.policy.v2019_06_01.models.PolicyDefinition]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[PolicyDefinition]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.PolicyDefinition"]] = None, next_link: Optional[str] = None, **kwargs
    ):
        """
        :keyword value: An array of policy definitions.
        :paramtype value: list[~azure.mgmt.resource.policy.v2019_06_01.models.PolicyDefinition]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PolicyDefinitionReference(_serialization.Model):
    """The policy definition reference.

    :ivar policy_definition_id: The ID of the policy definition or policy set definition.
    :vartype policy_definition_id: str
    :ivar parameters: Required if a parameter is used in policy rule.
    :vartype parameters: JSON
    """

    _attribute_map = {
        "policy_definition_id": {"key": "policyDefinitionId", "type": "str"},
        "parameters": {"key": "parameters", "type": "object"},
    }

    def __init__(self, *, policy_definition_id: Optional[str] = None, parameters: Optional[JSON] = None, **kwargs):
        """
        :keyword policy_definition_id: The ID of the policy definition or policy set definition.
        :paramtype policy_definition_id: str
        :keyword parameters: Required if a parameter is used in policy rule.
        :paramtype parameters: JSON
        """
        super().__init__(**kwargs)
        self.policy_definition_id = policy_definition_id
        self.parameters = parameters


class PolicySetDefinition(_serialization.Model):
    """The policy set definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy set definition.
    :vartype id: str
    :ivar name: The name of the policy set definition.
    :vartype name: str
    :ivar type: The type of the resource (Microsoft.Authorization/policySetDefinitions).
    :vartype type: str
    :ivar policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
     and Custom. Known values are: "NotSpecified", "BuiltIn", and "Custom".
    :vartype policy_type: str or ~azure.mgmt.resource.policy.v2019_06_01.models.PolicyType
    :ivar display_name: The display name of the policy set definition.
    :vartype display_name: str
    :ivar description: The policy set definition description.
    :vartype description: str
    :ivar metadata: The policy set definition metadata.
    :vartype metadata: JSON
    :ivar parameters: The policy set definition parameters that can be used in policy definition
     references.
    :vartype parameters: JSON
    :ivar policy_definitions: An array of policy definition references.
    :vartype policy_definitions:
     list[~azure.mgmt.resource.policy.v2019_06_01.models.PolicyDefinitionReference]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "policy_type": {"key": "properties.policyType", "type": "str"},
        "display_name": {"key": "properties.displayName", "type": "str"},
        "description": {"key": "properties.description", "type": "str"},
        "metadata": {"key": "properties.metadata", "type": "object"},
        "parameters": {"key": "properties.parameters", "type": "object"},
        "policy_definitions": {"key": "properties.policyDefinitions", "type": "[PolicyDefinitionReference]"},
    }

    def __init__(
        self,
        *,
        policy_type: Optional[Union[str, "_models.PolicyType"]] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[JSON] = None,
        parameters: Optional[JSON] = None,
        policy_definitions: Optional[List["_models.PolicyDefinitionReference"]] = None,
        **kwargs
    ):
        """
        :keyword policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
         and Custom. Known values are: "NotSpecified", "BuiltIn", and "Custom".
        :paramtype policy_type: str or ~azure.mgmt.resource.policy.v2019_06_01.models.PolicyType
        :keyword display_name: The display name of the policy set definition.
        :paramtype display_name: str
        :keyword description: The policy set definition description.
        :paramtype description: str
        :keyword metadata: The policy set definition metadata.
        :paramtype metadata: JSON
        :keyword parameters: The policy set definition parameters that can be used in policy definition
         references.
        :paramtype parameters: JSON
        :keyword policy_definitions: An array of policy definition references.
        :paramtype policy_definitions:
         list[~azure.mgmt.resource.policy.v2019_06_01.models.PolicyDefinitionReference]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.policy_type = policy_type
        self.display_name = display_name
        self.description = description
        self.metadata = metadata
        self.parameters = parameters
        self.policy_definitions = policy_definitions


class PolicySetDefinitionListResult(_serialization.Model):
    """List of policy set definitions.

    :ivar value: An array of policy set definitions.
    :vartype value: list[~azure.mgmt.resource.policy.v2019_06_01.models.PolicySetDefinition]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[PolicySetDefinition]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.PolicySetDefinition"]] = None, next_link: Optional[str] = None, **kwargs
    ):
        """
        :keyword value: An array of policy set definitions.
        :paramtype value: list[~azure.mgmt.resource.policy.v2019_06_01.models.PolicySetDefinition]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PolicySku(_serialization.Model):
    """The policy sku. This property is optional, obsolete, and will be ignored.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The name of the policy sku. Possible values are A0 and A1. Required.
    :vartype name: str
    :ivar tier: The policy sku tier. Possible values are Free and Standard.
    :vartype tier: str
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "tier": {"key": "tier", "type": "str"},
    }

    def __init__(self, *, name: str, tier: Optional[str] = None, **kwargs):
        """
        :keyword name: The name of the policy sku. Possible values are A0 and A1. Required.
        :paramtype name: str
        :keyword tier: The policy sku tier. Possible values are Free and Standard.
        :paramtype tier: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.tier = tier
