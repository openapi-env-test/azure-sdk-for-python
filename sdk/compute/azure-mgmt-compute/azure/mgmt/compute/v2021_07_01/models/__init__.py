# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AdditionalCapabilities
from ._models_py3 import AdditionalUnattendContent
from ._models_py3 import ApiEntityReference
from ._models_py3 import ApiError
from ._models_py3 import ApiErrorBase
from ._models_py3 import ApplicationProfile
from ._models_py3 import AutomaticOSUpgradePolicy
from ._models_py3 import AutomaticOSUpgradeProperties
from ._models_py3 import AutomaticRepairsPolicy
from ._models_py3 import AvailabilitySet
from ._models_py3 import AvailabilitySetListResult
from ._models_py3 import AvailabilitySetUpdate
from ._models_py3 import AvailablePatchSummary
from ._models_py3 import BillingProfile
from ._models_py3 import BootDiagnostics
from ._models_py3 import BootDiagnosticsInstanceView
from ._models_py3 import CapacityReservation
from ._models_py3 import CapacityReservationGroup
from ._models_py3 import CapacityReservationGroupInstanceView
from ._models_py3 import CapacityReservationGroupListResult
from ._models_py3 import CapacityReservationGroupUpdate
from ._models_py3 import CapacityReservationInstanceView
from ._models_py3 import CapacityReservationInstanceViewWithName
from ._models_py3 import CapacityReservationListResult
from ._models_py3 import CapacityReservationProfile
from ._models_py3 import CapacityReservationUpdate
from ._models_py3 import CapacityReservationUtilization
from ._models_py3 import CommunityGallery
from ._models_py3 import CommunityGalleryImage
from ._models_py3 import CommunityGalleryImageVersion
from ._models_py3 import ComputeOperationListResult
from ._models_py3 import ComputeOperationValue
from ._models_py3 import DataDisk
from ._models_py3 import DataDiskImage
from ._models_py3 import DataDiskImageEncryption
from ._models_py3 import DedicatedHost
from ._models_py3 import DedicatedHostAllocatableVM
from ._models_py3 import DedicatedHostAvailableCapacity
from ._models_py3 import DedicatedHostGroup
from ._models_py3 import DedicatedHostGroupInstanceView
from ._models_py3 import DedicatedHostGroupListResult
from ._models_py3 import DedicatedHostGroupUpdate
from ._models_py3 import DedicatedHostInstanceView
from ._models_py3 import DedicatedHostInstanceViewWithName
from ._models_py3 import DedicatedHostListResult
from ._models_py3 import DedicatedHostUpdate
from ._models_py3 import DiagnosticsProfile
from ._models_py3 import DiffDiskSettings
from ._models_py3 import Disallowed
from ._models_py3 import DisallowedConfiguration
from ._models_py3 import DiskEncryptionSetParameters
from ._models_py3 import DiskEncryptionSettings
from ._models_py3 import DiskImageEncryption
from ._models_py3 import DiskInstanceView
from ._models_py3 import EncryptionImages
from ._models_py3 import ExtendedLocation
from ._models_py3 import Gallery
from ._models_py3 import GalleryApplication
from ._models_py3 import GalleryApplicationList
from ._models_py3 import GalleryApplicationUpdate
from ._models_py3 import GalleryApplicationVersion
from ._models_py3 import GalleryApplicationVersionList
from ._models_py3 import GalleryApplicationVersionPublishingProfile
from ._models_py3 import GalleryApplicationVersionUpdate
from ._models_py3 import GalleryArtifactPublishingProfileBase
from ._models_py3 import GalleryArtifactSource
from ._models_py3 import GalleryArtifactVersionSource
from ._models_py3 import GalleryDataDiskImage
from ._models_py3 import GalleryDiskImage
from ._models_py3 import GalleryIdentifier
from ._models_py3 import GalleryImage
from ._models_py3 import GalleryImageFeature
from ._models_py3 import GalleryImageIdentifier
from ._models_py3 import GalleryImageList
from ._models_py3 import GalleryImageUpdate
from ._models_py3 import GalleryImageVersion
from ._models_py3 import GalleryImageVersionList
from ._models_py3 import GalleryImageVersionPublishingProfile
from ._models_py3 import GalleryImageVersionStorageProfile
from ._models_py3 import GalleryImageVersionUpdate
from ._models_py3 import GalleryList
from ._models_py3 import GalleryOSDiskImage
from ._models_py3 import GalleryUpdate
from ._models_py3 import HardwareProfile
from ._models_py3 import Image
from ._models_py3 import ImageDataDisk
from ._models_py3 import ImageDisk
from ._models_py3 import ImageListResult
from ._models_py3 import ImageOSDisk
from ._models_py3 import ImagePurchasePlan
from ._models_py3 import ImageReference
from ._models_py3 import ImageStorageProfile
from ._models_py3 import ImageUpdate
from ._models_py3 import InnerError
from ._models_py3 import InstanceViewStatus
from ._models_py3 import KeyVaultKeyReference
from ._models_py3 import KeyVaultSecretReference
from ._models_py3 import LastPatchInstallationSummary
from ._models_py3 import LinuxConfiguration
from ._models_py3 import LinuxParameters
from ._models_py3 import LinuxPatchSettings
from ._models_py3 import ListUsagesResult
from ._models_py3 import LogAnalyticsInputBase
from ._models_py3 import LogAnalyticsOperationResult
from ._models_py3 import LogAnalyticsOutput
from ._models_py3 import MaintenanceRedeployStatus
from ._models_py3 import ManagedArtifact
from ._models_py3 import ManagedDiskParameters
from ._models_py3 import NetworkInterfaceReference
from ._models_py3 import NetworkProfile
from ._models_py3 import OSDisk
from ._models_py3 import OSDiskImage
from ._models_py3 import OSDiskImageEncryption
from ._models_py3 import OSProfile
from ._models_py3 import OrchestrationServiceStateInput
from ._models_py3 import OrchestrationServiceSummary
from ._models_py3 import PatchInstallationDetail
from ._models_py3 import PatchSettings
from ._models_py3 import PirCommunityGalleryResource
from ._models_py3 import PirResource
from ._models_py3 import PirSharedGalleryResource
from ._models_py3 import Plan
from ._models_py3 import ProximityPlacementGroup
from ._models_py3 import ProximityPlacementGroupListResult
from ._models_py3 import ProximityPlacementGroupUpdate
from ._models_py3 import ProxyResource
from ._models_py3 import PublicIPAddressSku
from ._models_py3 import PurchasePlan
from ._models_py3 import RecommendedMachineConfiguration
from ._models_py3 import RecoveryWalkResponse
from ._models_py3 import RegionalReplicationStatus
from ._models_py3 import ReplicationStatus
from ._models_py3 import RequestRateByIntervalInput
from ._models_py3 import Resource
from ._models_py3 import ResourceRange
from ._models_py3 import ResourceSku
from ._models_py3 import ResourceSkuCapabilities
from ._models_py3 import ResourceSkuCapacity
from ._models_py3 import ResourceSkuCosts
from ._models_py3 import ResourceSkuLocationInfo
from ._models_py3 import ResourceSkuRestrictionInfo
from ._models_py3 import ResourceSkuRestrictions
from ._models_py3 import ResourceSkuZoneDetails
from ._models_py3 import ResourceSkusResult
from ._models_py3 import RestorePoint
from ._models_py3 import RestorePointCollection
from ._models_py3 import RestorePointCollectionListResult
from ._models_py3 import RestorePointCollectionSourceProperties
from ._models_py3 import RestorePointCollectionUpdate
from ._models_py3 import RestorePointSourceMetadata
from ._models_py3 import RestorePointSourceVMDataDisk
from ._models_py3 import RestorePointSourceVMOSDisk
from ._models_py3 import RestorePointSourceVMStorageProfile
from ._models_py3 import RetrieveBootDiagnosticsDataResult
from ._models_py3 import RollbackStatusInfo
from ._models_py3 import RollingUpgradePolicy
from ._models_py3 import RollingUpgradeProgressInfo
from ._models_py3 import RollingUpgradeRunningStatus
from ._models_py3 import RollingUpgradeStatusInfo
from ._models_py3 import RunCommandDocument
from ._models_py3 import RunCommandDocumentBase
from ._models_py3 import RunCommandInput
from ._models_py3 import RunCommandInputParameter
from ._models_py3 import RunCommandListResult
from ._models_py3 import RunCommandParameterDefinition
from ._models_py3 import RunCommandResult
from ._models_py3 import ScaleInPolicy
from ._models_py3 import ScheduledEventsProfile
from ._models_py3 import SecurityProfile
from ._models_py3 import SharedGallery
from ._models_py3 import SharedGalleryImage
from ._models_py3 import SharedGalleryImageList
from ._models_py3 import SharedGalleryImageVersion
from ._models_py3 import SharedGalleryImageVersionList
from ._models_py3 import SharedGalleryList
from ._models_py3 import SharingProfile
from ._models_py3 import SharingProfileGroup
from ._models_py3 import SharingUpdate
from ._models_py3 import Sku
from ._models_py3 import SoftDeletePolicy
from ._models_py3 import SpotRestorePolicy
from ._models_py3 import SshConfiguration
from ._models_py3 import SshPublicKey
from ._models_py3 import SshPublicKeyGenerateKeyPairResult
from ._models_py3 import SshPublicKeyResource
from ._models_py3 import SshPublicKeyUpdateResource
from ._models_py3 import SshPublicKeysGroupListResult
from ._models_py3 import StorageProfile
from ._models_py3 import SubResource
from ._models_py3 import SubResourceReadOnly
from ._models_py3 import SubResourceWithColocationStatus
from ._models_py3 import TargetRegion
from ._models_py3 import TerminateNotificationProfile
from ._models_py3 import ThrottledRequestsInput
from ._models_py3 import UefiSettings
from ._models_py3 import UpdateResource
from ._models_py3 import UpdateResourceDefinition
from ._models_py3 import UpgradeOperationHistoricalStatusInfo
from ._models_py3 import UpgradeOperationHistoricalStatusInfoProperties
from ._models_py3 import UpgradeOperationHistoryStatus
from ._models_py3 import UpgradePolicy
from ._models_py3 import Usage
from ._models_py3 import UsageName
from ._models_py3 import UserArtifactManage
from ._models_py3 import UserArtifactSource
from ._models_py3 import UserAssignedIdentitiesValue
from ._models_py3 import VMGalleryApplication
from ._models_py3 import VMScaleSetConvertToSinglePlacementGroupInput
from ._models_py3 import VMSizeProperties
from ._models_py3 import VaultCertificate
from ._models_py3 import VaultSecretGroup
from ._models_py3 import VirtualHardDisk
from ._models_py3 import VirtualMachine
from ._models_py3 import VirtualMachineAgentInstanceView
from ._models_py3 import VirtualMachineAssessPatchesResult
from ._models_py3 import VirtualMachineCaptureParameters
from ._models_py3 import VirtualMachineCaptureResult
from ._models_py3 import VirtualMachineExtension
from ._models_py3 import VirtualMachineExtensionHandlerInstanceView
from ._models_py3 import VirtualMachineExtensionImage
from ._models_py3 import VirtualMachineExtensionInstanceView
from ._models_py3 import VirtualMachineExtensionUpdate
from ._models_py3 import VirtualMachineExtensionsListResult
from ._models_py3 import VirtualMachineHealthStatus
from ._models_py3 import VirtualMachineIdentity
from ._models_py3 import VirtualMachineImage
from ._models_py3 import VirtualMachineImageFeature
from ._models_py3 import VirtualMachineImageResource
from ._models_py3 import VirtualMachineInstallPatchesParameters
from ._models_py3 import VirtualMachineInstallPatchesResult
from ._models_py3 import VirtualMachineInstanceView
from ._models_py3 import VirtualMachineIpTag
from ._models_py3 import VirtualMachineListResult
from ._models_py3 import VirtualMachineNetworkInterfaceConfiguration
from ._models_py3 import VirtualMachineNetworkInterfaceDnsSettingsConfiguration
from ._models_py3 import VirtualMachineNetworkInterfaceIPConfiguration
from ._models_py3 import VirtualMachinePatchStatus
from ._models_py3 import VirtualMachinePublicIPAddressConfiguration
from ._models_py3 import VirtualMachinePublicIPAddressDnsSettingsConfiguration
from ._models_py3 import VirtualMachineReimageParameters
from ._models_py3 import VirtualMachineRunCommand
from ._models_py3 import VirtualMachineRunCommandInstanceView
from ._models_py3 import VirtualMachineRunCommandScriptSource
from ._models_py3 import VirtualMachineRunCommandUpdate
from ._models_py3 import VirtualMachineRunCommandsListResult
from ._models_py3 import VirtualMachineScaleSet
from ._models_py3 import VirtualMachineScaleSetDataDisk
from ._models_py3 import VirtualMachineScaleSetExtension
from ._models_py3 import VirtualMachineScaleSetExtensionListResult
from ._models_py3 import VirtualMachineScaleSetExtensionProfile
from ._models_py3 import VirtualMachineScaleSetExtensionUpdate
from ._models_py3 import VirtualMachineScaleSetIPConfiguration
from ._models_py3 import VirtualMachineScaleSetIdentity
from ._models_py3 import VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue
from ._models_py3 import VirtualMachineScaleSetInstanceView
from ._models_py3 import VirtualMachineScaleSetInstanceViewStatusesSummary
from ._models_py3 import VirtualMachineScaleSetIpTag
from ._models_py3 import VirtualMachineScaleSetListOSUpgradeHistory
from ._models_py3 import VirtualMachineScaleSetListResult
from ._models_py3 import VirtualMachineScaleSetListSkusResult
from ._models_py3 import VirtualMachineScaleSetListWithLinkResult
from ._models_py3 import VirtualMachineScaleSetManagedDiskParameters
from ._models_py3 import VirtualMachineScaleSetNetworkConfiguration
from ._models_py3 import VirtualMachineScaleSetNetworkConfigurationDnsSettings
from ._models_py3 import VirtualMachineScaleSetNetworkProfile
from ._models_py3 import VirtualMachineScaleSetOSDisk
from ._models_py3 import VirtualMachineScaleSetOSProfile
from ._models_py3 import VirtualMachineScaleSetPublicIPAddressConfiguration
from ._models_py3 import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
from ._models_py3 import VirtualMachineScaleSetReimageParameters
from ._models_py3 import VirtualMachineScaleSetSku
from ._models_py3 import VirtualMachineScaleSetSkuCapacity
from ._models_py3 import VirtualMachineScaleSetStorageProfile
from ._models_py3 import VirtualMachineScaleSetUpdate
from ._models_py3 import VirtualMachineScaleSetUpdateIPConfiguration
from ._models_py3 import VirtualMachineScaleSetUpdateNetworkConfiguration
from ._models_py3 import VirtualMachineScaleSetUpdateNetworkProfile
from ._models_py3 import VirtualMachineScaleSetUpdateOSDisk
from ._models_py3 import VirtualMachineScaleSetUpdateOSProfile
from ._models_py3 import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
from ._models_py3 import VirtualMachineScaleSetUpdateStorageProfile
from ._models_py3 import VirtualMachineScaleSetUpdateVMProfile
from ._models_py3 import VirtualMachineScaleSetVM
from ._models_py3 import VirtualMachineScaleSetVMExtension
from ._models_py3 import VirtualMachineScaleSetVMExtensionUpdate
from ._models_py3 import VirtualMachineScaleSetVMExtensionsListResult
from ._models_py3 import VirtualMachineScaleSetVMExtensionsSummary
from ._models_py3 import VirtualMachineScaleSetVMInstanceIDs
from ._models_py3 import VirtualMachineScaleSetVMInstanceRequiredIDs
from ._models_py3 import VirtualMachineScaleSetVMInstanceView
from ._models_py3 import VirtualMachineScaleSetVMListResult
from ._models_py3 import VirtualMachineScaleSetVMNetworkProfileConfiguration
from ._models_py3 import VirtualMachineScaleSetVMProfile
from ._models_py3 import VirtualMachineScaleSetVMProtectionPolicy
from ._models_py3 import VirtualMachineScaleSetVMReimageParameters
from ._models_py3 import VirtualMachineSize
from ._models_py3 import VirtualMachineSizeListResult
from ._models_py3 import VirtualMachineSoftwarePatchProperties
from ._models_py3 import VirtualMachineStatusCodeCount
from ._models_py3 import VirtualMachineUpdate
from ._models_py3 import WinRMConfiguration
from ._models_py3 import WinRMListener
from ._models_py3 import WindowsConfiguration
from ._models_py3 import WindowsParameters

from ._compute_management_client_enums import AggregatedReplicationState
from ._compute_management_client_enums import AvailabilitySetSkuTypes
from ._compute_management_client_enums import CachingTypes
from ._compute_management_client_enums import CapacityReservationGroupInstanceViewTypes
from ._compute_management_client_enums import CapacityReservationInstanceViewTypes
from ._compute_management_client_enums import ConsistencyModeTypes
from ._compute_management_client_enums import DedicatedHostLicenseTypes
from ._compute_management_client_enums import DeleteOptions
from ._compute_management_client_enums import DiffDiskOptions
from ._compute_management_client_enums import DiffDiskPlacement
from ._compute_management_client_enums import DiskCreateOptionTypes
from ._compute_management_client_enums import DiskDeleteOptionTypes
from ._compute_management_client_enums import DiskDetachOptionTypes
from ._compute_management_client_enums import ExecutionState
from ._compute_management_client_enums import ExpandTypesForGetCapacityReservationGroups
from ._compute_management_client_enums import ExpandTypesForGetVMScaleSets
from ._compute_management_client_enums import ExtendedLocationType
from ._compute_management_client_enums import ExtendedLocationTypes
from ._compute_management_client_enums import GalleryApplicationVersionPropertiesProvisioningState
from ._compute_management_client_enums import GalleryImagePropertiesProvisioningState
from ._compute_management_client_enums import GalleryImageVersionPropertiesProvisioningState
from ._compute_management_client_enums import GalleryPropertiesProvisioningState
from ._compute_management_client_enums import GallerySharingPermissionTypes
from ._compute_management_client_enums import HostCaching
from ._compute_management_client_enums import HyperVGeneration
from ._compute_management_client_enums import HyperVGenerationType
from ._compute_management_client_enums import HyperVGenerationTypes
from ._compute_management_client_enums import IPVersion
from ._compute_management_client_enums import IPVersions
from ._compute_management_client_enums import InstanceViewTypes
from ._compute_management_client_enums import IntervalInMins
from ._compute_management_client_enums import LinuxPatchAssessmentMode
from ._compute_management_client_enums import LinuxVMGuestPatchMode
from ._compute_management_client_enums import MaintenanceOperationResultCodeTypes
from ._compute_management_client_enums import NetworkApiVersion
from ._compute_management_client_enums import OperatingSystemStateTypes
from ._compute_management_client_enums import OperatingSystemType
from ._compute_management_client_enums import OperatingSystemTypes
from ._compute_management_client_enums import OrchestrationMode
from ._compute_management_client_enums import OrchestrationServiceNames
from ._compute_management_client_enums import OrchestrationServiceState
from ._compute_management_client_enums import OrchestrationServiceStateAction
from ._compute_management_client_enums import PatchAssessmentState
from ._compute_management_client_enums import PatchInstallationState
from ._compute_management_client_enums import PatchOperationStatus
from ._compute_management_client_enums import ProtocolTypes
from ._compute_management_client_enums import ProximityPlacementGroupType
from ._compute_management_client_enums import PublicIPAddressSkuName
from ._compute_management_client_enums import PublicIPAddressSkuTier
from ._compute_management_client_enums import PublicIPAllocationMethod
from ._compute_management_client_enums import ReplicationMode
from ._compute_management_client_enums import ReplicationState
from ._compute_management_client_enums import ReplicationStatusTypes
from ._compute_management_client_enums import ResourceIdentityType
from ._compute_management_client_enums import ResourceSkuCapacityScaleType
from ._compute_management_client_enums import ResourceSkuRestrictionsReasonCode
from ._compute_management_client_enums import ResourceSkuRestrictionsType
from ._compute_management_client_enums import RestorePointCollectionExpandOptions
from ._compute_management_client_enums import RollingUpgradeActionType
from ._compute_management_client_enums import RollingUpgradeStatusCode
from ._compute_management_client_enums import SecurityTypes
from ._compute_management_client_enums import SelectPermissions
from ._compute_management_client_enums import SettingNames
from ._compute_management_client_enums import SharedToValues
from ._compute_management_client_enums import SharingProfileGroupTypes
from ._compute_management_client_enums import SharingUpdateOperationTypes
from ._compute_management_client_enums import StatusLevelTypes
from ._compute_management_client_enums import StorageAccountType
from ._compute_management_client_enums import StorageAccountTypes
from ._compute_management_client_enums import UpgradeMode
from ._compute_management_client_enums import UpgradeOperationInvoker
from ._compute_management_client_enums import UpgradeState
from ._compute_management_client_enums import VMGuestPatchClassificationLinux
from ._compute_management_client_enums import VMGuestPatchClassificationWindows
from ._compute_management_client_enums import VMGuestPatchRebootBehavior
from ._compute_management_client_enums import VMGuestPatchRebootSetting
from ._compute_management_client_enums import VMGuestPatchRebootStatus
from ._compute_management_client_enums import VirtualMachineEvictionPolicyTypes
from ._compute_management_client_enums import VirtualMachinePriorityTypes
from ._compute_management_client_enums import VirtualMachineScaleSetScaleInRules
from ._compute_management_client_enums import VirtualMachineScaleSetSkuScaleType
from ._compute_management_client_enums import VirtualMachineSizeTypes
from ._compute_management_client_enums import VmDiskTypes
from ._compute_management_client_enums import WindowsPatchAssessmentMode
from ._compute_management_client_enums import WindowsVMGuestPatchMode
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AdditionalCapabilities",
    "AdditionalUnattendContent",
    "ApiEntityReference",
    "ApiError",
    "ApiErrorBase",
    "ApplicationProfile",
    "AutomaticOSUpgradePolicy",
    "AutomaticOSUpgradeProperties",
    "AutomaticRepairsPolicy",
    "AvailabilitySet",
    "AvailabilitySetListResult",
    "AvailabilitySetUpdate",
    "AvailablePatchSummary",
    "BillingProfile",
    "BootDiagnostics",
    "BootDiagnosticsInstanceView",
    "CapacityReservation",
    "CapacityReservationGroup",
    "CapacityReservationGroupInstanceView",
    "CapacityReservationGroupListResult",
    "CapacityReservationGroupUpdate",
    "CapacityReservationInstanceView",
    "CapacityReservationInstanceViewWithName",
    "CapacityReservationListResult",
    "CapacityReservationProfile",
    "CapacityReservationUpdate",
    "CapacityReservationUtilization",
    "CommunityGallery",
    "CommunityGalleryImage",
    "CommunityGalleryImageVersion",
    "ComputeOperationListResult",
    "ComputeOperationValue",
    "DataDisk",
    "DataDiskImage",
    "DataDiskImageEncryption",
    "DedicatedHost",
    "DedicatedHostAllocatableVM",
    "DedicatedHostAvailableCapacity",
    "DedicatedHostGroup",
    "DedicatedHostGroupInstanceView",
    "DedicatedHostGroupListResult",
    "DedicatedHostGroupUpdate",
    "DedicatedHostInstanceView",
    "DedicatedHostInstanceViewWithName",
    "DedicatedHostListResult",
    "DedicatedHostUpdate",
    "DiagnosticsProfile",
    "DiffDiskSettings",
    "Disallowed",
    "DisallowedConfiguration",
    "DiskEncryptionSetParameters",
    "DiskEncryptionSettings",
    "DiskImageEncryption",
    "DiskInstanceView",
    "EncryptionImages",
    "ExtendedLocation",
    "Gallery",
    "GalleryApplication",
    "GalleryApplicationList",
    "GalleryApplicationUpdate",
    "GalleryApplicationVersion",
    "GalleryApplicationVersionList",
    "GalleryApplicationVersionPublishingProfile",
    "GalleryApplicationVersionUpdate",
    "GalleryArtifactPublishingProfileBase",
    "GalleryArtifactSource",
    "GalleryArtifactVersionSource",
    "GalleryDataDiskImage",
    "GalleryDiskImage",
    "GalleryIdentifier",
    "GalleryImage",
    "GalleryImageFeature",
    "GalleryImageIdentifier",
    "GalleryImageList",
    "GalleryImageUpdate",
    "GalleryImageVersion",
    "GalleryImageVersionList",
    "GalleryImageVersionPublishingProfile",
    "GalleryImageVersionStorageProfile",
    "GalleryImageVersionUpdate",
    "GalleryList",
    "GalleryOSDiskImage",
    "GalleryUpdate",
    "HardwareProfile",
    "Image",
    "ImageDataDisk",
    "ImageDisk",
    "ImageListResult",
    "ImageOSDisk",
    "ImagePurchasePlan",
    "ImageReference",
    "ImageStorageProfile",
    "ImageUpdate",
    "InnerError",
    "InstanceViewStatus",
    "KeyVaultKeyReference",
    "KeyVaultSecretReference",
    "LastPatchInstallationSummary",
    "LinuxConfiguration",
    "LinuxParameters",
    "LinuxPatchSettings",
    "ListUsagesResult",
    "LogAnalyticsInputBase",
    "LogAnalyticsOperationResult",
    "LogAnalyticsOutput",
    "MaintenanceRedeployStatus",
    "ManagedArtifact",
    "ManagedDiskParameters",
    "NetworkInterfaceReference",
    "NetworkProfile",
    "OSDisk",
    "OSDiskImage",
    "OSDiskImageEncryption",
    "OSProfile",
    "OrchestrationServiceStateInput",
    "OrchestrationServiceSummary",
    "PatchInstallationDetail",
    "PatchSettings",
    "PirCommunityGalleryResource",
    "PirResource",
    "PirSharedGalleryResource",
    "Plan",
    "ProximityPlacementGroup",
    "ProximityPlacementGroupListResult",
    "ProximityPlacementGroupUpdate",
    "ProxyResource",
    "PublicIPAddressSku",
    "PurchasePlan",
    "RecommendedMachineConfiguration",
    "RecoveryWalkResponse",
    "RegionalReplicationStatus",
    "ReplicationStatus",
    "RequestRateByIntervalInput",
    "Resource",
    "ResourceRange",
    "ResourceSku",
    "ResourceSkuCapabilities",
    "ResourceSkuCapacity",
    "ResourceSkuCosts",
    "ResourceSkuLocationInfo",
    "ResourceSkuRestrictionInfo",
    "ResourceSkuRestrictions",
    "ResourceSkuZoneDetails",
    "ResourceSkusResult",
    "RestorePoint",
    "RestorePointCollection",
    "RestorePointCollectionListResult",
    "RestorePointCollectionSourceProperties",
    "RestorePointCollectionUpdate",
    "RestorePointSourceMetadata",
    "RestorePointSourceVMDataDisk",
    "RestorePointSourceVMOSDisk",
    "RestorePointSourceVMStorageProfile",
    "RetrieveBootDiagnosticsDataResult",
    "RollbackStatusInfo",
    "RollingUpgradePolicy",
    "RollingUpgradeProgressInfo",
    "RollingUpgradeRunningStatus",
    "RollingUpgradeStatusInfo",
    "RunCommandDocument",
    "RunCommandDocumentBase",
    "RunCommandInput",
    "RunCommandInputParameter",
    "RunCommandListResult",
    "RunCommandParameterDefinition",
    "RunCommandResult",
    "ScaleInPolicy",
    "ScheduledEventsProfile",
    "SecurityProfile",
    "SharedGallery",
    "SharedGalleryImage",
    "SharedGalleryImageList",
    "SharedGalleryImageVersion",
    "SharedGalleryImageVersionList",
    "SharedGalleryList",
    "SharingProfile",
    "SharingProfileGroup",
    "SharingUpdate",
    "Sku",
    "SoftDeletePolicy",
    "SpotRestorePolicy",
    "SshConfiguration",
    "SshPublicKey",
    "SshPublicKeyGenerateKeyPairResult",
    "SshPublicKeyResource",
    "SshPublicKeyUpdateResource",
    "SshPublicKeysGroupListResult",
    "StorageProfile",
    "SubResource",
    "SubResourceReadOnly",
    "SubResourceWithColocationStatus",
    "TargetRegion",
    "TerminateNotificationProfile",
    "ThrottledRequestsInput",
    "UefiSettings",
    "UpdateResource",
    "UpdateResourceDefinition",
    "UpgradeOperationHistoricalStatusInfo",
    "UpgradeOperationHistoricalStatusInfoProperties",
    "UpgradeOperationHistoryStatus",
    "UpgradePolicy",
    "Usage",
    "UsageName",
    "UserArtifactManage",
    "UserArtifactSource",
    "UserAssignedIdentitiesValue",
    "VMGalleryApplication",
    "VMScaleSetConvertToSinglePlacementGroupInput",
    "VMSizeProperties",
    "VaultCertificate",
    "VaultSecretGroup",
    "VirtualHardDisk",
    "VirtualMachine",
    "VirtualMachineAgentInstanceView",
    "VirtualMachineAssessPatchesResult",
    "VirtualMachineCaptureParameters",
    "VirtualMachineCaptureResult",
    "VirtualMachineExtension",
    "VirtualMachineExtensionHandlerInstanceView",
    "VirtualMachineExtensionImage",
    "VirtualMachineExtensionInstanceView",
    "VirtualMachineExtensionUpdate",
    "VirtualMachineExtensionsListResult",
    "VirtualMachineHealthStatus",
    "VirtualMachineIdentity",
    "VirtualMachineImage",
    "VirtualMachineImageFeature",
    "VirtualMachineImageResource",
    "VirtualMachineInstallPatchesParameters",
    "VirtualMachineInstallPatchesResult",
    "VirtualMachineInstanceView",
    "VirtualMachineIpTag",
    "VirtualMachineListResult",
    "VirtualMachineNetworkInterfaceConfiguration",
    "VirtualMachineNetworkInterfaceDnsSettingsConfiguration",
    "VirtualMachineNetworkInterfaceIPConfiguration",
    "VirtualMachinePatchStatus",
    "VirtualMachinePublicIPAddressConfiguration",
    "VirtualMachinePublicIPAddressDnsSettingsConfiguration",
    "VirtualMachineReimageParameters",
    "VirtualMachineRunCommand",
    "VirtualMachineRunCommandInstanceView",
    "VirtualMachineRunCommandScriptSource",
    "VirtualMachineRunCommandUpdate",
    "VirtualMachineRunCommandsListResult",
    "VirtualMachineScaleSet",
    "VirtualMachineScaleSetDataDisk",
    "VirtualMachineScaleSetExtension",
    "VirtualMachineScaleSetExtensionListResult",
    "VirtualMachineScaleSetExtensionProfile",
    "VirtualMachineScaleSetExtensionUpdate",
    "VirtualMachineScaleSetIPConfiguration",
    "VirtualMachineScaleSetIdentity",
    "VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue",
    "VirtualMachineScaleSetInstanceView",
    "VirtualMachineScaleSetInstanceViewStatusesSummary",
    "VirtualMachineScaleSetIpTag",
    "VirtualMachineScaleSetListOSUpgradeHistory",
    "VirtualMachineScaleSetListResult",
    "VirtualMachineScaleSetListSkusResult",
    "VirtualMachineScaleSetListWithLinkResult",
    "VirtualMachineScaleSetManagedDiskParameters",
    "VirtualMachineScaleSetNetworkConfiguration",
    "VirtualMachineScaleSetNetworkConfigurationDnsSettings",
    "VirtualMachineScaleSetNetworkProfile",
    "VirtualMachineScaleSetOSDisk",
    "VirtualMachineScaleSetOSProfile",
    "VirtualMachineScaleSetPublicIPAddressConfiguration",
    "VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings",
    "VirtualMachineScaleSetReimageParameters",
    "VirtualMachineScaleSetSku",
    "VirtualMachineScaleSetSkuCapacity",
    "VirtualMachineScaleSetStorageProfile",
    "VirtualMachineScaleSetUpdate",
    "VirtualMachineScaleSetUpdateIPConfiguration",
    "VirtualMachineScaleSetUpdateNetworkConfiguration",
    "VirtualMachineScaleSetUpdateNetworkProfile",
    "VirtualMachineScaleSetUpdateOSDisk",
    "VirtualMachineScaleSetUpdateOSProfile",
    "VirtualMachineScaleSetUpdatePublicIPAddressConfiguration",
    "VirtualMachineScaleSetUpdateStorageProfile",
    "VirtualMachineScaleSetUpdateVMProfile",
    "VirtualMachineScaleSetVM",
    "VirtualMachineScaleSetVMExtension",
    "VirtualMachineScaleSetVMExtensionUpdate",
    "VirtualMachineScaleSetVMExtensionsListResult",
    "VirtualMachineScaleSetVMExtensionsSummary",
    "VirtualMachineScaleSetVMInstanceIDs",
    "VirtualMachineScaleSetVMInstanceRequiredIDs",
    "VirtualMachineScaleSetVMInstanceView",
    "VirtualMachineScaleSetVMListResult",
    "VirtualMachineScaleSetVMNetworkProfileConfiguration",
    "VirtualMachineScaleSetVMProfile",
    "VirtualMachineScaleSetVMProtectionPolicy",
    "VirtualMachineScaleSetVMReimageParameters",
    "VirtualMachineSize",
    "VirtualMachineSizeListResult",
    "VirtualMachineSoftwarePatchProperties",
    "VirtualMachineStatusCodeCount",
    "VirtualMachineUpdate",
    "WinRMConfiguration",
    "WinRMListener",
    "WindowsConfiguration",
    "WindowsParameters",
    "AggregatedReplicationState",
    "AvailabilitySetSkuTypes",
    "CachingTypes",
    "CapacityReservationGroupInstanceViewTypes",
    "CapacityReservationInstanceViewTypes",
    "ConsistencyModeTypes",
    "DedicatedHostLicenseTypes",
    "DeleteOptions",
    "DiffDiskOptions",
    "DiffDiskPlacement",
    "DiskCreateOptionTypes",
    "DiskDeleteOptionTypes",
    "DiskDetachOptionTypes",
    "ExecutionState",
    "ExpandTypesForGetCapacityReservationGroups",
    "ExpandTypesForGetVMScaleSets",
    "ExtendedLocationType",
    "ExtendedLocationTypes",
    "GalleryApplicationVersionPropertiesProvisioningState",
    "GalleryImagePropertiesProvisioningState",
    "GalleryImageVersionPropertiesProvisioningState",
    "GalleryPropertiesProvisioningState",
    "GallerySharingPermissionTypes",
    "HostCaching",
    "HyperVGeneration",
    "HyperVGenerationType",
    "HyperVGenerationTypes",
    "IPVersion",
    "IPVersions",
    "InstanceViewTypes",
    "IntervalInMins",
    "LinuxPatchAssessmentMode",
    "LinuxVMGuestPatchMode",
    "MaintenanceOperationResultCodeTypes",
    "NetworkApiVersion",
    "OperatingSystemStateTypes",
    "OperatingSystemType",
    "OperatingSystemTypes",
    "OrchestrationMode",
    "OrchestrationServiceNames",
    "OrchestrationServiceState",
    "OrchestrationServiceStateAction",
    "PatchAssessmentState",
    "PatchInstallationState",
    "PatchOperationStatus",
    "ProtocolTypes",
    "ProximityPlacementGroupType",
    "PublicIPAddressSkuName",
    "PublicIPAddressSkuTier",
    "PublicIPAllocationMethod",
    "ReplicationMode",
    "ReplicationState",
    "ReplicationStatusTypes",
    "ResourceIdentityType",
    "ResourceSkuCapacityScaleType",
    "ResourceSkuRestrictionsReasonCode",
    "ResourceSkuRestrictionsType",
    "RestorePointCollectionExpandOptions",
    "RollingUpgradeActionType",
    "RollingUpgradeStatusCode",
    "SecurityTypes",
    "SelectPermissions",
    "SettingNames",
    "SharedToValues",
    "SharingProfileGroupTypes",
    "SharingUpdateOperationTypes",
    "StatusLevelTypes",
    "StorageAccountType",
    "StorageAccountTypes",
    "UpgradeMode",
    "UpgradeOperationInvoker",
    "UpgradeState",
    "VMGuestPatchClassificationLinux",
    "VMGuestPatchClassificationWindows",
    "VMGuestPatchRebootBehavior",
    "VMGuestPatchRebootSetting",
    "VMGuestPatchRebootStatus",
    "VirtualMachineEvictionPolicyTypes",
    "VirtualMachinePriorityTypes",
    "VirtualMachineScaleSetScaleInRules",
    "VirtualMachineScaleSetSkuScaleType",
    "VirtualMachineSizeTypes",
    "VmDiskTypes",
    "WindowsPatchAssessmentMode",
    "WindowsVMGuestPatchMode",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
