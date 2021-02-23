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


class AccessPolicyUpdateKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ADD = "add"
    REPLACE = "replace"
    REMOVE = "remove"

class CertificatePermissions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ALL = "all"
    GET = "get"
    LIST = "list"
    DELETE = "delete"
    CREATE = "create"
    IMPORT_ENUM = "import"
    UPDATE = "update"
    MANAGECONTACTS = "managecontacts"
    GETISSUERS = "getissuers"
    LISTISSUERS = "listissuers"
    SETISSUERS = "setissuers"
    DELETEISSUERS = "deleteissuers"
    MANAGEISSUERS = "manageissuers"
    RECOVER = "recover"
    PURGE = "purge"
    BACKUP = "backup"
    RESTORE = "restore"

class CreateMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The vault's create mode to indicate whether the vault need to be recovered or not.
    """

    RECOVER = "recover"
    DEFAULT = "default"

class DeletionRecoveryLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The deletion recovery level currently in effect for the object. If it contains 'Purgeable',
    then the object can be permanently deleted by a privileged user; otherwise, only the system can
    purge the object at the end of the retention interval.
    """

    PURGEABLE = "Purgeable"
    RECOVERABLE_PURGEABLE = "Recoverable+Purgeable"
    RECOVERABLE = "Recoverable"
    RECOVERABLE_PROTECTED_SUBSCRIPTION = "Recoverable+ProtectedSubscription"

class JsonWebKeyCurveName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The elliptic curve name. For valid values, see JsonWebKeyCurveName.
    """

    P256 = "P-256"
    P384 = "P-384"
    P521 = "P-521"
    P256_K = "P-256K"

class JsonWebKeyOperation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The permitted JSON web key operations of the key. For more information, see
    JsonWebKeyOperation.
    """

    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    SIGN = "sign"
    VERIFY = "verify"
    WRAP_KEY = "wrapKey"
    UNWRAP_KEY = "unwrapKey"
    IMPORT_ENUM = "import"

class JsonWebKeyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the key. For valid values, see JsonWebKeyType.
    """

    EC = "EC"
    EC_HSM = "EC-HSM"
    RSA = "RSA"
    RSA_HSM = "RSA-HSM"

class KeyPermissions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ALL = "all"
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    WRAP_KEY = "wrapKey"
    UNWRAP_KEY = "unwrapKey"
    SIGN = "sign"
    VERIFY = "verify"
    GET = "get"
    LIST = "list"
    CREATE = "create"
    UPDATE = "update"
    IMPORT_ENUM = "import"
    DELETE = "delete"
    BACKUP = "backup"
    RESTORE = "restore"
    RECOVER = "recover"
    PURGE = "purge"

class NetworkRuleAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The default action when no rule from ipRules and from virtualNetworkRules match. This is only
    used after the bypass property has been evaluated.
    """

    ALLOW = "Allow"
    DENY = "Deny"

class NetworkRuleBypassOptions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Tells what traffic can bypass network rules. This can be 'AzureServices' or 'None'.  If not
    specified the default is 'AzureServices'.
    """

    AZURE_SERVICES = "AzureServices"
    NONE = "None"

class PrivateEndpointConnectionProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"
    DISCONNECTED = "Disconnected"

class PrivateEndpointServiceConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class Reason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason that a vault name could not be used. The Reason element is only returned if
    NameAvailable is false.
    """

    ACCOUNT_NAME_INVALID = "AccountNameInvalid"
    ALREADY_EXISTS = "AlreadyExists"

class SecretPermissions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ALL = "all"
    GET = "get"
    LIST = "list"
    SET = "set"
    DELETE = "delete"
    BACKUP = "backup"
    RESTORE = "restore"
    RECOVER = "recover"
    PURGE = "purge"

class SkuFamily(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """SKU family name
    """

    A = "A"

class SkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """SKU name to specify whether the key vault is a standard vault or a premium vault.
    """

    STANDARD = "standard"
    PREMIUM = "premium"

class StoragePermissions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ALL = "all"
    GET = "get"
    LIST = "list"
    DELETE = "delete"
    SET = "set"
    UPDATE = "update"
    REGENERATEKEY = "regeneratekey"
    RECOVER = "recover"
    PURGE = "purge"
    BACKUP = "backup"
    RESTORE = "restore"
    SETSAS = "setsas"
    LISTSAS = "listsas"
    GETSAS = "getsas"
    DELETESAS = "deletesas"

class VaultProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the vault.
    """

    SUCCEEDED = "Succeeded"
    REGISTERING_DNS = "RegisteringDns"
