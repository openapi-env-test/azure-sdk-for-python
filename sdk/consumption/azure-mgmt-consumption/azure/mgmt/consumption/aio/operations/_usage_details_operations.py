# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar, Union
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
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._usage_details_operations import build_list_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class UsageDetailsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.consumption.aio.ConsumptionManagementClient`'s
        :attr:`usage_details` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        scope: str,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        skiptoken: Optional[str] = None,
        top: Optional[int] = None,
        metric: Optional[Union[str, "_models.Metrictype"]] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.UsageDetail"]:
        """Lists the usage details for the defined scope. Usage details are available via this API only
        for May 1, 2014 or later.

        :param scope: The scope associated with usage details operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
         '/providers/Microsoft.Billing/departments/{departmentId}' for Department scope,
         '/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount
         scope and '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management
         Group scope. For subscription, billing account, department, enrollment account and management
         group, you can also add billing period to the scope using
         '/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'. For e.g. to specify billing
         period at department scope use
         '/providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'.
         Also, Modern Commerce Account scopes are
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for billingAccount scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners. Required.
        :type scope: str
        :param expand: May be used to expand the properties/additionalInfo or properties/meterDetails
         within a list of usage details. By default, these fields are not included when listing usage
         details. Default value is None.
        :type expand: str
        :param filter: May be used to filter usageDetails by properties/resourceGroup,
         properties/resourceName, properties/resourceId, properties/chargeType,
         properties/reservationId, properties/publisherType or tags. The filter supports 'eq', 'lt',
         'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is
         a key value pair string where key and value is separated by a colon (:). PublisherType Filter
         accepts two values azure and marketplace and it is currently supported for Web Direct Offer
         Type. Default value is None.
        :type filter: str
        :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If
         a previous response contains a nextLink element, the value of the nextLink element will include
         a skiptoken parameter that specifies a starting point to use for subsequent calls. Default
         value is None.
        :type skiptoken: str
        :param top: May be used to limit the number of results to the most recent N usageDetails.
         Default value is None.
        :type top: int
        :param metric: Allows to select different type of cost/usage records. Known values are:
         "actualcost", "amortizedcost", and "usage". Default value is None.
        :type metric: str or ~azure.mgmt.consumption.models.Metrictype
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either UsageDetail or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.consumption.models.UsageDetail]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.UsageDetailsListResult]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    scope=scope,
                    expand=expand,
                    filter=filter,
                    skiptoken=skiptoken,
                    top=top,
                    metric=metric,
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("UsageDetailsListResult", pipeline_response)
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

            if response.status_code not in [200, 204]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/{scope}/providers/Microsoft.Consumption/usageDetails"}  # type: ignore
