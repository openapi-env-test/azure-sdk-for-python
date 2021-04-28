# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AccessProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    #: Server Message Block protocol(SMB).
    SMB = "SMB"
    #: Network File System protocol(NFS).
    NFS = "NFS"

class AddressType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of address.
    """

    #: Address type not known.
    NONE = "None"
    #: Residential Address.
    RESIDENTIAL = "Residential"
    #: Commercial Address.
    COMMERCIAL = "Commercial"

class AddressValidationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The address validation status.
    """

    #: Address provided is valid.
    VALID = "Valid"
    #: Address provided is invalid or not supported.
    INVALID = "Invalid"
    #: Address provided is ambiguous, please choose one of the alternate addresses returned.
    AMBIGUOUS = "Ambiguous"

class ClassDiscriminator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the type of job details.
    """

    #: Data Box orders.
    DATA_BOX = "DataBox"
    #: Data Box Disk orders.
    DATA_BOX_DISK = "DataBoxDisk"
    #: Data Box Heavy orders.
    DATA_BOX_HEAVY = "DataBoxHeavy"

class CopyStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Status of the copy
    """

    #: Data copy hasn't started yet.
    NOT_STARTED = "NotStarted"
    #: Data copy is in progress.
    IN_PROGRESS = "InProgress"
    #: Data copy completed.
    COMPLETED = "Completed"
    #: Data copy completed with errors.
    COMPLETED_WITH_ERRORS = "CompletedWithErrors"
    #: Data copy failed. No data was copied.
    FAILED = "Failed"
    #: No copy triggered as device was not returned.
    NOT_RETURNED = "NotReturned"
    #: The Device has hit hardware issues.
    HARDWARE_ERROR = "HardwareError"
    #: Data copy failed. The Device was formatted by user.
    DEVICE_FORMATTED = "DeviceFormatted"
    #: Data copy failed. Device metadata was modified by user.
    DEVICE_METADATA_MODIFIED = "DeviceMetadataModified"
    #: Data copy failed. Storage Account was not accessible during copy.
    STORAGE_ACCOUNT_NOT_ACCESSIBLE = "StorageAccountNotAccessible"
    #: Data copy failed. The Device data content is not supported.
    UNSUPPORTED_DATA = "UnsupportedData"

class DataAccountType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the account.
    """

    #: Storage Accounts .
    STORAGE_ACCOUNT = "StorageAccount"
    #: Azure Managed disk storage.
    MANAGED_DISK = "ManagedDisk"

class FilterFileType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the filter file.
    """

    #: Filter file is of the type AzureBlob.
    AZURE_BLOB = "AzureBlob"
    #: Filter file is of the type AzureFiles.
    AZURE_FILE = "AzureFile"

class JobDeliveryType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Delivery type of Job.
    """

    #: Non Scheduled job.
    NON_SCHEDULED = "NonScheduled"
    #: Scheduled job.
    SCHEDULED = "Scheduled"

class KekType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of encryption key used for key encryption.
    """

    #: Key encryption key is managed by Microsoft.
    MICROSOFT_MANAGED = "MicrosoftManaged"
    #: Key encryption key is managed by the Customer.
    CUSTOMER_MANAGED = "CustomerManaged"

class LogCollectionLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Level of the logs to be collected.
    """

    #: Only Errors will be collected in the logs.
    ERROR = "Error"
    #: Verbose logging (includes Errors, CRC, size information and others).
    VERBOSE = "Verbose"

class NotificationStageName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of the stage.
    """

    #: Notification at device prepared stage.
    DEVICE_PREPARED = "DevicePrepared"
    #: Notification at device dispatched stage.
    DISPATCHED = "Dispatched"
    #: Notification at device delivered stage.
    DELIVERED = "Delivered"
    #: Notification at device picked up from user stage.
    PICKED_UP = "PickedUp"
    #: Notification at device received at Azure datacenter stage.
    AT_AZURE_DC = "AtAzureDC"
    #: Notification at data copy started stage.
    DATA_COPY = "DataCopy"

class OverallValidationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Overall validation status.
    """

    #: Every input request is valid.
    ALL_VALID_TO_PROCEED = "AllValidToProceed"
    #: Some input requests are not valid.
    INPUTS_REVISIT_REQUIRED = "InputsRevisitRequired"
    #: Certain input validations skipped.
    CERTAIN_INPUT_VALIDATIONS_SKIPPED = "CertainInputValidationsSkipped"

class ShareDestinationFormatType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the share.
    """

    #: Unknown format.
    UNKNOWN_TYPE = "UnknownType"
    #: Storsimple data format.
    HCS = "HCS"
    #: Azure storage block blob format.
    BLOCK_BLOB = "BlockBlob"
    #: Azure storage page blob format.
    PAGE_BLOB = "PageBlob"
    #: Azure storage file format.
    AZURE_FILE = "AzureFile"
    #: Azure Compute Disk.
    MANAGED_DISK = "ManagedDisk"

class SkuDisabledReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Reason why the Sku is disabled.
    """

    #: SKU is not disabled.
    NONE = "None"
    #: SKU is not available in the requested country.
    COUNTRY = "Country"
    #: SKU is not available to push data to the requested Azure region.
    REGION = "Region"
    #: Required features are not enabled for the SKU.
    FEATURE = "Feature"
    #: Subscription does not have required offer types for the SKU.
    OFFER_TYPE = "OfferType"
    #: Subscription has not registered to Microsoft.DataBox and Service does not have the subscription
    #: notification.
    NO_SUBSCRIPTION_INFO = "NoSubscriptionInfo"

class SkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    #: Data Box.
    DATA_BOX = "DataBox"
    #: Data Box Disk.
    DATA_BOX_DISK = "DataBoxDisk"
    #: Data Box Heavy.
    DATA_BOX_HEAVY = "DataBoxHeavy"

class StageName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of the stage which is in progress.
    """

    #: An order has been created.
    DEVICE_ORDERED = "DeviceOrdered"
    #: A device has been prepared for the order.
    DEVICE_PREPARED = "DevicePrepared"
    #: Device has been dispatched to the user of the order.
    DISPATCHED = "Dispatched"
    #: Device has been delivered to the user of the order.
    DELIVERED = "Delivered"
    #: Device has been picked up from user and in transit to Azure datacenter.
    PICKED_UP = "PickedUp"
    #: Device has been received at Azure datacenter from the user.
    AT_AZURE_DC = "AtAzureDC"
    #: Data copy from the device at Azure datacenter.
    DATA_COPY = "DataCopy"
    #: Order has completed.
    COMPLETED = "Completed"
    #: Order has completed with errors.
    COMPLETED_WITH_ERRORS = "CompletedWithErrors"
    #: Order has been cancelled.
    CANCELLED = "Cancelled"
    #: Order has failed due to issue reported by user.
    FAILED_ISSUE_REPORTED_AT_CUSTOMER = "Failed_IssueReportedAtCustomer"
    #: Order has failed due to issue detected at Azure datacenter.
    FAILED_ISSUE_DETECTED_AT_AZURE_DC = "Failed_IssueDetectedAtAzureDC"
    #: Order has been aborted.
    ABORTED = "Aborted"
    #: Order has completed with warnings.
    COMPLETED_WITH_WARNINGS = "CompletedWithWarnings"
    #: Device is ready to be handed to customer from Azure DC.
    READY_TO_DISPATCH_FROM_AZURE_DC = "ReadyToDispatchFromAzureDC"
    #: Device can be dropped off at Azure DC.
    READY_TO_RECEIVE_AT_AZURE_DC = "ReadyToReceiveAtAzureDC"

class StageStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the job stage.
    """

    #: No status available yet.
    NONE = "None"
    #: Stage is in progress.
    IN_PROGRESS = "InProgress"
    #: Stage has succeeded.
    SUCCEEDED = "Succeeded"
    #: Stage has failed.
    FAILED = "Failed"
    #: Stage has been cancelled.
    CANCELLED = "Cancelled"
    #: Stage is cancelling.
    CANCELLING = "Cancelling"
    #: Stage has succeeded with errors.
    SUCCEEDED_WITH_ERRORS = "SucceededWithErrors"
    #: Stage is stuck until customer takes some action.
    WAITING_FOR_CUSTOMER_ACTION = "WaitingForCustomerAction"
    #: Stage has succeeded with warnings.
    SUCCEEDED_WITH_WARNINGS = "SucceededWithWarnings"

class TransferConfigurationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the configuration for transfer.
    """

    #: Transfer all the data.
    TRANSFER_ALL = "TransferAll"
    #: Transfer using filter.
    TRANSFER_USING_FILTER = "TransferUsingFilter"

class TransferType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the transfer.
    """

    #: Import data to azure.
    IMPORT_TO_AZURE = "ImportToAzure"
    #: Export data from azure.
    EXPORT_FROM_AZURE = "ExportFromAzure"

class TransportShipmentTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Transport Shipment Type supported for given region.
    """

    #: Shipment Logistics is handled by the customer.
    CUSTOMER_MANAGED = "CustomerManaged"
    #: Shipment Logistics is handled by Microsoft.
    MICROSOFT_MANAGED = "MicrosoftManaged"

class ValidationInputDiscriminator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Identifies the type of validation request.
    """

    #: Identify request and response of address validation.
    VALIDATE_ADDRESS = "ValidateAddress"
    #: Identify request and response for validation of subscription permission to create job.
    VALIDATE_SUBSCRIPTION_IS_ALLOWED_TO_CREATE_JOB = "ValidateSubscriptionIsAllowedToCreateJob"
    #: Identify request and response of preference validation.
    VALIDATE_PREFERENCES = "ValidatePreferences"
    #: Identify request and response of create order limit for subscription validation.
    VALIDATE_CREATE_ORDER_LIMIT = "ValidateCreateOrderLimit"
    #: Identify request and response of active job limit for sku availability.
    VALIDATE_SKU_AVAILABILITY = "ValidateSkuAvailability"
    #: Identify request and response of data transfer details validation.
    VALIDATE_DATA_TRANSFER_DETAILS = "ValidateDataTransferDetails"

class ValidationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Create order limit validation status.
    """

    #: Validation is successful.
    VALID = "Valid"
    #: Validation is not successful.
    INVALID = "Invalid"
    #: Validation is skipped.
    SKIPPED = "Skipped"
