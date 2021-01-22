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
    from ._models_py3 import Activity
    from ._models_py3 import ActivityOutputType
    from ._models_py3 import ActivityParameter
    from ._models_py3 import ActivityParameterSet
    from ._models_py3 import ActivityParameterValidationSet
    from ._models_py3 import AdvancedSchedule
    from ._models_py3 import AdvancedScheduleMonthlyOccurrence
    from ._models_py3 import AgentRegistration
    from ._models_py3 import AgentRegistrationKeys
    from ._models_py3 import AgentRegistrationRegenerateKeyParameter
    from ._models_py3 import AutomationAccount
    from ._models_py3 import AutomationAccountCreateOrUpdateParameters
    from ._models_py3 import AutomationAccountUpdateParameters
    from ._models_py3 import Certificate
    from ._models_py3 import CertificateCreateOrUpdateParameters
    from ._models_py3 import CertificateUpdateParameters
    from ._models_py3 import Connection
    from ._models_py3 import ConnectionCreateOrUpdateParameters
    from ._models_py3 import ConnectionType
    from ._models_py3 import ConnectionTypeAssociationProperty
    from ._models_py3 import ConnectionTypeCreateOrUpdateParameters
    from ._models_py3 import ConnectionUpdateParameters
    from ._models_py3 import ContentHash
    from ._models_py3 import ContentLink
    from ._models_py3 import ContentSource
    from ._models_py3 import Credential
    from ._models_py3 import CredentialCreateOrUpdateParameters
    from ._models_py3 import CredentialUpdateParameters
    from ._models_py3 import DscCompilationJob
    from ._models_py3 import DscCompilationJobCreateParameters
    from ._models_py3 import DscConfiguration
    from ._models_py3 import DscConfigurationAssociationProperty
    from ._models_py3 import DscConfigurationCreateOrUpdateParameters
    from ._models_py3 import DscConfigurationParameter
    from ._models_py3 import DscConfigurationUpdateParameters
    from ._models_py3 import DscMetaConfiguration
    from ._models_py3 import DscNode
    from ._models_py3 import DscNodeConfiguration
    from ._models_py3 import DscNodeConfigurationCreateOrUpdateParameters
    from ._models_py3 import DscNodeExtensionHandlerAssociationProperty
    from ._models_py3 import DscNodeReport
    from ._models_py3 import DscNodeUpdateParameters
    from ._models_py3 import DscNodeUpdateParametersProperties
    from ._models_py3 import DscReportError
    from ._models_py3 import DscReportResource
    from ._models_py3 import DscReportResourceNavigation
    from ._models_py3 import EncryptionProperties
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import FieldDefinition
    from ._models_py3 import HybridRunbookWorker
    from ._models_py3 import HybridRunbookWorkerGroup
    from ._models_py3 import HybridRunbookWorkerGroupUpdateParameters
    from ._models_py3 import Identity
    from ._models_py3 import Job
    from ._models_py3 import JobCollectionItem
    from ._models_py3 import JobCreateParameters
    from ._models_py3 import JobNavigation
    from ._models_py3 import JobSchedule
    from ._models_py3 import JobScheduleCreateParameters
    from ._models_py3 import JobStream
    from ._models_py3 import JobStreamListResult
    from ._models_py3 import Key
    from ._models_py3 import KeyListResult
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import LinkedWorkspace
    from ._models_py3 import Module
    from ._models_py3 import ModuleCreateOrUpdateParameters
    from ._models_py3 import ModuleErrorInfo
    from ._models_py3 import ModuleUpdateParameters
    from ._models_py3 import NodeCount
    from ._models_py3 import NodeCountProperties
    from ._models_py3 import NodeCounts
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointProperty
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkServiceConnectionStateProperty
    from ._models_py3 import ProxyResource
    from ._models_py3 import PythonPackageCreateParameters
    from ._models_py3 import PythonPackageUpdateParameters
    from ._models_py3 import Resource
    from ._models_py3 import RunAsCredentialAssociationProperty
    from ._models_py3 import Runbook
    from ._models_py3 import RunbookAssociationProperty
    from ._models_py3 import RunbookCreateOrUpdateDraftParameters
    from ._models_py3 import RunbookCreateOrUpdateDraftProperties
    from ._models_py3 import RunbookCreateOrUpdateParameters
    from ._models_py3 import RunbookDraft
    from ._models_py3 import RunbookDraftUndoEditResult
    from ._models_py3 import RunbookParameter
    from ._models_py3 import RunbookUpdateParameters
    from ._models_py3 import Schedule
    from ._models_py3 import ScheduleAssociationProperty
    from ._models_py3 import ScheduleCreateOrUpdateParameters
    from ._models_py3 import ScheduleUpdateParameters
    from ._models_py3 import Sku
    from ._models_py3 import SoftwareUpdateConfigurationMachineRun
    from ._models_py3 import SoftwareUpdateConfigurationMachineRunListResult
    from ._models_py3 import SoftwareUpdateConfigurationRun
    from ._models_py3 import SoftwareUpdateConfigurationRunListResult
    from ._models_py3 import SoftwareUpdateConfigurationRunTaskProperties
    from ._models_py3 import SoftwareUpdateConfigurationRunTasks
    from ._models_py3 import SourceControl
    from ._models_py3 import SourceControlCreateOrUpdateParameters
    from ._models_py3 import SourceControlSecurityTokenProperties
    from ._models_py3 import SourceControlSyncJob
    from ._models_py3 import SourceControlSyncJobById
    from ._models_py3 import SourceControlSyncJobCreateParameters
    from ._models_py3 import SourceControlSyncJobStream
    from ._models_py3 import SourceControlSyncJobStreamById
    from ._models_py3 import SourceControlUpdateParameters
    from ._models_py3 import Statistics
    from ._models_py3 import TestJob
    from ._models_py3 import TestJobCreateParameters
    from ._models_py3 import TrackedResource
    from ._models_py3 import TypeField
    from ._models_py3 import UpdateConfigurationNavigation
    from ._models_py3 import Usage
    from ._models_py3 import UsageCounterName
    from ._models_py3 import Variable
    from ._models_py3 import VariableCreateOrUpdateParameters
    from ._models_py3 import VariableUpdateParameters
    from ._models_py3 import Watcher
    from ._models_py3 import WatcherUpdateParameters
    from ._models_py3 import Webhook
    from ._models_py3 import WebhookCreateOrUpdateParameters
    from ._models_py3 import WebhookUpdateParameters
except (SyntaxError, ImportError):
    from ._models import Activity
    from ._models import ActivityOutputType
    from ._models import ActivityParameter
    from ._models import ActivityParameterSet
    from ._models import ActivityParameterValidationSet
    from ._models import AdvancedSchedule
    from ._models import AdvancedScheduleMonthlyOccurrence
    from ._models import AgentRegistration
    from ._models import AgentRegistrationKeys
    from ._models import AgentRegistrationRegenerateKeyParameter
    from ._models import AutomationAccount
    from ._models import AutomationAccountCreateOrUpdateParameters
    from ._models import AutomationAccountUpdateParameters
    from ._models import Certificate
    from ._models import CertificateCreateOrUpdateParameters
    from ._models import CertificateUpdateParameters
    from ._models import Connection
    from ._models import ConnectionCreateOrUpdateParameters
    from ._models import ConnectionType
    from ._models import ConnectionTypeAssociationProperty
    from ._models import ConnectionTypeCreateOrUpdateParameters
    from ._models import ConnectionUpdateParameters
    from ._models import ContentHash
    from ._models import ContentLink
    from ._models import ContentSource
    from ._models import Credential
    from ._models import CredentialCreateOrUpdateParameters
    from ._models import CredentialUpdateParameters
    from ._models import DscCompilationJob
    from ._models import DscCompilationJobCreateParameters
    from ._models import DscConfiguration
    from ._models import DscConfigurationAssociationProperty
    from ._models import DscConfigurationCreateOrUpdateParameters
    from ._models import DscConfigurationParameter
    from ._models import DscConfigurationUpdateParameters
    from ._models import DscMetaConfiguration
    from ._models import DscNode
    from ._models import DscNodeConfiguration
    from ._models import DscNodeConfigurationCreateOrUpdateParameters
    from ._models import DscNodeExtensionHandlerAssociationProperty
    from ._models import DscNodeReport
    from ._models import DscNodeUpdateParameters
    from ._models import DscNodeUpdateParametersProperties
    from ._models import DscReportError
    from ._models import DscReportResource
    from ._models import DscReportResourceNavigation
    from ._models import EncryptionProperties
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import FieldDefinition
    from ._models import HybridRunbookWorker
    from ._models import HybridRunbookWorkerGroup
    from ._models import HybridRunbookWorkerGroupUpdateParameters
    from ._models import Identity
    from ._models import Job
    from ._models import JobCollectionItem
    from ._models import JobCreateParameters
    from ._models import JobNavigation
    from ._models import JobSchedule
    from ._models import JobScheduleCreateParameters
    from ._models import JobStream
    from ._models import JobStreamListResult
    from ._models import Key
    from ._models import KeyListResult
    from ._models import KeyVaultProperties
    from ._models import LinkedWorkspace
    from ._models import Module
    from ._models import ModuleCreateOrUpdateParameters
    from ._models import ModuleErrorInfo
    from ._models import ModuleUpdateParameters
    from ._models import NodeCount
    from ._models import NodeCountProperties
    from ._models import NodeCounts
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import PrivateEndpointConnection
    from ._models import PrivateEndpointProperty
    from ._models import PrivateLinkResource
    from ._models import PrivateLinkServiceConnectionStateProperty
    from ._models import ProxyResource
    from ._models import PythonPackageCreateParameters
    from ._models import PythonPackageUpdateParameters
    from ._models import Resource
    from ._models import RunAsCredentialAssociationProperty
    from ._models import Runbook
    from ._models import RunbookAssociationProperty
    from ._models import RunbookCreateOrUpdateDraftParameters
    from ._models import RunbookCreateOrUpdateDraftProperties
    from ._models import RunbookCreateOrUpdateParameters
    from ._models import RunbookDraft
    from ._models import RunbookDraftUndoEditResult
    from ._models import RunbookParameter
    from ._models import RunbookUpdateParameters
    from ._models import Schedule
    from ._models import ScheduleAssociationProperty
    from ._models import ScheduleCreateOrUpdateParameters
    from ._models import ScheduleUpdateParameters
    from ._models import Sku
    from ._models import SoftwareUpdateConfigurationMachineRun
    from ._models import SoftwareUpdateConfigurationMachineRunListResult
    from ._models import SoftwareUpdateConfigurationRun
    from ._models import SoftwareUpdateConfigurationRunListResult
    from ._models import SoftwareUpdateConfigurationRunTaskProperties
    from ._models import SoftwareUpdateConfigurationRunTasks
    from ._models import SourceControl
    from ._models import SourceControlCreateOrUpdateParameters
    from ._models import SourceControlSecurityTokenProperties
    from ._models import SourceControlSyncJob
    from ._models import SourceControlSyncJobById
    from ._models import SourceControlSyncJobCreateParameters
    from ._models import SourceControlSyncJobStream
    from ._models import SourceControlSyncJobStreamById
    from ._models import SourceControlUpdateParameters
    from ._models import Statistics
    from ._models import TestJob
    from ._models import TestJobCreateParameters
    from ._models import TrackedResource
    from ._models import TypeField
    from ._models import UpdateConfigurationNavigation
    from ._models import Usage
    from ._models import UsageCounterName
    from ._models import Variable
    from ._models import VariableCreateOrUpdateParameters
    from ._models import VariableUpdateParameters
    from ._models import Watcher
    from ._models import WatcherUpdateParameters
    from ._models import Webhook
    from ._models import WebhookCreateOrUpdateParameters
    from ._models import WebhookUpdateParameters
from ._paged_models import ActivityPaged
from ._paged_models import AutomationAccountPaged
from ._paged_models import CertificatePaged
from ._paged_models import ConnectionPaged
from ._paged_models import ConnectionTypePaged
from ._paged_models import CredentialPaged
from ._paged_models import DscCompilationJobPaged
from ._paged_models import DscConfigurationPaged
from ._paged_models import DscNodeConfigurationPaged
from ._paged_models import DscNodePaged
from ._paged_models import DscNodeReportPaged
from ._paged_models import HybridRunbookWorkerGroupPaged
from ._paged_models import JobCollectionItemPaged
from ._paged_models import JobSchedulePaged
from ._paged_models import JobStreamPaged
from ._paged_models import ModulePaged
from ._paged_models import OperationPaged
from ._paged_models import PrivateEndpointConnectionPaged
from ._paged_models import PrivateLinkResourcePaged
from ._paged_models import RunbookPaged
from ._paged_models import SchedulePaged
from ._paged_models import SourceControlPaged
from ._paged_models import SourceControlSyncJobPaged
from ._paged_models import SourceControlSyncJobStreamPaged
from ._paged_models import StatisticsPaged
from ._paged_models import TypeFieldPaged
from ._paged_models import UsagePaged
from ._paged_models import VariablePaged
from ._paged_models import WatcherPaged
from ._paged_models import WebhookPaged
from ._automation_client_enums import (
    ModuleProvisioningState,
    AgentRegistrationKeyName,
    ContentSourceType,
    JobProvisioningState,
    JobStatus,
    JobStreamType,
    SourceType,
    TokenType,
    ProvisioningState,
    SyncType,
    StreamType,
    SkuNameEnum,
    AutomationAccountState,
    EncryptionKeySourceType,
    ResourceIdentityType,
    AutomationKeyName,
    AutomationKeyPermissions,
    GroupTypeEnum,
    ScheduleDay,
    ScheduleFrequency,
    DscConfigurationProvisioningState,
    DscConfigurationState,
    RunbookTypeEnum,
    RunbookState,
    RunbookProvisioningState,
    HttpStatusCode,
    CountType,
)

__all__ = [
    'Activity',
    'ActivityOutputType',
    'ActivityParameter',
    'ActivityParameterSet',
    'ActivityParameterValidationSet',
    'AdvancedSchedule',
    'AdvancedScheduleMonthlyOccurrence',
    'AgentRegistration',
    'AgentRegistrationKeys',
    'AgentRegistrationRegenerateKeyParameter',
    'AutomationAccount',
    'AutomationAccountCreateOrUpdateParameters',
    'AutomationAccountUpdateParameters',
    'Certificate',
    'CertificateCreateOrUpdateParameters',
    'CertificateUpdateParameters',
    'Connection',
    'ConnectionCreateOrUpdateParameters',
    'ConnectionType',
    'ConnectionTypeAssociationProperty',
    'ConnectionTypeCreateOrUpdateParameters',
    'ConnectionUpdateParameters',
    'ContentHash',
    'ContentLink',
    'ContentSource',
    'Credential',
    'CredentialCreateOrUpdateParameters',
    'CredentialUpdateParameters',
    'DscCompilationJob',
    'DscCompilationJobCreateParameters',
    'DscConfiguration',
    'DscConfigurationAssociationProperty',
    'DscConfigurationCreateOrUpdateParameters',
    'DscConfigurationParameter',
    'DscConfigurationUpdateParameters',
    'DscMetaConfiguration',
    'DscNode',
    'DscNodeConfiguration',
    'DscNodeConfigurationCreateOrUpdateParameters',
    'DscNodeExtensionHandlerAssociationProperty',
    'DscNodeReport',
    'DscNodeUpdateParameters',
    'DscNodeUpdateParametersProperties',
    'DscReportError',
    'DscReportResource',
    'DscReportResourceNavigation',
    'EncryptionProperties',
    'ErrorResponse', 'ErrorResponseException',
    'FieldDefinition',
    'HybridRunbookWorker',
    'HybridRunbookWorkerGroup',
    'HybridRunbookWorkerGroupUpdateParameters',
    'Identity',
    'Job',
    'JobCollectionItem',
    'JobCreateParameters',
    'JobNavigation',
    'JobSchedule',
    'JobScheduleCreateParameters',
    'JobStream',
    'JobStreamListResult',
    'Key',
    'KeyListResult',
    'KeyVaultProperties',
    'LinkedWorkspace',
    'Module',
    'ModuleCreateOrUpdateParameters',
    'ModuleErrorInfo',
    'ModuleUpdateParameters',
    'NodeCount',
    'NodeCountProperties',
    'NodeCounts',
    'Operation',
    'OperationDisplay',
    'PrivateEndpointConnection',
    'PrivateEndpointProperty',
    'PrivateLinkResource',
    'PrivateLinkServiceConnectionStateProperty',
    'ProxyResource',
    'PythonPackageCreateParameters',
    'PythonPackageUpdateParameters',
    'Resource',
    'RunAsCredentialAssociationProperty',
    'Runbook',
    'RunbookAssociationProperty',
    'RunbookCreateOrUpdateDraftParameters',
    'RunbookCreateOrUpdateDraftProperties',
    'RunbookCreateOrUpdateParameters',
    'RunbookDraft',
    'RunbookDraftUndoEditResult',
    'RunbookParameter',
    'RunbookUpdateParameters',
    'Schedule',
    'ScheduleAssociationProperty',
    'ScheduleCreateOrUpdateParameters',
    'ScheduleUpdateParameters',
    'Sku',
    'SoftwareUpdateConfigurationMachineRun',
    'SoftwareUpdateConfigurationMachineRunListResult',
    'SoftwareUpdateConfigurationRun',
    'SoftwareUpdateConfigurationRunListResult',
    'SoftwareUpdateConfigurationRunTaskProperties',
    'SoftwareUpdateConfigurationRunTasks',
    'SourceControl',
    'SourceControlCreateOrUpdateParameters',
    'SourceControlSecurityTokenProperties',
    'SourceControlSyncJob',
    'SourceControlSyncJobById',
    'SourceControlSyncJobCreateParameters',
    'SourceControlSyncJobStream',
    'SourceControlSyncJobStreamById',
    'SourceControlUpdateParameters',
    'Statistics',
    'TestJob',
    'TestJobCreateParameters',
    'TrackedResource',
    'TypeField',
    'UpdateConfigurationNavigation',
    'Usage',
    'UsageCounterName',
    'Variable',
    'VariableCreateOrUpdateParameters',
    'VariableUpdateParameters',
    'Watcher',
    'WatcherUpdateParameters',
    'Webhook',
    'WebhookCreateOrUpdateParameters',
    'WebhookUpdateParameters',
    'PrivateEndpointConnectionPaged',
    'PrivateLinkResourcePaged',
    'ModulePaged',
    'DscNodePaged',
    'DscNodeReportPaged',
    'DscNodeConfigurationPaged',
    'DscCompilationJobPaged',
    'SourceControlPaged',
    'SourceControlSyncJobPaged',
    'SourceControlSyncJobStreamPaged',
    'AutomationAccountPaged',
    'StatisticsPaged',
    'UsagePaged',
    'CertificatePaged',
    'ConnectionPaged',
    'ConnectionTypePaged',
    'CredentialPaged',
    'HybridRunbookWorkerGroupPaged',
    'JobSchedulePaged',
    'ActivityPaged',
    'TypeFieldPaged',
    'SchedulePaged',
    'VariablePaged',
    'WatcherPaged',
    'DscConfigurationPaged',
    'JobCollectionItemPaged',
    'JobStreamPaged',
    'OperationPaged',
    'RunbookPaged',
    'WebhookPaged',
    'ModuleProvisioningState',
    'AgentRegistrationKeyName',
    'ContentSourceType',
    'JobProvisioningState',
    'JobStatus',
    'JobStreamType',
    'SourceType',
    'TokenType',
    'ProvisioningState',
    'SyncType',
    'StreamType',
    'SkuNameEnum',
    'AutomationAccountState',
    'EncryptionKeySourceType',
    'ResourceIdentityType',
    'AutomationKeyName',
    'AutomationKeyPermissions',
    'GroupTypeEnum',
    'ScheduleDay',
    'ScheduleFrequency',
    'DscConfigurationProvisioningState',
    'DscConfigurationState',
    'RunbookTypeEnum',
    'RunbookState',
    'RunbookProvisioningState',
    'HttpStatusCode',
    'CountType',
]
