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


class LinkedServicePaged(Paged):
    """
    A paging container for iterating over a list of :class:`LinkedService <azure.mgmt.loganalytics.models.LinkedService>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LinkedService]'}
    }

    def __init__(self, *args, **kwargs):

        super(LinkedServicePaged, self).__init__(*args, **kwargs)
class DataSourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`DataSource <azure.mgmt.loganalytics.models.DataSource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DataSource]'}
    }

    def __init__(self, *args, **kwargs):

        super(DataSourcePaged, self).__init__(*args, **kwargs)
class UsageMetricPaged(Paged):
    """
    A paging container for iterating over a list of :class:`UsageMetric <azure.mgmt.loganalytics.models.UsageMetric>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[UsageMetric]'}
    }

    def __init__(self, *args, **kwargs):

        super(UsageMetricPaged, self).__init__(*args, **kwargs)
class ManagementGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagementGroup <azure.mgmt.loganalytics.models.ManagementGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagementGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagementGroupPaged, self).__init__(*args, **kwargs)
class WorkspacePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Workspace <azure.mgmt.loganalytics.models.Workspace>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Workspace]'}
    }

    def __init__(self, *args, **kwargs):

        super(WorkspacePaged, self).__init__(*args, **kwargs)
class TablePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Table <azure.mgmt.loganalytics.models.Table>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Table]'}
    }

    def __init__(self, *args, **kwargs):

        super(TablePaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.loganalytics.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
