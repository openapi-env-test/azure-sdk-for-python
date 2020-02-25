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
    from ._models_py3 import AzureBackupGoalFeatureSupportRequest
    from ._models_py3 import AzureBackupServerContainer
    from ._models_py3 import AzureBackupServerEngine
    from ._models_py3 import AzureFileShareBackupRequest
    from ._models_py3 import AzureFileShareProtectableItem
    from ._models_py3 import AzureFileshareProtectedItem
    from ._models_py3 import AzureFileshareProtectedItemExtendedInfo
    from ._models_py3 import AzureFileShareProtectionPolicy
    from ._models_py3 import AzureFileShareProvisionILRRequest
    from ._models_py3 import AzureFileShareRecoveryPoint
    from ._models_py3 import AzureFileShareRestoreRequest
    from ._models_py3 import AzureIaaSClassicComputeVMContainer
    from ._models_py3 import AzureIaaSClassicComputeVMProtectableItem
    from ._models_py3 import AzureIaaSClassicComputeVMProtectedItem
    from ._models_py3 import AzureIaaSComputeVMContainer
    from ._models_py3 import AzureIaaSComputeVMProtectableItem
    from ._models_py3 import AzureIaaSComputeVMProtectedItem
    from ._models_py3 import AzureIaaSVMErrorInfo
    from ._models_py3 import AzureIaaSVMHealthDetails
    from ._models_py3 import AzureIaaSVMJob
    from ._models_py3 import AzureIaaSVMJobExtendedInfo
    from ._models_py3 import AzureIaaSVMJobTaskDetails
    from ._models_py3 import AzureIaaSVMProtectedItem
    from ._models_py3 import AzureIaaSVMProtectedItemExtendedInfo
    from ._models_py3 import AzureIaaSVMProtectionPolicy
    from ._models_py3 import AzureRecoveryServiceVaultProtectionIntent
    from ._models_py3 import AzureResourceProtectionIntent
    from ._models_py3 import AzureSQLAGWorkloadContainerProtectionContainer
    from ._models_py3 import AzureSqlContainer
    from ._models_py3 import AzureSqlProtectedItem
    from ._models_py3 import AzureSqlProtectedItemExtendedInfo
    from ._models_py3 import AzureSqlProtectionPolicy
    from ._models_py3 import AzureStorageContainer
    from ._models_py3 import AzureStorageErrorInfo
    from ._models_py3 import AzureStorageJob
    from ._models_py3 import AzureStorageJobExtendedInfo
    from ._models_py3 import AzureStorageJobTaskDetails
    from ._models_py3 import AzureStorageProtectableContainer
    from ._models_py3 import AzureVMAppContainerProtectableContainer
    from ._models_py3 import AzureVMAppContainerProtectionContainer
    from ._models_py3 import AzureVMResourceFeatureSupportRequest
    from ._models_py3 import AzureVMResourceFeatureSupportResponse
    from ._models_py3 import AzureVmWorkloadItem
    from ._models_py3 import AzureVmWorkloadProtectableItem
    from ._models_py3 import AzureVmWorkloadProtectedItem
    from ._models_py3 import AzureVmWorkloadProtectedItemExtendedInfo
    from ._models_py3 import AzureVmWorkloadProtectionPolicy
    from ._models_py3 import AzureVmWorkloadSAPAseDatabaseProtectedItem
    from ._models_py3 import AzureVmWorkloadSAPAseDatabaseWorkloadItem
    from ._models_py3 import AzureVmWorkloadSAPAseSystemProtectableItem
    from ._models_py3 import AzureVmWorkloadSAPAseSystemWorkloadItem
    from ._models_py3 import AzureVmWorkloadSAPHanaDatabaseProtectableItem
    from ._models_py3 import AzureVmWorkloadSAPHanaDatabaseProtectedItem
    from ._models_py3 import AzureVmWorkloadSAPHanaDatabaseWorkloadItem
    from ._models_py3 import AzureVmWorkloadSAPHanaSystemProtectableItem
    from ._models_py3 import AzureVmWorkloadSAPHanaSystemWorkloadItem
    from ._models_py3 import AzureVmWorkloadSQLAvailabilityGroupProtectableItem
    from ._models_py3 import AzureVmWorkloadSQLDatabaseProtectableItem
    from ._models_py3 import AzureVmWorkloadSQLDatabaseProtectedItem
    from ._models_py3 import AzureVmWorkloadSQLDatabaseWorkloadItem
    from ._models_py3 import AzureVmWorkloadSQLInstanceProtectableItem
    from ._models_py3 import AzureVmWorkloadSQLInstanceWorkloadItem
    from ._models_py3 import AzureWorkloadAutoProtectionIntent
    from ._models_py3 import AzureWorkloadBackupRequest
    from ._models_py3 import AzureWorkloadContainer
    from ._models_py3 import AzureWorkloadContainerExtendedInfo
    from ._models_py3 import AzureWorkloadErrorInfo
    from ._models_py3 import AzureWorkloadJob
    from ._models_py3 import AzureWorkloadJobExtendedInfo
    from ._models_py3 import AzureWorkloadJobTaskDetails
    from ._models_py3 import AzureWorkloadPointInTimeRecoveryPoint
    from ._models_py3 import AzureWorkloadPointInTimeRestoreRequest
    from ._models_py3 import AzureWorkloadRecoveryPoint
    from ._models_py3 import AzureWorkloadRestoreRequest
    from ._models_py3 import AzureWorkloadSAPHanaPointInTimeRecoveryPoint
    from ._models_py3 import AzureWorkloadSAPHanaPointInTimeRestoreRequest
    from ._models_py3 import AzureWorkloadSAPHanaRecoveryPoint
    from ._models_py3 import AzureWorkloadSAPHanaRestoreRequest
    from ._models_py3 import AzureWorkloadSQLAutoProtectionIntent
    from ._models_py3 import AzureWorkloadSQLPointInTimeRecoveryPoint
    from ._models_py3 import AzureWorkloadSQLPointInTimeRestoreRequest
    from ._models_py3 import AzureWorkloadSQLRecoveryPoint
    from ._models_py3 import AzureWorkloadSQLRecoveryPointExtendedInfo
    from ._models_py3 import AzureWorkloadSQLRestoreRequest
    from ._models_py3 import BackupEngineBase
    from ._models_py3 import BackupEngineBaseResource
    from ._models_py3 import BackupEngineExtendedInfo
    from ._models_py3 import BackupManagementUsage
    from ._models_py3 import BackupRequest
    from ._models_py3 import BackupRequestResource
    from ._models_py3 import BackupResourceConfig
    from ._models_py3 import BackupResourceConfigResource
    from ._models_py3 import BackupResourceVaultConfig
    from ._models_py3 import BackupResourceVaultConfigResource
    from ._models_py3 import BackupStatusRequest
    from ._models_py3 import BackupStatusResponse
    from ._models_py3 import BEKDetails
    from ._models_py3 import BMSBackupEngineQueryObject
    from ._models_py3 import BMSBackupEnginesQueryObject
    from ._models_py3 import BMSBackupSummariesQueryObject
    from ._models_py3 import BMSContainerQueryObject
    from ._models_py3 import BMSContainersInquiryQueryObject
    from ._models_py3 import BMSPOQueryObject
    from ._models_py3 import BMSRefreshContainersQueryObject
    from ._models_py3 import BMSRPQueryObject
    from ._models_py3 import BMSWorkloadItemQueryObject
    from ._models_py3 import ClientDiscoveryDisplay
    from ._models_py3 import ClientDiscoveryForLogSpecification
    from ._models_py3 import ClientDiscoveryForProperties
    from ._models_py3 import ClientDiscoveryForServiceSpecification
    from ._models_py3 import ClientDiscoveryValueForSingleApi
    from ._models_py3 import ClientScriptForConnect
    from ._models_py3 import ContainerIdentityInfo
    from ._models_py3 import DailyRetentionFormat
    from ._models_py3 import DailyRetentionSchedule
    from ._models_py3 import Day
    from ._models_py3 import DiskExclusionProperties
    from ._models_py3 import DiskInformation
    from ._models_py3 import DistributedNodesInfo
    from ._models_py3 import DpmBackupEngine
    from ._models_py3 import DpmContainer
    from ._models_py3 import DPMContainerExtendedInfo
    from ._models_py3 import DpmErrorInfo
    from ._models_py3 import DpmJob
    from ._models_py3 import DpmJobExtendedInfo
    from ._models_py3 import DpmJobTaskDetails
    from ._models_py3 import DPMProtectedItem
    from ._models_py3 import DPMProtectedItemExtendedInfo
    from ._models_py3 import EncryptionDetails
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import ExportJobsOperationResultInfo
    from ._models_py3 import ExtendedProperties
    from ._models_py3 import FeatureSupportRequest
    from ._models_py3 import GenericContainer
    from ._models_py3 import GenericContainerExtendedInfo
    from ._models_py3 import GenericProtectedItem
    from ._models_py3 import GenericProtectionPolicy
    from ._models_py3 import GenericRecoveryPoint
    from ._models_py3 import GetProtectedItemQueryObject
    from ._models_py3 import IaasVMBackupRequest
    from ._models_py3 import IaaSVMContainer
    from ._models_py3 import IaasVMILRRegistrationRequest
    from ._models_py3 import IaaSVMProtectableItem
    from ._models_py3 import IaasVMRecoveryPoint
    from ._models_py3 import IaasVMRestoreRequest
    from ._models_py3 import ILRRequest
    from ._models_py3 import ILRRequestResource
    from ._models_py3 import InquiryInfo
    from ._models_py3 import InquiryValidation
    from ._models_py3 import InstantItemRecoveryTarget
    from ._models_py3 import InstantRPAdditionalDetails
    from ._models_py3 import Job
    from ._models_py3 import JobQueryObject
    from ._models_py3 import JobResource
    from ._models_py3 import KEKDetails
    from ._models_py3 import KeyAndSecretDetails
    from ._models_py3 import LogSchedulePolicy
    from ._models_py3 import LongTermRetentionPolicy
    from ._models_py3 import LongTermSchedulePolicy
    from ._models_py3 import MabContainer
    from ._models_py3 import MabContainerExtendedInfo
    from ._models_py3 import MABContainerHealthDetails
    from ._models_py3 import MabErrorInfo
    from ._models_py3 import MabFileFolderProtectedItem
    from ._models_py3 import MabFileFolderProtectedItemExtendedInfo
    from ._models_py3 import MabJob
    from ._models_py3 import MabJobExtendedInfo
    from ._models_py3 import MabJobTaskDetails
    from ._models_py3 import MabProtectionPolicy
    from ._models_py3 import MonthlyRetentionSchedule
    from ._models_py3 import NameInfo
    from ._models_py3 import OperationResultInfo
    from ._models_py3 import OperationResultInfoBase
    from ._models_py3 import OperationResultInfoBaseResource
    from ._models_py3 import OperationStatus
    from ._models_py3 import OperationStatusError
    from ._models_py3 import OperationStatusExtendedInfo
    from ._models_py3 import OperationStatusJobExtendedInfo
    from ._models_py3 import OperationStatusJobsExtendedInfo
    from ._models_py3 import OperationStatusProvisionILRExtendedInfo
    from ._models_py3 import OperationWorkerResponse
    from ._models_py3 import PointInTimeRange
    from ._models_py3 import PreBackupValidation
    from ._models_py3 import PreValidateEnableBackupRequest
    from ._models_py3 import PreValidateEnableBackupResponse
    from ._models_py3 import ProtectableContainer
    from ._models_py3 import ProtectableContainerResource
    from ._models_py3 import ProtectedItem
    from ._models_py3 import ProtectedItemQueryObject
    from ._models_py3 import ProtectedItemResource
    from ._models_py3 import ProtectionContainer
    from ._models_py3 import ProtectionContainerResource
    from ._models_py3 import ProtectionIntent
    from ._models_py3 import ProtectionIntentQueryObject
    from ._models_py3 import ProtectionIntentResource
    from ._models_py3 import ProtectionPolicy
    from ._models_py3 import ProtectionPolicyQueryObject
    from ._models_py3 import ProtectionPolicyResource
    from ._models_py3 import RecoveryPoint
    from ._models_py3 import RecoveryPointDiskConfiguration
    from ._models_py3 import RecoveryPointResource
    from ._models_py3 import RecoveryPointTierInformation
    from ._models_py3 import Resource
    from ._models_py3 import ResourceList
    from ._models_py3 import RestoreFileSpecs
    from ._models_py3 import RestoreRequest
    from ._models_py3 import RestoreRequestResource
    from ._models_py3 import RetentionDuration
    from ._models_py3 import RetentionPolicy
    from ._models_py3 import SchedulePolicy
    from ._models_py3 import Settings
    from ._models_py3 import SimpleRetentionPolicy
    from ._models_py3 import SimpleSchedulePolicy
    from ._models_py3 import SQLDataDirectory
    from ._models_py3 import SQLDataDirectoryMapping
    from ._models_py3 import SubProtectionPolicy
    from ._models_py3 import TargetAFSRestoreInfo
    from ._models_py3 import TargetRestoreInfo
    from ._models_py3 import TokenInformation
    from ._models_py3 import ValidateIaasVMRestoreOperationRequest
    from ._models_py3 import ValidateOperationRequest
    from ._models_py3 import ValidateOperationResponse
    from ._models_py3 import ValidateOperationsResponse
    from ._models_py3 import ValidateRestoreOperationRequest
    from ._models_py3 import WeeklyRetentionFormat
    from ._models_py3 import WeeklyRetentionSchedule
    from ._models_py3 import WorkloadInquiryDetails
    from ._models_py3 import WorkloadItem
    from ._models_py3 import WorkloadItemResource
    from ._models_py3 import WorkloadProtectableItem
    from ._models_py3 import WorkloadProtectableItemResource
    from ._models_py3 import YearlyRetentionSchedule
except (SyntaxError, ImportError):
    from ._models import AzureBackupGoalFeatureSupportRequest
    from ._models import AzureBackupServerContainer
    from ._models import AzureBackupServerEngine
    from ._models import AzureFileShareBackupRequest
    from ._models import AzureFileShareProtectableItem
    from ._models import AzureFileshareProtectedItem
    from ._models import AzureFileshareProtectedItemExtendedInfo
    from ._models import AzureFileShareProtectionPolicy
    from ._models import AzureFileShareProvisionILRRequest
    from ._models import AzureFileShareRecoveryPoint
    from ._models import AzureFileShareRestoreRequest
    from ._models import AzureIaaSClassicComputeVMContainer
    from ._models import AzureIaaSClassicComputeVMProtectableItem
    from ._models import AzureIaaSClassicComputeVMProtectedItem
    from ._models import AzureIaaSComputeVMContainer
    from ._models import AzureIaaSComputeVMProtectableItem
    from ._models import AzureIaaSComputeVMProtectedItem
    from ._models import AzureIaaSVMErrorInfo
    from ._models import AzureIaaSVMHealthDetails
    from ._models import AzureIaaSVMJob
    from ._models import AzureIaaSVMJobExtendedInfo
    from ._models import AzureIaaSVMJobTaskDetails
    from ._models import AzureIaaSVMProtectedItem
    from ._models import AzureIaaSVMProtectedItemExtendedInfo
    from ._models import AzureIaaSVMProtectionPolicy
    from ._models import AzureRecoveryServiceVaultProtectionIntent
    from ._models import AzureResourceProtectionIntent
    from ._models import AzureSQLAGWorkloadContainerProtectionContainer
    from ._models import AzureSqlContainer
    from ._models import AzureSqlProtectedItem
    from ._models import AzureSqlProtectedItemExtendedInfo
    from ._models import AzureSqlProtectionPolicy
    from ._models import AzureStorageContainer
    from ._models import AzureStorageErrorInfo
    from ._models import AzureStorageJob
    from ._models import AzureStorageJobExtendedInfo
    from ._models import AzureStorageJobTaskDetails
    from ._models import AzureStorageProtectableContainer
    from ._models import AzureVMAppContainerProtectableContainer
    from ._models import AzureVMAppContainerProtectionContainer
    from ._models import AzureVMResourceFeatureSupportRequest
    from ._models import AzureVMResourceFeatureSupportResponse
    from ._models import AzureVmWorkloadItem
    from ._models import AzureVmWorkloadProtectableItem
    from ._models import AzureVmWorkloadProtectedItem
    from ._models import AzureVmWorkloadProtectedItemExtendedInfo
    from ._models import AzureVmWorkloadProtectionPolicy
    from ._models import AzureVmWorkloadSAPAseDatabaseProtectedItem
    from ._models import AzureVmWorkloadSAPAseDatabaseWorkloadItem
    from ._models import AzureVmWorkloadSAPAseSystemProtectableItem
    from ._models import AzureVmWorkloadSAPAseSystemWorkloadItem
    from ._models import AzureVmWorkloadSAPHanaDatabaseProtectableItem
    from ._models import AzureVmWorkloadSAPHanaDatabaseProtectedItem
    from ._models import AzureVmWorkloadSAPHanaDatabaseWorkloadItem
    from ._models import AzureVmWorkloadSAPHanaSystemProtectableItem
    from ._models import AzureVmWorkloadSAPHanaSystemWorkloadItem
    from ._models import AzureVmWorkloadSQLAvailabilityGroupProtectableItem
    from ._models import AzureVmWorkloadSQLDatabaseProtectableItem
    from ._models import AzureVmWorkloadSQLDatabaseProtectedItem
    from ._models import AzureVmWorkloadSQLDatabaseWorkloadItem
    from ._models import AzureVmWorkloadSQLInstanceProtectableItem
    from ._models import AzureVmWorkloadSQLInstanceWorkloadItem
    from ._models import AzureWorkloadAutoProtectionIntent
    from ._models import AzureWorkloadBackupRequest
    from ._models import AzureWorkloadContainer
    from ._models import AzureWorkloadContainerExtendedInfo
    from ._models import AzureWorkloadErrorInfo
    from ._models import AzureWorkloadJob
    from ._models import AzureWorkloadJobExtendedInfo
    from ._models import AzureWorkloadJobTaskDetails
    from ._models import AzureWorkloadPointInTimeRecoveryPoint
    from ._models import AzureWorkloadPointInTimeRestoreRequest
    from ._models import AzureWorkloadRecoveryPoint
    from ._models import AzureWorkloadRestoreRequest
    from ._models import AzureWorkloadSAPHanaPointInTimeRecoveryPoint
    from ._models import AzureWorkloadSAPHanaPointInTimeRestoreRequest
    from ._models import AzureWorkloadSAPHanaRecoveryPoint
    from ._models import AzureWorkloadSAPHanaRestoreRequest
    from ._models import AzureWorkloadSQLAutoProtectionIntent
    from ._models import AzureWorkloadSQLPointInTimeRecoveryPoint
    from ._models import AzureWorkloadSQLPointInTimeRestoreRequest
    from ._models import AzureWorkloadSQLRecoveryPoint
    from ._models import AzureWorkloadSQLRecoveryPointExtendedInfo
    from ._models import AzureWorkloadSQLRestoreRequest
    from ._models import BackupEngineBase
    from ._models import BackupEngineBaseResource
    from ._models import BackupEngineExtendedInfo
    from ._models import BackupManagementUsage
    from ._models import BackupRequest
    from ._models import BackupRequestResource
    from ._models import BackupResourceConfig
    from ._models import BackupResourceConfigResource
    from ._models import BackupResourceVaultConfig
    from ._models import BackupResourceVaultConfigResource
    from ._models import BackupStatusRequest
    from ._models import BackupStatusResponse
    from ._models import BEKDetails
    from ._models import BMSBackupEngineQueryObject
    from ._models import BMSBackupEnginesQueryObject
    from ._models import BMSBackupSummariesQueryObject
    from ._models import BMSContainerQueryObject
    from ._models import BMSContainersInquiryQueryObject
    from ._models import BMSPOQueryObject
    from ._models import BMSRefreshContainersQueryObject
    from ._models import BMSRPQueryObject
    from ._models import BMSWorkloadItemQueryObject
    from ._models import ClientDiscoveryDisplay
    from ._models import ClientDiscoveryForLogSpecification
    from ._models import ClientDiscoveryForProperties
    from ._models import ClientDiscoveryForServiceSpecification
    from ._models import ClientDiscoveryValueForSingleApi
    from ._models import ClientScriptForConnect
    from ._models import ContainerIdentityInfo
    from ._models import DailyRetentionFormat
    from ._models import DailyRetentionSchedule
    from ._models import Day
    from ._models import DiskExclusionProperties
    from ._models import DiskInformation
    from ._models import DistributedNodesInfo
    from ._models import DpmBackupEngine
    from ._models import DpmContainer
    from ._models import DPMContainerExtendedInfo
    from ._models import DpmErrorInfo
    from ._models import DpmJob
    from ._models import DpmJobExtendedInfo
    from ._models import DpmJobTaskDetails
    from ._models import DPMProtectedItem
    from ._models import DPMProtectedItemExtendedInfo
    from ._models import EncryptionDetails
    from ._models import ErrorAdditionalInfo
    from ._models import ErrorDetail
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import ExportJobsOperationResultInfo
    from ._models import ExtendedProperties
    from ._models import FeatureSupportRequest
    from ._models import GenericContainer
    from ._models import GenericContainerExtendedInfo
    from ._models import GenericProtectedItem
    from ._models import GenericProtectionPolicy
    from ._models import GenericRecoveryPoint
    from ._models import GetProtectedItemQueryObject
    from ._models import IaasVMBackupRequest
    from ._models import IaaSVMContainer
    from ._models import IaasVMILRRegistrationRequest
    from ._models import IaaSVMProtectableItem
    from ._models import IaasVMRecoveryPoint
    from ._models import IaasVMRestoreRequest
    from ._models import ILRRequest
    from ._models import ILRRequestResource
    from ._models import InquiryInfo
    from ._models import InquiryValidation
    from ._models import InstantItemRecoveryTarget
    from ._models import InstantRPAdditionalDetails
    from ._models import Job
    from ._models import JobQueryObject
    from ._models import JobResource
    from ._models import KEKDetails
    from ._models import KeyAndSecretDetails
    from ._models import LogSchedulePolicy
    from ._models import LongTermRetentionPolicy
    from ._models import LongTermSchedulePolicy
    from ._models import MabContainer
    from ._models import MabContainerExtendedInfo
    from ._models import MABContainerHealthDetails
    from ._models import MabErrorInfo
    from ._models import MabFileFolderProtectedItem
    from ._models import MabFileFolderProtectedItemExtendedInfo
    from ._models import MabJob
    from ._models import MabJobExtendedInfo
    from ._models import MabJobTaskDetails
    from ._models import MabProtectionPolicy
    from ._models import MonthlyRetentionSchedule
    from ._models import NameInfo
    from ._models import OperationResultInfo
    from ._models import OperationResultInfoBase
    from ._models import OperationResultInfoBaseResource
    from ._models import OperationStatus
    from ._models import OperationStatusError
    from ._models import OperationStatusExtendedInfo
    from ._models import OperationStatusJobExtendedInfo
    from ._models import OperationStatusJobsExtendedInfo
    from ._models import OperationStatusProvisionILRExtendedInfo
    from ._models import OperationWorkerResponse
    from ._models import PointInTimeRange
    from ._models import PreBackupValidation
    from ._models import PreValidateEnableBackupRequest
    from ._models import PreValidateEnableBackupResponse
    from ._models import ProtectableContainer
    from ._models import ProtectableContainerResource
    from ._models import ProtectedItem
    from ._models import ProtectedItemQueryObject
    from ._models import ProtectedItemResource
    from ._models import ProtectionContainer
    from ._models import ProtectionContainerResource
    from ._models import ProtectionIntent
    from ._models import ProtectionIntentQueryObject
    from ._models import ProtectionIntentResource
    from ._models import ProtectionPolicy
    from ._models import ProtectionPolicyQueryObject
    from ._models import ProtectionPolicyResource
    from ._models import RecoveryPoint
    from ._models import RecoveryPointDiskConfiguration
    from ._models import RecoveryPointResource
    from ._models import RecoveryPointTierInformation
    from ._models import Resource
    from ._models import ResourceList
    from ._models import RestoreFileSpecs
    from ._models import RestoreRequest
    from ._models import RestoreRequestResource
    from ._models import RetentionDuration
    from ._models import RetentionPolicy
    from ._models import SchedulePolicy
    from ._models import Settings
    from ._models import SimpleRetentionPolicy
    from ._models import SimpleSchedulePolicy
    from ._models import SQLDataDirectory
    from ._models import SQLDataDirectoryMapping
    from ._models import SubProtectionPolicy
    from ._models import TargetAFSRestoreInfo
    from ._models import TargetRestoreInfo
    from ._models import TokenInformation
    from ._models import ValidateIaasVMRestoreOperationRequest
    from ._models import ValidateOperationRequest
    from ._models import ValidateOperationResponse
    from ._models import ValidateOperationsResponse
    from ._models import ValidateRestoreOperationRequest
    from ._models import WeeklyRetentionFormat
    from ._models import WeeklyRetentionSchedule
    from ._models import WorkloadInquiryDetails
    from ._models import WorkloadItem
    from ._models import WorkloadItemResource
    from ._models import WorkloadProtectableItem
    from ._models import WorkloadProtectableItemResource
    from ._models import YearlyRetentionSchedule
from ._paged_models import BackupEngineBaseResourcePaged
from ._paged_models import BackupManagementUsagePaged
from ._paged_models import ClientDiscoveryValueForSingleApiPaged
from ._paged_models import JobResourcePaged
from ._paged_models import ProtectableContainerResourcePaged
from ._paged_models import ProtectedItemResourcePaged
from ._paged_models import ProtectionContainerResourcePaged
from ._paged_models import ProtectionIntentResourcePaged
from ._paged_models import ProtectionPolicyResourcePaged
from ._paged_models import RecoveryPointResourcePaged
from ._paged_models import WorkloadItemResourcePaged
from ._paged_models import WorkloadProtectableItemResourcePaged
from ._recovery_services_backup_client_enums import (
    ProtectionState,
    HealthStatus,
    RecoveryType,
    CopyOptions,
    RestoreRequestType,
    WorkloadType,
    PolicyType,
    JobSupportedAction,
    ProtectedItemState,
    LastBackupStatus,
    ProtectedItemHealthStatus,
    RestorePointType,
    OverwriteOptions,
    RecoveryMode,
    SQLDataDirectoryType,
    StorageType,
    StorageTypeState,
    EnhancedSecurityState,
    SoftDeleteFeatureState,
    RestorePointQueryType,
    RetentionDurationType,
    RecoveryPointTierType,
    RecoveryPointTierStatus,
    BackupManagementType,
    JobStatus,
    JobOperationType,
    DayOfWeek,
    RetentionScheduleFormat,
    WeekOfMonth,
    MonthOfYear,
    MabServerType,
    HttpStatusCode,
    DataSourceType,
    CreateMode,
    HealthState,
    ScheduleRunType,
    SupportStatus,
    WorkloadItemType,
    UsagesUnit,
    ProtectionStatus,
    FabricName,
    Type,
    ValidationStatus,
    IntentItemType,
    AzureFileShareType,
    InquiryStatus,
    BackupType,
    OperationType,
    ContainerType,
    BackupItemType,
    OperationStatusValues,
)

__all__ = [
    'AzureBackupGoalFeatureSupportRequest',
    'AzureBackupServerContainer',
    'AzureBackupServerEngine',
    'AzureFileShareBackupRequest',
    'AzureFileShareProtectableItem',
    'AzureFileshareProtectedItem',
    'AzureFileshareProtectedItemExtendedInfo',
    'AzureFileShareProtectionPolicy',
    'AzureFileShareProvisionILRRequest',
    'AzureFileShareRecoveryPoint',
    'AzureFileShareRestoreRequest',
    'AzureIaaSClassicComputeVMContainer',
    'AzureIaaSClassicComputeVMProtectableItem',
    'AzureIaaSClassicComputeVMProtectedItem',
    'AzureIaaSComputeVMContainer',
    'AzureIaaSComputeVMProtectableItem',
    'AzureIaaSComputeVMProtectedItem',
    'AzureIaaSVMErrorInfo',
    'AzureIaaSVMHealthDetails',
    'AzureIaaSVMJob',
    'AzureIaaSVMJobExtendedInfo',
    'AzureIaaSVMJobTaskDetails',
    'AzureIaaSVMProtectedItem',
    'AzureIaaSVMProtectedItemExtendedInfo',
    'AzureIaaSVMProtectionPolicy',
    'AzureRecoveryServiceVaultProtectionIntent',
    'AzureResourceProtectionIntent',
    'AzureSQLAGWorkloadContainerProtectionContainer',
    'AzureSqlContainer',
    'AzureSqlProtectedItem',
    'AzureSqlProtectedItemExtendedInfo',
    'AzureSqlProtectionPolicy',
    'AzureStorageContainer',
    'AzureStorageErrorInfo',
    'AzureStorageJob',
    'AzureStorageJobExtendedInfo',
    'AzureStorageJobTaskDetails',
    'AzureStorageProtectableContainer',
    'AzureVMAppContainerProtectableContainer',
    'AzureVMAppContainerProtectionContainer',
    'AzureVMResourceFeatureSupportRequest',
    'AzureVMResourceFeatureSupportResponse',
    'AzureVmWorkloadItem',
    'AzureVmWorkloadProtectableItem',
    'AzureVmWorkloadProtectedItem',
    'AzureVmWorkloadProtectedItemExtendedInfo',
    'AzureVmWorkloadProtectionPolicy',
    'AzureVmWorkloadSAPAseDatabaseProtectedItem',
    'AzureVmWorkloadSAPAseDatabaseWorkloadItem',
    'AzureVmWorkloadSAPAseSystemProtectableItem',
    'AzureVmWorkloadSAPAseSystemWorkloadItem',
    'AzureVmWorkloadSAPHanaDatabaseProtectableItem',
    'AzureVmWorkloadSAPHanaDatabaseProtectedItem',
    'AzureVmWorkloadSAPHanaDatabaseWorkloadItem',
    'AzureVmWorkloadSAPHanaSystemProtectableItem',
    'AzureVmWorkloadSAPHanaSystemWorkloadItem',
    'AzureVmWorkloadSQLAvailabilityGroupProtectableItem',
    'AzureVmWorkloadSQLDatabaseProtectableItem',
    'AzureVmWorkloadSQLDatabaseProtectedItem',
    'AzureVmWorkloadSQLDatabaseWorkloadItem',
    'AzureVmWorkloadSQLInstanceProtectableItem',
    'AzureVmWorkloadSQLInstanceWorkloadItem',
    'AzureWorkloadAutoProtectionIntent',
    'AzureWorkloadBackupRequest',
    'AzureWorkloadContainer',
    'AzureWorkloadContainerExtendedInfo',
    'AzureWorkloadErrorInfo',
    'AzureWorkloadJob',
    'AzureWorkloadJobExtendedInfo',
    'AzureWorkloadJobTaskDetails',
    'AzureWorkloadPointInTimeRecoveryPoint',
    'AzureWorkloadPointInTimeRestoreRequest',
    'AzureWorkloadRecoveryPoint',
    'AzureWorkloadRestoreRequest',
    'AzureWorkloadSAPHanaPointInTimeRecoveryPoint',
    'AzureWorkloadSAPHanaPointInTimeRestoreRequest',
    'AzureWorkloadSAPHanaRecoveryPoint',
    'AzureWorkloadSAPHanaRestoreRequest',
    'AzureWorkloadSQLAutoProtectionIntent',
    'AzureWorkloadSQLPointInTimeRecoveryPoint',
    'AzureWorkloadSQLPointInTimeRestoreRequest',
    'AzureWorkloadSQLRecoveryPoint',
    'AzureWorkloadSQLRecoveryPointExtendedInfo',
    'AzureWorkloadSQLRestoreRequest',
    'BackupEngineBase',
    'BackupEngineBaseResource',
    'BackupEngineExtendedInfo',
    'BackupManagementUsage',
    'BackupRequest',
    'BackupRequestResource',
    'BackupResourceConfig',
    'BackupResourceConfigResource',
    'BackupResourceVaultConfig',
    'BackupResourceVaultConfigResource',
    'BackupStatusRequest',
    'BackupStatusResponse',
    'BEKDetails',
    'BMSBackupEngineQueryObject',
    'BMSBackupEnginesQueryObject',
    'BMSBackupSummariesQueryObject',
    'BMSContainerQueryObject',
    'BMSContainersInquiryQueryObject',
    'BMSPOQueryObject',
    'BMSRefreshContainersQueryObject',
    'BMSRPQueryObject',
    'BMSWorkloadItemQueryObject',
    'ClientDiscoveryDisplay',
    'ClientDiscoveryForLogSpecification',
    'ClientDiscoveryForProperties',
    'ClientDiscoveryForServiceSpecification',
    'ClientDiscoveryValueForSingleApi',
    'ClientScriptForConnect',
    'ContainerIdentityInfo',
    'DailyRetentionFormat',
    'DailyRetentionSchedule',
    'Day',
    'DiskExclusionProperties',
    'DiskInformation',
    'DistributedNodesInfo',
    'DpmBackupEngine',
    'DpmContainer',
    'DPMContainerExtendedInfo',
    'DpmErrorInfo',
    'DpmJob',
    'DpmJobExtendedInfo',
    'DpmJobTaskDetails',
    'DPMProtectedItem',
    'DPMProtectedItemExtendedInfo',
    'EncryptionDetails',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse', 'ErrorResponseException',
    'ExportJobsOperationResultInfo',
    'ExtendedProperties',
    'FeatureSupportRequest',
    'GenericContainer',
    'GenericContainerExtendedInfo',
    'GenericProtectedItem',
    'GenericProtectionPolicy',
    'GenericRecoveryPoint',
    'GetProtectedItemQueryObject',
    'IaasVMBackupRequest',
    'IaaSVMContainer',
    'IaasVMILRRegistrationRequest',
    'IaaSVMProtectableItem',
    'IaasVMRecoveryPoint',
    'IaasVMRestoreRequest',
    'ILRRequest',
    'ILRRequestResource',
    'InquiryInfo',
    'InquiryValidation',
    'InstantItemRecoveryTarget',
    'InstantRPAdditionalDetails',
    'Job',
    'JobQueryObject',
    'JobResource',
    'KEKDetails',
    'KeyAndSecretDetails',
    'LogSchedulePolicy',
    'LongTermRetentionPolicy',
    'LongTermSchedulePolicy',
    'MabContainer',
    'MabContainerExtendedInfo',
    'MABContainerHealthDetails',
    'MabErrorInfo',
    'MabFileFolderProtectedItem',
    'MabFileFolderProtectedItemExtendedInfo',
    'MabJob',
    'MabJobExtendedInfo',
    'MabJobTaskDetails',
    'MabProtectionPolicy',
    'MonthlyRetentionSchedule',
    'NameInfo',
    'OperationResultInfo',
    'OperationResultInfoBase',
    'OperationResultInfoBaseResource',
    'OperationStatus',
    'OperationStatusError',
    'OperationStatusExtendedInfo',
    'OperationStatusJobExtendedInfo',
    'OperationStatusJobsExtendedInfo',
    'OperationStatusProvisionILRExtendedInfo',
    'OperationWorkerResponse',
    'PointInTimeRange',
    'PreBackupValidation',
    'PreValidateEnableBackupRequest',
    'PreValidateEnableBackupResponse',
    'ProtectableContainer',
    'ProtectableContainerResource',
    'ProtectedItem',
    'ProtectedItemQueryObject',
    'ProtectedItemResource',
    'ProtectionContainer',
    'ProtectionContainerResource',
    'ProtectionIntent',
    'ProtectionIntentQueryObject',
    'ProtectionIntentResource',
    'ProtectionPolicy',
    'ProtectionPolicyQueryObject',
    'ProtectionPolicyResource',
    'RecoveryPoint',
    'RecoveryPointDiskConfiguration',
    'RecoveryPointResource',
    'RecoveryPointTierInformation',
    'Resource',
    'ResourceList',
    'RestoreFileSpecs',
    'RestoreRequest',
    'RestoreRequestResource',
    'RetentionDuration',
    'RetentionPolicy',
    'SchedulePolicy',
    'Settings',
    'SimpleRetentionPolicy',
    'SimpleSchedulePolicy',
    'SQLDataDirectory',
    'SQLDataDirectoryMapping',
    'SubProtectionPolicy',
    'TargetAFSRestoreInfo',
    'TargetRestoreInfo',
    'TokenInformation',
    'ValidateIaasVMRestoreOperationRequest',
    'ValidateOperationRequest',
    'ValidateOperationResponse',
    'ValidateOperationsResponse',
    'ValidateRestoreOperationRequest',
    'WeeklyRetentionFormat',
    'WeeklyRetentionSchedule',
    'WorkloadInquiryDetails',
    'WorkloadItem',
    'WorkloadItemResource',
    'WorkloadProtectableItem',
    'WorkloadProtectableItemResource',
    'YearlyRetentionSchedule',
    'RecoveryPointResourcePaged',
    'ProtectionPolicyResourcePaged',
    'JobResourcePaged',
    'ProtectedItemResourcePaged',
    'ProtectionIntentResourcePaged',
    'BackupManagementUsagePaged',
    'BackupEngineBaseResourcePaged',
    'ProtectableContainerResourcePaged',
    'WorkloadItemResourcePaged',
    'WorkloadProtectableItemResourcePaged',
    'ProtectionContainerResourcePaged',
    'ClientDiscoveryValueForSingleApiPaged',
    'ProtectionState',
    'HealthStatus',
    'RecoveryType',
    'CopyOptions',
    'RestoreRequestType',
    'WorkloadType',
    'PolicyType',
    'JobSupportedAction',
    'ProtectedItemState',
    'LastBackupStatus',
    'ProtectedItemHealthStatus',
    'RestorePointType',
    'OverwriteOptions',
    'RecoveryMode',
    'SQLDataDirectoryType',
    'StorageType',
    'StorageTypeState',
    'EnhancedSecurityState',
    'SoftDeleteFeatureState',
    'RestorePointQueryType',
    'RetentionDurationType',
    'RecoveryPointTierType',
    'RecoveryPointTierStatus',
    'BackupManagementType',
    'JobStatus',
    'JobOperationType',
    'DayOfWeek',
    'RetentionScheduleFormat',
    'WeekOfMonth',
    'MonthOfYear',
    'MabServerType',
    'HttpStatusCode',
    'DataSourceType',
    'CreateMode',
    'HealthState',
    'ScheduleRunType',
    'SupportStatus',
    'WorkloadItemType',
    'UsagesUnit',
    'ProtectionStatus',
    'FabricName',
    'Type',
    'ValidationStatus',
    'IntentItemType',
    'AzureFileShareType',
    'InquiryStatus',
    'BackupType',
    'OperationType',
    'ContainerType',
    'BackupItemType',
    'OperationStatusValues',
]
