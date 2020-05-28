# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ProfilesOperations(object):
    """ProfilesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.cdn.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ProfileListResult"]
        """Lists all of the CDN profiles within an Azure subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ProfileListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.cdn.models.ProfileListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProfileListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-15"

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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProfileListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Cdn/profiles'}  # type: ignore

    def list_by_resource_group(
        self,
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ProfileListResult"]
        """Lists all of the CDN profiles within a resource group.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ProfileListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.cdn.models.ProfileListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProfileListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-15"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProfileListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Profile"
        """Gets a CDN profile with the specified profile name under the specified subscription and resource group.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
        :type profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Profile or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.Profile
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Profile"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-15"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str'),
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
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Profile', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}'}  # type: ignore

    def _create_initial(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        profile,  # type: "models.Profile"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Profile"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Profile"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-15"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str'),
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
        body_content = self._serialize.body(profile, 'Profile')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Profile', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Profile', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('Profile', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}'}  # type: ignore

    def begin_create(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        profile,  # type: "models.Profile"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Creates a new CDN profile with a profile name under the specified subscription and resource group.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
        :type profile_name: str
        :param profile: Profile properties needed to create a new profile.
        :type profile: ~azure.mgmt.cdn.models.Profile
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns Profile
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.cdn.models.Profile]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Profile"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._create_initial(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            profile=profile,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Profile', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}'}  # type: ignore

    def _update_initial(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Profile"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Profile"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _profile_update_parameters = models.ProfileUpdateParameters(tags=tags)
        api_version = "2019-06-15"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str'),
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
        body_content = self._serialize.body(_profile_update_parameters, 'ProfileUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Profile', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('Profile', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}'}  # type: ignore

    def begin_update(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Updates an existing CDN profile with the specified profile name under the specified subscription and resource group.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
        :type profile_name: str
        :param tags: Profile tags.
        :type tags: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns Profile
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.cdn.models.Profile]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Profile"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._update_initial(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            tags=tags,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Profile', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}'}  # type: ignore

    def _delete_initial(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-15"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}'}  # type: ignore

    def begin_delete(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Deletes an existing CDN profile with the specified parameters. Deleting a profile will result in the deletion of all of the sub-resources including endpoints, origins and custom domains.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
        :type profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}'}  # type: ignore

    def generate_sso_uri(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SsoUri"
        """Generates a dynamic SSO URI used to sign in to the CDN supplemental portal. Supplemental portal is used to configure advanced feature capabilities that are not yet available in the Azure portal, such as core reports in a standard profile; rules engine, advanced HTTP reports, and real-time stats and alerts in a premium profile. The SSO URI changes approximately every 10 minutes.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
        :type profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SsoUri or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.SsoUri
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SsoUri"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-15"

        # Construct URL
        url = self.generate_sso_uri.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SsoUri', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    generate_sso_uri.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/generateSsoUri'}  # type: ignore

    def list_supported_optimization_types(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SupportedOptimizationTypesListResult"
        """Gets the supported optimization types for the current profile. A user can create an endpoint with an optimization type from the listed values.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
        :type profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SupportedOptimizationTypesListResult or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.SupportedOptimizationTypesListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SupportedOptimizationTypesListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-15"

        # Construct URL
        url = self.list_supported_optimization_types.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SupportedOptimizationTypesListResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list_supported_optimization_types.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getSupportedOptimizationTypes'}  # type: ignore

    def list_resource_usage(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ResourceUsageListResult"]
        """Checks the quota and actual usage of endpoints under the given CDN profile.

        :param resource_group_name: Name of the Resource group within the Azure subscription.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
        :type profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ResourceUsageListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.cdn.models.ResourceUsageListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ResourceUsageListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-15"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_resource_usage.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'profileName': self._serialize.url("profile_name", profile_name, 'str'),
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
            request = self._client.post(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ResourceUsageListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_resource_usage.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/checkResourceUsage'}  # type: ignore
