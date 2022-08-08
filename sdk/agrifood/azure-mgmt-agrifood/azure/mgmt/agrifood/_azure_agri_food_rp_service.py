# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models
from ._configuration import AzureAgriFoodRPServiceConfiguration
from .operations import ExtensionsOperations, FarmBeatsExtensionsOperations, FarmBeatsModelsOperations, LocationsOperations, Operations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class AzureAgriFoodRPService:
    """APIs documentation for Azure AgriFood Resource Provider Service. test.

    :ivar extensions: ExtensionsOperations operations
    :vartype extensions: azure.mgmt.agrifood.operations.ExtensionsOperations
    :ivar farm_beats_extensions: FarmBeatsExtensionsOperations operations
    :vartype farm_beats_extensions: azure.mgmt.agrifood.operations.FarmBeatsExtensionsOperations
    :ivar farm_beats_models: FarmBeatsModelsOperations operations
    :vartype farm_beats_models: azure.mgmt.agrifood.operations.FarmBeatsModelsOperations
    :ivar locations: LocationsOperations operations
    :vartype locations: azure.mgmt.agrifood.operations.LocationsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.agrifood.operations.Operations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2020-05-12-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AzureAgriFoodRPServiceConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.extensions = ExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.farm_beats_extensions = FarmBeatsExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.farm_beats_models = FarmBeatsModelsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.locations = LocationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureAgriFoodRPService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
