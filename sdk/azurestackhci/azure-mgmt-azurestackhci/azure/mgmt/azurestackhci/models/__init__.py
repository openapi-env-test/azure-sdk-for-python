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
    from ._models_py3 import AvailableOperations
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import Cluster
    from ._models_py3 import ClusterNode
    from ._models_py3 import ClusterReportedProperties
    from ._models_py3 import ClusterUpdate
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import OperationDetail
    from ._models_py3 import OperationDisplay
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import AvailableOperations
    from ._models import AzureEntityResource
    from ._models import Cluster
    from ._models import ClusterNode
    from ._models import ClusterReportedProperties
    from ._models import ClusterUpdate
    from ._models import ErrorAdditionalInfo
    from ._models import ErrorDetail
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import OperationDetail
    from ._models import OperationDisplay
    from ._models import ProxyResource
    from ._models import Resource
    from ._models import TrackedResource
from ._paged_models import ClusterPaged
from ._azure_stack_hci_client_enums import (
    CreatedByType,
    ProvisioningState,
    Status,
)

__all__ = [
    'AvailableOperations',
    'AzureEntityResource',
    'Cluster',
    'ClusterNode',
    'ClusterReportedProperties',
    'ClusterUpdate',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse', 'ErrorResponseException',
    'OperationDetail',
    'OperationDisplay',
    'ProxyResource',
    'Resource',
    'TrackedResource',
    'ClusterPaged',
    'CreatedByType',
    'ProvisioningState',
    'Status',
]
