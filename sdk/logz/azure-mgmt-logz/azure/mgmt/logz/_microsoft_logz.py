# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import MicrosoftLogzConfiguration
from .operations import MonitorsOperations
from .operations import Operations
from .operations import TagRulesOperations
from .operations import SingleSignOnOperations
from .operations import SubAccountOperations
from .operations import SubAccountTagRulesOperations
from . import models


class MicrosoftLogz(object):
    """MicrosoftLogz.

    :ivar monitors: MonitorsOperations operations
    :vartype monitors: microsoft_logz.operations.MonitorsOperations
    :ivar operations: Operations operations
    :vartype operations: microsoft_logz.operations.Operations
    :ivar tag_rules: TagRulesOperations operations
    :vartype tag_rules: microsoft_logz.operations.TagRulesOperations
    :ivar single_sign_on: SingleSignOnOperations operations
    :vartype single_sign_on: microsoft_logz.operations.SingleSignOnOperations
    :ivar sub_account: SubAccountOperations operations
    :vartype sub_account: microsoft_logz.operations.SubAccountOperations
    :ivar sub_account_tag_rules: SubAccountTagRulesOperations operations
    :vartype sub_account_tag_rules: microsoft_logz.operations.SubAccountTagRulesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MicrosoftLogzConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.monitors = MonitorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tag_rules = TagRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.single_sign_on = SingleSignOnOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sub_account = SubAccountOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sub_account_tag_rules = SubAccountTagRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MicrosoftLogz
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
