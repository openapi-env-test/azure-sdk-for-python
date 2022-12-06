# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    resource_group_name: str,
    workspace_name: str,
    iot_connector_name: str,
    fhir_destination_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations/{fhirDestinationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, "str", max_length=24, min_length=3),
        "iotConnectorName": _SERIALIZER.url(
            "iot_connector_name", iot_connector_name, "str", max_length=24, min_length=3
        ),
        "fhirDestinationName": _SERIALIZER.url(
            "fhir_destination_name", fhir_destination_name, "str", max_length=24, min_length=3
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    resource_group_name: str,
    workspace_name: str,
    iot_connector_name: str,
    fhir_destination_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01-preview"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations/{fhirDestinationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, "str", max_length=24, min_length=3),
        "iotConnectorName": _SERIALIZER.url(
            "iot_connector_name", iot_connector_name, "str", max_length=24, min_length=3
        ),
        "fhirDestinationName": _SERIALIZER.url(
            "fhir_destination_name", fhir_destination_name, "str", max_length=24, min_length=3
        ),
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
    workspace_name: str,
    iot_connector_name: str,
    fhir_destination_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations/{fhirDestinationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, "str", max_length=24, min_length=3),
        "iotConnectorName": _SERIALIZER.url(
            "iot_connector_name", iot_connector_name, "str", max_length=24, min_length=3
        ),
        "fhirDestinationName": _SERIALIZER.url(
            "fhir_destination_name", fhir_destination_name, "str", max_length=24, min_length=3
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


class IotConnectorFhirDestinationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.healthcareapis.HealthcareApisManagementClient`'s
        :attr:`iot_connector_fhir_destination` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        workspace_name: str,
        iot_connector_name: str,
        fhir_destination_name: str,
        **kwargs: Any
    ) -> _models.IotFhirDestination:
        """Gets the properties of the specified Iot Connector FHIR destination.

        :param resource_group_name: The name of the resource group that contains the service instance.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of workspace resource. Required.
        :type workspace_name: str
        :param iot_connector_name: The name of IoT Connector resource. Required.
        :type iot_connector_name: str
        :param fhir_destination_name: The name of IoT Connector FHIR destination resource. Required.
        :type fhir_destination_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IotFhirDestination or the result of cls(response)
        :rtype: ~azure.mgmt.healthcareapis.models.IotFhirDestination
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.IotFhirDestination]

        request = build_get_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            iot_connector_name=iot_connector_name,
            fhir_destination_name=fhir_destination_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("IotFhirDestination", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations/{fhirDestinationName}"}  # type: ignore

    def _create_or_update_initial(
        self,
        resource_group_name: str,
        workspace_name: str,
        iot_connector_name: str,
        fhir_destination_name: str,
        iot_fhir_destination: Union[_models.IotFhirDestination, IO],
        **kwargs: Any
    ) -> _models.IotFhirDestination:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.IotFhirDestination]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(iot_fhir_destination, (IO, bytes)):
            _content = iot_fhir_destination
        else:
            _json = self._serialize.body(iot_fhir_destination, "IotFhirDestination")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            iot_connector_name=iot_connector_name,
            fhir_destination_name=fhir_destination_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._create_or_update_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDetails, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("IotFhirDestination", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("IotFhirDestination", pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize("IotFhirDestination", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations/{fhirDestinationName}"}  # type: ignore

    @overload
    def begin_create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        iot_connector_name: str,
        fhir_destination_name: str,
        iot_fhir_destination: _models.IotFhirDestination,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.IotFhirDestination]:
        """Creates or updates an IoT Connector FHIR destination resource with the specified parameters.

        :param resource_group_name: The name of the resource group that contains the service instance.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of workspace resource. Required.
        :type workspace_name: str
        :param iot_connector_name: The name of IoT Connector resource. Required.
        :type iot_connector_name: str
        :param fhir_destination_name: The name of IoT Connector FHIR destination resource. Required.
        :type fhir_destination_name: str
        :param iot_fhir_destination: The parameters for creating or updating an IoT Connector FHIR
         destination resource. Required.
        :type iot_fhir_destination: ~azure.mgmt.healthcareapis.models.IotFhirDestination
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either IotFhirDestination or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.healthcareapis.models.IotFhirDestination]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        iot_connector_name: str,
        fhir_destination_name: str,
        iot_fhir_destination: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.IotFhirDestination]:
        """Creates or updates an IoT Connector FHIR destination resource with the specified parameters.

        :param resource_group_name: The name of the resource group that contains the service instance.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of workspace resource. Required.
        :type workspace_name: str
        :param iot_connector_name: The name of IoT Connector resource. Required.
        :type iot_connector_name: str
        :param fhir_destination_name: The name of IoT Connector FHIR destination resource. Required.
        :type fhir_destination_name: str
        :param iot_fhir_destination: The parameters for creating or updating an IoT Connector FHIR
         destination resource. Required.
        :type iot_fhir_destination: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either IotFhirDestination or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.healthcareapis.models.IotFhirDestination]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        iot_connector_name: str,
        fhir_destination_name: str,
        iot_fhir_destination: Union[_models.IotFhirDestination, IO],
        **kwargs: Any
    ) -> LROPoller[_models.IotFhirDestination]:
        """Creates or updates an IoT Connector FHIR destination resource with the specified parameters.

        :param resource_group_name: The name of the resource group that contains the service instance.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of workspace resource. Required.
        :type workspace_name: str
        :param iot_connector_name: The name of IoT Connector resource. Required.
        :type iot_connector_name: str
        :param fhir_destination_name: The name of IoT Connector FHIR destination resource. Required.
        :type fhir_destination_name: str
        :param iot_fhir_destination: The parameters for creating or updating an IoT Connector FHIR
         destination resource. Is either a model type or a IO type. Required.
        :type iot_fhir_destination: ~azure.mgmt.healthcareapis.models.IotFhirDestination or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either IotFhirDestination or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.healthcareapis.models.IotFhirDestination]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.IotFhirDestination]
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(  # type: ignore
                resource_group_name=resource_group_name,
                workspace_name=workspace_name,
                iot_connector_name=iot_connector_name,
                fhir_destination_name=fhir_destination_name,
                iot_fhir_destination=iot_fhir_destination,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("IotFhirDestination", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(PollingMethod, ARMPolling(lro_delay, **kwargs))  # type: PollingMethod
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations/{fhirDestinationName}"}  # type: ignore

    def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        workspace_name: str,
        iot_connector_name: str,
        fhir_destination_name: str,
        **kwargs: Any
    ) -> None:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            iot_connector_name=iot_connector_name,
            fhir_destination_name=fhir_destination_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations/{fhirDestinationName}"}  # type: ignore

    @distributed_trace
    def begin_delete(
        self,
        resource_group_name: str,
        workspace_name: str,
        iot_connector_name: str,
        fhir_destination_name: str,
        **kwargs: Any
    ) -> LROPoller[None]:
        """Deletes an IoT Connector FHIR destination.

        :param resource_group_name: The name of the resource group that contains the service instance.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of workspace resource. Required.
        :type workspace_name: str
        :param iot_connector_name: The name of IoT Connector resource. Required.
        :type iot_connector_name: str
        :param fhir_destination_name: The name of IoT Connector FHIR destination resource. Required.
        :type fhir_destination_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                workspace_name=workspace_name,
                iot_connector_name=iot_connector_name,
                fhir_destination_name=fhir_destination_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = cast(PollingMethod, ARMPolling(lro_delay, **kwargs))  # type: PollingMethod
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/workspaces/{workspaceName}/iotconnectors/{iotConnectorName}/fhirdestinations/{fhirDestinationName}"}  # type: ignore
