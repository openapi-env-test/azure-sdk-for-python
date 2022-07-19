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
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(resource_uri: str, *, filter: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{resourceUri}/providers/microsoft.insights/metrics")
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class MetricsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~$(python-base-namespace).v2016_09_01.MonitorManagementClient`'s
        :attr:`metrics` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, resource_uri: str, filter: Optional[str] = None, **kwargs: Any) -> Iterable["_models.Metric"]:
        """Lists the metric values for a resource.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param filter: Reduces the set of data collected.:code:`<br>`The filter is optional. If present
         it must contain a list of metric names to retrieve of the form: *(name.value eq 'metricName'
         [or name.value eq 'metricName' or ...])*. Optionally, the filter can contain conditions for the
         following attributes *aggregationType*\ , *startTime*\ , *endTime*\ , and *timeGrain* of the
         form *attributeName operator value*. Where operator is one of *ne*\ , *eq*\ , *gt*\ ,
         *lt*.:code:`<br>`Several conditions can be combined with parentheses and logical operators,
         e.g: *and*\ , *or*.:code:`<br>`Some example filter expressions are::code:`<br>`-
         $filter=(name.value eq 'RunsSucceeded') and aggregationType eq 'Total' and startTime eq
         2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration'PT1M',:code:`<br>`-
         $filter=(name.value eq 'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq
         'Average') and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq
         duration'PT1H',:code:`<br>`- $filter=(name.value eq 'ActionsCompleted' or name.value eq
         'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq 'Average') and startTime
         eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq
         duration'PT1M'.:code:`<br>`:code:`<br>`\ **NOTE**\ : When a metrics query comes in with
         multiple metrics, but with no aggregation types defined, the service will pick the Primary
         aggregation type of the first metrics to be used as the default aggregation type for all the
         metrics. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Metric or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~$(python-base-namespace).v2016_09_01.models.Metric]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.MetricCollection]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_uri=resource_uri,
                    filter=filter,
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
            deserialized = self._deserialize("MetricCollection", pipeline_response)
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

    list.metadata = {"url": "/{resourceUri}/providers/microsoft.insights/metrics"}  # type: ignore
