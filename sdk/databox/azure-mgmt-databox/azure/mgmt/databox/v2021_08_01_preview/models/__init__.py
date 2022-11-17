# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccountCredentialDetails
from ._models_py3 import AdditionalErrorInfo
from ._models_py3 import AddressValidationOutput
from ._models_py3 import AddressValidationProperties
from ._models_py3 import ApiError
from ._models_py3 import ApplianceNetworkConfiguration
from ._models_py3 import ArmBaseObject
from ._models_py3 import AvailableSkuRequest
from ._models_py3 import AvailableSkusResult
from ._models_py3 import AzureFileFilterDetails
from ._models_py3 import BlobFilterDetails
from ._models_py3 import CancellationReason
from ._models_py3 import CloudError
from ._models_py3 import ContactDetails
from ._models_py3 import CopyLogDetails
from ._models_py3 import CopyProgress
from ._models_py3 import CreateJobValidations
from ._models_py3 import CreateOrderLimitForSubscriptionValidationRequest
from ._models_py3 import CreateOrderLimitForSubscriptionValidationResponseProperties
from ._models_py3 import CustomerDiskJobSecrets
from ._models_py3 import DataAccountDetails
from ._models_py3 import DataBoxAccountCopyLogDetails
from ._models_py3 import DataBoxCustomerDiskCopyLogDetails
from ._models_py3 import DataBoxCustomerDiskCopyProgress
from ._models_py3 import DataBoxCustomerDiskJobDetails
from ._models_py3 import DataBoxDiskCopyLogDetails
from ._models_py3 import DataBoxDiskCopyProgress
from ._models_py3 import DataBoxDiskJobDetails
from ._models_py3 import DataBoxDiskJobSecrets
from ._models_py3 import DataBoxHeavyAccountCopyLogDetails
from ._models_py3 import DataBoxHeavyJobDetails
from ._models_py3 import DataBoxHeavyJobSecrets
from ._models_py3 import DataBoxHeavySecret
from ._models_py3 import DataBoxJobDetails
from ._models_py3 import DataBoxScheduleAvailabilityRequest
from ._models_py3 import DataBoxSecret
from ._models_py3 import DataExportDetails
from ._models_py3 import DataImportDetails
from ._models_py3 import DataLocationToServiceLocationMap
from ._models_py3 import DataTransferDetailsValidationRequest
from ._models_py3 import DataTransferDetailsValidationResponseProperties
from ._models_py3 import DataboxJobSecrets
from ._models_py3 import DatacenterAddressInstructionResponse
from ._models_py3 import DatacenterAddressLocationResponse
from ._models_py3 import DatacenterAddressRequest
from ._models_py3 import DatacenterAddressResponse
from ._models_py3 import DcAccessSecurityCode
from ._models_py3 import Details
from ._models_py3 import DiskScheduleAvailabilityRequest
from ._models_py3 import DiskSecret
from ._models_py3 import EncryptionPreferences
from ._models_py3 import ErrorDetail
from ._models_py3 import ExportDiskDetails
from ._models_py3 import FilterFileDetails
from ._models_py3 import HeavyScheduleAvailabilityRequest
from ._models_py3 import IdentityProperties
from ._models_py3 import ImportDiskDetails
from ._models_py3 import JobDeliveryInfo
from ._models_py3 import JobDetails
from ._models_py3 import JobResource
from ._models_py3 import JobResourceList
from ._models_py3 import JobResourceUpdateParameter
from ._models_py3 import JobSecrets
from ._models_py3 import JobStages
from ._models_py3 import KeyEncryptionKey
from ._models_py3 import LastMitigationActionOnJob
from ._models_py3 import ManagedDiskDetails
from ._models_py3 import MarkDevicesShippedRequest
from ._models_py3 import MitigateJobRequest
from ._models_py3 import NotificationPreference
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationList
from ._models_py3 import PackageCarrierDetails
from ._models_py3 import PackageCarrierInfo
from ._models_py3 import PackageShippingDetails
from ._models_py3 import Preferences
from ._models_py3 import PreferencesValidationRequest
from ._models_py3 import PreferencesValidationResponseProperties
from ._models_py3 import RegionConfigurationRequest
from ._models_py3 import RegionConfigurationResponse
from ._models_py3 import Resource
from ._models_py3 import ResourceIdentity
from ._models_py3 import ScheduleAvailabilityRequest
from ._models_py3 import ScheduleAvailabilityResponse
from ._models_py3 import ShareCredentialDetails
from ._models_py3 import ShipmentPickUpRequest
from ._models_py3 import ShipmentPickUpResponse
from ._models_py3 import ShippingAddress
from ._models_py3 import Sku
from ._models_py3 import SkuAvailabilityValidationRequest
from ._models_py3 import SkuAvailabilityValidationResponseProperties
from ._models_py3 import SkuCapacity
from ._models_py3 import SkuCost
from ._models_py3 import SkuInformation
from ._models_py3 import StorageAccountDetails
from ._models_py3 import SubscriptionIsAllowedToCreateJobValidationRequest
from ._models_py3 import SubscriptionIsAllowedToCreateJobValidationResponseProperties
from ._models_py3 import SystemData
from ._models_py3 import TransferAllDetails
from ._models_py3 import TransferConfiguration
from ._models_py3 import TransferConfigurationTransferAllDetails
from ._models_py3 import TransferConfigurationTransferFilterDetails
from ._models_py3 import TransferFilterDetails
from ._models_py3 import TransportAvailabilityDetails
from ._models_py3 import TransportAvailabilityRequest
from ._models_py3 import TransportAvailabilityResponse
from ._models_py3 import TransportPreferences
from ._models_py3 import UnencryptedCredentials
from ._models_py3 import UnencryptedCredentialsList
from ._models_py3 import UpdateJobDetails
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import UserAssignedProperties
from ._models_py3 import ValidateAddress
from ._models_py3 import ValidationInputRequest
from ._models_py3 import ValidationInputResponse
from ._models_py3 import ValidationRequest
from ._models_py3 import ValidationResponse

from ._data_box_management_client_enums import AccessProtocol
from ._data_box_management_client_enums import AddressType
from ._data_box_management_client_enums import AddressValidationStatus
from ._data_box_management_client_enums import ClassDiscriminator
from ._data_box_management_client_enums import CopyStatus
from ._data_box_management_client_enums import CustomerResolutionCode
from ._data_box_management_client_enums import DataAccountType
from ._data_box_management_client_enums import DataCenterCode
from ._data_box_management_client_enums import DatacenterAddressType
from ._data_box_management_client_enums import DoubleEncryption
from ._data_box_management_client_enums import FilterFileType
from ._data_box_management_client_enums import JobDeliveryType
from ._data_box_management_client_enums import KekType
from ._data_box_management_client_enums import LogCollectionLevel
from ._data_box_management_client_enums import NotificationStageName
from ._data_box_management_client_enums import OverallValidationStatus
from ._data_box_management_client_enums import ShareDestinationFormatType
from ._data_box_management_client_enums import SkuDisabledReason
from ._data_box_management_client_enums import SkuName
from ._data_box_management_client_enums import StageName
from ._data_box_management_client_enums import StageStatus
from ._data_box_management_client_enums import TransferConfigurationType
from ._data_box_management_client_enums import TransferType
from ._data_box_management_client_enums import TransportShipmentTypes
from ._data_box_management_client_enums import ValidationInputDiscriminator
from ._data_box_management_client_enums import ValidationStatus
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AccountCredentialDetails',
    'AdditionalErrorInfo',
    'AddressValidationOutput',
    'AddressValidationProperties',
    'ApiError',
    'ApplianceNetworkConfiguration',
    'ArmBaseObject',
    'AvailableSkuRequest',
    'AvailableSkusResult',
    'AzureFileFilterDetails',
    'BlobFilterDetails',
    'CancellationReason',
    'CloudError',
    'ContactDetails',
    'CopyLogDetails',
    'CopyProgress',
    'CreateJobValidations',
    'CreateOrderLimitForSubscriptionValidationRequest',
    'CreateOrderLimitForSubscriptionValidationResponseProperties',
    'CustomerDiskJobSecrets',
    'DataAccountDetails',
    'DataBoxAccountCopyLogDetails',
    'DataBoxCustomerDiskCopyLogDetails',
    'DataBoxCustomerDiskCopyProgress',
    'DataBoxCustomerDiskJobDetails',
    'DataBoxDiskCopyLogDetails',
    'DataBoxDiskCopyProgress',
    'DataBoxDiskJobDetails',
    'DataBoxDiskJobSecrets',
    'DataBoxHeavyAccountCopyLogDetails',
    'DataBoxHeavyJobDetails',
    'DataBoxHeavyJobSecrets',
    'DataBoxHeavySecret',
    'DataBoxJobDetails',
    'DataBoxScheduleAvailabilityRequest',
    'DataBoxSecret',
    'DataExportDetails',
    'DataImportDetails',
    'DataLocationToServiceLocationMap',
    'DataTransferDetailsValidationRequest',
    'DataTransferDetailsValidationResponseProperties',
    'DataboxJobSecrets',
    'DatacenterAddressInstructionResponse',
    'DatacenterAddressLocationResponse',
    'DatacenterAddressRequest',
    'DatacenterAddressResponse',
    'DcAccessSecurityCode',
    'Details',
    'DiskScheduleAvailabilityRequest',
    'DiskSecret',
    'EncryptionPreferences',
    'ErrorDetail',
    'ExportDiskDetails',
    'FilterFileDetails',
    'HeavyScheduleAvailabilityRequest',
    'IdentityProperties',
    'ImportDiskDetails',
    'JobDeliveryInfo',
    'JobDetails',
    'JobResource',
    'JobResourceList',
    'JobResourceUpdateParameter',
    'JobSecrets',
    'JobStages',
    'KeyEncryptionKey',
    'LastMitigationActionOnJob',
    'ManagedDiskDetails',
    'MarkDevicesShippedRequest',
    'MitigateJobRequest',
    'NotificationPreference',
    'Operation',
    'OperationDisplay',
    'OperationList',
    'PackageCarrierDetails',
    'PackageCarrierInfo',
    'PackageShippingDetails',
    'Preferences',
    'PreferencesValidationRequest',
    'PreferencesValidationResponseProperties',
    'RegionConfigurationRequest',
    'RegionConfigurationResponse',
    'Resource',
    'ResourceIdentity',
    'ScheduleAvailabilityRequest',
    'ScheduleAvailabilityResponse',
    'ShareCredentialDetails',
    'ShipmentPickUpRequest',
    'ShipmentPickUpResponse',
    'ShippingAddress',
    'Sku',
    'SkuAvailabilityValidationRequest',
    'SkuAvailabilityValidationResponseProperties',
    'SkuCapacity',
    'SkuCost',
    'SkuInformation',
    'StorageAccountDetails',
    'SubscriptionIsAllowedToCreateJobValidationRequest',
    'SubscriptionIsAllowedToCreateJobValidationResponseProperties',
    'SystemData',
    'TransferAllDetails',
    'TransferConfiguration',
    'TransferConfigurationTransferAllDetails',
    'TransferConfigurationTransferFilterDetails',
    'TransferFilterDetails',
    'TransportAvailabilityDetails',
    'TransportAvailabilityRequest',
    'TransportAvailabilityResponse',
    'TransportPreferences',
    'UnencryptedCredentials',
    'UnencryptedCredentialsList',
    'UpdateJobDetails',
    'UserAssignedIdentity',
    'UserAssignedProperties',
    'ValidateAddress',
    'ValidationInputRequest',
    'ValidationInputResponse',
    'ValidationRequest',
    'ValidationResponse',
    'AccessProtocol',
    'AddressType',
    'AddressValidationStatus',
    'ClassDiscriminator',
    'CopyStatus',
    'CustomerResolutionCode',
    'DataAccountType',
    'DataCenterCode',
    'DatacenterAddressType',
    'DoubleEncryption',
    'FilterFileType',
    'JobDeliveryType',
    'KekType',
    'LogCollectionLevel',
    'NotificationStageName',
    'OverallValidationStatus',
    'ShareDestinationFormatType',
    'SkuDisabledReason',
    'SkuName',
    'StageName',
    'StageStatus',
    'TransferConfigurationType',
    'TransferType',
    'TransportShipmentTypes',
    'ValidationInputDiscriminator',
    'ValidationStatus',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()