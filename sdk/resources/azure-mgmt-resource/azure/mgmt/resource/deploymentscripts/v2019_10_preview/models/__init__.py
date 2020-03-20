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

try:
    from ._models_py3 import AzureCliScript
    from ._models_py3 import AzurePowerShellScript
    from ._models_py3 import AzureResourceBase
    from ._models_py3 import DeploymentScript
    from ._models_py3 import DeploymentScriptsError, DeploymentScriptsErrorException
    from ._models_py3 import DeploymentScriptUpdateParameter
    from ._models_py3 import EnvironmentVariable
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ManagedServiceIdentity
    from ._models_py3 import ScriptLog
    from ._models_py3 import ScriptLogsList
    from ._models_py3 import ScriptStatus
    from ._models_py3 import UserAssignedIdentity
except (SyntaxError, ImportError):
    from ._models import AzureCliScript
    from ._models import AzurePowerShellScript
    from ._models import AzureResourceBase
    from ._models import DeploymentScript
    from ._models import DeploymentScriptsError, DeploymentScriptsErrorException
    from ._models import DeploymentScriptUpdateParameter
    from ._models import EnvironmentVariable
    from ._models import ErrorAdditionalInfo
    from ._models import ErrorResponse
    from ._models import ManagedServiceIdentity
    from ._models import ScriptLog
    from ._models import ScriptLogsList
    from ._models import ScriptStatus
    from ._models import UserAssignedIdentity
from ._paged_models import DeploymentScriptPaged
from ._deployment_scripts_client_enums import (
    ManagedServiceIdentityType,
    CleanupOptions,
    ScriptProvisioningState,
)

__all__ = [
    'AzureCliScript',
    'AzurePowerShellScript',
    'AzureResourceBase',
    'DeploymentScript',
    'DeploymentScriptsError', 'DeploymentScriptsErrorException',
    'DeploymentScriptUpdateParameter',
    'EnvironmentVariable',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'ManagedServiceIdentity',
    'ScriptLog',
    'ScriptLogsList',
    'ScriptStatus',
    'UserAssignedIdentity',
    'DeploymentScriptPaged',
    'ManagedServiceIdentityType',
    'CleanupOptions',
    'ScriptProvisioningState',
]
