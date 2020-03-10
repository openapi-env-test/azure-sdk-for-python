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
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class Operation(Model):
    """Represents an operation returned by the GetOperations request.

    :param name: Name of the operation
    :type name: str
    :param display: Display name of the operation
    :type display: ~azure.mgmt.applicationinsights.models.OperationInfo
    :param origin: Origin of the operation
    :type origin: str
    :param properties: Properties of the operation
    :type properties: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationInfo'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, *, name: str=None, display=None, origin: str=None, properties=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin
        self.properties = properties


class OperationInfo(Model):
    """Information about an operation.

    :param provider: Name of the provider
    :type provider: str
    :param resource: Name of the resource type
    :type resource: str
    :param operation: Name of the operation
    :type operation: str
    :param description: Description of the operation
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, resource: str=None, operation: str=None, description: str=None, **kwargs) -> None:
        super(OperationInfo, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class TestResultFileResponse(Model):
    """Test result.

    :param data: File contents.
    :type data: str
    :param next_link: The URI that can be used to request the next section of
     the result file in the event the file is too large for a single request.
    :type next_link: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'str'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, data: str=None, next_link: str=None, **kwargs) -> None:
        super(TestResultFileResponse, self).__init__(**kwargs)
        self.data = data
        self.next_link = next_link
