# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._inbound_security_rule_operations import build_create_or_update_request_initial
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class InboundSecurityRuleOperations:
    """InboundSecurityRuleOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.network.v2021_05_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        network_virtual_appliance_name: str,
        rule_collection_name: str,
        parameters: "_models.InboundSecurityRule",
        **kwargs: Any
    ) -> "_models.InboundSecurityRule":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.InboundSecurityRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'InboundSecurityRule')

        request = build_create_or_update_request_initial(
            resource_group_name=resource_group_name,
            network_virtual_appliance_name=network_virtual_appliance_name,
            rule_collection_name=rule_collection_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self._create_or_update_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('InboundSecurityRule', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('InboundSecurityRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/inboundSecurityRules/{ruleCollectionName}'}  # type: ignore


    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        network_virtual_appliance_name: str,
        rule_collection_name: str,
        parameters: "_models.InboundSecurityRule",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.InboundSecurityRule"]:
        """Creates or updates the specified Network Virtual Appliance Inbound Security Rules.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param network_virtual_appliance_name: The name of the Network Virtual Appliance.
        :type network_virtual_appliance_name: str
        :param rule_collection_name: The name of security rule collection.
        :type rule_collection_name: str
        :param parameters: Parameters supplied to the create or update Network Virtual Appliance
         Inbound Security Rules operation.
        :type parameters: ~azure.mgmt.network.v2021_05_01.models.InboundSecurityRule
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either InboundSecurityRule or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2021_05_01.models.InboundSecurityRule]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.InboundSecurityRule"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                network_virtual_appliance_name=network_virtual_appliance_name,
                rule_collection_name=rule_collection_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('InboundSecurityRule', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/inboundSecurityRules/{ruleCollectionName}'}  # type: ignore
