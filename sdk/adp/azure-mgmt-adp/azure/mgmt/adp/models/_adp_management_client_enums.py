# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CheckNameAvailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the reason that an account name could not be used. The reason element is only returned if
    nameAvailable is false.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the status of the account at the time the operation was called."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    ACCEPTED = "Accepted"
    PROVISIONING = "Provisioning"
    DELETING = "Deleting"


class StorageSkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SKU name."""

    STANDARD_LRS = "Standard_LRS"
    STANDARD_GRS = "Standard_GRS"
    STANDARD_RAGRS = "Standard_Ragrs"
    STANDARD_ZRS = "Standard_ZRS"
    PREMIUM_LRS = "Premium_LRS"
    PREMIUM_ZRS = "Premium_ZRS"
    STANDARD_GZRS = "Standard_Gzrs"
    STANDARD_RAGZRS = "Standard_Ragzrs"


class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of resource, Microsoft.AutonomousDevelopmentPlatform/accounts."""

    MICROSOFT_AUTONOMOUS_DEVELOPMENT_PLATFORM_ACCOUNTS = "Microsoft.AutonomousDevelopmentPlatform/accounts"
