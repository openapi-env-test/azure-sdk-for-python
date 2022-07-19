# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
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
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_create_or_update_request(
    resource_group_name: str,
    namespace_name: str,
    event_hub_name: str,
    consumer_group_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01-preview"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, "str", max_length=50, min_length=6),
        "eventHubName": _SERIALIZER.url("event_hub_name", event_hub_name, "str", max_length=256, min_length=1),
        "consumerGroupName": _SERIALIZER.url(
            "consumer_group_name", consumer_group_name, "str", max_length=50, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str,
    namespace_name: str,
    event_hub_name: str,
    consumer_group_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, "str", max_length=50, min_length=6),
        "eventHubName": _SERIALIZER.url("event_hub_name", event_hub_name, "str", max_length=256, min_length=1),
        "consumerGroupName": _SERIALIZER.url(
            "consumer_group_name", consumer_group_name, "str", max_length=50, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str,
    namespace_name: str,
    event_hub_name: str,
    consumer_group_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, "str", max_length=50, min_length=6),
        "eventHubName": _SERIALIZER.url("event_hub_name", event_hub_name, "str", max_length=256, min_length=1),
        "consumerGroupName": _SERIALIZER.url(
            "consumer_group_name", consumer_group_name, "str", max_length=50, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_event_hub_request(
    resource_group_name: str,
    namespace_name: str,
    event_hub_name: str,
    subscription_id: str,
    *,
    skip: Optional[int] = None,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "namespaceName": _SERIALIZER.url("namespace_name", namespace_name, "str", max_length=50, min_length=6),
        "eventHubName": _SERIALIZER.url("event_hub_name", event_hub_name, "str", max_length=256, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skip is not None:
        _params["$skip"] = _SERIALIZER.query("skip", skip, "int", maximum=1000, minimum=0)
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int", maximum=1000, minimum=1)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class ConsumerGroupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.eventhub.v2021_06_01_preview.EventHubManagementClient`'s
        :attr:`consumer_groups` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        parameters: _models.ConsumerGroup,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConsumerGroup:
        """Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
        :param parameters: Parameters supplied to create or update a consumer group resource. Required.
        :type parameters: ~azure.mgmt.eventhub.v2021_06_01_preview.models.ConsumerGroup
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConsumerGroup or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_06_01_preview.models.ConsumerGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConsumerGroup:
        """Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
        :param parameters: Parameters supplied to create or update a consumer group resource. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConsumerGroup or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_06_01_preview.models.ConsumerGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        parameters: Union[_models.ConsumerGroup, IO],
        **kwargs: Any
    ) -> _models.ConsumerGroup:
        """Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
        :param parameters: Parameters supplied to create or update a consumer group resource. Is either
         a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.eventhub.v2021_06_01_preview.models.ConsumerGroup or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConsumerGroup or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_06_01_preview.models.ConsumerGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01-preview"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ConsumerGroup]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ConsumerGroup")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            event_hub_name=event_hub_name,
            consumer_group_name=consumer_group_name,
            subscription_id=self._config.subscription_id,
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

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ConsumerGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName}"}  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a consumer group from the specified Event Hub and resource group.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            event_hub_name=event_hub_name,
            consumer_group_name=consumer_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName}"}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        **kwargs: Any
    ) -> _models.ConsumerGroup:
        """Gets a description for the specified consumer group.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConsumerGroup or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_06_01_preview.models.ConsumerGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ConsumerGroup]

        request = build_get_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            event_hub_name=event_hub_name,
            consumer_group_name=consumer_group_name,
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

        deserialized = self._deserialize("ConsumerGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName}"}  # type: ignore

    @distributed_trace
    def list_by_event_hub(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.ConsumerGroup"]:
        """Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group
        exists in the Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param skip: Skip is only used if a previous operation returned a partial result. If a previous
         response contains a nextLink element, the value of the nextLink element will include a skip
         parameter that specifies a starting point to use for subsequent calls. Default value is None.
        :type skip: int
        :param top: May be used to limit the number of results to the most recent N usageDetails.
         Default value is None.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ConsumerGroup or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.eventhub.v2021_06_01_preview.models.ConsumerGroup]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ConsumerGroupListResult]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_event_hub_request(
                    resource_group_name=resource_group_name,
                    namespace_name=namespace_name,
                    event_hub_name=event_hub_name,
                    subscription_id=self._config.subscription_id,
                    skip=skip,
                    top=top,
                    api_version=api_version,
                    template_url=self.list_by_event_hub.metadata["url"],
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
            deserialized = self._deserialize("ConsumerGroupListResult", pipeline_response)
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

    list_by_event_hub.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups"}  # type: ignore
