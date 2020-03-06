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

from msrest.paging import Paged


class ManagementGroupInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagementGroupInfo <azure.mgmt.managementgroups.models.ManagementGroupInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagementGroupInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagementGroupInfoPaged, self).__init__(*args, **kwargs)
class DescendantInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DescendantInfo <azure.mgmt.managementgroups.models.DescendantInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DescendantInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(DescendantInfoPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.managementgroups.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class EntityInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`EntityInfo <azure.mgmt.managementgroups.models.EntityInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[EntityInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(EntityInfoPaged, self).__init__(*args, **kwargs)
