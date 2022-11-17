# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AccessProtocol.
    """

    #: Server Message Block protocol(SMB).
    SMB = "SMB"
    #: Network File System protocol(NFS).
    NFS = "NFS"

class AddressType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of address.
    """

    #: Address type not known.
    NONE = "None"
    #: Residential Address.
    RESIDENTIAL = "Residential"
    #: Commercial Address.
    COMMERCIAL = "Commercial"

class AddressValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The address validation status.
    """

    #: Address provided is valid.
    VALID = "Valid"
    #: Address provided is invalid or not supported.
    INVALID = "Invalid"
    #: Address provided is ambiguous, please choose one of the alternate addresses returned.
    AMBIGUOUS = "Ambiguous"

class ClassDiscriminator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of job details.
    """

    #: Data Box orders.
    DATA_BOX = "DataBox"
    #: Data Box Disk orders.
    DATA_BOX_DISK = "DataBoxDisk"
    #: Data Box Heavy orders.
    DATA_BOX_HEAVY = "DataBoxHeavy"
    #: Data Box Customer Disk orders.
    DATA_BOX_CUSTOMER_DISK = "DataBoxCustomerDisk"

class CopyStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Status of the copy.
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
    #: No copy triggered as device was not received.
    DRIVE_NOT_RECEIVED = "DriveNotReceived"
    #: No copy triggered as device type is not supported.
    UNSUPPORTED_DRIVE = "UnsupportedDrive"
    #: Copy failed due to service error.
    OTHER_SERVICE_ERROR = "OtherServiceError"
    #: Copy failed due to user error.
    OTHER_USER_ERROR = "OtherUserError"
    #: Copy failed due to disk detection error.
    DRIVE_NOT_DETECTED = "DriveNotDetected"
    #: Copy failed due to corrupted drive.
    DRIVE_CORRUPTED = "DriveCorrupted"
    #: Copy failed due to modified or removed metadata files.
    METADATA_FILES_MODIFIED_OR_REMOVED = "MetadataFilesModifiedOrRemoved"

class CustomerResolutionCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CustomerResolutionCode.
    """

    #: No Resolution Yet
    NONE = "None"
    #: Clean the device
    MOVE_TO_CLEAN_UP_DEVICE = "MoveToCleanUpDevice"
    #: Resume the job to same stage
    RESUME = "Resume"
    #: Restart whole action.
    RESTART = "Restart"
    #: Reach out to operation for further action.
    REACH_OUT_TO_OPERATION = "ReachOutToOperation"

class DataAccountType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the account.
    """

    #: Storage Accounts .
    STORAGE_ACCOUNT = "StorageAccount"
    #: Azure Managed disk storage.
    MANAGED_DISK = "ManagedDisk"

class DatacenterAddressType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Data center address type.
    """

    #: Data center address location.
    DATACENTER_ADDRESS_LOCATION = "DatacenterAddressLocation"
    #: Data center address instruction.
    DATACENTER_ADDRESS_INSTRUCTION = "DatacenterAddressInstruction"

class DataCenterCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DataCenter code.
    """

    INVALID = "Invalid"
    BY2 = "BY2"
    BY1 = "BY1"
    ORK70 = "ORK70"
    AM2 = "AM2"
    AMS20 = "AMS20"
    BY21 = "BY21"
    BY24 = "BY24"
    MWH01 = "MWH01"
    AMS06 = "AMS06"
    SSE90 = "SSE90"
    SYD03 = "SYD03"
    SYD23 = "SYD23"
    CBR20 = "CBR20"
    YTO20 = "YTO20"
    CWL20 = "CWL20"
    LON24 = "LON24"
    BOM01 = "BOM01"
    BL20 = "BL20"
    BL7 = "BL7"
    SEL20 = "SEL20"
    TYO01 = "TYO01"
    BN1 = "BN1"
    SN5 = "SN5"
    CYS04 = "CYS04"
    TYO22 = "TYO22"
    YTO21 = "YTO21"
    YQB20 = "YQB20"
    FRA22 = "FRA22"
    MAA01 = "MAA01"
    CPQ02 = "CPQ02"
    CPQ20 = "CPQ20"
    SIN20 = "SIN20"
    HKG20 = "HKG20"
    SG2 = "SG2"
    MEL23 = "MEL23"
    SEL21 = "SEL21"
    OSA20 = "OSA20"
    SHA03 = "SHA03"
    BJB = "BJB"
    JNB22 = "JNB22"
    JNB21 = "JNB21"
    MNZ21 = "MNZ21"
    SN8 = "SN8"
    AUH20 = "AUH20"
    ZRH20 = "ZRH20"
    PUS20 = "PUS20"
    AD_HOC = "AdHoc"
    CH1 = "CH1"
    DSM05 = "DSM05"
    DUB07 = "DUB07"
    PNQ01 = "PNQ01"
    SVG20 = "SVG20"
    OSA02 = "OSA02"
    OSA22 = "OSA22"
    PAR22 = "PAR22"
    BN7 = "BN7"
    SN6 = "SN6"
    BJS20 = "BJS20"

class DoubleEncryption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines secondary layer of software-based encryption enablement.
    """

    #: Software-based encryption is enabled.
    ENABLED = "Enabled"
    #: Software-based encryption is disabled.
    DISABLED = "Disabled"

class FilterFileType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the filter file.
    """

    #: Filter file is of the type AzureBlob.
    AZURE_BLOB = "AzureBlob"
    #: Filter file is of the type AzureFiles.
    AZURE_FILE = "AzureFile"

class JobDeliveryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Delivery type of Job.
    """

    #: Non Scheduled job.
    NON_SCHEDULED = "NonScheduled"
    #: Scheduled job.
    SCHEDULED = "Scheduled"

class KekType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of encryption key used for key encryption.
    """

    #: Key encryption key is managed by Microsoft.
    MICROSOFT_MANAGED = "MicrosoftManaged"
    #: Key encryption key is managed by the Customer.
    CUSTOMER_MANAGED = "CustomerManaged"

class LogCollectionLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Level of the logs to be collected.
    """

    #: Only Errors will be collected in the logs.
    ERROR = "Error"
    #: Verbose logging (includes Errors, CRC, size information and others).
    VERBOSE = "Verbose"

class NotificationStageName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
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
    #: Notification at job created stage.
    CREATED = "Created"
    #: Notification at shipped devices to customer stage.
    SHIPPED_TO_CUSTOMER = "ShippedToCustomer"

class OverallValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Overall validation status.
    """

    #: Every input request is valid.
    ALL_VALID_TO_PROCEED = "AllValidToProceed"
    #: Some input requests are not valid.
    INPUTS_REVISIT_REQUIRED = "InputsRevisitRequired"
    #: Certain input validations skipped.
    CERTAIN_INPUT_VALIDATIONS_SKIPPED = "CertainInputValidationsSkipped"

class ShareDestinationFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
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

class SkuDisabledReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
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

class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SkuName.
    """

    #: Data Box.
    DATA_BOX = "DataBox"
    #: Data Box Disk.
    DATA_BOX_DISK = "DataBoxDisk"
    #: Data Box Heavy.
    DATA_BOX_HEAVY = "DataBoxHeavy"
    #: Data Box Customer Disk
    DATA_BOX_CUSTOMER_DISK = "DataBoxCustomerDisk"

class StageName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
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
    #: Job created by the customer.
    CREATED = "Created"
    #: User shipped the device to AzureDC.
    SHIPPED_TO_AZURE_DC = "ShippedToAzureDC"
    #: Awaiting shipment details of device from customer.
    AWAITING_SHIPMENT_DETAILS = "AwaitingShipmentDetails"
    #: Preparing the device to ship to customer.
    PREPARING_TO_SHIP_FROM_AZURE_DC = "PreparingToShipFromAzureDC"
    #: Shipped the device to customer.
    SHIPPED_TO_CUSTOMER = "ShippedToCustomer"

class StageStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
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
    #: Stage is waiting for customer action for kek action items.
    WAITING_FOR_CUSTOMER_ACTION_FOR_KEK = "WaitingForCustomerActionForKek"
    #: Stage is waiting for customer action for clean up.
    WAITING_FOR_CUSTOMER_ACTION_FOR_CLEAN_UP = "WaitingForCustomerActionForCleanUp"
    #: Stage has performed customer action for clean up.
    CUSTOMER_ACTION_PERFORMED_FOR_CLEAN_UP = "CustomerActionPerformedForCleanUp"
    #: Stage has performed customer action.
    CUSTOMER_ACTION_PERFORMED = "CustomerActionPerformed"

class TransferConfigurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the configuration for transfer.
    """

    #: Transfer all the data.
    TRANSFER_ALL = "TransferAll"
    #: Transfer using filter.
    TRANSFER_USING_FILTER = "TransferUsingFilter"

class TransferType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the transfer.
    """

    #: Import data to azure.
    IMPORT_TO_AZURE = "ImportToAzure"
    #: Export data from azure.
    EXPORT_FROM_AZURE = "ExportFromAzure"

class TransportShipmentTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Transport Shipment Type supported for given region.
    """

    #: Shipment Logistics is handled by the customer.
    CUSTOMER_MANAGED = "CustomerManaged"
    #: Shipment Logistics is handled by Microsoft.
    MICROSOFT_MANAGED = "MicrosoftManaged"

class ValidationInputDiscriminator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
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

class ValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Create order limit validation status.
    """

    #: Validation is successful
    VALID = "Valid"
    #: Validation is not successful
    INVALID = "Invalid"
    #: Validation is skipped
    SKIPPED = "Skipped"
