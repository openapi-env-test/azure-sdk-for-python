# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._disk_restore_point_operations import (
    build_get_request,
    build_grant_access_request,
    build_list_by_restore_point_request,
    build_revoke_access_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DiskRestorePointOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2021_04_01.aio.ComputeManagementClient`'s
        :attr:`disk_restore_point` attribute.
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
        resource_group_name: str,
        restore_point_collection_name: str,
        vm_restore_point_name: str,
        disk_restore_point_name: str,
        **kwargs: Any
    ) -> _models.DiskRestorePoint:
        """Get disk restorePoint resource.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param restore_point_collection_name: The name of the restore point collection that the disk
         restore point belongs. Required.
        :type restore_point_collection_name: str
        :param vm_restore_point_name: The name of the vm restore point that the disk disk restore point
         belongs. Required.
        :type vm_restore_point_name: str
        :param disk_restore_point_name: The name of the disk restore point created. Required.
        :type disk_restore_point_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DiskRestorePoint or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_04_01.models.DiskRestorePoint
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.DiskRestorePoint]

        request = build_get_request(
            resource_group_name=resource_group_name,
            restore_point_collection_name=restore_point_collection_name,
            vm_restore_point_name=vm_restore_point_name,
            disk_restore_point_name=disk_restore_point_name,
            subscription_id=self._config.subscription_id,
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DiskRestorePoint", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}/restorePoints/{vmRestorePointName}/diskRestorePoints/{diskRestorePointName}"}  # type: ignore

    @distributed_trace
    def list_by_restore_point(
        self, resource_group_name: str, restore_point_collection_name: str, vm_restore_point_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.DiskRestorePoint"]:
        """Lists diskRestorePoints under a vmRestorePoint.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param restore_point_collection_name: The name of the restore point collection that the disk
         restore point belongs. Required.
        :type restore_point_collection_name: str
        :param vm_restore_point_name: The name of the vm restore point that the disk disk restore point
         belongs. Required.
        :type vm_restore_point_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DiskRestorePoint or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.compute.v2021_04_01.models.DiskRestorePoint]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.DiskRestorePointList]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_restore_point_request(
                    resource_group_name=resource_group_name,
                    restore_point_collection_name=restore_point_collection_name,
                    vm_restore_point_name=vm_restore_point_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_restore_point.metadata["url"],
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
            deserialized = self._deserialize("DiskRestorePointList", pipeline_response)
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

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_restore_point.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}/restorePoints/{vmRestorePointName}/diskRestorePoints"}  # type: ignore

    async def _grant_access_initial(
        self,
        resource_group_name: str,
        restore_point_collection_name: str,
        vm_restore_point_name: str,
        disk_restore_point_name: str,
        grant_access_data: Union[_models.GrantAccessData, IO],
        **kwargs: Any
    ) -> Optional[_models.AccessUri]:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[_models.AccessUri]]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(grant_access_data, (IO, bytes)):
            _content = grant_access_data
        else:
            _json = self._serialize.body(grant_access_data, "GrantAccessData")

        request = build_grant_access_request(
            resource_group_name=resource_group_name,
            restore_point_collection_name=restore_point_collection_name,
            vm_restore_point_name=vm_restore_point_name,
            disk_restore_point_name=disk_restore_point_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._grant_access_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("AccessUri", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _grant_access_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}/restorePoints/{vmRestorePointName}/diskRestorePoints/{diskRestorePointName}/beginGetAccess"}  # type: ignore

    @overload
    async def begin_grant_access(
        self,
        resource_group_name: str,
        restore_point_collection_name: str,
        vm_restore_point_name: str,
        disk_restore_point_name: str,
        grant_access_data: _models.GrantAccessData,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AccessUri]:
        """Grants access to a diskRestorePoint.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param restore_point_collection_name: The name of the restore point collection that the disk
         restore point belongs. Required.
        :type restore_point_collection_name: str
        :param vm_restore_point_name: The name of the vm restore point that the disk disk restore point
         belongs. Required.
        :type vm_restore_point_name: str
        :param disk_restore_point_name: The name of the disk restore point created. Required.
        :type disk_restore_point_name: str
        :param grant_access_data: Access data object supplied in the body of the get disk access
         operation. Required.
        :type grant_access_data: ~azure.mgmt.compute.v2021_04_01.models.GrantAccessData
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either AccessUri or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2021_04_01.models.AccessUri]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_grant_access(
        self,
        resource_group_name: str,
        restore_point_collection_name: str,
        vm_restore_point_name: str,
        disk_restore_point_name: str,
        grant_access_data: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AccessUri]:
        """Grants access to a diskRestorePoint.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param restore_point_collection_name: The name of the restore point collection that the disk
         restore point belongs. Required.
        :type restore_point_collection_name: str
        :param vm_restore_point_name: The name of the vm restore point that the disk disk restore point
         belongs. Required.
        :type vm_restore_point_name: str
        :param disk_restore_point_name: The name of the disk restore point created. Required.
        :type disk_restore_point_name: str
        :param grant_access_data: Access data object supplied in the body of the get disk access
         operation. Required.
        :type grant_access_data: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either AccessUri or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2021_04_01.models.AccessUri]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_grant_access(
        self,
        resource_group_name: str,
        restore_point_collection_name: str,
        vm_restore_point_name: str,
        disk_restore_point_name: str,
        grant_access_data: Union[_models.GrantAccessData, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AccessUri]:
        """Grants access to a diskRestorePoint.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param restore_point_collection_name: The name of the restore point collection that the disk
         restore point belongs. Required.
        :type restore_point_collection_name: str
        :param vm_restore_point_name: The name of the vm restore point that the disk disk restore point
         belongs. Required.
        :type vm_restore_point_name: str
        :param disk_restore_point_name: The name of the disk restore point created. Required.
        :type disk_restore_point_name: str
        :param grant_access_data: Access data object supplied in the body of the get disk access
         operation. Is either a model type or a IO type. Required.
        :type grant_access_data: ~azure.mgmt.compute.v2021_04_01.models.GrantAccessData or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either AccessUri or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2021_04_01.models.AccessUri]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AccessUri]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._grant_access_initial(  # type: ignore
                resource_group_name=resource_group_name,
                restore_point_collection_name=restore_point_collection_name,
                vm_restore_point_name=vm_restore_point_name,
                disk_restore_point_name=disk_restore_point_name,
                grant_access_data=grant_access_data,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("AccessUri", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_grant_access.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}/restorePoints/{vmRestorePointName}/diskRestorePoints/{diskRestorePointName}/beginGetAccess"}  # type: ignore

    async def _revoke_access_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        restore_point_collection_name: str,
        vm_restore_point_name: str,
        disk_restore_point_name: str,
        **kwargs: Any
    ) -> None:
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_revoke_access_request(
            resource_group_name=resource_group_name,
            restore_point_collection_name=restore_point_collection_name,
            vm_restore_point_name=vm_restore_point_name,
            disk_restore_point_name=disk_restore_point_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._revoke_access_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _revoke_access_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}/restorePoints/{vmRestorePointName}/diskRestorePoints/{diskRestorePointName}/endGetAccess"}  # type: ignore

    @distributed_trace_async
    async def begin_revoke_access(
        self,
        resource_group_name: str,
        restore_point_collection_name: str,
        vm_restore_point_name: str,
        disk_restore_point_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Revokes access to a diskRestorePoint.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param restore_point_collection_name: The name of the restore point collection that the disk
         restore point belongs. Required.
        :type restore_point_collection_name: str
        :param vm_restore_point_name: The name of the vm restore point that the disk disk restore point
         belongs. Required.
        :type vm_restore_point_name: str
        :param disk_restore_point_name: The name of the disk restore point created. Required.
        :type disk_restore_point_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._revoke_access_initial(  # type: ignore
                resource_group_name=resource_group_name,
                restore_point_collection_name=restore_point_collection_name,
                vm_restore_point_name=vm_restore_point_name,
                disk_restore_point_name=disk_restore_point_name,
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
            polling_method = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_revoke_access.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}/restorePoints/{vmRestorePointName}/diskRestorePoints/{diskRestorePointName}/endGetAccess"}  # type: ignore
