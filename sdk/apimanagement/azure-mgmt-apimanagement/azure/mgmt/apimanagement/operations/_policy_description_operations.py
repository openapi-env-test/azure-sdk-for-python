# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
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
from .._vendor import MixinABC, _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_service_request(
    resource_group_name: str,
    service_name: str,
    subscription_id: str,
    *,
    scope: Optional[Union[str, "_models.PolicyScopeContract"]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-08-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/policyDescriptions",
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
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if scope is not None:
        _params["scope"] = _SERIALIZER.query("scope", scope, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class PolicyDescriptionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.apimanagement.ApiManagementClient`'s
        :attr:`policy_description` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_service(
        self,
        resource_group_name: str,
        service_name: str,
        scope: Optional[Union[str, "_models.PolicyScopeContract"]] = None,
        **kwargs: Any
    ) -> _models.PolicyDescriptionCollection:
        """Lists all policy descriptions.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param scope: Policy scope. Known values are: "Tenant", "Product", "Api", "Operation", and
         "All". Default value is None.
        :type scope: str or ~azure.mgmt.apimanagement.models.PolicyScopeContract
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyDescriptionCollection or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.PolicyDescriptionCollection
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PolicyDescriptionCollection]

        request = build_list_by_service_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            subscription_id=self._config.subscription_id,
            scope=scope,
            api_version=api_version,
            template_url=self.list_by_service.metadata["url"],
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

        deserialized = self._deserialize("PolicyDescriptionCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_service.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/policyDescriptions"}  # type: ignore
