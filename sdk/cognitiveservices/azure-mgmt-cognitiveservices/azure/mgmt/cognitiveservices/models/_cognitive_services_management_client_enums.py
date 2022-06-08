# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DeploymentProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the status of the resource at the time the operation was called.
    """

    ACCEPTED = "Accepted"
    CREATING = "Creating"
    DELETING = "Deleting"
    MOVING = "Moving"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"

class DeploymentScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Deployment scale type.
    """

    STANDARD = "Standard"
    MANUAL = "Manual"

class HostingModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Account hosting model.
    """

    WEB = "Web"
    CONNECTED_CONTAINER = "ConnectedContainer"
    DISCONNECTED_CONTAINER = "DisconnectedContainer"

class KeyName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """key name to generate (Key1|Key2)
    """

    KEY1 = "Key1"
    KEY2 = "Key2"

class KeySource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enumerates the possible value of keySource for Encryption
    """

    MICROSOFT_COGNITIVE_SERVICES = "Microsoft.CognitiveServices"
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"

class NetworkRuleAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default action when no rule from ipRules and from virtualNetworkRules match. This is only
    used after the bypass property has been evaluated.
    """

    ALLOW = "Allow"
    DENY = "Deny"

class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system"
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PrivateEndpointServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the status of the cognitive services account at the time the operation was called.
    """

    ACCEPTED = "Accepted"
    CREATING = "Creating"
    DELETING = "Deleting"
    MOVING = "Moving"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    RESOLVING_DNS = "ResolvingDNS"

class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether or not public endpoint access is allowed for this account.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class QuotaUsageStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Cognitive Services account quota usage status.
    """

    INCLUDED = "Included"
    BLOCKED = "Blocked"
    IN_OVERAGE = "InOverage"
    UNKNOWN = "Unknown"

class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"

class ResourceSkuRestrictionsReasonCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason for restriction.
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"

class ResourceSkuRestrictionsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of restrictions.
    """

    LOCATION = "Location"
    ZONE = "Zone"

class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This field is required to be implemented by the Resource Provider if the service has more than
    one tier, but is not required on a PUT.
    """

    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    ENTERPRISE = "Enterprise"

class UnitType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The unit of the metric.
    """

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
    MILLISECONDS = "Milliseconds"
