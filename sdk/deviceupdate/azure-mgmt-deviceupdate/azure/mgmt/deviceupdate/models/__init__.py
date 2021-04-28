# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Account
    from ._models_py3 import AccountList
    from ._models_py3 import AccountUpdate
    from ._models_py3 import CheckNameAvailabilityRequest
    from ._models_py3 import CheckNameAvailabilityResponse
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import Identity
    from ._models_py3 import Instance
    from ._models_py3 import InstanceList
    from ._models_py3 import IotHubSettings
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import Resource
    from ._models_py3 import SystemData
    from ._models_py3 import TagUpdate
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import Account  # type: ignore
    from ._models import AccountList  # type: ignore
    from ._models import AccountUpdate  # type: ignore
    from ._models import CheckNameAvailabilityRequest  # type: ignore
    from ._models import CheckNameAvailabilityResponse  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import Instance  # type: ignore
    from ._models import InstanceList  # type: ignore
    from ._models import IotHubSettings  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TagUpdate  # type: ignore
    from ._models import TrackedResource  # type: ignore

from ._device_update_enums import (
    ActionType,
    CheckNameAvailabilityReason,
    CreatedByType,
    Origin,
    ProvisioningState,
    ResourceIdentityType,
)

__all__ = [
    'Account',
    'AccountList',
    'AccountUpdate',
    'CheckNameAvailabilityRequest',
    'CheckNameAvailabilityResponse',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'Identity',
    'Instance',
    'InstanceList',
    'IotHubSettings',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'Resource',
    'SystemData',
    'TagUpdate',
    'TrackedResource',
    'ActionType',
    'CheckNameAvailabilityReason',
    'CreatedByType',
    'Origin',
    'ProvisioningState',
    'ResourceIdentityType',
]
