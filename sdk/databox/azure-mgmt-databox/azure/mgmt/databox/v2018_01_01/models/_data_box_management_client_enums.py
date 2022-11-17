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
    """AccessProtocol."""

    #: Server Message Block protocol(SMB).
    SMB = "SMB"
    #: Network File System protocol(NFS).
    NFS = "NFS"


class AddressType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of address."""

    #: Address type not known.
    NONE = "None"
    #: Residential Address.
    RESIDENTIAL = "Residential"
    #: Commercial Address.
    COMMERCIAL = "Commercial"


class AddressValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The address validation status."""

    #: Address provided is valid.
    VALID = "Valid"
    #: Address provided is invalid or not supported.
    INVALID = "Invalid"
    #: Address provided is ambiguous, please choose one of the alternate addresses returned.
    AMBIGUOUS = "Ambiguous"


class ClassDiscriminator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of job details."""

    #: DataBox orders.
    DATA_BOX = "DataBox"
    #: DataBoxDisk orders.
    DATA_BOX_DISK = "DataBoxDisk"
    #: DataBoxHeavy orders.
    DATA_BOX_HEAVY = "DataBoxHeavy"


class CopyStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Status of the copy."""

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


class DataDestinationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Data Destination Type."""

    #: Unknown type.
    UNKNOWN_TYPE = "UnknownType"
    #: Storage Accounts .
    STORAGE_ACCOUNT = "StorageAccount"
    #: Azure Managed disk storage.
    MANAGED_DISK = "ManagedDisk"


class NotificationStageName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the stage."""

    #: Notification at device prepared stage.
    DEVICE_PREPARED = "DevicePrepared"
    #: Notification at device dispatched stage.
    DISPATCHED = "Dispatched"
    #: Notification at device delivered stage.
    DELIVERED = "Delivered"
    #: Notification at device picked up from user stage.
    PICKED_UP = "PickedUp"
    #: Notification at device received at azure datacenter stage.
    AT_AZURE_DC = "AtAzureDC"
    #: Notification at data copy started stage.
    DATA_COPY = "DataCopy"


class ShareDestinationFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the share."""

    #: Unknown format.
    UNKNOWN_TYPE = "UnknownType"
    #: StorSimple data format.
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
    """Reason why the Sku is disabled."""

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
    """SkuName."""

    #: DataBox.
    DATA_BOX = "DataBox"
    #: DataBoxDisk.
    DATA_BOX_DISK = "DataBoxDisk"
    #: DataBoxHeavy.
    DATA_BOX_HEAVY = "DataBoxHeavy"


class StageName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the stage which is in progress."""

    #: An order has been created.
    DEVICE_ORDERED = "DeviceOrdered"
    #: A device has been prepared for the order.
    DEVICE_PREPARED = "DevicePrepared"
    #: Device has been dispatched to the user of the order.
    DISPATCHED = "Dispatched"
    #: Device has been delivered to the user of the order.
    DELIVERED = "Delivered"
    #: Device has been picked up from user and in transit to azure datacenter.
    PICKED_UP = "PickedUp"
    #: Device has been received at azure datacenter from the user.
    AT_AZURE_DC = "AtAzureDC"
    #: Data copy from the device at azure datacenter.
    DATA_COPY = "DataCopy"
    #: Order has completed.
    COMPLETED = "Completed"
    #: Order has completed with errors.
    COMPLETED_WITH_ERRORS = "CompletedWithErrors"
    #: Order has been cancelled.
    CANCELLED = "Cancelled"
    #: Order has failed due to issue reported by user.
    FAILED_ISSUE_REPORTED_AT_CUSTOMER = "Failed_IssueReportedAtCustomer"
    #: Order has failed due to issue detected at azure datacenter.
    FAILED_ISSUE_DETECTED_AT_AZURE_DC = "Failed_IssueDetectedAtAzureDC"
    #: Order has been aborted.
    ABORTED = "Aborted"


class StageStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the job stage."""

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
