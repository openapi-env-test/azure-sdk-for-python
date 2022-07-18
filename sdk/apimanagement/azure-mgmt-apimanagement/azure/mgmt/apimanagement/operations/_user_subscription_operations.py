# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
from urllib.parse import parse_qs, urljoin, urlparse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import MixinABC, _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_group_name: str,
    service_name: str,
    user_id: str,
    subscription_id: str,
    *,
    filter: Optional[str] = None,
    top: Optional[int] = None,
    skip: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-04-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}/subscriptions",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "serviceName": _SERIALIZER.url(
            "service_name",
            service_name,
            "str",
            max_length=50,
            min_length=1,
            pattern=r"^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$",
        ),
        "userId": _SERIALIZER.url("user_id", user_id, "str", max_length=80, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int", minimum=1)
    if skip is not None:
        _params["$skip"] = _SERIALIZER.query("skip", skip, "int", minimum=0)
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, service_name: str, user_id: str, sid: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-04-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}/subscriptions/{sid}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "serviceName": _SERIALIZER.url(
            "service_name",
            service_name,
            "str",
            max_length=50,
            min_length=1,
            pattern=r"^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$",
        ),
        "userId": _SERIALIZER.url("user_id", user_id, "str", max_length=80, min_length=1),
        "sid": _SERIALIZER.url("sid", sid, "str", max_length=256, pattern=r"^[^*#&+:<>?]+$"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class UserSubscriptionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.apimanagement.ApiManagementClient`'s
        :attr:`user_subscription` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        service_name: str,
        user_id: str,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.SubscriptionContract"]:
        """Lists the collection of subscriptions of the specified user.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param user_id: User identifier. Must be unique in the current API Management service instance.
         Required.
        :type user_id: str
        :param filter: | Field     |     Usage     |     Supported operators    | Supported functions
         |</br>|-------------|------------------------|-----------------------------------|</br>|name |
         filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith
         |</br>|displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith,
         endswith |</br>|stateComment | filter | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |</br>|ownerId | filter | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |</br>|scope | filter | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |</br>|userId | filter | ge, le, eq, ne, gt, lt | substringof, contains,
         startswith, endswith |</br>|productId | filter | ge, le, eq, ne, gt, lt | substringof,
         contains, startswith, endswith |</br>. Default value is None.
        :type filter: str
        :param top: Number of records to return. Default value is None.
        :type top: int
        :param skip: Number of records to skip. Default value is None.
        :type skip: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SubscriptionContract or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.apimanagement.models.SubscriptionContract]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SubscriptionCollection]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    service_name=service_name,
                    user_id=user_id,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    skip=skip,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("SubscriptionCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}/subscriptions"}  # type: ignore

    @distributed_trace
    def get(
        self, resource_group_name: str, service_name: str, user_id: str, sid: str, **kwargs: Any
    ) -> _models.SubscriptionContract:
        """Gets the specified Subscription entity associated with a particular user.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param user_id: User identifier. Must be unique in the current API Management service instance.
         Required.
        :type user_id: str
        :param sid: Subscription entity Identifier. The entity represents the association between a
         user and a product in API Management. Required.
        :type sid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SubscriptionContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.SubscriptionContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SubscriptionContract]

        request = build_get_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            user_id=user_id,
            sid=sid,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("SubscriptionContract", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}/subscriptions/{sid}"}  # type: ignore
