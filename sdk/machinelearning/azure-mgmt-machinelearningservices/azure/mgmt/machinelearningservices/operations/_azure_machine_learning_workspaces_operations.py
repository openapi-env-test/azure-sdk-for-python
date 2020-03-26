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

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling
from .. import models
import uuid


class AzureMachineLearningWorkspacesOperationsMixin(object):

    def list_skus(
            self, custom_headers=None, raw=False, **operation_config):
        """Lists all skus with associated features.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of WorkspaceSku
        :rtype:
         ~azure.mgmt.machinelearningservices.models.WorkspaceSkuPaged[~azure.mgmt.machinelearningservices.models.WorkspaceSku]
        :raises:
         :class:`MachineLearningServiceErrorException<azure.mgmt.machinelearningservices.models.MachineLearningServiceErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_skus.metadata['url']
                path_format_arguments = {
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
                raise models.MachineLearningServiceErrorException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.WorkspaceSkuPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_skus.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/workspaces/skus'}
