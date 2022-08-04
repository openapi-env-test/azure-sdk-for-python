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
    resource_group_name: str, capacity_reservation_group_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "capacityReservationGroupName": _SERIALIZER.url(
            "capacity_reservation_group_name", capacity_reservation_group_name, "str"
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


def build_update_request(
    resource_group_name: str, capacity_reservation_group_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "capacityReservationGroupName": _SERIALIZER.url(
            "capacity_reservation_group_name", capacity_reservation_group_name, "str"
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

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str, capacity_reservation_group_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "capacityReservationGroupName": _SERIALIZER.url(
            "capacity_reservation_group_name", capacity_reservation_group_name, "str"
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
    capacity_reservation_group_name: str,
    subscription_id: str,
    *,
    expand: Optional[Union[str, "_models.CapacityReservationGroupInstanceViewTypes"]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "capacityReservationGroupName": _SERIALIZER.url(
            "capacity_reservation_group_name", capacity_reservation_group_name, "str"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", expand, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_resource_group_request(
    resource_group_name: str,
    subscription_id: str,
    *,
    expand: Optional[Union[str, "_models.ExpandTypesForGetCapacityReservationGroups"]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", expand, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_subscription_request(
    subscription_id: str,
    *,
    expand: Optional[Union[str, "_models.ExpandTypesForGetCapacityReservationGroups"]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/capacityReservationGroups"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", expand, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class CapacityReservationGroupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2021_07_01.ComputeManagementClient`'s
        :attr:`capacity_reservation_groups` attribute.
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
        capacity_reservation_group_name: str,
        parameters: _models.CapacityReservationGroup,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CapacityReservationGroup:
        """The operation to create or update a capacity reservation group. When updating a capacity
        reservation group, only tags may be modified. Please refer to
        https://aka.ms/CapacityReservation for more details.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param capacity_reservation_group_name: The name of the capacity reservation group. Required.
        :type capacity_reservation_group_name: str
        :param parameters: Parameters supplied to the Create capacity reservation Group. Required.
        :type parameters: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CapacityReservationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        capacity_reservation_group_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CapacityReservationGroup:
        """The operation to create or update a capacity reservation group. When updating a capacity
        reservation group, only tags may be modified. Please refer to
        https://aka.ms/CapacityReservation for more details.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param capacity_reservation_group_name: The name of the capacity reservation group. Required.
        :type capacity_reservation_group_name: str
        :param parameters: Parameters supplied to the Create capacity reservation Group. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CapacityReservationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        capacity_reservation_group_name: str,
        parameters: Union[_models.CapacityReservationGroup, IO],
        **kwargs: Any
    ) -> _models.CapacityReservationGroup:
        """The operation to create or update a capacity reservation group. When updating a capacity
        reservation group, only tags may be modified. Please refer to
        https://aka.ms/CapacityReservation for more details.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param capacity_reservation_group_name: The name of the capacity reservation group. Required.
        :type capacity_reservation_group_name: str
        :param parameters: Parameters supplied to the Create capacity reservation Group. Is either a
         model type or a IO type. Required.
        :type parameters: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CapacityReservationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CapacityReservationGroup]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "CapacityReservationGroup")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            capacity_reservation_group_name=capacity_reservation_group_name,
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

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("CapacityReservationGroup", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("CapacityReservationGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}"}  # type: ignore

    @overload
    def update(
        self,
        resource_group_name: str,
        capacity_reservation_group_name: str,
        parameters: _models.CapacityReservationGroupUpdate,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CapacityReservationGroup:
        """The operation to update a capacity reservation group. When updating a capacity reservation
        group, only tags may be modified.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param capacity_reservation_group_name: The name of the capacity reservation group. Required.
        :type capacity_reservation_group_name: str
        :param parameters: Parameters supplied to the Update capacity reservation Group operation.
         Required.
        :type parameters: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroupUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CapacityReservationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        resource_group_name: str,
        capacity_reservation_group_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CapacityReservationGroup:
        """The operation to update a capacity reservation group. When updating a capacity reservation
        group, only tags may be modified.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param capacity_reservation_group_name: The name of the capacity reservation group. Required.
        :type capacity_reservation_group_name: str
        :param parameters: Parameters supplied to the Update capacity reservation Group operation.
         Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CapacityReservationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        capacity_reservation_group_name: str,
        parameters: Union[_models.CapacityReservationGroupUpdate, IO],
        **kwargs: Any
    ) -> _models.CapacityReservationGroup:
        """The operation to update a capacity reservation group. When updating a capacity reservation
        group, only tags may be modified.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param capacity_reservation_group_name: The name of the capacity reservation group. Required.
        :type capacity_reservation_group_name: str
        :param parameters: Parameters supplied to the Update capacity reservation Group operation. Is
         either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroupUpdate or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CapacityReservationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CapacityReservationGroup]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "CapacityReservationGroupUpdate")

        request = build_update_request(
            resource_group_name=resource_group_name,
            capacity_reservation_group_name=capacity_reservation_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CapacityReservationGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}"}  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, capacity_reservation_group_name: str, **kwargs: Any
    ) -> None:
        """The operation to delete a capacity reservation group. This operation is allowed only if all the
        associated resources are disassociated from the reservation group and all capacity reservations
        under the reservation group have also been deleted. Please refer to
        https://aka.ms/CapacityReservation for more details.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param capacity_reservation_group_name: The name of the capacity reservation group. Required.
        :type capacity_reservation_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            capacity_reservation_group_name=capacity_reservation_group_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}"}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        capacity_reservation_group_name: str,
        expand: Optional[Union[str, "_models.CapacityReservationGroupInstanceViewTypes"]] = None,
        **kwargs: Any
    ) -> _models.CapacityReservationGroup:
        """The operation that retrieves information about a capacity reservation group.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param capacity_reservation_group_name: The name of the capacity reservation group. Required.
        :type capacity_reservation_group_name: str
        :param expand: The expand expression to apply on the operation. 'InstanceView' will retrieve
         the list of instance views of the capacity reservations under the capacity reservation group
         which is a snapshot of the runtime properties of a capacity reservation that is managed by the
         platform and can change outside of control plane operations. "instanceView" Default value is
         None.
        :type expand: str or
         ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroupInstanceViewTypes
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CapacityReservationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CapacityReservationGroup]

        request = build_get_request(
            resource_group_name=resource_group_name,
            capacity_reservation_group_name=capacity_reservation_group_name,
            subscription_id=self._config.subscription_id,
            expand=expand,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CapacityReservationGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}"}  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self,
        resource_group_name: str,
        expand: Optional[Union[str, "_models.ExpandTypesForGetCapacityReservationGroups"]] = None,
        **kwargs: Any
    ) -> Iterable["_models.CapacityReservationGroup"]:
        """Lists all of the capacity reservation groups in the specified resource group. Use the nextLink
        property in the response to get the next page of capacity reservation groups.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param expand: The expand expression to apply on the operation. Based on the expand param(s)
         specified we return Virtual Machine or ScaleSet VM Instance or both resource Ids which are
         associated to capacity reservation group in the response. Known values are:
         "virtualMachineScaleSetVMs/$ref" and "virtualMachines/$ref". Default value is None.
        :type expand: str or
         ~azure.mgmt.compute.v2021_07_01.models.ExpandTypesForGetCapacityReservationGroups
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CapacityReservationGroup or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CapacityReservationGroupListResult]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    expand=expand,
                    api_version=api_version,
                    template_url=self.list_by_resource_group.metadata["url"],
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
            deserialized = self._deserialize("CapacityReservationGroupListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups"}  # type: ignore

    @distributed_trace
    def list_by_subscription(
        self, expand: Optional[Union[str, "_models.ExpandTypesForGetCapacityReservationGroups"]] = None, **kwargs: Any
    ) -> Iterable["_models.CapacityReservationGroup"]:
        """Lists all of the capacity reservation groups in the subscription. Use the nextLink property in
        the response to get the next page of capacity reservation groups.

        :param expand: The expand expression to apply on the operation. Based on the expand param(s)
         specified we return Virtual Machine or ScaleSet VM Instance or both resource Ids which are
         associated to capacity reservation group in the response. Known values are:
         "virtualMachineScaleSetVMs/$ref" and "virtualMachines/$ref". Default value is None.
        :type expand: str or
         ~azure.mgmt.compute.v2021_07_01.models.ExpandTypesForGetCapacityReservationGroups
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CapacityReservationGroup or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.compute.v2021_07_01.models.CapacityReservationGroup]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-07-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CapacityReservationGroupListResult]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    expand=expand,
                    api_version=api_version,
                    template_url=self.list_by_subscription.metadata["url"],
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
            deserialized = self._deserialize("CapacityReservationGroupListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_subscription.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/capacityReservationGroups"}  # type: ignore
