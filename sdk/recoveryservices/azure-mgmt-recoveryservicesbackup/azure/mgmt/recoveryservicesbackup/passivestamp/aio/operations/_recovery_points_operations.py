# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._recovery_points_operations import build_get_access_token_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class RecoveryPointsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.recoveryservicesbackup.passivestamp.aio.RecoveryServicesBackupPassiveClient`'s
        :attr:`recovery_points` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def get_access_token(
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        parameters: _models.AADPropertiesResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CrrAccessTokenResource:
        """Returns the Access token for communication between BMS and Protection service.

        Returns the Access token for communication between BMS and Protection service.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the container. Required.
        :type fabric_name: str
        :param container_name: Name of the container. Required.
        :type container_name: str
        :param protected_item_name: Name of the Protected Item. Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery Point Id. Required.
        :type recovery_point_id: str
        :param parameters: Get Access Token request. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.passivestamp.models.AADPropertiesResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CrrAccessTokenResource or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.passivestamp.models.CrrAccessTokenResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def get_access_token(
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CrrAccessTokenResource:
        """Returns the Access token for communication between BMS and Protection service.

        Returns the Access token for communication between BMS and Protection service.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the container. Required.
        :type fabric_name: str
        :param container_name: Name of the container. Required.
        :type container_name: str
        :param protected_item_name: Name of the Protected Item. Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery Point Id. Required.
        :type recovery_point_id: str
        :param parameters: Get Access Token request. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CrrAccessTokenResource or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.passivestamp.models.CrrAccessTokenResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def get_access_token(
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        parameters: Union[_models.AADPropertiesResource, IO],
        **kwargs: Any
    ) -> _models.CrrAccessTokenResource:
        """Returns the Access token for communication between BMS and Protection service.

        Returns the Access token for communication between BMS and Protection service.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the container. Required.
        :type fabric_name: str
        :param container_name: Name of the container. Required.
        :type container_name: str
        :param protected_item_name: Name of the Protected Item. Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery Point Id. Required.
        :type recovery_point_id: str
        :param parameters: Get Access Token request. Is either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.passivestamp.models.AADPropertiesResource
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CrrAccessTokenResource or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.passivestamp.models.CrrAccessTokenResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response, error_format=ARMErrorFormat),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CrrAccessTokenResource]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "AADPropertiesResource")

        request = build_get_access_token_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            fabric_name=fabric_name,
            container_name=container_name,
            protected_item_name=protected_item_name,
            recovery_point_id=recovery_point_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.get_access_token.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.NewErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CrrAccessTokenResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_access_token.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/accessToken"}  # type: ignore
