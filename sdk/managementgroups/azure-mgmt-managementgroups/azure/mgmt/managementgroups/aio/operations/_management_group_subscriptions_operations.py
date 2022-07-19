# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar
from urllib.parse import parse_qs, urljoin, urlparse

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._management_group_subscriptions_operations import (
    build_create_request,
    build_delete_request,
    build_get_subscription_request,
    build_get_subscriptions_under_management_group_request,
)
from .._vendor import MixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ManagementGroupSubscriptionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.managementgroups.aio.ManagementGroupsAPI`'s
        :attr:`management_group_subscriptions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def create(
        self, group_id: str, subscription_id: str, cache_control: str = "no-cache", **kwargs: Any
    ) -> _models.SubscriptionUnderManagementGroup:
        """Associates existing subscription with the management group.

        :param group_id: Management Group ID. Required.
        :type group_id: str
        :param subscription_id: Subscription ID. Required.
        :type subscription_id: str
        :param cache_control: Indicates whether the request should utilize any caches. Populate the
         header with 'no-cache' value to bypass existing caches. Default value is "no-cache".
        :type cache_control: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SubscriptionUnderManagementGroup or the result of cls(response)
        :rtype: ~azure.mgmt.managementgroups.models.SubscriptionUnderManagementGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SubscriptionUnderManagementGroup]

        request = build_create_request(
            group_id=group_id,
            subscription_id=subscription_id,
            cache_control=cache_control,
            api_version=api_version,
            template_url=self.create.metadata["url"],
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

        deserialized = self._deserialize("SubscriptionUnderManagementGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {"url": "/providers/Microsoft.Management/managementGroups/{groupId}/subscriptions/{subscriptionId}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, group_id: str, subscription_id: str, cache_control: str = "no-cache", **kwargs: Any
    ) -> None:
        """De-associates subscription from the management group.

        :param group_id: Management Group ID. Required.
        :type group_id: str
        :param subscription_id: Subscription ID. Required.
        :type subscription_id: str
        :param cache_control: Indicates whether the request should utilize any caches. Populate the
         header with 'no-cache' value to bypass existing caches. Default value is "no-cache".
        :type cache_control: str
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
            group_id=group_id,
            subscription_id=subscription_id,
            cache_control=cache_control,
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

    delete.metadata = {"url": "/providers/Microsoft.Management/managementGroups/{groupId}/subscriptions/{subscriptionId}"}  # type: ignore

    @distributed_trace_async
    async def get_subscription(
        self, group_id: str, subscription_id: str, cache_control: str = "no-cache", **kwargs: Any
    ) -> _models.SubscriptionUnderManagementGroup:
        """Retrieves details about given subscription which is associated with the management group.

        :param group_id: Management Group ID. Required.
        :type group_id: str
        :param subscription_id: Subscription ID. Required.
        :type subscription_id: str
        :param cache_control: Indicates whether the request should utilize any caches. Populate the
         header with 'no-cache' value to bypass existing caches. Default value is "no-cache".
        :type cache_control: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SubscriptionUnderManagementGroup or the result of cls(response)
        :rtype: ~azure.mgmt.managementgroups.models.SubscriptionUnderManagementGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SubscriptionUnderManagementGroup]

        request = build_get_subscription_request(
            group_id=group_id,
            subscription_id=subscription_id,
            cache_control=cache_control,
            api_version=api_version,
            template_url=self.get_subscription.metadata["url"],
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

        deserialized = self._deserialize("SubscriptionUnderManagementGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_subscription.metadata = {"url": "/providers/Microsoft.Management/managementGroups/{groupId}/subscriptions/{subscriptionId}"}  # type: ignore

    @distributed_trace
    def get_subscriptions_under_management_group(
        self, group_id: str, skiptoken: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.SubscriptionUnderManagementGroup"]:
        """Retrieves details about all subscriptions which are associated with the management group.

        :param group_id: Management Group ID. Required.
        :type group_id: str
        :param skiptoken: Page continuation token is only used if a previous operation returned a
         partial result.
         If a previous response contains a nextLink element, the value of the nextLink element will
         include a token parameter that specifies a starting point to use for subsequent calls. Default
         value is None.
        :type skiptoken: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SubscriptionUnderManagementGroup or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.managementgroups.models.SubscriptionUnderManagementGroup]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ListSubscriptionUnderManagementGroup]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_get_subscriptions_under_management_group_request(
                    group_id=group_id,
                    skiptoken=skiptoken,
                    api_version=api_version,
                    template_url=self.get_subscriptions_under_management_group.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urlparse(next_link)
                _next_request_params = case_insensitive_dict(parse_qs(_parsed_next_link.query))
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest("GET", urljoin(next_link, _parsed_next_link.path), params=_next_request_params)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ListSubscriptionUnderManagementGroup", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    get_subscriptions_under_management_group.metadata = {"url": "/providers/Microsoft.Management/managementGroups/{groupId}/subscriptions"}  # type: ignore
