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


class AzureResourceBase(Model):
    """Common properties for all Azure resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
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

    def __init__(self, **kwargs):
        super(AzureResourceBase, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class DeploymentScript(AzureResourceBase):
    """Deployment script object.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzurePowerShellScript, AzureCliScript

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :param identity: Required. Managed identity to be used for this deployment
     script. Currently, only user-assigned MSI is supported.
    :type identity:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ManagedServiceIdentity
    :param location: Required. The location of the ACI and the storage account
     for the deployment script.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :ivar system_data: The system metadata related to this resource.
    :vartype system_data:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.SystemData
    :param kind: Required. Constant filled by server.
    :type kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'identity': {'required': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'AzurePowerShell': 'AzurePowerShellScript', 'AzureCLI': 'AzureCliScript'}
    }

    def __init__(self, **kwargs):
        super(DeploymentScript, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.system_data = None
        self.kind = None
        self.kind = 'DeploymentScript'


class AzureCliScript(DeploymentScript):
    """Object model for the Azure CLI script.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :param identity: Required. Managed identity to be used for this deployment
     script. Currently, only user-assigned MSI is supported.
    :type identity:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ManagedServiceIdentity
    :param location: Required. The location of the ACI and the storage account
     for the deployment script.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :ivar system_data: The system metadata related to this resource.
    :vartype system_data:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.SystemData
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param container_settings: Container settings.
    :type container_settings:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ContainerConfiguration
    :param cleanup_preference: The clean up preference when the script
     execution gets in a terminal state. Default setting is 'Always'. Possible
     values include: 'Always', 'OnSuccess', 'OnExpiration'
    :type cleanup_preference: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.CleanupOptions
    :ivar provisioning_state: State of the script execution. This only appears
     in the response. Possible values include: 'Creating',
     'ProvisioningResources', 'Running', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptProvisioningState
    :ivar status: Contains the results of script execution.
    :vartype status:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptStatus
    :ivar outputs: List of script outputs.
    :vartype outputs: dict[str, object]
    :param primary_script_uri: Uri for the script. This is the entry point for
     the external script.
    :type primary_script_uri: str
    :param supporting_script_uris: Supporting files for the external script.
    :type supporting_script_uris: list[str]
    :param script_content: Script body.
    :type script_content: str
    :param arguments: Command line arguments to pass to the script. Arguments
     are separated by spaces. ex: -Name blue* -Location 'West US 2'
    :type arguments: str
    :param environment_variables: The environment variables to pass over to
     the script.
    :type environment_variables:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.EnvironmentVariable]
    :param force_update_tag: Gets or sets how the deployment script should be
     forced to execute even if the script resource has not changed. Can be
     current time stamp or a GUID.
    :type force_update_tag: str
    :param retention_interval: Required. Interval for which the service
     retains the script resource after it reaches a terminal state. Resource
     will be deleted when this duration expires. Duration is based on ISO 8601
     pattern (for example P7D means one week).
    :type retention_interval: timedelta
    :param timeout: Maximum allowed script execution time specified in ISO
     8601 format. Default value is PT1H
    :type timeout: timedelta
    :param az_cli_version: Required. Azure CLI module version to be used.
    :type az_cli_version: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'identity': {'required': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
        'kind': {'required': True},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'outputs': {'readonly': True},
        'script_content': {'max_length': 32000},
        'retention_interval': {'required': True},
        'az_cli_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'kind': {'key': 'kind', 'type': 'str'},
        'container_settings': {'key': 'properties.containerSettings', 'type': 'ContainerConfiguration'},
        'cleanup_preference': {'key': 'properties.cleanupPreference', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'ScriptStatus'},
        'outputs': {'key': 'properties.outputs', 'type': '{object}'},
        'primary_script_uri': {'key': 'properties.primaryScriptUri', 'type': 'str'},
        'supporting_script_uris': {'key': 'properties.supportingScriptUris', 'type': '[str]'},
        'script_content': {'key': 'properties.scriptContent', 'type': 'str'},
        'arguments': {'key': 'properties.arguments', 'type': 'str'},
        'environment_variables': {'key': 'properties.environmentVariables', 'type': '[EnvironmentVariable]'},
        'force_update_tag': {'key': 'properties.forceUpdateTag', 'type': 'str'},
        'retention_interval': {'key': 'properties.retentionInterval', 'type': 'duration'},
        'timeout': {'key': 'properties.timeout', 'type': 'duration'},
        'az_cli_version': {'key': 'properties.azCliVersion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureCliScript, self).__init__(**kwargs)
        self.container_settings = kwargs.get('container_settings', None)
        self.cleanup_preference = kwargs.get('cleanup_preference', None)
        self.provisioning_state = None
        self.status = None
        self.outputs = None
        self.primary_script_uri = kwargs.get('primary_script_uri', None)
        self.supporting_script_uris = kwargs.get('supporting_script_uris', None)
        self.script_content = kwargs.get('script_content', None)
        self.arguments = kwargs.get('arguments', None)
        self.environment_variables = kwargs.get('environment_variables', None)
        self.force_update_tag = kwargs.get('force_update_tag', None)
        self.retention_interval = kwargs.get('retention_interval', None)
        self.timeout = kwargs.get('timeout', None)
        self.az_cli_version = kwargs.get('az_cli_version', None)
        self.kind = 'AzureCLI'


class AzurePowerShellScript(DeploymentScript):
    """Object model for the Azure PowerShell script.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :param identity: Required. Managed identity to be used for this deployment
     script. Currently, only user-assigned MSI is supported.
    :type identity:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ManagedServiceIdentity
    :param location: Required. The location of the ACI and the storage account
     for the deployment script.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :ivar system_data: The system metadata related to this resource.
    :vartype system_data:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.SystemData
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param container_settings: Container settings.
    :type container_settings:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ContainerConfiguration
    :param cleanup_preference: The clean up preference when the script
     execution gets in a terminal state. Default setting is 'Always'. Possible
     values include: 'Always', 'OnSuccess', 'OnExpiration'
    :type cleanup_preference: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.CleanupOptions
    :ivar provisioning_state: State of the script execution. This only appears
     in the response. Possible values include: 'Creating',
     'ProvisioningResources', 'Running', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptProvisioningState
    :ivar status: Contains the results of script execution.
    :vartype status:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptStatus
    :ivar outputs: List of script outputs.
    :vartype outputs: dict[str, object]
    :param primary_script_uri: Uri for the script. This is the entry point for
     the external script.
    :type primary_script_uri: str
    :param supporting_script_uris: Supporting files for the external script.
    :type supporting_script_uris: list[str]
    :param script_content: Script body.
    :type script_content: str
    :param arguments: Command line arguments to pass to the script. Arguments
     are separated by spaces. ex: -Name blue* -Location 'West US 2'
    :type arguments: str
    :param environment_variables: The environment variables to pass over to
     the script.
    :type environment_variables:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.EnvironmentVariable]
    :param force_update_tag: Gets or sets how the deployment script should be
     forced to execute even if the script resource has not changed. Can be
     current time stamp or a GUID.
    :type force_update_tag: str
    :param retention_interval: Required. Interval for which the service
     retains the script resource after it reaches a terminal state. Resource
     will be deleted when this duration expires. Duration is based on ISO 8601
     pattern (for example P7D means one week).
    :type retention_interval: timedelta
    :param timeout: Maximum allowed script execution time specified in ISO
     8601 format. Default value is PT1H
    :type timeout: timedelta
    :param az_power_shell_version: Required. Azure PowerShell module version
     to be used.
    :type az_power_shell_version: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'identity': {'required': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
        'kind': {'required': True},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'outputs': {'readonly': True},
        'script_content': {'max_length': 32000},
        'retention_interval': {'required': True},
        'az_power_shell_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'kind': {'key': 'kind', 'type': 'str'},
        'container_settings': {'key': 'properties.containerSettings', 'type': 'ContainerConfiguration'},
        'cleanup_preference': {'key': 'properties.cleanupPreference', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'ScriptStatus'},
        'outputs': {'key': 'properties.outputs', 'type': '{object}'},
        'primary_script_uri': {'key': 'properties.primaryScriptUri', 'type': 'str'},
        'supporting_script_uris': {'key': 'properties.supportingScriptUris', 'type': '[str]'},
        'script_content': {'key': 'properties.scriptContent', 'type': 'str'},
        'arguments': {'key': 'properties.arguments', 'type': 'str'},
        'environment_variables': {'key': 'properties.environmentVariables', 'type': '[EnvironmentVariable]'},
        'force_update_tag': {'key': 'properties.forceUpdateTag', 'type': 'str'},
        'retention_interval': {'key': 'properties.retentionInterval', 'type': 'duration'},
        'timeout': {'key': 'properties.timeout', 'type': 'duration'},
        'az_power_shell_version': {'key': 'properties.azPowerShellVersion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzurePowerShellScript, self).__init__(**kwargs)
        self.container_settings = kwargs.get('container_settings', None)
        self.cleanup_preference = kwargs.get('cleanup_preference', None)
        self.provisioning_state = None
        self.status = None
        self.outputs = None
        self.primary_script_uri = kwargs.get('primary_script_uri', None)
        self.supporting_script_uris = kwargs.get('supporting_script_uris', None)
        self.script_content = kwargs.get('script_content', None)
        self.arguments = kwargs.get('arguments', None)
        self.environment_variables = kwargs.get('environment_variables', None)
        self.force_update_tag = kwargs.get('force_update_tag', None)
        self.retention_interval = kwargs.get('retention_interval', None)
        self.timeout = kwargs.get('timeout', None)
        self.az_power_shell_version = kwargs.get('az_power_shell_version', None)
        self.kind = 'AzurePowerShell'


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ContainerConfiguration(Model):
    """Settings to customize ACI container instance.

    :param container_group_name: Container group name, if not specified then
     the name will get auto-generated. Not specifying a 'containerGroupName'
     indicates the system to generate a unique name which might end up flagging
     an Azure Policy as non-compliant. Use 'containerGroupName' when you have
     an Azure Policy that expects a specific naming convention or when you want
     to fully control the name. 'containerGroupName' property must be between 1
     and 63 characters long, must contain only lowercase letters, numbers, and
     dashes and it cannot start or end with a dash and consecutive dashes are
     not allowed. To specify a 'containerGroupName', add the following object
     to properties: { "containerSettings": { "containerGroupName":
     "contoso-container" } }. If you do not want to specify a
     'containerGroupName' then do not add 'containerSettings' property.
    :type container_group_name: str
    """

    _validation = {
        'container_group_name': {'max_length': 63, 'min_length': 1},
    }

    _attribute_map = {
        'container_group_name': {'key': 'containerGroupName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerConfiguration, self).__init__(**kwargs)
        self.container_group_name = kwargs.get('container_group_name', None)


class DeploymentScriptPropertiesBase(Model):
    """Common properties for the deployment script.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param container_settings: Container settings.
    :type container_settings:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ContainerConfiguration
    :param cleanup_preference: The clean up preference when the script
     execution gets in a terminal state. Default setting is 'Always'. Possible
     values include: 'Always', 'OnSuccess', 'OnExpiration'
    :type cleanup_preference: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.CleanupOptions
    :ivar provisioning_state: State of the script execution. This only appears
     in the response. Possible values include: 'Creating',
     'ProvisioningResources', 'Running', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptProvisioningState
    :ivar status: Contains the results of script execution.
    :vartype status:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptStatus
    :ivar outputs: List of script outputs.
    :vartype outputs: dict[str, object]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'outputs': {'readonly': True},
    }

    _attribute_map = {
        'container_settings': {'key': 'containerSettings', 'type': 'ContainerConfiguration'},
        'cleanup_preference': {'key': 'cleanupPreference', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'status': {'key': 'status', 'type': 'ScriptStatus'},
        'outputs': {'key': 'outputs', 'type': '{object}'},
    }

    def __init__(self, **kwargs):
        super(DeploymentScriptPropertiesBase, self).__init__(**kwargs)
        self.container_settings = kwargs.get('container_settings', None)
        self.cleanup_preference = kwargs.get('cleanup_preference', None)
        self.provisioning_state = None
        self.status = None
        self.outputs = None


class DeploymentScriptsError(Model):
    """Deployment scripts error response.

    :param error:
    :type error:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, **kwargs):
        super(DeploymentScriptsError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class DeploymentScriptsErrorException(HttpOperationError):
    """Server responsed with exception of type: 'DeploymentScriptsError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(DeploymentScriptsErrorException, self).__init__(deserialize, response, 'DeploymentScriptsError', *args)


class DeploymentScriptUpdateParameter(AzureResourceBase):
    """Deployment script parameters to be updated. .

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :param tags: Resource tags to be updated.
    :type tags: dict[str, str]
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
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(DeploymentScriptUpdateParameter, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class EnvironmentVariable(Model):
    """The environment variable to pass to the script in the container instance.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the environment variable.
    :type name: str
    :param value: The value of the environment variable.
    :type value: str
    :param secure_value: The value of the secure environment variable.
    :type secure_value: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'secure_value': {'key': 'secureValue', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EnvironmentVariable, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.value = kwargs.get('value', None)
        self.secure_value = kwargs.get('secure_value', None)


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

    def __init__(self, **kwargs):
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
    :vartype details:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ErrorAdditionalInfo]
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

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ManagedServiceIdentity(Model):
    """Managed identity generic object.

    :param type: Type of the managed identity. Possible values include:
     'UserAssigned'
    :type type: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ManagedServiceIdentityType
    :param user_assigned_identities: The list of user-assigned managed
     identities associated with the resource. Key is the Azure resource Id of
     the managed identity.
    :type user_assigned_identities: dict[str,
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.UserAssignedIdentity]
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': '{UserAssignedIdentity}'},
    }

    def __init__(self, **kwargs):
        super(ManagedServiceIdentity, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.user_assigned_identities = kwargs.get('user_assigned_identities', None)


class ScriptConfigurationBase(Model):
    """Common configuration settings for both Azure PowerShell and Azure CLI
    scripts.

    All required parameters must be populated in order to send to Azure.

    :param primary_script_uri: Uri for the script. This is the entry point for
     the external script.
    :type primary_script_uri: str
    :param supporting_script_uris: Supporting files for the external script.
    :type supporting_script_uris: list[str]
    :param script_content: Script body.
    :type script_content: str
    :param arguments: Command line arguments to pass to the script. Arguments
     are separated by spaces. ex: -Name blue* -Location 'West US 2'
    :type arguments: str
    :param environment_variables: The environment variables to pass over to
     the script.
    :type environment_variables:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.EnvironmentVariable]
    :param force_update_tag: Gets or sets how the deployment script should be
     forced to execute even if the script resource has not changed. Can be
     current time stamp or a GUID.
    :type force_update_tag: str
    :param retention_interval: Required. Interval for which the service
     retains the script resource after it reaches a terminal state. Resource
     will be deleted when this duration expires. Duration is based on ISO 8601
     pattern (for example P7D means one week).
    :type retention_interval: timedelta
    :param timeout: Maximum allowed script execution time specified in ISO
     8601 format. Default value is PT1H
    :type timeout: timedelta
    """

    _validation = {
        'script_content': {'max_length': 32000},
        'retention_interval': {'required': True},
    }

    _attribute_map = {
        'primary_script_uri': {'key': 'primaryScriptUri', 'type': 'str'},
        'supporting_script_uris': {'key': 'supportingScriptUris', 'type': '[str]'},
        'script_content': {'key': 'scriptContent', 'type': 'str'},
        'arguments': {'key': 'arguments', 'type': 'str'},
        'environment_variables': {'key': 'environmentVariables', 'type': '[EnvironmentVariable]'},
        'force_update_tag': {'key': 'forceUpdateTag', 'type': 'str'},
        'retention_interval': {'key': 'retentionInterval', 'type': 'duration'},
        'timeout': {'key': 'timeout', 'type': 'duration'},
    }

    def __init__(self, **kwargs):
        super(ScriptConfigurationBase, self).__init__(**kwargs)
        self.primary_script_uri = kwargs.get('primary_script_uri', None)
        self.supporting_script_uris = kwargs.get('supporting_script_uris', None)
        self.script_content = kwargs.get('script_content', None)
        self.arguments = kwargs.get('arguments', None)
        self.environment_variables = kwargs.get('environment_variables', None)
        self.force_update_tag = kwargs.get('force_update_tag', None)
        self.retention_interval = kwargs.get('retention_interval', None)
        self.timeout = kwargs.get('timeout', None)


class ScriptLog(AzureResourceBase):
    """Script execution log object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar log: Script execution logs in text format.
    :vartype log: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'log': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'log': {'key': 'properties.log', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ScriptLog, self).__init__(**kwargs)
        self.log = None


class ScriptLogsList(Model):
    """Deployment script execution logs.

    :param value: Deployment scripts logs.
    :type value:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptLog]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ScriptLog]'},
    }

    def __init__(self, **kwargs):
        super(ScriptLogsList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ScriptStatus(Model):
    """Generic object modeling results of script execution.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar container_instance_id: ACI resource Id.
    :vartype container_instance_id: str
    :ivar storage_account_id: Storage account resource Id.
    :vartype storage_account_id: str
    :ivar start_time: Start time of the script execution.
    :vartype start_time: datetime
    :ivar end_time: End time of the script execution.
    :vartype end_time: datetime
    :ivar expiration_time: Time the deployment script resource will expire.
    :vartype expiration_time: datetime
    :param error: Error that is relayed from the script execution.
    :type error:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ErrorResponse
    """

    _validation = {
        'container_instance_id': {'readonly': True},
        'storage_account_id': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'expiration_time': {'readonly': True},
    }

    _attribute_map = {
        'container_instance_id': {'key': 'containerInstanceId', 'type': 'str'},
        'storage_account_id': {'key': 'storageAccountId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'expiration_time': {'key': 'expirationTime', 'type': 'iso-8601'},
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, **kwargs):
        super(ScriptStatus, self).__init__(**kwargs)
        self.container_instance_id = None
        self.storage_account_id = None
        self.start_time = None
        self.end_time = None
        self.expiration_time = None
        self.error = kwargs.get('error', None)


class SystemData(Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource.
     Possible values include: 'User', 'Application', 'ManagedIdentity', 'Key'
    :type created_by_type: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the
     resource. Possible values include: 'User', 'Application',
     'ManagedIdentity', 'Key'
    :type last_modified_by_type: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.CreatedByType
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

    def __init__(self, **kwargs):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = kwargs.get('created_by', None)
        self.created_by_type = kwargs.get('created_by_type', None)
        self.created_at = kwargs.get('created_at', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.last_modified_by_type = kwargs.get('last_modified_by_type', None)
        self.last_modified_at = kwargs.get('last_modified_at', None)


class UserAssignedIdentity(Model):
    """User-assigned managed identity.

    :param principal_id: Azure Active Directory principal ID associated with
     this identity.
    :type principal_id: str
    :param client_id: Client App Id associated with this identity.
    :type client_id: str
    """

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UserAssignedIdentity, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)
        self.client_id = kwargs.get('client_id', None)
