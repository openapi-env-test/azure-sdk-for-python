# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class DisableSerialConsoleResult(Model):
    """Serial Console Disable Result.

    Returns whether or not Serial Console is disabled.

    :param disabled: Whether or not Serial Console is disabled.
    :type disabled: bool
    """

    _attribute_map = {
        'disabled': {'key': 'disabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(DisableSerialConsoleResult, self).__init__(**kwargs)
        self.disabled = kwargs.get('disabled', None)


class EnableSerialConsoleResult(Model):
    """Serial Console Enable Result.

    Returns whether or not Serial Console is disabled (enabled).

    :param disabled: Whether or not Serial Console is disabled (enabled).
    :type disabled: bool
    """

    _attribute_map = {
        'disabled': {'key': 'disabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(EnableSerialConsoleResult, self).__init__(**kwargs)
        self.disabled = kwargs.get('disabled', None)


class GetSerialConsoleSubscriptionNotFound(Model):
    """Serial Console subscription not found.

    Error saying that the provided subscription could not be found.

    :param code: Error code
    :type code: str
    :param message: Subscription not found message
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GetSerialConsoleSubscriptionNotFound, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class SerialConsoleOperations(Model):
    """Serial Console operations.

    Serial Console operations.

    :param value: A list of Serial Console operations
    :type value:
     list[~azure.mgmt.serialconsole.models.SerialConsoleOperationsValueItem]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SerialConsoleOperationsValueItem]'},
    }

    def __init__(self, **kwargs):
        super(SerialConsoleOperations, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class SerialConsoleOperationsValueItem(Model):
    """SerialConsoleOperationsValueItem.

    :param name:
    :type name: str
    :param is_data_action:
    :type is_data_action: str
    :param display:
    :type display:
     ~azure.mgmt.serialconsole.models.SerialConsoleOperationsValueItemDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'str'},
        'display': {'key': 'display', 'type': 'SerialConsoleOperationsValueItemDisplay'},
    }

    def __init__(self, **kwargs):
        super(SerialConsoleOperationsValueItem, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_data_action = kwargs.get('is_data_action', None)
        self.display = kwargs.get('display', None)


class SerialConsoleOperationsValueItemDisplay(Model):
    """SerialConsoleOperationsValueItemDisplay.

    :param provider:
    :type provider: str
    :param resource:
    :type resource: str
    :param operation:
    :type operation: str
    :param description:
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SerialConsoleOperationsValueItemDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class SerialConsoleStatus(Model):
    """Serial Console GET Result.

    Returns whether or not Serial Console is disabled.

    :param disabled: Whether or not Serial Console is disabled.
    :type disabled: bool
    """

    _attribute_map = {
        'disabled': {'key': 'disabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(SerialConsoleStatus, self).__init__(**kwargs)
        self.disabled = kwargs.get('disabled', None)
