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


class DisasterRecoveryConfigsOperations(object):
    """DisasterRecoveryConfigsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API Version. Constant value: "2017-04-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2017-04-01"

        self.config = config

    def list_authorization_rules(
            self, resource_group_name, namespace_name, alias, custom_headers=None, raw=False, **operation_config):
        """Gets a list of authorization rules for a Namespace.

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name
        :type alias: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of AuthorizationRule
        :rtype:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.AuthorizationRulePaged[~azure.mgmt.eventhub.v2018_01_01_preview.models.AuthorizationRule]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_authorization_rules.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
                    'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
                    'alias': self._serialize.url("alias", alias, 'str', max_length=50, min_length=1),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
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
        deserialized = models.AuthorizationRulePaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_authorization_rules.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/authorizationRules'}

    def get_authorization_rule(
            self, resource_group_name, namespace_name, alias, authorization_rule_name, custom_headers=None, raw=False, **operation_config):
        """Gets an AuthorizationRule for a Namespace by rule name.

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name
        :type alias: str
        :param authorization_rule_name: The authorization rule name.
        :type authorization_rule_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AuthorizationRule or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.AuthorizationRule or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_authorization_rule.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'alias': self._serialize.url("alias", alias, 'str', max_length=50, min_length=1),
            'authorizationRuleName': self._serialize.url("authorization_rule_name", authorization_rule_name, 'str', min_length=1),
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

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AuthorizationRule', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_authorization_rule.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/authorizationRules/{authorizationRuleName}'}

    def list_keys(
            self, resource_group_name, namespace_name, alias, authorization_rule_name, custom_headers=None, raw=False, **operation_config):
        """Gets the primary and secondary connection strings for the Namespace.

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name
        :type alias: str
        :param authorization_rule_name: The authorization rule name.
        :type authorization_rule_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AccessKeys or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.eventhub.v2018_01_01_preview.models.AccessKeys or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_keys.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'alias': self._serialize.url("alias", alias, 'str', max_length=50, min_length=1),
            'authorizationRuleName': self._serialize.url("authorization_rule_name", authorization_rule_name, 'str', min_length=1),
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
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AccessKeys', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_keys.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/authorizationRules/{authorizationRuleName}/listKeys'}

    def check_name_availability(
            self, resource_group_name, namespace_name, name, custom_headers=None, raw=False, **operation_config):
        """Check the give Namespace name availability.

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param name: Name to check the namespace name availability
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckNameAvailabilityResult or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.CheckNameAvailabilityResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        parameters = models.CheckNameAvailabilityParameter(name=name)

        # Construct URL
        url = self.check_name_availability.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6)
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
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'CheckNameAvailabilityParameter')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    check_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/checkNameAvailability'}

    def list(
            self, resource_group_name, namespace_name, custom_headers=None, raw=False, **operation_config):
        """Gets all Alias(Disaster Recovery configurations).

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of ArmDisasterRecovery
        :rtype:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.ArmDisasterRecoveryPaged[~azure.mgmt.eventhub.v2018_01_01_preview.models.ArmDisasterRecovery]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
                    'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
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
        deserialized = models.ArmDisasterRecoveryPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs'}

    def create_or_update(
            self, resource_group_name, namespace_name, alias, partner_namespace=None, alternate_name=None, custom_headers=None, raw=False, **operation_config):
        """Creates or updates a new Alias(Disaster Recovery configuration).

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name
        :type alias: str
        :param partner_namespace: ARM Id of the Primary/Secondary eventhub
         namespace name, which is part of GEO DR pairing
        :type partner_namespace: str
        :param alternate_name: Alternate name specified when alias and
         namespace names are same.
        :type alternate_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ArmDisasterRecovery or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.ArmDisasterRecovery or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        parameters = models.ArmDisasterRecovery(partner_namespace=partner_namespace, alternate_name=alternate_name)

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'alias': self._serialize.url("alias", alias, 'str', max_length=50, min_length=1),
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
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ArmDisasterRecovery')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ArmDisasterRecovery', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}'}

    def delete(
            self, resource_group_name, namespace_name, alias, custom_headers=None, raw=False, **operation_config):
        """Deletes an Alias(Disaster Recovery configuration).

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name
        :type alias: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'alias': self._serialize.url("alias", alias, 'str', max_length=50, min_length=1),
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
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}'}

    def get(
            self, resource_group_name, namespace_name, alias, custom_headers=None, raw=False, **operation_config):
        """Retrieves Alias(Disaster Recovery configuration) for primary or
        secondary namespace.

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name
        :type alias: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ArmDisasterRecovery or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.ArmDisasterRecovery or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'alias': self._serialize.url("alias", alias, 'str', max_length=50, min_length=1),
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

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ArmDisasterRecovery', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}'}

    def break_pairing(
            self, resource_group_name, namespace_name, alias, custom_headers=None, raw=False, **operation_config):
        """This operation disables the Disaster Recovery and stops replicating
        changes from primary to secondary namespaces.

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name
        :type alias: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.break_pairing.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'alias': self._serialize.url("alias", alias, 'str', max_length=50, min_length=1),
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
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    break_pairing.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/breakPairing'}

    def fail_over(
            self, resource_group_name, namespace_name, alias, custom_headers=None, raw=False, **operation_config):
        """Invokes GEO DR failover and reconfigure the alias to point to the
        secondary namespace.

        :param resource_group_name: Name of the resource group within the
         azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name
        :type alias: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.fail_over.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'alias': self._serialize.url("alias", alias, 'str', max_length=50, min_length=1),
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
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    fail_over.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/failover'}
