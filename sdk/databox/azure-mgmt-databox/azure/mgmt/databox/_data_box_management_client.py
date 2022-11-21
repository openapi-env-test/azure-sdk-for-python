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

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import DataBoxManagementClientConfiguration
from ._operations_mixin import DataBoxManagementClientOperationsMixin
from ._serialization import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class DataBoxManagementClient(DataBoxManagementClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """The DataBox Client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Subscription Id. Required.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2022-09-01'
    _PROFILE_TAG = "azure.mgmt.databox.DataBoxManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        api_version=None, # type: Optional[str]
        base_url: str = "https://management.azure.com",
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        self._config = DataBoxManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(DataBoxManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2018-01-01: :mod:`v2018_01_01.models<azure.mgmt.databox.v2018_01_01.models>`
           * 2019-09-01: :mod:`v2019_09_01.models<azure.mgmt.databox.v2019_09_01.models>`
           * 2020-04-01: :mod:`v2020_04_01.models<azure.mgmt.databox.v2020_04_01.models>`
           * 2020-11-01: :mod:`v2020_11_01.models<azure.mgmt.databox.v2020_11_01.models>`
           * 2021-03-01: :mod:`v2021_03_01.models<azure.mgmt.databox.v2021_03_01.models>`
           * 2021-05-01: :mod:`v2021_05_01.models<azure.mgmt.databox.v2021_05_01.models>`
           * 2021-08-01-preview: :mod:`v2021_08_01_preview.models<azure.mgmt.databox.v2021_08_01_preview.models>`
           * 2021-12-01: :mod:`v2021_12_01.models<azure.mgmt.databox.v2021_12_01.models>`
           * 2022-02-01: :mod:`v2022_02_01.models<azure.mgmt.databox.v2022_02_01.models>`
           * 2022-09-01: :mod:`v2022_09_01.models<azure.mgmt.databox.v2022_09_01.models>`
        """
        if api_version == '2018-01-01':
            from .v2018_01_01 import models
            return models
        elif api_version == '2019-09-01':
            from .v2019_09_01 import models
            return models
        elif api_version == '2020-04-01':
            from .v2020_04_01 import models
            return models
        elif api_version == '2020-11-01':
            from .v2020_11_01 import models
            return models
        elif api_version == '2021-03-01':
            from .v2021_03_01 import models
            return models
        elif api_version == '2021-05-01':
            from .v2021_05_01 import models
            return models
        elif api_version == '2021-08-01-preview':
            from .v2021_08_01_preview import models
            return models
        elif api_version == '2021-12-01':
            from .v2021_12_01 import models
            return models
        elif api_version == '2022-02-01':
            from .v2022_02_01 import models
            return models
        elif api_version == '2022-09-01':
            from .v2022_09_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def jobs(self):
        """Instance depends on the API version:

           * 2018-01-01: :class:`JobsOperations<azure.mgmt.databox.v2018_01_01.operations.JobsOperations>`
           * 2019-09-01: :class:`JobsOperations<azure.mgmt.databox.v2019_09_01.operations.JobsOperations>`
           * 2020-04-01: :class:`JobsOperations<azure.mgmt.databox.v2020_04_01.operations.JobsOperations>`
           * 2020-11-01: :class:`JobsOperations<azure.mgmt.databox.v2020_11_01.operations.JobsOperations>`
           * 2021-03-01: :class:`JobsOperations<azure.mgmt.databox.v2021_03_01.operations.JobsOperations>`
           * 2021-05-01: :class:`JobsOperations<azure.mgmt.databox.v2021_05_01.operations.JobsOperations>`
           * 2021-08-01-preview: :class:`JobsOperations<azure.mgmt.databox.v2021_08_01_preview.operations.JobsOperations>`
           * 2021-12-01: :class:`JobsOperations<azure.mgmt.databox.v2021_12_01.operations.JobsOperations>`
           * 2022-02-01: :class:`JobsOperations<azure.mgmt.databox.v2022_02_01.operations.JobsOperations>`
           * 2022-09-01: :class:`JobsOperations<azure.mgmt.databox.v2022_09_01.operations.JobsOperations>`
        """
        api_version = self._get_api_version('jobs')
        if api_version == '2018-01-01':
            from .v2018_01_01.operations import JobsOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import JobsOperations as OperationClass
        elif api_version == '2020-04-01':
            from .v2020_04_01.operations import JobsOperations as OperationClass
        elif api_version == '2020-11-01':
            from .v2020_11_01.operations import JobsOperations as OperationClass
        elif api_version == '2021-03-01':
            from .v2021_03_01.operations import JobsOperations as OperationClass
        elif api_version == '2021-05-01':
            from .v2021_05_01.operations import JobsOperations as OperationClass
        elif api_version == '2021-08-01-preview':
            from .v2021_08_01_preview.operations import JobsOperations as OperationClass
        elif api_version == '2021-12-01':
            from .v2021_12_01.operations import JobsOperations as OperationClass
        elif api_version == '2022-02-01':
            from .v2022_02_01.operations import JobsOperations as OperationClass
        elif api_version == '2022-09-01':
            from .v2022_09_01.operations import JobsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'jobs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2018-01-01: :class:`Operations<azure.mgmt.databox.v2018_01_01.operations.Operations>`
           * 2019-09-01: :class:`Operations<azure.mgmt.databox.v2019_09_01.operations.Operations>`
           * 2020-04-01: :class:`Operations<azure.mgmt.databox.v2020_04_01.operations.Operations>`
           * 2020-11-01: :class:`Operations<azure.mgmt.databox.v2020_11_01.operations.Operations>`
           * 2021-03-01: :class:`Operations<azure.mgmt.databox.v2021_03_01.operations.Operations>`
           * 2021-05-01: :class:`Operations<azure.mgmt.databox.v2021_05_01.operations.Operations>`
           * 2021-08-01-preview: :class:`Operations<azure.mgmt.databox.v2021_08_01_preview.operations.Operations>`
           * 2021-12-01: :class:`Operations<azure.mgmt.databox.v2021_12_01.operations.Operations>`
           * 2022-02-01: :class:`Operations<azure.mgmt.databox.v2022_02_01.operations.Operations>`
           * 2022-09-01: :class:`Operations<azure.mgmt.databox.v2022_09_01.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2018-01-01':
            from .v2018_01_01.operations import Operations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import Operations as OperationClass
        elif api_version == '2020-04-01':
            from .v2020_04_01.operations import Operations as OperationClass
        elif api_version == '2020-11-01':
            from .v2020_11_01.operations import Operations as OperationClass
        elif api_version == '2021-03-01':
            from .v2021_03_01.operations import Operations as OperationClass
        elif api_version == '2021-05-01':
            from .v2021_05_01.operations import Operations as OperationClass
        elif api_version == '2021-08-01-preview':
            from .v2021_08_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-12-01':
            from .v2021_12_01.operations import Operations as OperationClass
        elif api_version == '2022-02-01':
            from .v2022_02_01.operations import Operations as OperationClass
        elif api_version == '2022-09-01':
            from .v2022_09_01.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def service(self):
        """Instance depends on the API version:

           * 2018-01-01: :class:`ServiceOperations<azure.mgmt.databox.v2018_01_01.operations.ServiceOperations>`
           * 2019-09-01: :class:`ServiceOperations<azure.mgmt.databox.v2019_09_01.operations.ServiceOperations>`
           * 2020-04-01: :class:`ServiceOperations<azure.mgmt.databox.v2020_04_01.operations.ServiceOperations>`
           * 2020-11-01: :class:`ServiceOperations<azure.mgmt.databox.v2020_11_01.operations.ServiceOperations>`
           * 2021-03-01: :class:`ServiceOperations<azure.mgmt.databox.v2021_03_01.operations.ServiceOperations>`
           * 2021-05-01: :class:`ServiceOperations<azure.mgmt.databox.v2021_05_01.operations.ServiceOperations>`
           * 2021-08-01-preview: :class:`ServiceOperations<azure.mgmt.databox.v2021_08_01_preview.operations.ServiceOperations>`
           * 2021-12-01: :class:`ServiceOperations<azure.mgmt.databox.v2021_12_01.operations.ServiceOperations>`
           * 2022-02-01: :class:`ServiceOperations<azure.mgmt.databox.v2022_02_01.operations.ServiceOperations>`
           * 2022-09-01: :class:`ServiceOperations<azure.mgmt.databox.v2022_09_01.operations.ServiceOperations>`
        """
        api_version = self._get_api_version('service')
        if api_version == '2018-01-01':
            from .v2018_01_01.operations import ServiceOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import ServiceOperations as OperationClass
        elif api_version == '2020-04-01':
            from .v2020_04_01.operations import ServiceOperations as OperationClass
        elif api_version == '2020-11-01':
            from .v2020_11_01.operations import ServiceOperations as OperationClass
        elif api_version == '2021-03-01':
            from .v2021_03_01.operations import ServiceOperations as OperationClass
        elif api_version == '2021-05-01':
            from .v2021_05_01.operations import ServiceOperations as OperationClass
        elif api_version == '2021-08-01-preview':
            from .v2021_08_01_preview.operations import ServiceOperations as OperationClass
        elif api_version == '2021-12-01':
            from .v2021_12_01.operations import ServiceOperations as OperationClass
        elif api_version == '2022-02-01':
            from .v2022_02_01.operations import ServiceOperations as OperationClass
        elif api_version == '2022-09-01':
            from .v2022_09_01.operations import ServiceOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'service'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
