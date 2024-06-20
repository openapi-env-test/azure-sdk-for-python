# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import ArmOperationStatusResourceProvisioningState
from ._models import ArmResource
from ._models import ArmResourceBase
from ._models import Asset
from ._models import AssetEndpointProfile
from ._models import AssetEndpointProfileListResult
from ._models import AssetEndpointProfileProperties
from ._models import AssetEndpointProfileUpdate
from ._models import AssetEndpointProfileUpdateProperties
from ._models import AssetListResult
from ._models import AssetProperties
from ._models import AssetStatus
from ._models import AssetStatusError
from ._models import AssetUpdate
from ._models import AssetUpdateProperties
from ._models import DataPoint
from ._models import ErrorAdditionalInfo
from ._models import ErrorDetail
from ._models import ErrorResponse
from ._models import Event
from ._models import ExtendedLocation
from ._models import Operation
from ._models import OperationDisplay
from ._models import OperationStatusResult
from ._models import OwnCertificate
from ._models import PagedOperation
from ._models import SystemData
from ._models import TrackedResourceBase
from ._models import TransportAuthentication
from ._models import UserAuthentication
from ._models import UsernamePasswordCredentials
from ._models import X509Credentials

from ._enums import ActionType
from ._enums import CreatedByType
from ._enums import DataPointsObservabilityMode
from ._enums import EventsObservabilityMode
from ._enums import Origin
from ._enums import ProvisioningState
from ._enums import ResourceProvisioningState
from ._enums import UserAuthenticationMode
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ArmOperationStatusResourceProvisioningState",
    "ArmResource",
    "ArmResourceBase",
    "Asset",
    "AssetEndpointProfile",
    "AssetEndpointProfileListResult",
    "AssetEndpointProfileProperties",
    "AssetEndpointProfileUpdate",
    "AssetEndpointProfileUpdateProperties",
    "AssetListResult",
    "AssetProperties",
    "AssetStatus",
    "AssetStatusError",
    "AssetUpdate",
    "AssetUpdateProperties",
    "DataPoint",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "Event",
    "ExtendedLocation",
    "Operation",
    "OperationDisplay",
    "OperationStatusResult",
    "OwnCertificate",
    "PagedOperation",
    "SystemData",
    "TrackedResourceBase",
    "TransportAuthentication",
    "UserAuthentication",
    "UsernamePasswordCredentials",
    "X509Credentials",
    "ActionType",
    "CreatedByType",
    "DataPointsObservabilityMode",
    "EventsObservabilityMode",
    "Origin",
    "ProvisioningState",
    "ResourceProvisioningState",
    "UserAuthenticationMode",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
