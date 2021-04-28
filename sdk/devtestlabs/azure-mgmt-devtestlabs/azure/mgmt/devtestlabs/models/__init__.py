# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ApplicableSchedule
    from ._models_py3 import ApplicableScheduleFragment
    from ._models_py3 import ApplyArtifactsRequest
    from ._models_py3 import ArmTemplate
    from ._models_py3 import ArmTemplateInfo
    from ._models_py3 import ArmTemplateList
    from ._models_py3 import ArmTemplateParameterProperties
    from ._models_py3 import Artifact
    from ._models_py3 import ArtifactDeploymentStatusProperties
    from ._models_py3 import ArtifactInstallProperties
    from ._models_py3 import ArtifactList
    from ._models_py3 import ArtifactParameterProperties
    from ._models_py3 import ArtifactSource
    from ._models_py3 import ArtifactSourceFragment
    from ._models_py3 import ArtifactSourceList
    from ._models_py3 import AttachDiskProperties
    from ._models_py3 import AttachNewDataDiskOptions
    from ._models_py3 import BulkCreationParameters
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import ComputeDataDisk
    from ._models_py3 import ComputeVmInstanceViewStatus
    from ._models_py3 import ComputeVmProperties
    from ._models_py3 import CostThresholdProperties
    from ._models_py3 import CustomImage
    from ._models_py3 import CustomImageFragment
    from ._models_py3 import CustomImageList
    from ._models_py3 import CustomImagePropertiesCustom
    from ._models_py3 import CustomImagePropertiesFromPlan
    from ._models_py3 import CustomImagePropertiesFromVm
    from ._models_py3 import DataDiskProperties
    from ._models_py3 import DataDiskStorageTypeInfo
    from ._models_py3 import DayDetails
    from ._models_py3 import DetachDataDiskProperties
    from ._models_py3 import DetachDiskProperties
    from ._models_py3 import Disk
    from ._models_py3 import DiskFragment
    from ._models_py3 import DiskList
    from ._models_py3 import DtlEnvironment
    from ._models_py3 import DtlEnvironmentFragment
    from ._models_py3 import DtlEnvironmentList
    from ._models_py3 import EnvironmentDeploymentProperties
    from ._models_py3 import EvaluatePoliciesProperties
    from ._models_py3 import EvaluatePoliciesRequest
    from ._models_py3 import EvaluatePoliciesResponse
    from ._models_py3 import Event
    from ._models_py3 import ExportResourceUsageParameters
    from ._models_py3 import ExternalSubnet
    from ._models_py3 import Formula
    from ._models_py3 import FormulaFragment
    from ._models_py3 import FormulaList
    from ._models_py3 import FormulaPropertiesFromVm
    from ._models_py3 import GalleryImage
    from ._models_py3 import GalleryImageList
    from ._models_py3 import GalleryImageReference
    from ._models_py3 import GenerateArmTemplateRequest
    from ._models_py3 import GenerateUploadUriParameter
    from ._models_py3 import GenerateUploadUriResponse
    from ._models_py3 import HourDetails
    from ._models_py3 import IdentityProperties
    from ._models_py3 import ImportLabVirtualMachineRequest
    from ._models_py3 import InboundNatRule
    from ._models_py3 import Lab
    from ._models_py3 import LabAnnouncementProperties
    from ._models_py3 import LabCost
    from ._models_py3 import LabCostDetailsProperties
    from ._models_py3 import LabCostSummaryProperties
    from ._models_py3 import LabFragment
    from ._models_py3 import LabList
    from ._models_py3 import LabResourceCostProperties
    from ._models_py3 import LabSupportProperties
    from ._models_py3 import LabVhd
    from ._models_py3 import LabVhdList
    from ._models_py3 import LabVirtualMachine
    from ._models_py3 import LabVirtualMachineCreationParameter
    from ._models_py3 import LabVirtualMachineFragment
    from ._models_py3 import LabVirtualMachineList
    from ._models_py3 import LinuxOsInfo
    from ._models_py3 import NetworkInterfaceProperties
    from ._models_py3 import NotificationChannel
    from ._models_py3 import NotificationChannelFragment
    from ._models_py3 import NotificationChannelList
    from ._models_py3 import NotificationSettings
    from ._models_py3 import NotifyParameters
    from ._models_py3 import OperationError
    from ._models_py3 import OperationMetadata
    from ._models_py3 import OperationMetadataDisplay
    from ._models_py3 import OperationResult
    from ._models_py3 import ParameterInfo
    from ._models_py3 import ParametersValueFileInfo
    from ._models_py3 import PercentageCostThresholdProperties
    from ._models_py3 import Policy
    from ._models_py3 import PolicyFragment
    from ._models_py3 import PolicyList
    from ._models_py3 import PolicySetResult
    from ._models_py3 import PolicyViolation
    from ._models_py3 import Port
    from ._models_py3 import ProviderOperationResult
    from ._models_py3 import RdpConnection
    from ._models_py3 import ResizeLabVirtualMachineProperties
    from ._models_py3 import Resource
    from ._models_py3 import RetargetScheduleProperties
    from ._models_py3 import Schedule
    from ._models_py3 import ScheduleCreationParameter
    from ._models_py3 import ScheduleFragment
    from ._models_py3 import ScheduleList
    from ._models_py3 import Secret
    from ._models_py3 import SecretFragment
    from ._models_py3 import SecretList
    from ._models_py3 import ServiceFabric
    from ._models_py3 import ServiceFabricFragment
    from ._models_py3 import ServiceFabricList
    from ._models_py3 import ServiceRunner
    from ._models_py3 import ServiceRunnerList
    from ._models_py3 import SharedPublicIpAddressConfiguration
    from ._models_py3 import ShutdownNotificationContent
    from ._models_py3 import Subnet
    from ._models_py3 import SubnetOverride
    from ._models_py3 import SubnetSharedPublicIpAddressConfiguration
    from ._models_py3 import TargetCostProperties
    from ._models_py3 import UpdateResource
    from ._models_py3 import User
    from ._models_py3 import UserFragment
    from ._models_py3 import UserIdentity
    from ._models_py3 import UserList
    from ._models_py3 import UserSecretStore
    from ._models_py3 import VirtualNetwork
    from ._models_py3 import VirtualNetworkFragment
    from ._models_py3 import VirtualNetworkList
    from ._models_py3 import WeekDetails
    from ._models_py3 import WindowsOsInfo
except (SyntaxError, ImportError):
    from ._models import ApplicableSchedule  # type: ignore
    from ._models import ApplicableScheduleFragment  # type: ignore
    from ._models import ApplyArtifactsRequest  # type: ignore
    from ._models import ArmTemplate  # type: ignore
    from ._models import ArmTemplateInfo  # type: ignore
    from ._models import ArmTemplateList  # type: ignore
    from ._models import ArmTemplateParameterProperties  # type: ignore
    from ._models import Artifact  # type: ignore
    from ._models import ArtifactDeploymentStatusProperties  # type: ignore
    from ._models import ArtifactInstallProperties  # type: ignore
    from ._models import ArtifactList  # type: ignore
    from ._models import ArtifactParameterProperties  # type: ignore
    from ._models import ArtifactSource  # type: ignore
    from ._models import ArtifactSourceFragment  # type: ignore
    from ._models import ArtifactSourceList  # type: ignore
    from ._models import AttachDiskProperties  # type: ignore
    from ._models import AttachNewDataDiskOptions  # type: ignore
    from ._models import BulkCreationParameters  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import ComputeDataDisk  # type: ignore
    from ._models import ComputeVmInstanceViewStatus  # type: ignore
    from ._models import ComputeVmProperties  # type: ignore
    from ._models import CostThresholdProperties  # type: ignore
    from ._models import CustomImage  # type: ignore
    from ._models import CustomImageFragment  # type: ignore
    from ._models import CustomImageList  # type: ignore
    from ._models import CustomImagePropertiesCustom  # type: ignore
    from ._models import CustomImagePropertiesFromPlan  # type: ignore
    from ._models import CustomImagePropertiesFromVm  # type: ignore
    from ._models import DataDiskProperties  # type: ignore
    from ._models import DataDiskStorageTypeInfo  # type: ignore
    from ._models import DayDetails  # type: ignore
    from ._models import DetachDataDiskProperties  # type: ignore
    from ._models import DetachDiskProperties  # type: ignore
    from ._models import Disk  # type: ignore
    from ._models import DiskFragment  # type: ignore
    from ._models import DiskList  # type: ignore
    from ._models import DtlEnvironment  # type: ignore
    from ._models import DtlEnvironmentFragment  # type: ignore
    from ._models import DtlEnvironmentList  # type: ignore
    from ._models import EnvironmentDeploymentProperties  # type: ignore
    from ._models import EvaluatePoliciesProperties  # type: ignore
    from ._models import EvaluatePoliciesRequest  # type: ignore
    from ._models import EvaluatePoliciesResponse  # type: ignore
    from ._models import Event  # type: ignore
    from ._models import ExportResourceUsageParameters  # type: ignore
    from ._models import ExternalSubnet  # type: ignore
    from ._models import Formula  # type: ignore
    from ._models import FormulaFragment  # type: ignore
    from ._models import FormulaList  # type: ignore
    from ._models import FormulaPropertiesFromVm  # type: ignore
    from ._models import GalleryImage  # type: ignore
    from ._models import GalleryImageList  # type: ignore
    from ._models import GalleryImageReference  # type: ignore
    from ._models import GenerateArmTemplateRequest  # type: ignore
    from ._models import GenerateUploadUriParameter  # type: ignore
    from ._models import GenerateUploadUriResponse  # type: ignore
    from ._models import HourDetails  # type: ignore
    from ._models import IdentityProperties  # type: ignore
    from ._models import ImportLabVirtualMachineRequest  # type: ignore
    from ._models import InboundNatRule  # type: ignore
    from ._models import Lab  # type: ignore
    from ._models import LabAnnouncementProperties  # type: ignore
    from ._models import LabCost  # type: ignore
    from ._models import LabCostDetailsProperties  # type: ignore
    from ._models import LabCostSummaryProperties  # type: ignore
    from ._models import LabFragment  # type: ignore
    from ._models import LabList  # type: ignore
    from ._models import LabResourceCostProperties  # type: ignore
    from ._models import LabSupportProperties  # type: ignore
    from ._models import LabVhd  # type: ignore
    from ._models import LabVhdList  # type: ignore
    from ._models import LabVirtualMachine  # type: ignore
    from ._models import LabVirtualMachineCreationParameter  # type: ignore
    from ._models import LabVirtualMachineFragment  # type: ignore
    from ._models import LabVirtualMachineList  # type: ignore
    from ._models import LinuxOsInfo  # type: ignore
    from ._models import NetworkInterfaceProperties  # type: ignore
    from ._models import NotificationChannel  # type: ignore
    from ._models import NotificationChannelFragment  # type: ignore
    from ._models import NotificationChannelList  # type: ignore
    from ._models import NotificationSettings  # type: ignore
    from ._models import NotifyParameters  # type: ignore
    from ._models import OperationError  # type: ignore
    from ._models import OperationMetadata  # type: ignore
    from ._models import OperationMetadataDisplay  # type: ignore
    from ._models import OperationResult  # type: ignore
    from ._models import ParameterInfo  # type: ignore
    from ._models import ParametersValueFileInfo  # type: ignore
    from ._models import PercentageCostThresholdProperties  # type: ignore
    from ._models import Policy  # type: ignore
    from ._models import PolicyFragment  # type: ignore
    from ._models import PolicyList  # type: ignore
    from ._models import PolicySetResult  # type: ignore
    from ._models import PolicyViolation  # type: ignore
    from ._models import Port  # type: ignore
    from ._models import ProviderOperationResult  # type: ignore
    from ._models import RdpConnection  # type: ignore
    from ._models import ResizeLabVirtualMachineProperties  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RetargetScheduleProperties  # type: ignore
    from ._models import Schedule  # type: ignore
    from ._models import ScheduleCreationParameter  # type: ignore
    from ._models import ScheduleFragment  # type: ignore
    from ._models import ScheduleList  # type: ignore
    from ._models import Secret  # type: ignore
    from ._models import SecretFragment  # type: ignore
    from ._models import SecretList  # type: ignore
    from ._models import ServiceFabric  # type: ignore
    from ._models import ServiceFabricFragment  # type: ignore
    from ._models import ServiceFabricList  # type: ignore
    from ._models import ServiceRunner  # type: ignore
    from ._models import ServiceRunnerList  # type: ignore
    from ._models import SharedPublicIpAddressConfiguration  # type: ignore
    from ._models import ShutdownNotificationContent  # type: ignore
    from ._models import Subnet  # type: ignore
    from ._models import SubnetOverride  # type: ignore
    from ._models import SubnetSharedPublicIpAddressConfiguration  # type: ignore
    from ._models import TargetCostProperties  # type: ignore
    from ._models import UpdateResource  # type: ignore
    from ._models import User  # type: ignore
    from ._models import UserFragment  # type: ignore
    from ._models import UserIdentity  # type: ignore
    from ._models import UserList  # type: ignore
    from ._models import UserSecretStore  # type: ignore
    from ._models import VirtualNetwork  # type: ignore
    from ._models import VirtualNetworkFragment  # type: ignore
    from ._models import VirtualNetworkList  # type: ignore
    from ._models import WeekDetails  # type: ignore
    from ._models import WindowsOsInfo  # type: ignore

from ._dev_test_labs_client_enums import (
    CostThresholdStatus,
    CostType,
    CustomImageOsType,
    EnableStatus,
    EnvironmentPermission,
    FileUploadOptions,
    HostCachingOptions,
    HttpStatusCode,
    LinuxOsState,
    ManagedIdentityType,
    NotificationChannelEventType,
    PolicyEvaluatorType,
    PolicyFactName,
    PolicyStatus,
    PremiumDataDisk,
    ReportingCycleType,
    SourceControlType,
    StorageType,
    TargetCostStatus,
    TransportProtocol,
    UsagePermissionType,
    VirtualMachineCreationSource,
    WindowsOsState,
)

__all__ = [
    'ApplicableSchedule',
    'ApplicableScheduleFragment',
    'ApplyArtifactsRequest',
    'ArmTemplate',
    'ArmTemplateInfo',
    'ArmTemplateList',
    'ArmTemplateParameterProperties',
    'Artifact',
    'ArtifactDeploymentStatusProperties',
    'ArtifactInstallProperties',
    'ArtifactList',
    'ArtifactParameterProperties',
    'ArtifactSource',
    'ArtifactSourceFragment',
    'ArtifactSourceList',
    'AttachDiskProperties',
    'AttachNewDataDiskOptions',
    'BulkCreationParameters',
    'CloudErrorBody',
    'ComputeDataDisk',
    'ComputeVmInstanceViewStatus',
    'ComputeVmProperties',
    'CostThresholdProperties',
    'CustomImage',
    'CustomImageFragment',
    'CustomImageList',
    'CustomImagePropertiesCustom',
    'CustomImagePropertiesFromPlan',
    'CustomImagePropertiesFromVm',
    'DataDiskProperties',
    'DataDiskStorageTypeInfo',
    'DayDetails',
    'DetachDataDiskProperties',
    'DetachDiskProperties',
    'Disk',
    'DiskFragment',
    'DiskList',
    'DtlEnvironment',
    'DtlEnvironmentFragment',
    'DtlEnvironmentList',
    'EnvironmentDeploymentProperties',
    'EvaluatePoliciesProperties',
    'EvaluatePoliciesRequest',
    'EvaluatePoliciesResponse',
    'Event',
    'ExportResourceUsageParameters',
    'ExternalSubnet',
    'Formula',
    'FormulaFragment',
    'FormulaList',
    'FormulaPropertiesFromVm',
    'GalleryImage',
    'GalleryImageList',
    'GalleryImageReference',
    'GenerateArmTemplateRequest',
    'GenerateUploadUriParameter',
    'GenerateUploadUriResponse',
    'HourDetails',
    'IdentityProperties',
    'ImportLabVirtualMachineRequest',
    'InboundNatRule',
    'Lab',
    'LabAnnouncementProperties',
    'LabCost',
    'LabCostDetailsProperties',
    'LabCostSummaryProperties',
    'LabFragment',
    'LabList',
    'LabResourceCostProperties',
    'LabSupportProperties',
    'LabVhd',
    'LabVhdList',
    'LabVirtualMachine',
    'LabVirtualMachineCreationParameter',
    'LabVirtualMachineFragment',
    'LabVirtualMachineList',
    'LinuxOsInfo',
    'NetworkInterfaceProperties',
    'NotificationChannel',
    'NotificationChannelFragment',
    'NotificationChannelList',
    'NotificationSettings',
    'NotifyParameters',
    'OperationError',
    'OperationMetadata',
    'OperationMetadataDisplay',
    'OperationResult',
    'ParameterInfo',
    'ParametersValueFileInfo',
    'PercentageCostThresholdProperties',
    'Policy',
    'PolicyFragment',
    'PolicyList',
    'PolicySetResult',
    'PolicyViolation',
    'Port',
    'ProviderOperationResult',
    'RdpConnection',
    'ResizeLabVirtualMachineProperties',
    'Resource',
    'RetargetScheduleProperties',
    'Schedule',
    'ScheduleCreationParameter',
    'ScheduleFragment',
    'ScheduleList',
    'Secret',
    'SecretFragment',
    'SecretList',
    'ServiceFabric',
    'ServiceFabricFragment',
    'ServiceFabricList',
    'ServiceRunner',
    'ServiceRunnerList',
    'SharedPublicIpAddressConfiguration',
    'ShutdownNotificationContent',
    'Subnet',
    'SubnetOverride',
    'SubnetSharedPublicIpAddressConfiguration',
    'TargetCostProperties',
    'UpdateResource',
    'User',
    'UserFragment',
    'UserIdentity',
    'UserList',
    'UserSecretStore',
    'VirtualNetwork',
    'VirtualNetworkFragment',
    'VirtualNetworkList',
    'WeekDetails',
    'WindowsOsInfo',
    'CostThresholdStatus',
    'CostType',
    'CustomImageOsType',
    'EnableStatus',
    'EnvironmentPermission',
    'FileUploadOptions',
    'HostCachingOptions',
    'HttpStatusCode',
    'LinuxOsState',
    'ManagedIdentityType',
    'NotificationChannelEventType',
    'PolicyEvaluatorType',
    'PolicyFactName',
    'PolicyStatus',
    'PremiumDataDisk',
    'ReportingCycleType',
    'SourceControlType',
    'StorageType',
    'TargetCostStatus',
    'TransportProtocol',
    'UsagePermissionType',
    'VirtualMachineCreationSource',
    'WindowsOsState',
]
