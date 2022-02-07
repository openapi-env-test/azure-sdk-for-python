# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_check_dns_name_availability_request(
    location: str,
    subscription_id: str,
    *,
    domain_name_label: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-01-01"
    accept = "application/json, text/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/CheckDnsNameAvailability')
    path_format_arguments = {
        "location": _SERIALIZER.url("location", location, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['domainNameLabel'] = _SERIALIZER.query("domain_name_label", domain_name_label, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class NetworkManagementClientOperationsMixin(object):

    @distributed_trace
    def check_dns_name_availability(
        self,
        location: str,
        domain_name_label: str,
        **kwargs: Any
    ) -> "_models.DnsNameAvailabilityResult":
        """Checks whether a domain name in the cloudapp.azure.com zone is available for use.

        :param location: The location of the domain name.
        :type location: str
        :param domain_name_label: The domain name to be verified. It must conform to the following
         regular expression: ^[a-z][a-z0-9-]{1,61}[a-z0-9]$.
        :type domain_name_label: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DnsNameAvailabilityResult, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2018_01_01.models.DnsNameAvailabilityResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DnsNameAvailabilityResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_check_dns_name_availability_request(
            location=location,
            subscription_id=self._config.subscription_id,
            domain_name_label=domain_name_label,
            template_url=self.check_dns_name_availability.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DnsNameAvailabilityResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_dns_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/CheckDnsNameAvailability'}  # type: ignore

