# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from abc import ABC
from typing import TYPE_CHECKING

from azure.core.pipeline.transport import HttpRequest

from ._configuration import RecoveryServicesBackupClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core import PipelineClient

    from ._serialization import Deserializer, Serializer


def _convert_request(request, files=None):
    data = request.content if not files else None
    request = HttpRequest(method=request.method, url=request.url, headers=request.headers, data=data)
    if files:
        request.set_formdata_body(files)
    return request


def _format_url_section(template, **kwargs):
    components = template.split("/")
    while components:
        try:
            return template.format(**kwargs)
        except KeyError as key:
            formatted_components = template.split("/")
            components = [c for c in formatted_components if "{}".format(key.args[0]) not in c]
            template = "/".join(components)


class RecoveryServicesBackupClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: RecoveryServicesBackupClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
