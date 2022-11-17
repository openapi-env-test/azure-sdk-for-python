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
from ...operations._api_operation_policy_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_entity_tag_request,
    build_get_request,
    build_list_by_operation_request,
)
from .._vendor import MixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ApiOperationPolicyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.apimanagement.aio.ApiManagementClient`'s
        :attr:`api_operation_policy` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def list_by_operation(
        self, resource_group_name: str, service_name: str, api_id: str, operation_id: str, **kwargs: Any
    ) -> _models.PolicyCollection:
        """Get the list of policy configuration at the API Operation level.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyCollection or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.PolicyCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PolicyCollection]

        request = build_list_by_operation_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_by_operation.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PolicyCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_operation.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies"}  # type: ignore

    @distributed_trace_async
    async def get_entity_tag(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        policy_id: Union[str, "_models.PolicyIdName"],
        **kwargs: Any
    ) -> bool:
        """Gets the entity state (Etag) version of the API operation policy specified by its identifier.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type operation_id: str
        :param policy_id: The identifier of the Policy. "policy" Required.
        :type policy_id: str or ~azure.mgmt.apimanagement.models.PolicyIdName
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_entity_tag_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            policy_id=policy_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_entity_tag.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        if cls:
            return cls(pipeline_response, None, response_headers)
        return 200 <= response.status_code <= 299

    get_entity_tag.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies/{policyId}"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        policy_id: Union[str, "_models.PolicyIdName"],
        format: Union[str, "_models.PolicyExportFormat"] = "xml",
        **kwargs: Any
    ) -> _models.PolicyContract:
        """Get the policy configuration at the API Operation level.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type operation_id: str
        :param policy_id: The identifier of the Policy. "policy" Required.
        :type policy_id: str or ~azure.mgmt.apimanagement.models.PolicyIdName
        :param format: Policy Export Format. Known values are: "xml" and "rawxml". Default value is
         "xml".
        :type format: str or ~azure.mgmt.apimanagement.models.PolicyExportFormat
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.PolicyContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PolicyContract]

        request = build_get_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            policy_id=policy_id,
            subscription_id=self._config.subscription_id,
            format=format,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("PolicyContract", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies/{policyId}"}  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        policy_id: Union[str, "_models.PolicyIdName"],
        parameters: _models.PolicyContract,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PolicyContract:
        """Creates or updates policy configuration for the API Operation level.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type operation_id: str
        :param policy_id: The identifier of the Policy. "policy" Required.
        :type policy_id: str or ~azure.mgmt.apimanagement.models.PolicyIdName
        :param parameters: The policy contents to apply. Required.
        :type parameters: ~azure.mgmt.apimanagement.models.PolicyContract
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.PolicyContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        policy_id: Union[str, "_models.PolicyIdName"],
        parameters: IO,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PolicyContract:
        """Creates or updates policy configuration for the API Operation level.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type operation_id: str
        :param policy_id: The identifier of the Policy. "policy" Required.
        :type policy_id: str or ~azure.mgmt.apimanagement.models.PolicyIdName
        :param parameters: The policy contents to apply. Required.
        :type parameters: IO
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.PolicyContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        policy_id: Union[str, "_models.PolicyIdName"],
        parameters: Union[_models.PolicyContract, IO],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.PolicyContract:
        """Creates or updates policy configuration for the API Operation level.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type operation_id: str
        :param policy_id: The identifier of the Policy. "policy" Required.
        :type policy_id: str or ~azure.mgmt.apimanagement.models.PolicyIdName
        :param parameters: The policy contents to apply. Is either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.apimanagement.models.PolicyContract or IO
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.PolicyContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PolicyContract]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "PolicyContract", is_xml=True)

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            policy_id=policy_id,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

            deserialized = self._deserialize("PolicyContract", pipeline_response)

        if response.status_code == 201:
            response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

            deserialized = self._deserialize("PolicyContract", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies/{policyId}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        service_name: str,
        api_id: str,
        operation_id: str,
        policy_id: Union[str, "_models.PolicyIdName"],
        if_match: str,
        **kwargs: Any
    ) -> None:
        """Deletes the policy configuration at the Api Operation.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param api_id: API revision identifier. Must be unique in the current API Management service
         instance. Non-current revision has ;rev=n as a suffix where n is the revision number. Required.
        :type api_id: str
        :param operation_id: Operation identifier within an API. Must be unique in the current API
         Management service instance. Required.
        :type operation_id: str
        :param policy_id: The identifier of the Policy. "policy" Required.
        :type policy_id: str or ~azure.mgmt.apimanagement.models.PolicyIdName
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update. Required.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            api_id=api_id,
            operation_id=operation_id,
            policy_id=policy_id,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/operations/{operationId}/policies/{policyId}"}  # type: ignore
