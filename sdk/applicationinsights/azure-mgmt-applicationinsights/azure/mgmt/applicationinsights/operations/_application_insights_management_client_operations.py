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
from .. import models
import uuid


class ApplicationInsightsManagementClientOperationsMixin(object):

    def get_test_result_file(
            self, resource_group_name, web_test_name, geo_location_id, time_stamp, download_as, test_successful_criteria=None, continuation_token=None, custom_headers=None, raw=False, **operation_config):
        """Returns a file test result for the matching test.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param web_test_name: The name of the Application Insights webtest
         resource.
        :type web_test_name: str
        :param geo_location_id: The location ID where the webtest was
         physically run.
        :type geo_location_id: str
        :param time_stamp: The posix (epoch) time stamp for the webtest
         result.
        :type time_stamp: long
        :param download_as: The format to use when returning the webtest
         result. Possible values include: 'WebTestResult', 'Json'
        :type download_as: str or
         ~azure.mgmt.applicationinsights.models.DownloadAs
        :param test_successful_criteria: The success state criteria for the
         webtest result.
        :type test_successful_criteria: bool
        :param continuation_token: The continuation token.
        :type continuation_token: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TestResultFileResponse or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.applicationinsights.models.TestResultFileResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.applicationinsights.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_test_result_file.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
            'webTestName': self._serialize.url("web_test_name", web_test_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)
        query_parameters['geoLocationId'] = self._serialize.query("geo_location_id", geo_location_id, 'str')
        query_parameters['timeStamp'] = self._serialize.query("time_stamp", time_stamp, 'long')
        query_parameters['downloadAs'] = self._serialize.query("download_as", download_as, 'str')
        if test_successful_criteria is not None:
            query_parameters['testSuccessfulCriteria'] = self._serialize.query("test_successful_criteria", test_successful_criteria, 'bool')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query("continuation_token", continuation_token, 'str')

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
            deserialized = self._deserialize('TestResultFileResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_test_result_file.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/webtests/{webTestName}/getTestResultFile'}
