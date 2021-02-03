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

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import StorageManagementClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class StorageManagementClient(MultiApiClientMixin, _SDKClient):
    """The Azure Storage Management API.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2019-06-01'
    _PROFILE_TAG = "azure.mgmt.storage.StorageManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'usage': '2018-02-01',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "AsyncTokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = StorageManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(StorageManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-06-15: :mod:`v2015_06_15.models<azure.mgmt.storage.v2015_06_15.models>`
           * 2016-01-01: :mod:`v2016_01_01.models<azure.mgmt.storage.v2016_01_01.models>`
           * 2016-12-01: :mod:`v2016_12_01.models<azure.mgmt.storage.v2016_12_01.models>`
           * 2017-06-01: :mod:`v2017_06_01.models<azure.mgmt.storage.v2017_06_01.models>`
           * 2017-10-01: :mod:`v2017_10_01.models<azure.mgmt.storage.v2017_10_01.models>`
           * 2018-02-01: :mod:`v2018_02_01.models<azure.mgmt.storage.v2018_02_01.models>`
           * 2018-03-01-preview: :mod:`v2018_03_01_preview.models<azure.mgmt.storage.v2018_03_01_preview.models>`
           * 2018-07-01: :mod:`v2018_07_01.models<azure.mgmt.storage.v2018_07_01.models>`
           * 2018-11-01: :mod:`v2018_11_01.models<azure.mgmt.storage.v2018_11_01.models>`
           * 2019-04-01: :mod:`v2019_04_01.models<azure.mgmt.storage.v2019_04_01.models>`
           * 2019-06-01: :mod:`v2019_06_01.models<azure.mgmt.storage.v2019_06_01.models>`
           * 2020-08-01-preview: :mod:`v2020_08_01_preview.models<azure.mgmt.storage.v2020_08_01_preview.models>`
        """
        if api_version == '2015-06-15':
            from ..v2015_06_15 import models
            return models
        elif api_version == '2016-01-01':
            from ..v2016_01_01 import models
            return models
        elif api_version == '2016-12-01':
            from ..v2016_12_01 import models
            return models
        elif api_version == '2017-06-01':
            from ..v2017_06_01 import models
            return models
        elif api_version == '2017-10-01':
            from ..v2017_10_01 import models
            return models
        elif api_version == '2018-02-01':
            from ..v2018_02_01 import models
            return models
        elif api_version == '2018-03-01-preview':
            from ..v2018_03_01_preview import models
            return models
        elif api_version == '2018-07-01':
            from ..v2018_07_01 import models
            return models
        elif api_version == '2018-11-01':
            from ..v2018_11_01 import models
            return models
        elif api_version == '2019-04-01':
            from ..v2019_04_01 import models
            return models
        elif api_version == '2019-06-01':
            from ..v2019_06_01 import models
            return models
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def blob_containers(self):
        """Instance depends on the API version:

           * 2018-02-01: :class:`BlobContainersOperations<azure.mgmt.storage.v2018_02_01.aio.operations.BlobContainersOperations>`
           * 2018-03-01-preview: :class:`BlobContainersOperations<azure.mgmt.storage.v2018_03_01_preview.aio.operations.BlobContainersOperations>`
           * 2018-07-01: :class:`BlobContainersOperations<azure.mgmt.storage.v2018_07_01.aio.operations.BlobContainersOperations>`
           * 2018-11-01: :class:`BlobContainersOperations<azure.mgmt.storage.v2018_11_01.aio.operations.BlobContainersOperations>`
           * 2019-04-01: :class:`BlobContainersOperations<azure.mgmt.storage.v2019_04_01.aio.operations.BlobContainersOperations>`
           * 2019-06-01: :class:`BlobContainersOperations<azure.mgmt.storage.v2019_06_01.aio.operations.BlobContainersOperations>`
           * 2020-08-01-preview: :class:`BlobContainersOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.BlobContainersOperations>`
        """
        api_version = self._get_api_version('blob_containers')
        if api_version == '2018-02-01':
            from ..v2018_02_01.aio.operations import BlobContainersOperations as OperationClass
        elif api_version == '2018-03-01-preview':
            from ..v2018_03_01_preview.aio.operations import BlobContainersOperations as OperationClass
        elif api_version == '2018-07-01':
            from ..v2018_07_01.aio.operations import BlobContainersOperations as OperationClass
        elif api_version == '2018-11-01':
            from ..v2018_11_01.aio.operations import BlobContainersOperations as OperationClass
        elif api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import BlobContainersOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import BlobContainersOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import BlobContainersOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'blob_containers'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def blob_inventory_policies(self):
        """Instance depends on the API version:

           * 2019-06-01: :class:`BlobInventoryPoliciesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.BlobInventoryPoliciesOperations>`
           * 2020-08-01-preview: :class:`BlobInventoryPoliciesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.BlobInventoryPoliciesOperations>`
        """
        api_version = self._get_api_version('blob_inventory_policies')
        if api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import BlobInventoryPoliciesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import BlobInventoryPoliciesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'blob_inventory_policies'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def blob_services(self):
        """Instance depends on the API version:

           * 2018-07-01: :class:`BlobServicesOperations<azure.mgmt.storage.v2018_07_01.aio.operations.BlobServicesOperations>`
           * 2018-11-01: :class:`BlobServicesOperations<azure.mgmt.storage.v2018_11_01.aio.operations.BlobServicesOperations>`
           * 2019-04-01: :class:`BlobServicesOperations<azure.mgmt.storage.v2019_04_01.aio.operations.BlobServicesOperations>`
           * 2019-06-01: :class:`BlobServicesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.BlobServicesOperations>`
           * 2020-08-01-preview: :class:`BlobServicesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.BlobServicesOperations>`
        """
        api_version = self._get_api_version('blob_services')
        if api_version == '2018-07-01':
            from ..v2018_07_01.aio.operations import BlobServicesOperations as OperationClass
        elif api_version == '2018-11-01':
            from ..v2018_11_01.aio.operations import BlobServicesOperations as OperationClass
        elif api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import BlobServicesOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import BlobServicesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import BlobServicesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'blob_services'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def deleted_accounts(self):
        """Instance depends on the API version:

           * 2020-08-01-preview: :class:`DeletedAccountsOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.DeletedAccountsOperations>`
        """
        api_version = self._get_api_version('deleted_accounts')
        if api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import DeletedAccountsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'deleted_accounts'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def encryption_scopes(self):
        """Instance depends on the API version:

           * 2019-06-01: :class:`EncryptionScopesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.EncryptionScopesOperations>`
           * 2020-08-01-preview: :class:`EncryptionScopesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.EncryptionScopesOperations>`
        """
        api_version = self._get_api_version('encryption_scopes')
        if api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import EncryptionScopesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import EncryptionScopesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'encryption_scopes'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def file_services(self):
        """Instance depends on the API version:

           * 2019-04-01: :class:`FileServicesOperations<azure.mgmt.storage.v2019_04_01.aio.operations.FileServicesOperations>`
           * 2019-06-01: :class:`FileServicesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.FileServicesOperations>`
           * 2020-08-01-preview: :class:`FileServicesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.FileServicesOperations>`
        """
        api_version = self._get_api_version('file_services')
        if api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import FileServicesOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import FileServicesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import FileServicesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'file_services'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def file_shares(self):
        """Instance depends on the API version:

           * 2019-04-01: :class:`FileSharesOperations<azure.mgmt.storage.v2019_04_01.aio.operations.FileSharesOperations>`
           * 2019-06-01: :class:`FileSharesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.FileSharesOperations>`
           * 2020-08-01-preview: :class:`FileSharesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.FileSharesOperations>`
        """
        api_version = self._get_api_version('file_shares')
        if api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import FileSharesOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import FileSharesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import FileSharesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'file_shares'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def management_policies(self):
        """Instance depends on the API version:

           * 2018-07-01: :class:`ManagementPoliciesOperations<azure.mgmt.storage.v2018_07_01.aio.operations.ManagementPoliciesOperations>`
           * 2018-11-01: :class:`ManagementPoliciesOperations<azure.mgmt.storage.v2018_11_01.aio.operations.ManagementPoliciesOperations>`
           * 2019-04-01: :class:`ManagementPoliciesOperations<azure.mgmt.storage.v2019_04_01.aio.operations.ManagementPoliciesOperations>`
           * 2019-06-01: :class:`ManagementPoliciesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.ManagementPoliciesOperations>`
           * 2020-08-01-preview: :class:`ManagementPoliciesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.ManagementPoliciesOperations>`
        """
        api_version = self._get_api_version('management_policies')
        if api_version == '2018-07-01':
            from ..v2018_07_01.aio.operations import ManagementPoliciesOperations as OperationClass
        elif api_version == '2018-11-01':
            from ..v2018_11_01.aio.operations import ManagementPoliciesOperations as OperationClass
        elif api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import ManagementPoliciesOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import ManagementPoliciesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import ManagementPoliciesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'management_policies'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def object_replication_policies(self):
        """Instance depends on the API version:

           * 2019-06-01: :class:`ObjectReplicationPoliciesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.ObjectReplicationPoliciesOperations>`
           * 2020-08-01-preview: :class:`ObjectReplicationPoliciesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.ObjectReplicationPoliciesOperations>`
        """
        api_version = self._get_api_version('object_replication_policies')
        if api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import ObjectReplicationPoliciesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import ObjectReplicationPoliciesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'object_replication_policies'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2017-06-01: :class:`Operations<azure.mgmt.storage.v2017_06_01.aio.operations.Operations>`
           * 2017-10-01: :class:`Operations<azure.mgmt.storage.v2017_10_01.aio.operations.Operations>`
           * 2018-02-01: :class:`Operations<azure.mgmt.storage.v2018_02_01.aio.operations.Operations>`
           * 2018-03-01-preview: :class:`Operations<azure.mgmt.storage.v2018_03_01_preview.aio.operations.Operations>`
           * 2018-07-01: :class:`Operations<azure.mgmt.storage.v2018_07_01.aio.operations.Operations>`
           * 2018-11-01: :class:`Operations<azure.mgmt.storage.v2018_11_01.aio.operations.Operations>`
           * 2019-04-01: :class:`Operations<azure.mgmt.storage.v2019_04_01.aio.operations.Operations>`
           * 2019-06-01: :class:`Operations<azure.mgmt.storage.v2019_06_01.aio.operations.Operations>`
           * 2020-08-01-preview: :class:`Operations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2017-06-01':
            from ..v2017_06_01.aio.operations import Operations as OperationClass
        elif api_version == '2017-10-01':
            from ..v2017_10_01.aio.operations import Operations as OperationClass
        elif api_version == '2018-02-01':
            from ..v2018_02_01.aio.operations import Operations as OperationClass
        elif api_version == '2018-03-01-preview':
            from ..v2018_03_01_preview.aio.operations import Operations as OperationClass
        elif api_version == '2018-07-01':
            from ..v2018_07_01.aio.operations import Operations as OperationClass
        elif api_version == '2018-11-01':
            from ..v2018_11_01.aio.operations import Operations as OperationClass
        elif api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import Operations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import Operations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2019-06-01: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.storage.v2019_06_01.aio.operations.PrivateEndpointConnectionsOperations>`
           * 2020-08-01-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_endpoint_connections'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_resources(self):
        """Instance depends on the API version:

           * 2019-06-01: :class:`PrivateLinkResourcesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.PrivateLinkResourcesOperations>`
           * 2020-08-01-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.PrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_resources')
        if api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import PrivateLinkResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def queue(self):
        """Instance depends on the API version:

           * 2019-06-01: :class:`QueueOperations<azure.mgmt.storage.v2019_06_01.aio.operations.QueueOperations>`
           * 2020-08-01-preview: :class:`QueueOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.QueueOperations>`
        """
        api_version = self._get_api_version('queue')
        if api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import QueueOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import QueueOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'queue'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def queue_services(self):
        """Instance depends on the API version:

           * 2019-06-01: :class:`QueueServicesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.QueueServicesOperations>`
           * 2020-08-01-preview: :class:`QueueServicesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.QueueServicesOperations>`
        """
        api_version = self._get_api_version('queue_services')
        if api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import QueueServicesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import QueueServicesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'queue_services'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def skus(self):
        """Instance depends on the API version:

           * 2017-06-01: :class:`SkusOperations<azure.mgmt.storage.v2017_06_01.aio.operations.SkusOperations>`
           * 2017-10-01: :class:`SkusOperations<azure.mgmt.storage.v2017_10_01.aio.operations.SkusOperations>`
           * 2018-02-01: :class:`SkusOperations<azure.mgmt.storage.v2018_02_01.aio.operations.SkusOperations>`
           * 2018-03-01-preview: :class:`SkusOperations<azure.mgmt.storage.v2018_03_01_preview.aio.operations.SkusOperations>`
           * 2018-07-01: :class:`SkusOperations<azure.mgmt.storage.v2018_07_01.aio.operations.SkusOperations>`
           * 2018-11-01: :class:`SkusOperations<azure.mgmt.storage.v2018_11_01.aio.operations.SkusOperations>`
           * 2019-04-01: :class:`SkusOperations<azure.mgmt.storage.v2019_04_01.aio.operations.SkusOperations>`
           * 2019-06-01: :class:`SkusOperations<azure.mgmt.storage.v2019_06_01.aio.operations.SkusOperations>`
           * 2020-08-01-preview: :class:`SkusOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.SkusOperations>`
        """
        api_version = self._get_api_version('skus')
        if api_version == '2017-06-01':
            from ..v2017_06_01.aio.operations import SkusOperations as OperationClass
        elif api_version == '2017-10-01':
            from ..v2017_10_01.aio.operations import SkusOperations as OperationClass
        elif api_version == '2018-02-01':
            from ..v2018_02_01.aio.operations import SkusOperations as OperationClass
        elif api_version == '2018-03-01-preview':
            from ..v2018_03_01_preview.aio.operations import SkusOperations as OperationClass
        elif api_version == '2018-07-01':
            from ..v2018_07_01.aio.operations import SkusOperations as OperationClass
        elif api_version == '2018-11-01':
            from ..v2018_11_01.aio.operations import SkusOperations as OperationClass
        elif api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import SkusOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import SkusOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import SkusOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'skus'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def storage_accounts(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`StorageAccountsOperations<azure.mgmt.storage.v2015_06_15.aio.operations.StorageAccountsOperations>`
           * 2016-01-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2016_01_01.aio.operations.StorageAccountsOperations>`
           * 2016-12-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2016_12_01.aio.operations.StorageAccountsOperations>`
           * 2017-06-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2017_06_01.aio.operations.StorageAccountsOperations>`
           * 2017-10-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2017_10_01.aio.operations.StorageAccountsOperations>`
           * 2018-02-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2018_02_01.aio.operations.StorageAccountsOperations>`
           * 2018-03-01-preview: :class:`StorageAccountsOperations<azure.mgmt.storage.v2018_03_01_preview.aio.operations.StorageAccountsOperations>`
           * 2018-07-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2018_07_01.aio.operations.StorageAccountsOperations>`
           * 2018-11-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2018_11_01.aio.operations.StorageAccountsOperations>`
           * 2019-04-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2019_04_01.aio.operations.StorageAccountsOperations>`
           * 2019-06-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2019_06_01.aio.operations.StorageAccountsOperations>`
           * 2020-08-01-preview: :class:`StorageAccountsOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.StorageAccountsOperations>`
        """
        api_version = self._get_api_version('storage_accounts')
        if api_version == '2015-06-15':
            from ..v2015_06_15.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2016-01-01':
            from ..v2016_01_01.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2016-12-01':
            from ..v2016_12_01.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2017-06-01':
            from ..v2017_06_01.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2017-10-01':
            from ..v2017_10_01.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2018-02-01':
            from ..v2018_02_01.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2018-03-01-preview':
            from ..v2018_03_01_preview.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2018-07-01':
            from ..v2018_07_01.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2018-11-01':
            from ..v2018_11_01.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import StorageAccountsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'storage_accounts'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def table(self):
        """Instance depends on the API version:

           * 2019-06-01: :class:`TableOperations<azure.mgmt.storage.v2019_06_01.aio.operations.TableOperations>`
           * 2020-08-01-preview: :class:`TableOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.TableOperations>`
        """
        api_version = self._get_api_version('table')
        if api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import TableOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import TableOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'table'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def table_services(self):
        """Instance depends on the API version:

           * 2019-06-01: :class:`TableServicesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.TableServicesOperations>`
           * 2020-08-01-preview: :class:`TableServicesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.TableServicesOperations>`
        """
        api_version = self._get_api_version('table_services')
        if api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import TableServicesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import TableServicesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'table_services'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def usage(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`UsageOperations<azure.mgmt.storage.v2015_06_15.aio.operations.UsageOperations>`
           * 2016-01-01: :class:`UsageOperations<azure.mgmt.storage.v2016_01_01.aio.operations.UsageOperations>`
           * 2016-12-01: :class:`UsageOperations<azure.mgmt.storage.v2016_12_01.aio.operations.UsageOperations>`
           * 2017-06-01: :class:`UsageOperations<azure.mgmt.storage.v2017_06_01.aio.operations.UsageOperations>`
           * 2017-10-01: :class:`UsageOperations<azure.mgmt.storage.v2017_10_01.aio.operations.UsageOperations>`
           * 2018-02-01: :class:`UsageOperations<azure.mgmt.storage.v2018_02_01.aio.operations.UsageOperations>`
        """
        api_version = self._get_api_version('usage')
        if api_version == '2015-06-15':
            from ..v2015_06_15.aio.operations import UsageOperations as OperationClass
        elif api_version == '2016-01-01':
            from ..v2016_01_01.aio.operations import UsageOperations as OperationClass
        elif api_version == '2016-12-01':
            from ..v2016_12_01.aio.operations import UsageOperations as OperationClass
        elif api_version == '2017-06-01':
            from ..v2017_06_01.aio.operations import UsageOperations as OperationClass
        elif api_version == '2017-10-01':
            from ..v2017_10_01.aio.operations import UsageOperations as OperationClass
        elif api_version == '2018-02-01':
            from ..v2018_02_01.aio.operations import UsageOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'usage'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def usages(self):
        """Instance depends on the API version:

           * 2018-03-01-preview: :class:`UsagesOperations<azure.mgmt.storage.v2018_03_01_preview.aio.operations.UsagesOperations>`
           * 2018-07-01: :class:`UsagesOperations<azure.mgmt.storage.v2018_07_01.aio.operations.UsagesOperations>`
           * 2018-11-01: :class:`UsagesOperations<azure.mgmt.storage.v2018_11_01.aio.operations.UsagesOperations>`
           * 2019-04-01: :class:`UsagesOperations<azure.mgmt.storage.v2019_04_01.aio.operations.UsagesOperations>`
           * 2019-06-01: :class:`UsagesOperations<azure.mgmt.storage.v2019_06_01.aio.operations.UsagesOperations>`
           * 2020-08-01-preview: :class:`UsagesOperations<azure.mgmt.storage.v2020_08_01_preview.aio.operations.UsagesOperations>`
        """
        api_version = self._get_api_version('usages')
        if api_version == '2018-03-01-preview':
            from ..v2018_03_01_preview.aio.operations import UsagesOperations as OperationClass
        elif api_version == '2018-07-01':
            from ..v2018_07_01.aio.operations import UsagesOperations as OperationClass
        elif api_version == '2018-11-01':
            from ..v2018_11_01.aio.operations import UsagesOperations as OperationClass
        elif api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import UsagesOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import UsagesOperations as OperationClass
        elif api_version == '2020-08-01-preview':
            from ..v2020_08_01_preview.aio.operations import UsagesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'usages'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
