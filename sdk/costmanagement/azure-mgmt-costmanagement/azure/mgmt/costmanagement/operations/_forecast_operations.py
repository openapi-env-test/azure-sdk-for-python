# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ForecastOperations(object):
    """ForecastOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.costmanagement.models
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

    def usage(
        self,
        scope,  # type: str
        parameters,  # type: "_models.ForecastDefinition"
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.QueryResult"
        """Lists the forecast charges for scope defined.

        :param scope: The scope associated with forecast operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :param parameters: Parameters supplied to the CreateOrUpdate Forecast Config operation.
        :type parameters: ~azure.mgmt.costmanagement.models.ForecastDefinition
        :param filter: May be used to filter forecasts by properties/usageDate (Utc time),
         properties/chargeType or properties/grain. The filter supports 'eq', 'lt', 'gt', 'le', 'ge',
         and 'and'. It does not currently support 'ne', 'or', or 'not'.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryResult, or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.QueryResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.QueryResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.usage.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'ForecastDefinition')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('QueryResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    usage.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/forecast'}  # type: ignore

    def external_cloud_provider_usage(
        self,
        external_cloud_provider_type,  # type: Union[str, "_models.ExternalCloudProviderType"]
        external_cloud_provider_id,  # type: str
        parameters,  # type: "_models.ForecastDefinition"
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.QueryResult"
        """Lists the forecast charges for external cloud provider type defined.

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account.
        :type external_cloud_provider_type: str or ~azure.mgmt.costmanagement.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
        :type external_cloud_provider_id: str
        :param parameters: Parameters supplied to the CreateOrUpdate Forecast Config operation.
        :type parameters: ~azure.mgmt.costmanagement.models.ForecastDefinition
        :param filter: May be used to filter forecasts by properties/usageDate (Utc time),
         properties/chargeType or properties/grain. The filter supports 'eq', 'lt', 'gt', 'le', 'ge',
         and 'and'. It does not currently support 'ne', 'or', or 'not'.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryResult, or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.QueryResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.QueryResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.external_cloud_provider_usage.metadata['url']  # type: ignore
        path_format_arguments = {
            'externalCloudProviderType': self._serialize.url("external_cloud_provider_type", external_cloud_provider_type, 'str'),
            'externalCloudProviderId': self._serialize.url("external_cloud_provider_id", external_cloud_provider_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'ForecastDefinition')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('QueryResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    external_cloud_provider_usage.metadata = {'url': '/providers/Microsoft.CostManagement/{externalCloudProviderType}/{externalCloudProviderId}/forecast'}  # type: ignore
