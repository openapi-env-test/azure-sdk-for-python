# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class P2SVpnGatewaysOperations:
    """P2SVpnGatewaysOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.network.v2019_09_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        resource_group_name: str,
        gateway_name: str,
        **kwargs
    ) -> "models.P2SVpnGateway":
        """Retrieves the details of a virtual wan p2s vpn gateway.

        :param resource_group_name: The resource group name of the P2SVpnGateway.
        :type resource_group_name: str
        :param gateway_name: The name of the gateway.
        :type gateway_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: P2SVpnGateway or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2019_09_01.models.P2SVpnGateway
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.P2SVpnGateway"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-09-01"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('P2SVpnGateway', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}'}  # type: ignore

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        gateway_name: str,
        p2_s_vpn_gateway_parameters: "models.P2SVpnGateway",
        **kwargs
    ) -> "models.P2SVpnGateway":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.P2SVpnGateway"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-09-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(p2_s_vpn_gateway_parameters, 'P2SVpnGateway')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('P2SVpnGateway', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('P2SVpnGateway', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}'}  # type: ignore

    async def create_or_update(
        self,
        resource_group_name: str,
        gateway_name: str,
        p2_s_vpn_gateway_parameters: "models.P2SVpnGateway",
        **kwargs
    ) -> "models.P2SVpnGateway":
        """Creates a virtual wan p2s vpn gateway if it doesn't exist else updates the existing gateway.

        :param resource_group_name: The resource group name of the P2SVpnGateway.
        :type resource_group_name: str
        :param gateway_name: The name of the gateway.
        :type gateway_name: str
        :param p2_s_vpn_gateway_parameters: Parameters supplied to create or Update a virtual wan p2s
     vpn gateway.
        :type p2_s_vpn_gateway_parameters: ~azure.mgmt.network.v2019_09_01.models.P2SVpnGateway
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: P2SVpnGateway
        :rtype: ~azure.mgmt.network.v2019_09_01.models.P2SVpnGateway
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.P2SVpnGateway"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = await self._create_or_update_initial(
            resource_group_name=resource_group_name,
            gateway_name=gateway_name,
            p2_s_vpn_gateway_parameters=p2_s_vpn_gateway_parameters,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('P2SVpnGateway', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'},  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}'}  # type: ignore

    async def update_tags(
        self,
        resource_group_name: str,
        gateway_name: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> "models.P2SVpnGateway":
        """Updates virtual wan p2s vpn gateway tags.

        :param resource_group_name: The resource group name of the P2SVpnGateway.
        :type resource_group_name: str
        :param gateway_name: The name of the gateway.
        :type gateway_name: str
        :param tags: Resource tags.
        :type tags: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: P2SVpnGateway or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2019_09_01.models.P2SVpnGateway
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.P2SVpnGateway"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _p2_s_vpn_gateway_parameters = models.TagsObject(tags=tags)
        api_version = "2019-09-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_tags.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_p2_s_vpn_gateway_parameters, 'TagsObject')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('P2SVpnGateway', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    update_tags.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}'}  # type: ignore

    async def _delete_initial(
        self,
        resource_group_name: str,
        gateway_name: str,
        **kwargs
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-09-01"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        gateway_name: str,
        **kwargs
    ) -> None:
        """Deletes a virtual wan p2s vpn gateway.

        :param resource_group_name: The resource group name of the P2SVpnGateway.
        :type resource_group_name: str
        :param gateway_name: The name of the gateway.
        :type gateway_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = await self._delete_initial(
            resource_group_name=resource_group_name,
            gateway_name=gateway_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'},  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}'}  # type: ignore

    def list_by_resource_group(
        self,
        resource_group_name: str,
        **kwargs
    ) -> AsyncIterable["models.ListP2SVpnGatewaysResult"]:
        """Lists all the P2SVpnGateways in a resource group.

        :param resource_group_name: The resource group name of the P2SVpnGateway.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ListP2SVpnGatewaysResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2019_09_01.models.ListP2SVpnGatewaysResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ListP2SVpnGatewaysResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-09-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ListP2SVpnGatewaysResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways'}  # type: ignore

    def list(
        self,
        **kwargs
    ) -> AsyncIterable["models.ListP2SVpnGatewaysResult"]:
        """Lists all the P2SVpnGateways in a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ListP2SVpnGatewaysResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2019_09_01.models.ListP2SVpnGatewaysResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ListP2SVpnGatewaysResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-09-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ListP2SVpnGatewaysResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Network/p2svpnGateways'}  # type: ignore

    async def _generate_vpn_profile_initial(
        self,
        resource_group_name: str,
        gateway_name: str,
        authentication_method: Optional[Union[str, "models.AuthenticationMethod"]] = None,
        **kwargs
    ) -> "models.VpnProfileResponse":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.VpnProfileResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _parameters = models.P2SVpnProfileParameters(authentication_method=authentication_method)
        api_version = "2019-09-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._generate_vpn_profile_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_parameters, 'P2SVpnProfileParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('VpnProfileResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _generate_vpn_profile_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/generatevpnprofile'}  # type: ignore

    async def generate_vpn_profile(
        self,
        resource_group_name: str,
        gateway_name: str,
        authentication_method: Optional[Union[str, "models.AuthenticationMethod"]] = None,
        **kwargs
    ) -> "models.VpnProfileResponse":
        """Generates VPN profile for P2S client of the P2SVpnGateway in the specified resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param gateway_name: The name of the P2SVpnGateway.
        :type gateway_name: str
        :param authentication_method: VPN client authentication method.
        :type authentication_method: str or ~azure.mgmt.network.v2019_09_01.models.AuthenticationMethod
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: VpnProfileResponse
        :rtype: ~azure.mgmt.network.v2019_09_01.models.VpnProfileResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.VpnProfileResponse"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = await self._generate_vpn_profile_initial(
            resource_group_name=resource_group_name,
            gateway_name=gateway_name,
            authentication_method=authentication_method,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('VpnProfileResponse', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'},  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    generate_vpn_profile.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/generatevpnprofile'}  # type: ignore

    async def _get_p2_s_vpn_connection_health_initial(
        self,
        resource_group_name: str,
        gateway_name: str,
        **kwargs
    ) -> "models.P2SVpnGateway":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.P2SVpnGateway"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-09-01"

        # Construct URL
        url = self._get_p2_s_vpn_connection_health_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('P2SVpnGateway', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _get_p2_s_vpn_connection_health_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/getP2sVpnConnectionHealth'}  # type: ignore

    async def get_p2_s_vpn_connection_health(
        self,
        resource_group_name: str,
        gateway_name: str,
        **kwargs
    ) -> "models.P2SVpnGateway":
        """Gets the connection health of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param gateway_name: The name of the P2SVpnGateway.
        :type gateway_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: P2SVpnGateway
        :rtype: ~azure.mgmt.network.v2019_09_01.models.P2SVpnGateway
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.P2SVpnGateway"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = await self._get_p2_s_vpn_connection_health_initial(
            resource_group_name=resource_group_name,
            gateway_name=gateway_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('P2SVpnGateway', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'},  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    get_p2_s_vpn_connection_health.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/getP2sVpnConnectionHealth'}  # type: ignore

    async def _get_p2_s_vpn_connection_health_detailed_initial(
        self,
        resource_group_name: str,
        gateway_name: str,
        vpn_user_names_filter: Optional[List[str]] = None,
        output_blob_sas_url: Optional[str] = None,
        **kwargs
    ) -> "models.P2SVpnConnectionHealth":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.P2SVpnConnectionHealth"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _request = models.P2SVpnConnectionHealthRequest(vpn_user_names_filter=vpn_user_names_filter, output_blob_sas_url=output_blob_sas_url)
        api_version = "2019-09-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._get_p2_s_vpn_connection_health_detailed_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_request, 'P2SVpnConnectionHealthRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('P2SVpnConnectionHealth', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _get_p2_s_vpn_connection_health_detailed_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/getP2sVpnConnectionHealthDetailed'}  # type: ignore

    async def get_p2_s_vpn_connection_health_detailed(
        self,
        resource_group_name: str,
        gateway_name: str,
        vpn_user_names_filter: Optional[List[str]] = None,
        output_blob_sas_url: Optional[str] = None,
        **kwargs
    ) -> "models.P2SVpnConnectionHealth":
        """Gets the sas url to get the connection health detail of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param gateway_name: The name of the P2SVpnGateway.
        :type gateway_name: str
        :param vpn_user_names_filter: The list of p2s vpn user names whose p2s vpn connection detailed
     health to retrieve for.
        :type vpn_user_names_filter: list[str]
        :param output_blob_sas_url: The sas-url to download the P2S Vpn connection health detail.
        :type output_blob_sas_url: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: P2SVpnConnectionHealth
        :rtype: ~azure.mgmt.network.v2019_09_01.models.P2SVpnConnectionHealth
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.P2SVpnConnectionHealth"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = await self._get_p2_s_vpn_connection_health_detailed_initial(
            resource_group_name=resource_group_name,
            gateway_name=gateway_name,
            vpn_user_names_filter=vpn_user_names_filter,
            output_blob_sas_url=output_blob_sas_url,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('P2SVpnConnectionHealth', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'},  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    get_p2_s_vpn_connection_health_detailed.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/getP2sVpnConnectionHealthDetailed'}  # type: ignore
