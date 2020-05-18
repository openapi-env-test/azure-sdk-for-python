# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import PolicyAssignment
    from ._models_py3 import PolicyAssignmentListResult
    from ._models_py3 import PolicyDefinition
    from ._models_py3 import PolicyDefinitionListResult
except (SyntaxError, ImportError):
    from ._models import PolicyAssignment  # type: ignore
    from ._models import PolicyAssignmentListResult  # type: ignore
    from ._models import PolicyDefinition  # type: ignore
    from ._models import PolicyDefinitionListResult  # type: ignore

from ._policy_client_enums import (
    PolicyType,
)

__all__ = [
    'PolicyAssignment',
    'PolicyAssignmentListResult',
    'PolicyDefinition',
    'PolicyDefinitionListResult',
    'PolicyType',
]
