# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import Alias
from ._models_py3 import AliasPath
from ._models_py3 import AliasPathMetadata
from ._models_py3 import AliasPattern
from ._models_py3 import DataEffect
from ._models_py3 import DataManifestCustomResourceFunctionDefinition
from ._models_py3 import DataPolicyManifest
from ._models_py3 import DataPolicyManifestListResult
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorResponse
from ._models_py3 import Identity
from ._models_py3 import NonComplianceMessage
from ._models_py3 import ParameterDefinitionsValue
from ._models_py3 import ParameterDefinitionsValueMetadata
from ._models_py3 import ParameterValuesValue
from ._models_py3 import PolicyAssignment
from ._models_py3 import PolicyAssignmentListResult
from ._models_py3 import PolicyDefinition
from ._models_py3 import PolicyDefinitionGroup
from ._models_py3 import PolicyDefinitionListResult
from ._models_py3 import PolicyDefinitionReference
from ._models_py3 import PolicyExemption
from ._models_py3 import PolicyExemptionListResult
from ._models_py3 import PolicySetDefinition
from ._models_py3 import PolicySetDefinitionListResult
from ._models_py3 import ResourceTypeAliases
from ._models_py3 import SystemData

from ._policy_client_enums import AliasPathAttributes
from ._policy_client_enums import AliasPathTokenType
from ._policy_client_enums import AliasPatternType
from ._policy_client_enums import AliasType
from ._policy_client_enums import CreatedByType
from ._policy_client_enums import EnforcementMode
from ._policy_client_enums import ExemptionCategory
from ._policy_client_enums import ParameterType
from ._policy_client_enums import PolicyType
from ._policy_client_enums import ResourceIdentityType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Alias",
    "AliasPath",
    "AliasPathMetadata",
    "AliasPattern",
    "DataEffect",
    "DataManifestCustomResourceFunctionDefinition",
    "DataPolicyManifest",
    "DataPolicyManifestListResult",
    "ErrorAdditionalInfo",
    "ErrorResponse",
    "Identity",
    "NonComplianceMessage",
    "ParameterDefinitionsValue",
    "ParameterDefinitionsValueMetadata",
    "ParameterValuesValue",
    "PolicyAssignment",
    "PolicyAssignmentListResult",
    "PolicyDefinition",
    "PolicyDefinitionGroup",
    "PolicyDefinitionListResult",
    "PolicyDefinitionReference",
    "PolicyExemption",
    "PolicyExemptionListResult",
    "PolicySetDefinition",
    "PolicySetDefinitionListResult",
    "ResourceTypeAliases",
    "SystemData",
    "AliasPathAttributes",
    "AliasPathTokenType",
    "AliasPatternType",
    "AliasType",
    "CreatedByType",
    "EnforcementMode",
    "ExemptionCategory",
    "ParameterType",
    "PolicyType",
    "ResourceIdentityType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
