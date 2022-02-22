# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse
from msrest import Deserializer, Serializer

from ._configuration import PurviewMetadataPoliciesClientConfiguration
from .operations import MetadataPolicyOperations, MetadataRolesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

    from azure.core.credentials import TokenCredential

class PurviewMetadataPoliciesClient:
    """PurviewMetadataPoliciesClient.

    :ivar metadata_roles: MetadataRolesOperations operations
    :vartype metadata_roles:
     azure.purview.administration.metadatapolicies.operations.MetadataRolesOperations
    :ivar metadata_policy: MetadataPolicyOperations operations
    :vartype metadata_policy:
     azure.purview.administration.metadatapolicies.operations.MetadataPolicyOperations
    :param endpoint: The endpoint of your Purview account. Example:
     https://{accountName}.purview.azure.com.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :keyword api_version: Api Version. The default value is "2021-07-01-preview". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        endpoint: str,
        credential: "TokenCredential",
        **kwargs: Any
    ) -> None:
        _endpoint = '{Endpoint}/policyStore'
        self._config = PurviewMetadataPoliciesClientConfiguration(endpoint=endpoint, credential=credential, **kwargs)
        self._client = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.metadata_roles = MetadataRolesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.metadata_policy = MetadataPolicyOperations(self._client, self._config, self._serialize, self._deserialize)


    def send_request(
        self,
        request,  # type: HttpRequest
        **kwargs: Any
    ) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> PurviewMetadataPoliciesClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
