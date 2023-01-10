# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccountType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of storage accessed on the storage account."""

    GENERAL_PURPOSE_STORAGE = "GeneralPurposeStorage"
    BLOB_STORAGE = "BlobStorage"


class AlertSeverity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Severity of the alert."""

    INFORMATIONAL = "Informational"
    WARNING = "Warning"
    CRITICAL = "Critical"


class AuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type."""

    INVALID = "Invalid"
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"


class AzureContainerDataFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Storage format used for the file represented by the share."""

    BLOCK_BLOB = "BlockBlob"
    PAGE_BLOB = "PageBlob"
    AZURE_FILE = "AzureFile"


class ClientPermissionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of access to be allowed for the client."""

    NO_ACCESS = "NoAccess"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class DataBoxEdgeDeviceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the Data Box Edge/Gateway device."""

    READY_TO_SETUP = "ReadyToSetup"
    ONLINE = "Online"
    OFFLINE = "Offline"
    NEEDS_ATTENTION = "NeedsAttention"
    DISCONNECTED = "Disconnected"
    PARTIALLY_DISCONNECTED = "PartiallyDisconnected"


class DataPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Data policy of the share."""

    CLOUD = "Cloud"
    LOCAL = "Local"


class DayOfWeek(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DayOfWeek."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class DeviceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the Data Box Edge/Gateway device."""

    DATA_BOX_EDGE_DEVICE = "DataBoxEdgeDevice"


class DownloadPhase(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The download phase."""

    UNKNOWN = "Unknown"
    INITIALIZING = "Initializing"
    DOWNLOADING = "Downloading"
    VERIFYING = "Verifying"


class EncryptionAlgorithm(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The algorithm used to encrypt "Value"."""

    NONE = "None"
    AES256 = "AES256"
    RSAES_PKCS1_V1_5 = "RSAES_PKCS1_v_1_5"


class InstallRebootBehavior(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates if updates are available and at least one of the updates needs a reboot."""

    NEVER_REBOOTS = "NeverReboots"
    REQUIRES_REBOOT = "RequiresReboot"
    REQUEST_REBOOT = "RequestReboot"


class JobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current status of the job."""

    INVALID = "Invalid"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PAUSED = "Paused"
    SCHEDULED = "Scheduled"


class JobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the job."""

    INVALID = "Invalid"
    SCAN_FOR_UPDATES = "ScanForUpdates"
    DOWNLOAD_UPDATES = "DownloadUpdates"
    INSTALL_UPDATES = "InstallUpdates"
    REFRESH_SHARE = "RefreshShare"


class MetricAggregationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Metric aggregation type."""

    NOT_SPECIFIED = "NotSpecified"
    NONE = "None"
    AVERAGE = "Average"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    TOTAL = "Total"
    COUNT = "Count"


class MetricCategory(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Metric category."""

    CAPACITY = "Capacity"
    TRANSACTION = "Transaction"


class MetricUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Metric units."""

    NOT_SPECIFIED = "NotSpecified"
    PERCENT = "Percent"
    COUNT = "Count"
    SECONDS = "Seconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    BYTES_PER_SECOND = "BytesPerSecond"
    COUNT_PER_SECOND = "CountPerSecond"


class MonitoringStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current monitoring status of the share."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class NetworkAdapterDHCPStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Value indicating whether this adapter has DHCP enabled."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class NetworkAdapterRDMAStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Value indicating whether this adapter is RDMA capable."""

    INCAPABLE = "Incapable"
    CAPABLE = "Capable"


class NetworkAdapterStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Value indicating whether this adapter is valid."""

    INACTIVE = "Inactive"
    ACTIVE = "Active"


class NetworkGroup(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The network group."""

    NONE = "None"
    NON_RDMA = "NonRDMA"
    RDMA = "RDMA"


class OrderState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the order as per the allowed status types."""

    UNTRACKED = "Untracked"
    AWAITING_FULFILMENT = "AwaitingFulfilment"
    AWAITING_PREPARATION = "AwaitingPreparation"
    AWAITING_SHIPMENT = "AwaitingShipment"
    SHIPPED = "Shipped"
    ARRIVING = "Arriving"
    DELIVERED = "Delivered"
    REPLACEMENT_REQUESTED = "ReplacementRequested"
    LOST_DEVICE = "LostDevice"
    DECLINED = "Declined"
    RETURN_INITIATED = "ReturnInitiated"
    AWAITING_RETURN_SHIPMENT = "AwaitingReturnShipment"
    SHIPPED_BACK = "ShippedBack"
    COLLECTED_AT_MICROSOFT = "CollectedAtMicrosoft"


class PlatformType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Host OS supported by the IoT role."""

    WINDOWS = "Windows"
    LINUX = "Linux"


class RoleStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Role status."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RoleTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """RoleTypes."""

    IOT = "IOT"
    ASA = "ASA"
    FUNCTIONS = "Functions"
    COGNITIVE = "Cognitive"


class ShareAccessProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Access protocol to be used by the share."""

    SMB = "SMB"
    NFS = "NFS"


class ShareAccessType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of access to be allowed on the share for this user."""

    CHANGE = "Change"
    READ = "Read"
    CUSTOM = "Custom"


class ShareStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current status of the share."""

    ONLINE = "Online"
    OFFLINE = "Offline"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SKU name."""

    GATEWAY = "Gateway"
    EDGE = "Edge"


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SKU tier. This is based on the SKU name."""

    STANDARD = "Standard"


class SSLStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Signifies whether SSL needs to be enabled or not."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TimeGrain(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """TimeGrain."""

    PT1_M = "PT1M"
    PT5_M = "PT5M"
    PT15_M = "PT15M"
    PT30_M = "PT30M"
    PT1_H = "PT1H"
    PT6_H = "PT6H"
    PT12_H = "PT12H"
    PT1_D = "PT1D"


class TriggerEventType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Trigger Kind."""

    FILE_EVENT = "FileEvent"
    PERIODIC_TIMER_EVENT = "PeriodicTimerEvent"


class UpdateOperation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current update operation."""

    NONE = "None"
    SCAN = "Scan"
    DOWNLOAD = "Download"
    INSTALL = "Install"


class UpdateOperationStage(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current stage of the update operation."""

    UNKNOWN = "Unknown"
    INITIAL = "Initial"
    SCAN_STARTED = "ScanStarted"
    SCAN_COMPLETE = "ScanComplete"
    SCAN_FAILED = "ScanFailed"
    DOWNLOAD_STARTED = "DownloadStarted"
    DOWNLOAD_COMPLETE = "DownloadComplete"
    DOWNLOAD_FAILED = "DownloadFailed"
    INSTALL_STARTED = "InstallStarted"
    INSTALL_COMPLETE = "InstallComplete"
    INSTALL_FAILED = "InstallFailed"
    REBOOT_INITIATED = "RebootInitiated"
    SUCCESS = "Success"
    FAILURE = "Failure"
    RESCAN_STARTED = "RescanStarted"
    RESCAN_COMPLETE = "RescanComplete"
    RESCAN_FAILED = "RescanFailed"
