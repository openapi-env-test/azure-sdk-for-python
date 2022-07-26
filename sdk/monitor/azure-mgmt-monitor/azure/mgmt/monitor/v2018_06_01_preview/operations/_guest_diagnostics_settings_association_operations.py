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


def build_create_or_update_request(resource_uri: str, association_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
        "associationName": _SERIALIZER.url("association_name", association_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(resource_uri: str, association_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
        "associationName": _SERIALIZER.url("association_name", association_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(resource_uri: str, association_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
        "associationName": _SERIALIZER.url("association_name", association_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(resource_uri: str, association_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
        "associationName": _SERIALIZER.url("association_name", association_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/microsoft.insights/guestDiagnosticSettingsAssociations",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_resource_group_request(resource_group_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/guestDiagnosticSettingsAssociations",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class GuestDiagnosticsSettingsAssociationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~$(python-base-namespace).v2018_06_01_preview.MonitorManagementClient`'s
        :attr:`guest_diagnostics_settings_association` attribute.
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
        resource_uri: str,
        association_name: str,
        diagnostic_settings_association: _models.GuestDiagnosticSettingsAssociationResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GuestDiagnosticSettingsAssociationResource:
        """Creates or updates guest diagnostics settings association.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Required.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association. Required.
        :type association_name: str
        :param diagnostic_settings_association: The diagnostic settings association to create or
         update. Required.
        :type diagnostic_settings_association:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_uri: str,
        association_name: str,
        diagnostic_settings_association: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GuestDiagnosticSettingsAssociationResource:
        """Creates or updates guest diagnostics settings association.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Required.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association. Required.
        :type association_name: str
        :param diagnostic_settings_association: The diagnostic settings association to create or
         update. Required.
        :type diagnostic_settings_association: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_uri: str,
        association_name: str,
        diagnostic_settings_association: Union[_models.GuestDiagnosticSettingsAssociationResource, IO],
        **kwargs: Any
    ) -> _models.GuestDiagnosticSettingsAssociationResource:
        """Creates or updates guest diagnostics settings association.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Required.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association. Required.
        :type association_name: str
        :param diagnostic_settings_association: The diagnostic settings association to create or
         update. Is either a model type or a IO type. Required.
        :type diagnostic_settings_association:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GuestDiagnosticSettingsAssociationResource]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(diagnostic_settings_association, (IO, bytes)):
            _content = diagnostic_settings_association
        else:
            _json = self._serialize.body(diagnostic_settings_association, "GuestDiagnosticSettingsAssociationResource")

        request = build_create_or_update_request(
            resource_uri=resource_uri,
            association_name=association_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("GuestDiagnosticSettingsAssociationResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("GuestDiagnosticSettingsAssociationResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}"}  # type: ignore

    @distributed_trace
    def get(
        self, resource_uri: str, association_name: str, **kwargs: Any
    ) -> _models.GuestDiagnosticSettingsAssociationResource:
        """Gets guest diagnostics association settings.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Required.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association. Required.
        :type association_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GuestDiagnosticSettingsAssociationResource]

        request = build_get_request(
            resource_uri=resource_uri,
            association_name=association_name,
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

        deserialized = self._deserialize("GuestDiagnosticSettingsAssociationResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}"}  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_uri: str, association_name: str, **kwargs: Any
    ) -> None:
        """Delete guest diagnostics association settings.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Required.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association. Required.
        :type association_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_uri=resource_uri,
            association_name=association_name,
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

    delete.metadata = {"url": "/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}"}  # type: ignore

    @overload
    def update(
        self,
        resource_uri: str,
        association_name: str,
        parameters: _models.GuestDiagnosticSettingsAssociationResourcePatch,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GuestDiagnosticSettingsAssociationResource:
        """Updates an existing guestDiagnosticsSettingsAssociation Resource. To update other fields use
        the CreateOrUpdate method.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Required.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association. Required.
        :type association_name: str
        :param parameters: Parameters supplied to the operation. Required.
        :type parameters:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResourcePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        resource_uri: str,
        association_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GuestDiagnosticSettingsAssociationResource:
        """Updates an existing guestDiagnosticsSettingsAssociation Resource. To update other fields use
        the CreateOrUpdate method.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Required.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association. Required.
        :type association_name: str
        :param parameters: Parameters supplied to the operation. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(
        self,
        resource_uri: str,
        association_name: str,
        parameters: Union[_models.GuestDiagnosticSettingsAssociationResourcePatch, IO],
        **kwargs: Any
    ) -> _models.GuestDiagnosticSettingsAssociationResource:
        """Updates an existing guestDiagnosticsSettingsAssociation Resource. To update other fields use
        the CreateOrUpdate method.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type. Required.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association. Required.
        :type association_name: str
        :param parameters: Parameters supplied to the operation. Is either a model type or a IO type.
         Required.
        :type parameters:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResourcePatch
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GuestDiagnosticSettingsAssociationResource]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "GuestDiagnosticSettingsAssociationResourcePatch")

        request = build_update_request(
            resource_uri=resource_uri,
            association_name=association_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("GuestDiagnosticSettingsAssociationResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}"}  # type: ignore

    @distributed_trace
    def list(self, **kwargs: Any) -> Iterable["_models.GuestDiagnosticSettingsAssociationResource"]:
        """Get a list of all guest diagnostic settings association in a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GuestDiagnosticSettingsAssociationResource or the
         result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GuestDiagnosticSettingsAssociationList]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    subscription_id=self._config.subscription_id,
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
            deserialized = self._deserialize("GuestDiagnosticSettingsAssociationList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

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

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/microsoft.insights/guestDiagnosticSettingsAssociations"}  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, **kwargs: Any
    ) -> Iterable["_models.GuestDiagnosticSettingsAssociationResource"]:
        """Get a list of all guest diagnostic settings association in a resource group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GuestDiagnosticSettingsAssociationResource or the
         result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GuestDiagnosticSettingsAssociationList]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
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
            deserialized = self._deserialize("GuestDiagnosticSettingsAssociationList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

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

    list_by_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/guestDiagnosticSettingsAssociations"}  # type: ignore
