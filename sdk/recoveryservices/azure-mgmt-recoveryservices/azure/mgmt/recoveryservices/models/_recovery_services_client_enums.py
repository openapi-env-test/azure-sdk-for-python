# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AlertsState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AlertsState."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class AuthType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the authentication type."""

    INVALID = "Invalid"
    ACS = "ACS"
    AAD = "AAD"
    ACCESS_CONTROL_SERVICE = "AccessControlService"
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"


class BackupStorageVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backup storage version."""

    V1 = "V1"
    V2 = "V2"
    UNASSIGNED = "Unassigned"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class CrossRegionRestore(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Flag to show if Cross Region Restore is enabled on the Vault or not."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ImmutabilityState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ImmutabilityState."""

    DISABLED = "Disabled"
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"


class InfrastructureEncryptionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enabling/Disabling the Double Encryption state."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class PrivateEndpointConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets provisioning state of the private endpoint connection."""

    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    FAILED = "Failed"
    PENDING = "Pending"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an
    implicitly created identity and a set of user-assigned identities. The type 'None' will remove
    any identities.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class ResourceMoveState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The State of the Resource after the move operation."""

    UNKNOWN = "Unknown"
    IN_PROGRESS = "InProgress"
    PREPARE_FAILED = "PrepareFailed"
    COMMIT_FAILED = "CommitFailed"
    PREPARE_TIMEDOUT = "PrepareTimedout"
    COMMIT_TIMEDOUT = "CommitTimedout"
    MOVE_SUCCEEDED = "MoveSucceeded"
    FAILURE = "Failure"
    CRITICAL_FAILURE = "CriticalFailure"
    PARTIAL_SUCCESS = "PartialSuccess"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Sku name."""

    STANDARD = "Standard"
    RS0 = "RS0"


class StandardTierStorageRedundancy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The storage redundancy setting of a vault."""

    LOCALLY_REDUNDANT = "LocallyRedundant"
    GEO_REDUNDANT = "GeoRedundant"
    ZONE_REDUNDANT = "ZoneRedundant"


class TriggerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The way the vault upgrade was triggered."""

    USER_TRIGGERED = "UserTriggered"
    FORCED_UPGRADE = "ForcedUpgrade"


class UsagesUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Unit of the usage."""

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"


class VaultPrivateEndpointState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Private endpoint state for backup."""

    NONE = "None"
    ENABLED = "Enabled"


class VaultUpgradeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the vault upgrade operation."""

    UNKNOWN = "Unknown"
    IN_PROGRESS = "InProgress"
    UPGRADED = "Upgraded"
    FAILED = "Failed"
