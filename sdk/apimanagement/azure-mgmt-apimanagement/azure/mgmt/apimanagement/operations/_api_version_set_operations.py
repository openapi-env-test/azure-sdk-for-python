# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ApiVersionSetOperations(object):
    """ApiVersionSetOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API to be used with the client request. Constant value: "2020-06-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-06-01-preview"

        self.config = config

    def list_by_service(
            self, resource_group_name, service_name, filter=None, top=None, skip=None, custom_headers=None, raw=False, **operation_config):
        """Lists a collection of API Version Sets in the specified service
        instance.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param filter: |   Field     |     Usage     |     Supported operators
         |     Supported functions
         |</br>|-------------|-------------|-------------|-------------|</br>
        :type filter: str
        :param top: Number of records to return.
        :type top: int
        :param skip: Number of records to skip.
        :type skip: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of ApiVersionSetContract
        :rtype:
         ~azure.mgmt.apimanagement.models.ApiVersionSetContractPaged[~azure.mgmt.apimanagement.models.ApiVersionSetContract]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.apimanagement.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_service.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=1)
                if skip is not None:
                    query_parameters['$skip'] = self._serialize.query("skip", skip, 'int', minimum=0)
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.ApiVersionSetContractPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_service.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apiVersionSets'}

    def get_entity_tag(
            self, resource_group_name, service_name, version_set_id, custom_headers=None, raw=False, **operation_config):
        """Gets the entity state (Etag) version of the Api Version Set specified
        by its identifier.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param version_set_id: Api Version Set identifier. Must be unique in
         the current API Management service instance.
        :type version_set_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.apimanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_entity_tag.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'versionSetId': self._serialize.url("version_set_id", version_set_id, 'str', max_length=80, min_length=1, pattern=r'^[^*#&+:<>?]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'ETag': 'str',
            })
            return client_raw_response
    get_entity_tag.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apiVersionSets/{versionSetId}'}

    def get(
            self, resource_group_name, service_name, version_set_id, custom_headers=None, raw=False, **operation_config):
        """Gets the details of the Api Version Set specified by its identifier.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param version_set_id: Api Version Set identifier. Must be unique in
         the current API Management service instance.
        :type version_set_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ApiVersionSetContract or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.apimanagement.models.ApiVersionSetContract or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.apimanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'versionSetId': self._serialize.url("version_set_id", version_set_id, 'str', max_length=80, min_length=1, pattern=r'^[^*#&+:<>?]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ApiVersionSetContract', response)
            header_dict = {
                'ETag': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apiVersionSets/{versionSetId}'}

    def create_or_update(
            self, resource_group_name, service_name, version_set_id, parameters, if_match=None, custom_headers=None, raw=False, **operation_config):
        """Creates or Updates a Api Version Set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param version_set_id: Api Version Set identifier. Must be unique in
         the current API Management service instance.
        :type version_set_id: str
        :param parameters: Create or update parameters.
        :type parameters:
         ~azure.mgmt.apimanagement.models.ApiVersionSetContract
        :param if_match: ETag of the Entity. Not required when creating an
         entity, but required when updating an entity.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ApiVersionSetContract or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.apimanagement.models.ApiVersionSetContract or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.apimanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'versionSetId': self._serialize.url("version_set_id", version_set_id, 'str', max_length=80, min_length=1, pattern=r'^[^*#&+:<>?]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ApiVersionSetContract')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ErrorResponseException(self._deserialize, response)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ApiVersionSetContract', response)
            header_dict = {
                'ETag': 'str',
            }
        if response.status_code == 201:
            deserialized = self._deserialize('ApiVersionSetContract', response)
            header_dict = {
                'ETag': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apiVersionSets/{versionSetId}'}

    def update(
            self, resource_group_name, service_name, version_set_id, parameters, if_match, custom_headers=None, raw=False, **operation_config):
        """Updates the details of the Api VersionSet specified by its identifier.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param version_set_id: Api Version Set identifier. Must be unique in
         the current API Management service instance.
        :type version_set_id: str
        :param parameters: Update parameters.
        :type parameters:
         ~azure.mgmt.apimanagement.models.ApiVersionSetUpdateParameters
        :param if_match: ETag of the Entity. ETag should match the current
         entity state from the header response of the GET request or it should
         be * for unconditional update.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.apimanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'versionSetId': self._serialize.url("version_set_id", version_set_id, 'str', max_length=80, min_length=1, pattern=r'^[^*#&+:<>?]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ApiVersionSetUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apiVersionSets/{versionSetId}'}

    def delete(
            self, resource_group_name, service_name, version_set_id, if_match, custom_headers=None, raw=False, **operation_config):
        """Deletes specific Api Version Set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param version_set_id: Api Version Set identifier. Must be unique in
         the current API Management service instance.
        :type version_set_id: str
        :param if_match: ETag of the Entity. ETag should match the current
         entity state from the header response of the GET request or it should
         be * for unconditional update.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.apimanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
            'versionSetId': self._serialize.url("version_set_id", version_set_id, 'str', max_length=80, min_length=1, pattern=r'^[^*#&+:<>?]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apiVersionSets/{versionSetId}'}
