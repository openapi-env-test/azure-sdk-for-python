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


class ComplianceResultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ComplianceResult <azure.mgmt.security.models.ComplianceResult>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ComplianceResult]'}
    }

    def __init__(self, *args, **kwargs):

        super(ComplianceResultPaged, self).__init__(*args, **kwargs)
class AlertPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Alert <azure.mgmt.security.models.Alert>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Alert]'}
    }

    def __init__(self, *args, **kwargs):

        super(AlertPaged, self).__init__(*args, **kwargs)
class SettingPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Setting <azure.mgmt.security.models.Setting>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Setting]'}
    }

    def __init__(self, *args, **kwargs):

        super(SettingPaged, self).__init__(*args, **kwargs)
class DeviceSecurityGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DeviceSecurityGroup <azure.mgmt.security.models.DeviceSecurityGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DeviceSecurityGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(DeviceSecurityGroupPaged, self).__init__(*args, **kwargs)
class IoTSecuritySolutionModelPaged(Paged):
    """
    A paging container for iterating over a list of :class:`IoTSecuritySolutionModel <azure.mgmt.security.models.IoTSecuritySolutionModel>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[IoTSecuritySolutionModel]'}
    }

    def __init__(self, *args, **kwargs):

        super(IoTSecuritySolutionModelPaged, self).__init__(*args, **kwargs)
class IoTSecurityAggregatedAlertPaged(Paged):
    """
    A paging container for iterating over a list of :class:`IoTSecurityAggregatedAlert <azure.mgmt.security.models.IoTSecurityAggregatedAlert>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[IoTSecurityAggregatedAlert]'}
    }

    def __init__(self, *args, **kwargs):

        super(IoTSecurityAggregatedAlertPaged, self).__init__(*args, **kwargs)
class IoTSecurityAggregatedRecommendationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`IoTSecurityAggregatedRecommendation <azure.mgmt.security.models.IoTSecurityAggregatedRecommendation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[IoTSecurityAggregatedRecommendation]'}
    }

    def __init__(self, *args, **kwargs):

        super(IoTSecurityAggregatedRecommendationPaged, self).__init__(*args, **kwargs)
class DiscoveredSecuritySolutionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DiscoveredSecuritySolution <azure.mgmt.security.models.DiscoveredSecuritySolution>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DiscoveredSecuritySolution]'}
    }

    def __init__(self, *args, **kwargs):

        super(DiscoveredSecuritySolutionPaged, self).__init__(*args, **kwargs)
class ExternalSecuritySolutionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExternalSecuritySolution <azure.mgmt.security.models.ExternalSecuritySolution>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExternalSecuritySolution]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExternalSecuritySolutionPaged, self).__init__(*args, **kwargs)
class JitNetworkAccessPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`JitNetworkAccessPolicy <azure.mgmt.security.models.JitNetworkAccessPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JitNetworkAccessPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(JitNetworkAccessPolicyPaged, self).__init__(*args, **kwargs)
class AscLocationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AscLocation <azure.mgmt.security.models.AscLocation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AscLocation]'}
    }

    def __init__(self, *args, **kwargs):

        super(AscLocationPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.security.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class SecurityTaskPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SecurityTask <azure.mgmt.security.models.SecurityTask>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SecurityTask]'}
    }

    def __init__(self, *args, **kwargs):

        super(SecurityTaskPaged, self).__init__(*args, **kwargs)
class AutoProvisioningSettingPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AutoProvisioningSetting <azure.mgmt.security.models.AutoProvisioningSetting>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AutoProvisioningSetting]'}
    }

    def __init__(self, *args, **kwargs):

        super(AutoProvisioningSettingPaged, self).__init__(*args, **kwargs)
class CompliancePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Compliance <azure.mgmt.security.models.Compliance>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Compliance]'}
    }

    def __init__(self, *args, **kwargs):

        super(CompliancePaged, self).__init__(*args, **kwargs)
class InformationProtectionPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`InformationProtectionPolicy <azure.mgmt.security.models.InformationProtectionPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[InformationProtectionPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(InformationProtectionPolicyPaged, self).__init__(*args, **kwargs)
class SecurityContactPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SecurityContact <azure.mgmt.security.models.SecurityContact>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SecurityContact]'}
    }

    def __init__(self, *args, **kwargs):

        super(SecurityContactPaged, self).__init__(*args, **kwargs)
class WorkspaceSettingPaged(Paged):
    """
    A paging container for iterating over a list of :class:`WorkspaceSetting <azure.mgmt.security.models.WorkspaceSetting>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WorkspaceSetting]'}
    }

    def __init__(self, *args, **kwargs):

        super(WorkspaceSettingPaged, self).__init__(*args, **kwargs)
class RegulatoryComplianceStandardPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RegulatoryComplianceStandard <azure.mgmt.security.models.RegulatoryComplianceStandard>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RegulatoryComplianceStandard]'}
    }

    def __init__(self, *args, **kwargs):

        super(RegulatoryComplianceStandardPaged, self).__init__(*args, **kwargs)
class RegulatoryComplianceControlPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RegulatoryComplianceControl <azure.mgmt.security.models.RegulatoryComplianceControl>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RegulatoryComplianceControl]'}
    }

    def __init__(self, *args, **kwargs):

        super(RegulatoryComplianceControlPaged, self).__init__(*args, **kwargs)
class RegulatoryComplianceAssessmentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RegulatoryComplianceAssessment <azure.mgmt.security.models.RegulatoryComplianceAssessment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RegulatoryComplianceAssessment]'}
    }

    def __init__(self, *args, **kwargs):

        super(RegulatoryComplianceAssessmentPaged, self).__init__(*args, **kwargs)
class SecuritySubAssessmentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SecuritySubAssessment <azure.mgmt.security.models.SecuritySubAssessment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SecuritySubAssessment]'}
    }

    def __init__(self, *args, **kwargs):

        super(SecuritySubAssessmentPaged, self).__init__(*args, **kwargs)
class AutomationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Automation <azure.mgmt.security.models.Automation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Automation]'}
    }

    def __init__(self, *args, **kwargs):

        super(AutomationPaged, self).__init__(*args, **kwargs)
class SecurityAssessmentMetadataPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SecurityAssessmentMetadata <azure.mgmt.security.models.SecurityAssessmentMetadata>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SecurityAssessmentMetadata]'}
    }

    def __init__(self, *args, **kwargs):

        super(SecurityAssessmentMetadataPaged, self).__init__(*args, **kwargs)
class SecurityAssessmentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SecurityAssessment <azure.mgmt.security.models.SecurityAssessment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SecurityAssessment]'}
    }

    def __init__(self, *args, **kwargs):

        super(SecurityAssessmentPaged, self).__init__(*args, **kwargs)
class AdaptiveNetworkHardeningPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AdaptiveNetworkHardening <azure.mgmt.security.models.AdaptiveNetworkHardening>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AdaptiveNetworkHardening]'}
    }

    def __init__(self, *args, **kwargs):

        super(AdaptiveNetworkHardeningPaged, self).__init__(*args, **kwargs)
class AllowedConnectionsResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`AllowedConnectionsResource <azure.mgmt.security.models.AllowedConnectionsResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AllowedConnectionsResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(AllowedConnectionsResourcePaged, self).__init__(*args, **kwargs)
class TopologyResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`TopologyResource <azure.mgmt.security.models.TopologyResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[TopologyResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(TopologyResourcePaged, self).__init__(*args, **kwargs)
