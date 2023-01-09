# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import sys
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._job_target_executions_operations import (
    build_get_request,
    build_list_by_job_execution_request,
    build_list_by_step_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class JobTargetExecutionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sql.aio.SqlManagementClient`'s
        :attr:`job_target_executions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_job_execution(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        create_time_min: Optional[datetime.datetime] = None,
        create_time_max: Optional[datetime.datetime] = None,
        end_time_min: Optional[datetime.datetime] = None,
        end_time_max: Optional[datetime.datetime] = None,
        is_active: Optional[bool] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.JobExecution"]:
        """Lists target executions for all steps of a job execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param job_agent_name: The name of the job agent. Required.
        :type job_agent_name: str
        :param job_name: The name of the job to get. Required.
        :type job_name: str
        :param job_execution_id: The id of the job execution. Required.
        :type job_execution_id: str
        :param create_time_min: If specified, only job executions created at or after the specified
         time are included. Default value is None.
        :type create_time_min: ~datetime.datetime
        :param create_time_max: If specified, only job executions created before the specified time are
         included. Default value is None.
        :type create_time_max: ~datetime.datetime
        :param end_time_min: If specified, only job executions completed at or after the specified time
         are included. Default value is None.
        :type end_time_min: ~datetime.datetime
        :param end_time_max: If specified, only job executions completed before the specified time are
         included. Default value is None.
        :type end_time_max: ~datetime.datetime
        :param is_active: If specified, only active or only completed job executions are included.
         Default value is None.
        :type is_active: bool
        :param skip: The number of elements in the collection to skip. Default value is None.
        :type skip: int
        :param top: The number of elements to return from the collection. Default value is None.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JobExecution or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.sql.models.JobExecution]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-11-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2020-11-01-preview")
        )
        cls: ClsType[_models.JobExecutionListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_job_execution_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    job_agent_name=job_agent_name,
                    job_name=job_name,
                    job_execution_id=job_execution_id,
                    subscription_id=self._config.subscription_id,
                    create_time_min=create_time_min,
                    create_time_max=create_time_max,
                    end_time_min=end_time_min,
                    end_time_max=end_time_max,
                    is_active=is_active,
                    skip=skip,
                    top=top,
                    api_version=api_version,
                    template_url=self.list_by_job_execution.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("JobExecutionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_job_execution.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/targets"
    }

    @distributed_trace
    def list_by_step(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        step_name: str,
        create_time_min: Optional[datetime.datetime] = None,
        create_time_max: Optional[datetime.datetime] = None,
        end_time_min: Optional[datetime.datetime] = None,
        end_time_max: Optional[datetime.datetime] = None,
        is_active: Optional[bool] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.JobExecution"]:
        """Lists the target executions of a job step execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param job_agent_name: The name of the job agent. Required.
        :type job_agent_name: str
        :param job_name: The name of the job to get. Required.
        :type job_name: str
        :param job_execution_id: The id of the job execution. Required.
        :type job_execution_id: str
        :param step_name: The name of the step. Required.
        :type step_name: str
        :param create_time_min: If specified, only job executions created at or after the specified
         time are included. Default value is None.
        :type create_time_min: ~datetime.datetime
        :param create_time_max: If specified, only job executions created before the specified time are
         included. Default value is None.
        :type create_time_max: ~datetime.datetime
        :param end_time_min: If specified, only job executions completed at or after the specified time
         are included. Default value is None.
        :type end_time_min: ~datetime.datetime
        :param end_time_max: If specified, only job executions completed before the specified time are
         included. Default value is None.
        :type end_time_max: ~datetime.datetime
        :param is_active: If specified, only active or only completed job executions are included.
         Default value is None.
        :type is_active: bool
        :param skip: The number of elements in the collection to skip. Default value is None.
        :type skip: int
        :param top: The number of elements to return from the collection. Default value is None.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JobExecution or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.sql.models.JobExecution]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-11-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2020-11-01-preview")
        )
        cls: ClsType[_models.JobExecutionListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_step_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    job_agent_name=job_agent_name,
                    job_name=job_name,
                    job_execution_id=job_execution_id,
                    step_name=step_name,
                    subscription_id=self._config.subscription_id,
                    create_time_min=create_time_min,
                    create_time_max=create_time_max,
                    end_time_min=end_time_min,
                    end_time_max=end_time_max,
                    is_active=is_active,
                    skip=skip,
                    top=top,
                    api_version=api_version,
                    template_url=self.list_by_step.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("JobExecutionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_step.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps/{stepName}/targets"
    }

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        server_name: str,
        job_agent_name: str,
        job_name: str,
        job_execution_id: str,
        step_name: str,
        target_id: str,
        **kwargs: Any
    ) -> _models.JobExecution:
        """Gets a target execution.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param job_agent_name: The name of the job agent. Required.
        :type job_agent_name: str
        :param job_name: The name of the job to get. Required.
        :type job_name: str
        :param job_execution_id: The unique id of the job execution. Required.
        :type job_execution_id: str
        :param step_name: The name of the step. Required.
        :type step_name: str
        :param target_id: The target id. Required.
        :type target_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobExecution or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.JobExecution
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-11-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2020-11-01-preview")
        )
        cls: ClsType[_models.JobExecution] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            server_name=server_name,
            job_agent_name=job_agent_name,
            job_name=job_name,
            job_execution_id=job_execution_id,
            step_name=step_name,
            target_id=target_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("JobExecution", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps/{stepName}/targets/{targetId}"
    }
