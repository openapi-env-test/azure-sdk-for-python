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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._reservation_recommendation_details_operations import build_get_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ReservationRecommendationDetailsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.consumption.aio.ConsumptionManagementClient`'s
        :attr:`reservation_recommendation_details` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self,
        resource_scope: str,
        scope: Union[str, "_models.Scope"],
        region: str,
        term: Union[str, "_models.Term"],
        look_back_period: Union[str, "_models.LookBackPeriod"],
        product: str,
        **kwargs: Any
    ) -> Optional[_models.ReservationRecommendationDetailsModel]:
        """Details of a reservation recommendation for what-if analysis of reserved instances.

        :param resource_scope: The scope associated with reservation recommendation details operations.
         This includes '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resource group scope,
         /providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for BillingAccount scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope. Required.
        :type resource_scope: str
        :param scope: Scope of the reservation. Known values are: "Single" and "Shared". Required.
        :type scope: str or ~azure.mgmt.consumption.models.Scope
        :param region: Used to select the region the recommendation should be generated for. Required.
        :type region: str
        :param term: Specify length of reservation recommendation term. Known values are: "P1Y" and
         "P3Y". Required.
        :type term: str or ~azure.mgmt.consumption.models.Term
        :param look_back_period: Filter the time period on which reservation recommendation results are
         based. Known values are: "Last7Days", "Last30Days", and "Last60Days". Required.
        :type look_back_period: str or ~azure.mgmt.consumption.models.LookBackPeriod
        :param product: Filter the products for which reservation recommendation results are generated.
         Examples: Standard_DS1_v2 (for VM), Premium_SSD_Managed_Disks_P30 (for Managed Disks).
         Required.
        :type product: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReservationRecommendationDetailsModel or None or the result of cls(response)
        :rtype: ~azure.mgmt.consumption.models.ReservationRecommendationDetailsModel or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[_models.ReservationRecommendationDetailsModel]]

        request = build_get_request(
            resource_scope=resource_scope,
            scope=scope,
            region=region,
            term=term,
            look_back_period=look_back_period,
            product=product,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.HighCasedErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("ReservationRecommendationDetailsModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{resourceScope}/providers/Microsoft.Consumption/reservationRecommendationDetails"}  # type: ignore
