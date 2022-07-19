# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._namespaces_operations import NamespacesOperations
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._private_link_resources_operations import PrivateLinkResourcesOperations
from ._operations import Operations
from ._event_hubs_operations import EventHubsOperations
from ._disaster_recovery_configs_operations import DisasterRecoveryConfigsOperations
from ._consumer_groups_operations import ConsumerGroupsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "NamespacesOperations",
    "PrivateEndpointConnectionsOperations",
    "PrivateLinkResourcesOperations",
    "Operations",
    "EventHubsOperations",
    "DisasterRecoveryConfigsOperations",
    "ConsumerGroupsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
