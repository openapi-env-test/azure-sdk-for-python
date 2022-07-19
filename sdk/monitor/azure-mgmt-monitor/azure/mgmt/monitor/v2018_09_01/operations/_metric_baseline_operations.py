# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

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
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    resource_uri: str,
    metric_name: str,
    *,
    timespan: Optional[str] = None,
    interval: Optional[datetime.timedelta] = None,
    aggregation: Optional[str] = None,
    sensitivities: Optional[str] = None,
    result_type: Optional[Union[str, "_models.ResultType"]] = None,
    metricnamespace: Optional[str] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/{resourceUri}/providers/Microsoft.Insights/baseline/{metricName}")
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
        "metricName": _SERIALIZER.url("metric_name", metric_name, "str"),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if timespan is not None:
        query_parameters["timespan"] = _SERIALIZER.query("timespan", timespan, "str")
    if interval is not None:
        query_parameters["interval"] = _SERIALIZER.query("interval", interval, "duration")
    if aggregation is not None:
        query_parameters["aggregation"] = _SERIALIZER.query("aggregation", aggregation, "str")
    if sensitivities is not None:
        query_parameters["sensitivities"] = _SERIALIZER.query("sensitivities", sensitivities, "str")
    if result_type is not None:
        query_parameters["resultType"] = _SERIALIZER.query("result_type", result_type, "str")
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if metricnamespace is not None:
        query_parameters["metricnamespace"] = _SERIALIZER.query("metricnamespace", metricnamespace, "str")
    if filter is not None:
        query_parameters["$filter"] = _SERIALIZER.query("filter", filter, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_calculate_baseline_request(
    resource_uri: str, *, json: JSONType = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    api_version = "2018-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/{resourceUri}/providers/Microsoft.Insights/calculatebaseline")
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="POST", url=url, params=query_parameters, headers=header_parameters, json=json, content=content, **kwargs
    )


class MetricBaselineOperations(object):
    """MetricBaselineOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~$(python-base-namespace).v2018_09_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get(
        self,
        resource_uri: str,
        metric_name: str,
        timespan: Optional[str] = None,
        interval: Optional[datetime.timedelta] = None,
        aggregation: Optional[str] = None,
        sensitivities: Optional[str] = None,
        result_type: Optional[Union[str, "_models.ResultType"]] = None,
        metricnamespace: Optional[str] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.BaselineResponse":
        """**Gets the baseline values for a specific metric**.

        :param resource_uri: The identifier of the resource. It has the following structure:
         subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}.
         For example:
         subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1.
        :type resource_uri: str
        :param metric_name: The name of the metric to retrieve the baseline for.
        :type metric_name: str
        :param timespan: The timespan of the query. It is a string with the following format
         'startDateTime_ISO/endDateTime_ISO'.
        :type timespan: str
        :param interval: The interval (i.e. timegrain) of the query.
        :type interval: ~datetime.timedelta
        :param aggregation: The aggregation type of the metric to retrieve the baseline for.
        :type aggregation: str
        :param sensitivities: The list of sensitivities (comma separated) to retrieve.
        :type sensitivities: str
        :param result_type: Allows retrieving only metadata of the baseline. On data request all
         information is retrieved.
        :type result_type: str or ~$(python-base-namespace).v2018_09_01.models.ResultType
        :param metricnamespace: Metric namespace to query metric definitions for.
        :type metricnamespace: str
        :param filter: The **$filter** is used to describe a set of dimensions with their concrete
         values which produce a specific metric's time series, in which a baseline is requested for.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BaselineResponse, or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2018_09_01.models.BaselineResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.BaselineResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_request(
            resource_uri=resource_uri,
            metric_name=metric_name,
            timespan=timespan,
            interval=interval,
            aggregation=aggregation,
            sensitivities=sensitivities,
            result_type=result_type,
            metricnamespace=metricnamespace,
            filter=filter,
            template_url=self.get.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("BaselineResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{resourceUri}/providers/Microsoft.Insights/baseline/{metricName}"}  # type: ignore

    @distributed_trace
    def calculate_baseline(
        self, resource_uri: str, time_series_information: "_models.TimeSeriesInformation", **kwargs: Any
    ) -> "_models.CalculateBaselineResponse":
        """**Lists the baseline values for a resource**.

        :param resource_uri: The identifier of the resource. It has the following structure:
         subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}.
         For example:
         subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1.
        :type resource_uri: str
        :param time_series_information: Information that need to be specified to calculate a baseline
         on a time series.
        :type time_series_information:
         ~$(python-base-namespace).v2018_09_01.models.TimeSeriesInformation
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CalculateBaselineResponse, or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2018_09_01.models.CalculateBaselineResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.CalculateBaselineResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = self._serialize.body(time_series_information, "TimeSeriesInformation")

        request = build_calculate_baseline_request(
            resource_uri=resource_uri,
            content_type=content_type,
            json=_json,
            template_url=self.calculate_baseline.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CalculateBaselineResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    calculate_baseline.metadata = {"url": "/{resourceUri}/providers/Microsoft.Insights/calculatebaseline"}  # type: ignore
