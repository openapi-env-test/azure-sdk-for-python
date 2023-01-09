# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import RecoveryServicesBackupClientMixinABC, _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_trigger_request(
    vault_name: str,
    resource_group_name: str,
    fabric_name: str,
    container_name: str,
    protected_item_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-09-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-09-01-preview")
    )
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/backup",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, "str"),
        "containerName": _SERIALIZER.url("container_name", container_name, "str"),
        "protectedItemName": _SERIALIZER.url("protected_item_name", protected_item_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class BackupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.recoveryservicesbackup.activestamp.RecoveryServicesBackupClient`'s
        :attr:`backups` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def trigger(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        parameters: _models.BackupRequestResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Triggers backup for specified backed up item. This is an asynchronous operation. To know the
        status of the
        operation, call GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backup item. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backup item. Required.
        :type container_name: str
        :param protected_item_name: Backup item for which backup needs to be triggered. Required.
        :type protected_item_name: str
        :param parameters: resource backup request. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.activestamp.models.BackupRequestResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def trigger(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Triggers backup for specified backed up item. This is an asynchronous operation. To know the
        status of the
        operation, call GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backup item. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backup item. Required.
        :type container_name: str
        :param protected_item_name: Backup item for which backup needs to be triggered. Required.
        :type protected_item_name: str
        :param parameters: resource backup request. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def trigger(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        parameters: Union[_models.BackupRequestResource, IO],
        **kwargs: Any
    ) -> None:
        """Triggers backup for specified backed up item. This is an asynchronous operation. To know the
        status of the
        operation, call GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backup item. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backup item. Required.
        :type container_name: str
        :param protected_item_name: Backup item for which backup needs to be triggered. Required.
        :type protected_item_name: str
        :param parameters: resource backup request. Is either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.activestamp.models.BackupRequestResource
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "BackupRequestResource")

        request = build_trigger_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            fabric_name=fabric_name,
            container_name=container_name,
            protected_item_name=protected_item_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.trigger.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    trigger.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/backup"
    }
