# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._data_box_management_client_operations import build_mitigate_request
from .._vendor import MixinABC
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DataBoxManagementClientOperationsMixin(MixinABC):

    @overload
    async def mitigate(  # pylint: disable=inconsistent-return-statements
        self,
        job_name: str,
        resource_group_name: str,
        mitigate_job_request: _models.MitigateJobRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Request to mitigate for a given job.

        :param job_name: The name of the job Resource within the specified resource group. job names
         must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
         Required.
        :type job_name: str
        :param resource_group_name: The Resource Group Name. Required.
        :type resource_group_name: str
        :param mitigate_job_request: Mitigation Request. Required.
        :type mitigate_job_request: ~azure.mgmt.databox.v2021_12_01.models.MitigateJobRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def mitigate(  # pylint: disable=inconsistent-return-statements
        self,
        job_name: str,
        resource_group_name: str,
        mitigate_job_request: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Request to mitigate for a given job.

        :param job_name: The name of the job Resource within the specified resource group. job names
         must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
         Required.
        :type job_name: str
        :param resource_group_name: The Resource Group Name. Required.
        :type resource_group_name: str
        :param mitigate_job_request: Mitigation Request. Required.
        :type mitigate_job_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """


    @distributed_trace_async
    async def mitigate(  # pylint: disable=inconsistent-return-statements
        self,
        job_name: str,
        resource_group_name: str,
        mitigate_job_request: Union[_models.MitigateJobRequest, IO],
        **kwargs: Any
    ) -> None:
        """Request to mitigate for a given job.

        :param job_name: The name of the job Resource within the specified resource group. job names
         must be between 3 and 24 characters in length and use any alphanumeric and underscore only.
         Required.
        :type job_name: str
        :param resource_group_name: The Resource Group Name. Required.
        :type resource_group_name: str
        :param mitigate_job_request: Mitigation Request. Is either a model type or a IO type. Required.
        :type mitigate_job_request: ~azure.mgmt.databox.v2021_12_01.models.MitigateJobRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-12-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(mitigate_job_request, (IO, bytes)):
            _content = mitigate_job_request
        else:
            _json = self._serialize.body(mitigate_job_request, 'MitigateJobRequest')

        request = build_mitigate_request(
            job_name=job_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.mitigate.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ApiError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    mitigate.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/jobs/{jobName}/mitigate"}  # type: ignore

