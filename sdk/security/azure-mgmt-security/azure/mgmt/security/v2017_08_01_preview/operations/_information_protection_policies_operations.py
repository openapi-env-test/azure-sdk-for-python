# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
from urllib.parse import parse_qs, urljoin, urlparse

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
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
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    scope: str,
    information_protection_policy_name: Union[str, "_models.InformationProtectionPolicyName"],
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2017-08-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Security/informationProtectionPolicies/{informationProtectionPolicyName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
        "informationProtectionPolicyName": _SERIALIZER.url("information_protection_policy_name", information_protection_policy_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_create_or_update_request(
    scope: str,
    information_protection_policy_name: Union[str, "_models.InformationProtectionPolicyName"],
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2017-08-01-preview"))  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Security/informationProtectionPolicies/{informationProtectionPolicyName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
        "informationProtectionPolicyName": _SERIALIZER.url("information_protection_policy_name", information_protection_policy_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_list_request(
    scope: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2017-08-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Security/informationProtectionPolicies")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

class InformationProtectionPoliciesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2017_08_01_preview.SecurityCenter`'s
        :attr:`information_protection_policies` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def get(
        self,
        scope: str,
        information_protection_policy_name: Union[str, "_models.InformationProtectionPolicyName"],
        **kwargs: Any
    ) -> _models.InformationProtectionPolicy:
        """Details of the information protection policy.

        :param scope: Scope of the query, can be subscription
         (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group
         (/providers/Microsoft.Management/managementGroups/mgName). Required.
        :type scope: str
        :param information_protection_policy_name: Name of the information protection policy. Known
         values are: "effective" and "custom". Required.
        :type information_protection_policy_name: str or
         ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicyName
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: InformationProtectionPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2017-08-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.InformationProtectionPolicy]

        
        request = build_get_request(
            scope=scope,
            information_protection_policy_name=information_protection_policy_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('InformationProtectionPolicy', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/{scope}/providers/Microsoft.Security/informationProtectionPolicies/{informationProtectionPolicyName}"}  # type: ignore


    @overload
    def create_or_update(
        self,
        scope: str,
        information_protection_policy_name: Union[str, "_models.InformationProtectionPolicyName"],
        information_protection_policy: _models.InformationProtectionPolicy,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.InformationProtectionPolicy:
        """Details of the information protection policy.

        :param scope: Scope of the query, can be subscription
         (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group
         (/providers/Microsoft.Management/managementGroups/mgName). Required.
        :type scope: str
        :param information_protection_policy_name: Name of the information protection policy. Known
         values are: "effective" and "custom". Required.
        :type information_protection_policy_name: str or
         ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicyName
        :param information_protection_policy: Information protection policy. Required.
        :type information_protection_policy:
         ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicy
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: InformationProtectionPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        scope: str,
        information_protection_policy_name: Union[str, "_models.InformationProtectionPolicyName"],
        information_protection_policy: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.InformationProtectionPolicy:
        """Details of the information protection policy.

        :param scope: Scope of the query, can be subscription
         (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group
         (/providers/Microsoft.Management/managementGroups/mgName). Required.
        :type scope: str
        :param information_protection_policy_name: Name of the information protection policy. Known
         values are: "effective" and "custom". Required.
        :type information_protection_policy_name: str or
         ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicyName
        :param information_protection_policy: Information protection policy. Required.
        :type information_protection_policy: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: InformationProtectionPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """


    @distributed_trace
    def create_or_update(
        self,
        scope: str,
        information_protection_policy_name: Union[str, "_models.InformationProtectionPolicyName"],
        information_protection_policy: Union[_models.InformationProtectionPolicy, IO],
        **kwargs: Any
    ) -> _models.InformationProtectionPolicy:
        """Details of the information protection policy.

        :param scope: Scope of the query, can be subscription
         (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group
         (/providers/Microsoft.Management/managementGroups/mgName). Required.
        :type scope: str
        :param information_protection_policy_name: Name of the information protection policy. Known
         values are: "effective" and "custom". Required.
        :type information_protection_policy_name: str or
         ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicyName
        :param information_protection_policy: Information protection policy. Is either a model type or
         a IO type. Required.
        :type information_protection_policy:
         ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicy or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: InformationProtectionPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2017-08-01-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.InformationProtectionPolicy]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(information_protection_policy, (IO, bytes)):
            _content = information_protection_policy
        else:
            _json = self._serialize.body(information_protection_policy, 'InformationProtectionPolicy')

        request = build_create_or_update_request(
            scope=scope,
            information_protection_policy_name=information_protection_policy_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('InformationProtectionPolicy', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('InformationProtectionPolicy', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/{scope}/providers/Microsoft.Security/informationProtectionPolicies/{informationProtectionPolicyName}"}  # type: ignore


    @distributed_trace
    def list(
        self,
        scope: str,
        **kwargs: Any
    ) -> Iterable["_models.InformationProtectionPolicy"]:
        """Information protection policies of a specific management group.

        :param scope: Scope of the query, can be subscription
         (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group
         (/providers/Microsoft.Management/managementGroups/mgName). Required.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either InformationProtectionPolicy or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.security.v2017_08_01_preview.models.InformationProtectionPolicy]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2017-08-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.InformationProtectionPolicyList]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    scope=scope,
                    api_version=api_version,
                    template_url=self.list.metadata['url'],
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
            deserialized = self._deserialize("InformationProtectionPolicyList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/{scope}/providers/Microsoft.Security/informationProtectionPolicies"}  # type: ignore
