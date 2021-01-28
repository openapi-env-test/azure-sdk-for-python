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

try:
    from ._models_py3 import AADCheckRequirements
    from ._models_py3 import AADDataConnector
    from ._models_py3 import AATPCheckRequirements
    from ._models_py3 import AATPDataConnector
    from ._models_py3 import AccountEntity
    from ._models_py3 import ActionPropertiesBase
    from ._models_py3 import ActionRequest
    from ._models_py3 import ActionResponse
    from ._models_py3 import ActivityTimelineItem
    from ._models_py3 import Aggregations
    from ._models_py3 import AggregationsKind
    from ._models_py3 import AlertRule
    from ._models_py3 import AlertRuleKind1
    from ._models_py3 import AlertRuleTemplate
    from ._models_py3 import AlertRuleTemplateDataSource
    from ._models_py3 import AlertRuleTemplatePropertiesBase
    from ._models_py3 import AlertsDataTypeOfDataConnector
    from ._models_py3 import AlertsDataTypeOfDataConnectorAlerts
    from ._models_py3 import ASCCheckRequirements
    from ._models_py3 import ASCDataConnector
    from ._models_py3 import AwsCloudTrailCheckRequirements
    from ._models_py3 import AwsCloudTrailDataConnector
    from ._models_py3 import AwsCloudTrailDataConnectorDataTypes
    from ._models_py3 import AwsCloudTrailDataConnectorDataTypesLogs
    from ._models_py3 import AzureResourceEntity
    from ._models_py3 import Bookmark
    from ._models_py3 import BookmarkExpandParameters
    from ._models_py3 import BookmarkExpandResponse
    from ._models_py3 import BookmarkExpandResponseValue
    from ._models_py3 import BookmarkTimelineItem
    from ._models_py3 import Case
    from ._models_py3 import CaseComment
    from ._models_py3 import CaseRelation
    from ._models_py3 import CasesAggregation
    from ._models_py3 import CasesAggregationBySeverityProperties
    from ._models_py3 import CasesAggregationByStatusProperties
    from ._models_py3 import ClientInfo
    from ._models_py3 import CloudApplicationEntity
    from ._models_py3 import DataConnector
    from ._models_py3 import DataConnectorDataTypeCommon
    from ._models_py3 import DataConnectorKind1
    from ._models_py3 import DataConnectorRequirementsState
    from ._models_py3 import DataConnectorsCheckRequirements
    from ._models_py3 import DataConnectorTenantId
    from ._models_py3 import DataConnectorWithAlertsProperties
    from ._models_py3 import DnsEntity
    from ._models_py3 import Dynamics365CheckRequirements
    from ._models_py3 import Dynamics365DataConnector
    from ._models_py3 import Dynamics365DataConnectorDataTypes
    from ._models_py3 import Dynamics365DataConnectorDataTypesDynamics365CdsActivities
    from ._models_py3 import Entity
    from ._models_py3 import EntityAnalytics
    from ._models_py3 import EntityCommonProperties
    from ._models_py3 import EntityExpandParameters
    from ._models_py3 import EntityExpandResponse
    from ._models_py3 import EntityExpandResponseValue
    from ._models_py3 import EntityGetInsightsParameters
    from ._models_py3 import EntityGetInsightsResponse
    from ._models_py3 import EntityInsightItem
    from ._models_py3 import EntityInsightItemQueryTimeInterval
    from ._models_py3 import EntityKind1
    from ._models_py3 import EntityQuery
    from ._models_py3 import EntityQueryItem
    from ._models_py3 import EntityQueryItemProperties
    from ._models_py3 import EntityQueryItemPropertiesDataTypesItem
    from ._models_py3 import EntityQueryKind1
    from ._models_py3 import EntityTimelineItem
    from ._models_py3 import EntityTimelineParameters
    from ._models_py3 import EntityTimelineResponse
    from ._models_py3 import EventGroupingSettings
    from ._models_py3 import ExpansionEntityQuery
    from ._models_py3 import ExpansionResultAggregation
    from ._models_py3 import ExpansionResultsMetadata
    from ._models_py3 import EyesOn
    from ._models_py3 import FileEntity
    from ._models_py3 import FileHashEntity
    from ._models_py3 import FusionAlertRule
    from ._models_py3 import FusionAlertRuleTemplate
    from ._models_py3 import GeoLocation
    from ._models_py3 import GetInsightsError
    from ._models_py3 import GetInsightsResultsMetadata
    from ._models_py3 import GetQueriesResponse
    from ._models_py3 import GroupingConfiguration
    from ._models_py3 import HostEntity
    from ._models_py3 import HuntingBookmark
    from ._models_py3 import Incident
    from ._models_py3 import IncidentAdditionalData
    from ._models_py3 import IncidentAlertList
    from ._models_py3 import IncidentBookmarkList
    from ._models_py3 import IncidentComment
    from ._models_py3 import IncidentConfiguration
    from ._models_py3 import IncidentEntitiesResponse
    from ._models_py3 import IncidentEntitiesResultsMetadata
    from ._models_py3 import IncidentInfo
    from ._models_py3 import IncidentLabel
    from ._models_py3 import IncidentOwnerInfo
    from ._models_py3 import InsightQueryItem
    from ._models_py3 import InsightQueryItemProperties
    from ._models_py3 import InsightQueryItemPropertiesAdditionalQuery
    from ._models_py3 import InsightQueryItemPropertiesDefaultTimeRange
    from ._models_py3 import InsightQueryItemPropertiesReferenceTimeRange
    from ._models_py3 import InsightQueryItemPropertiesTableQuery
    from ._models_py3 import InsightQueryItemPropertiesTableQueryColumnsDefinitionsItem
    from ._models_py3 import InsightQueryItemPropertiesTableQueryQueriesDefinitionsItem
    from ._models_py3 import InsightQueryItemPropertiesTableQueryQueriesDefinitionsItemLinkColumnsDefinitionsItem
    from ._models_py3 import InsightsTableResult
    from ._models_py3 import InsightsTableResultColumnsItem
    from ._models_py3 import IoTDeviceEntity
    from ._models_py3 import IpEntity
    from ._models_py3 import MailboxEntity
    from ._models_py3 import MailClusterEntity
    from ._models_py3 import MailMessageEntity
    from ._models_py3 import MalwareEntity
    from ._models_py3 import MCASCheckRequirements
    from ._models_py3 import MCASDataConnector
    from ._models_py3 import MCASDataConnectorDataTypes
    from ._models_py3 import MCASDataConnectorDataTypesDiscoveryLogs
    from ._models_py3 import MDATPCheckRequirements
    from ._models_py3 import MDATPDataConnector
    from ._models_py3 import MicrosoftSecurityIncidentCreationAlertRule
    from ._models_py3 import MicrosoftSecurityIncidentCreationAlertRuleCommonProperties
    from ._models_py3 import MicrosoftSecurityIncidentCreationAlertRuleTemplate
    from ._models_py3 import OfficeATPCheckRequirements
    from ._models_py3 import OfficeATPDataConnector
    from ._models_py3 import OfficeConsent
    from ._models_py3 import OfficeDataConnector
    from ._models_py3 import OfficeDataConnectorDataTypes
    from ._models_py3 import OfficeDataConnectorDataTypesExchange
    from ._models_py3 import OfficeDataConnectorDataTypesSharePoint
    from ._models_py3 import OfficeDataConnectorDataTypesTeams
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import ProcessEntity
    from ._models_py3 import RegistryKeyEntity
    from ._models_py3 import RegistryValueEntity
    from ._models_py3 import Relation
    from ._models_py3 import RelationBase
    from ._models_py3 import RelationNode
    from ._models_py3 import RelationsModelInput
    from ._models_py3 import Resource
    from ._models_py3 import ResourceWithEtag
    from ._models_py3 import ScheduledAlertRule
    from ._models_py3 import ScheduledAlertRuleCommonProperties
    from ._models_py3 import ScheduledAlertRuleTemplate
    from ._models_py3 import SecurityAlert
    from ._models_py3 import SecurityAlertPropertiesConfidenceReasonsItem
    from ._models_py3 import SecurityAlertTimelineItem
    from ._models_py3 import SecurityGroupEntity
    from ._models_py3 import SettingList
    from ._models_py3 import Settings
    from ._models_py3 import SettingsKind
    from ._models_py3 import SubmissionMailEntity
    from ._models_py3 import ThreatIntelligence
    from ._models_py3 import ThreatIntelligenceAppendTags
    from ._models_py3 import ThreatIntelligenceFilteringCriteria
    from ._models_py3 import ThreatIntelligenceGranularMarkingModel
    from ._models_py3 import ThreatIntelligenceIndicatorModel
    from ._models_py3 import ThreatIntelligenceIndicatorModelForRequestBody
    from ._models_py3 import ThreatIntelligenceInformation
    from ._models_py3 import ThreatIntelligenceKillChainPhase
    from ._models_py3 import ThreatIntelligenceMetric
    from ._models_py3 import ThreatIntelligenceMetricEntity
    from ._models_py3 import ThreatIntelligenceMetrics
    from ._models_py3 import ThreatIntelligenceMetricsList
    from ._models_py3 import ThreatIntelligenceResourceKind1
    from ._models_py3 import ThreatIntelligenceSortingCriteria1
    from ._models_py3 import TICheckRequirements
    from ._models_py3 import TIDataConnector
    from ._models_py3 import TIDataConnectorDataTypes
    from ._models_py3 import TIDataConnectorDataTypesIndicators
    from ._models_py3 import TimelineAggregation
    from ._models_py3 import TimelineError
    from ._models_py3 import TimelineResultsMetadata
    from ._models_py3 import TiTaxiiCheckRequirements
    from ._models_py3 import TiTaxiiDataConnector
    from ._models_py3 import TiTaxiiDataConnectorDataTypes
    from ._models_py3 import TiTaxiiDataConnectorDataTypesTaxiiClient
    from ._models_py3 import Ueba
    from ._models_py3 import UrlEntity
    from ._models_py3 import UserInfo
    from ._models_py3 import Watchlist
    from ._models_py3 import WatchlistItem
except (SyntaxError, ImportError):
    from ._models import AADCheckRequirements
    from ._models import AADDataConnector
    from ._models import AATPCheckRequirements
    from ._models import AATPDataConnector
    from ._models import AccountEntity
    from ._models import ActionPropertiesBase
    from ._models import ActionRequest
    from ._models import ActionResponse
    from ._models import ActivityTimelineItem
    from ._models import Aggregations
    from ._models import AggregationsKind
    from ._models import AlertRule
    from ._models import AlertRuleKind1
    from ._models import AlertRuleTemplate
    from ._models import AlertRuleTemplateDataSource
    from ._models import AlertRuleTemplatePropertiesBase
    from ._models import AlertsDataTypeOfDataConnector
    from ._models import AlertsDataTypeOfDataConnectorAlerts
    from ._models import ASCCheckRequirements
    from ._models import ASCDataConnector
    from ._models import AwsCloudTrailCheckRequirements
    from ._models import AwsCloudTrailDataConnector
    from ._models import AwsCloudTrailDataConnectorDataTypes
    from ._models import AwsCloudTrailDataConnectorDataTypesLogs
    from ._models import AzureResourceEntity
    from ._models import Bookmark
    from ._models import BookmarkExpandParameters
    from ._models import BookmarkExpandResponse
    from ._models import BookmarkExpandResponseValue
    from ._models import BookmarkTimelineItem
    from ._models import Case
    from ._models import CaseComment
    from ._models import CaseRelation
    from ._models import CasesAggregation
    from ._models import CasesAggregationBySeverityProperties
    from ._models import CasesAggregationByStatusProperties
    from ._models import ClientInfo
    from ._models import CloudApplicationEntity
    from ._models import DataConnector
    from ._models import DataConnectorDataTypeCommon
    from ._models import DataConnectorKind1
    from ._models import DataConnectorRequirementsState
    from ._models import DataConnectorsCheckRequirements
    from ._models import DataConnectorTenantId
    from ._models import DataConnectorWithAlertsProperties
    from ._models import DnsEntity
    from ._models import Dynamics365CheckRequirements
    from ._models import Dynamics365DataConnector
    from ._models import Dynamics365DataConnectorDataTypes
    from ._models import Dynamics365DataConnectorDataTypesDynamics365CdsActivities
    from ._models import Entity
    from ._models import EntityAnalytics
    from ._models import EntityCommonProperties
    from ._models import EntityExpandParameters
    from ._models import EntityExpandResponse
    from ._models import EntityExpandResponseValue
    from ._models import EntityGetInsightsParameters
    from ._models import EntityGetInsightsResponse
    from ._models import EntityInsightItem
    from ._models import EntityInsightItemQueryTimeInterval
    from ._models import EntityKind1
    from ._models import EntityQuery
    from ._models import EntityQueryItem
    from ._models import EntityQueryItemProperties
    from ._models import EntityQueryItemPropertiesDataTypesItem
    from ._models import EntityQueryKind1
    from ._models import EntityTimelineItem
    from ._models import EntityTimelineParameters
    from ._models import EntityTimelineResponse
    from ._models import EventGroupingSettings
    from ._models import ExpansionEntityQuery
    from ._models import ExpansionResultAggregation
    from ._models import ExpansionResultsMetadata
    from ._models import EyesOn
    from ._models import FileEntity
    from ._models import FileHashEntity
    from ._models import FusionAlertRule
    from ._models import FusionAlertRuleTemplate
    from ._models import GeoLocation
    from ._models import GetInsightsError
    from ._models import GetInsightsResultsMetadata
    from ._models import GetQueriesResponse
    from ._models import GroupingConfiguration
    from ._models import HostEntity
    from ._models import HuntingBookmark
    from ._models import Incident
    from ._models import IncidentAdditionalData
    from ._models import IncidentAlertList
    from ._models import IncidentBookmarkList
    from ._models import IncidentComment
    from ._models import IncidentConfiguration
    from ._models import IncidentEntitiesResponse
    from ._models import IncidentEntitiesResultsMetadata
    from ._models import IncidentInfo
    from ._models import IncidentLabel
    from ._models import IncidentOwnerInfo
    from ._models import InsightQueryItem
    from ._models import InsightQueryItemProperties
    from ._models import InsightQueryItemPropertiesAdditionalQuery
    from ._models import InsightQueryItemPropertiesDefaultTimeRange
    from ._models import InsightQueryItemPropertiesReferenceTimeRange
    from ._models import InsightQueryItemPropertiesTableQuery
    from ._models import InsightQueryItemPropertiesTableQueryColumnsDefinitionsItem
    from ._models import InsightQueryItemPropertiesTableQueryQueriesDefinitionsItem
    from ._models import InsightQueryItemPropertiesTableQueryQueriesDefinitionsItemLinkColumnsDefinitionsItem
    from ._models import InsightsTableResult
    from ._models import InsightsTableResultColumnsItem
    from ._models import IoTDeviceEntity
    from ._models import IpEntity
    from ._models import MailboxEntity
    from ._models import MailClusterEntity
    from ._models import MailMessageEntity
    from ._models import MalwareEntity
    from ._models import MCASCheckRequirements
    from ._models import MCASDataConnector
    from ._models import MCASDataConnectorDataTypes
    from ._models import MCASDataConnectorDataTypesDiscoveryLogs
    from ._models import MDATPCheckRequirements
    from ._models import MDATPDataConnector
    from ._models import MicrosoftSecurityIncidentCreationAlertRule
    from ._models import MicrosoftSecurityIncidentCreationAlertRuleCommonProperties
    from ._models import MicrosoftSecurityIncidentCreationAlertRuleTemplate
    from ._models import OfficeATPCheckRequirements
    from ._models import OfficeATPDataConnector
    from ._models import OfficeConsent
    from ._models import OfficeDataConnector
    from ._models import OfficeDataConnectorDataTypes
    from ._models import OfficeDataConnectorDataTypesExchange
    from ._models import OfficeDataConnectorDataTypesSharePoint
    from ._models import OfficeDataConnectorDataTypesTeams
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import ProcessEntity
    from ._models import RegistryKeyEntity
    from ._models import RegistryValueEntity
    from ._models import Relation
    from ._models import RelationBase
    from ._models import RelationNode
    from ._models import RelationsModelInput
    from ._models import Resource
    from ._models import ResourceWithEtag
    from ._models import ScheduledAlertRule
    from ._models import ScheduledAlertRuleCommonProperties
    from ._models import ScheduledAlertRuleTemplate
    from ._models import SecurityAlert
    from ._models import SecurityAlertPropertiesConfidenceReasonsItem
    from ._models import SecurityAlertTimelineItem
    from ._models import SecurityGroupEntity
    from ._models import SettingList
    from ._models import Settings
    from ._models import SettingsKind
    from ._models import SubmissionMailEntity
    from ._models import ThreatIntelligence
    from ._models import ThreatIntelligenceAppendTags
    from ._models import ThreatIntelligenceFilteringCriteria
    from ._models import ThreatIntelligenceGranularMarkingModel
    from ._models import ThreatIntelligenceIndicatorModel
    from ._models import ThreatIntelligenceIndicatorModelForRequestBody
    from ._models import ThreatIntelligenceInformation
    from ._models import ThreatIntelligenceKillChainPhase
    from ._models import ThreatIntelligenceMetric
    from ._models import ThreatIntelligenceMetricEntity
    from ._models import ThreatIntelligenceMetrics
    from ._models import ThreatIntelligenceMetricsList
    from ._models import ThreatIntelligenceResourceKind1
    from ._models import ThreatIntelligenceSortingCriteria1
    from ._models import TICheckRequirements
    from ._models import TIDataConnector
    from ._models import TIDataConnectorDataTypes
    from ._models import TIDataConnectorDataTypesIndicators
    from ._models import TimelineAggregation
    from ._models import TimelineError
    from ._models import TimelineResultsMetadata
    from ._models import TiTaxiiCheckRequirements
    from ._models import TiTaxiiDataConnector
    from ._models import TiTaxiiDataConnectorDataTypes
    from ._models import TiTaxiiDataConnectorDataTypesTaxiiClient
    from ._models import Ueba
    from ._models import UrlEntity
    from ._models import UserInfo
    from ._models import Watchlist
    from ._models import WatchlistItem
from ._paged_models import ActionResponsePaged
from ._paged_models import AlertRulePaged
from ._paged_models import AlertRuleTemplatePaged
from ._paged_models import BookmarkPaged
from ._paged_models import CaseCommentPaged
from ._paged_models import CasePaged
from ._paged_models import CaseRelationPaged
from ._paged_models import DataConnectorPaged
from ._paged_models import EntityPaged
from ._paged_models import EntityQueryPaged
from ._paged_models import IncidentCommentPaged
from ._paged_models import IncidentPaged
from ._paged_models import OfficeConsentPaged
from ._paged_models import OperationPaged
from ._paged_models import RelationPaged
from ._paged_models import ThreatIntelligenceInformationPaged
from ._paged_models import WatchlistPaged
from ._security_insights_enums import (
    AlertRuleKind,
    TemplateStatus,
    TriggerOperator,
    AlertSeverity,
    AttackTactic,
    RelationTypes,
    RelationNodeKind,
    CaseSeverity,
    EntityKind,
    CloseReason,
    CaseStatus,
    DataConnectorAuthorizationState,
    DataConnectorLicenseState,
    DataTypeState,
    DataConnectorKind,
    EntityTimelineKind,
    EntityType,
    EntityQueryKind,
    FileHashAlgorithm,
    OSFamily,
    IncidentClassification,
    IncidentClassificationReason,
    IncidentLabelType,
    IncidentSeverity,
    IncidentStatus,
    ConfidenceLevel,
    ConfidenceScoreStatus,
    KillChainIntent,
    AlertStatus,
    AntispamMailDirection,
    DeliveryAction,
    DeliveryLocation,
    MicrosoftSecurityProductName,
    ElevationToken,
    RegistryHive,
    RegistryValueKind,
    EntitiesMatchingMethod,
    GroupingEntityType,
    EventGroupingAggregationKind,
    SettingKind,
    UebaDataSources,
    Source,
    ThreatIntelligenceResourceKind,
    ThreatIntelligenceSortingCriteria,
)

__all__ = [
    'AADCheckRequirements',
    'AADDataConnector',
    'AATPCheckRequirements',
    'AATPDataConnector',
    'AccountEntity',
    'ActionPropertiesBase',
    'ActionRequest',
    'ActionResponse',
    'ActivityTimelineItem',
    'Aggregations',
    'AggregationsKind',
    'AlertRule',
    'AlertRuleKind1',
    'AlertRuleTemplate',
    'AlertRuleTemplateDataSource',
    'AlertRuleTemplatePropertiesBase',
    'AlertsDataTypeOfDataConnector',
    'AlertsDataTypeOfDataConnectorAlerts',
    'ASCCheckRequirements',
    'ASCDataConnector',
    'AwsCloudTrailCheckRequirements',
    'AwsCloudTrailDataConnector',
    'AwsCloudTrailDataConnectorDataTypes',
    'AwsCloudTrailDataConnectorDataTypesLogs',
    'AzureResourceEntity',
    'Bookmark',
    'BookmarkExpandParameters',
    'BookmarkExpandResponse',
    'BookmarkExpandResponseValue',
    'BookmarkTimelineItem',
    'Case',
    'CaseComment',
    'CaseRelation',
    'CasesAggregation',
    'CasesAggregationBySeverityProperties',
    'CasesAggregationByStatusProperties',
    'ClientInfo',
    'CloudApplicationEntity',
    'DataConnector',
    'DataConnectorDataTypeCommon',
    'DataConnectorKind1',
    'DataConnectorRequirementsState',
    'DataConnectorsCheckRequirements',
    'DataConnectorTenantId',
    'DataConnectorWithAlertsProperties',
    'DnsEntity',
    'Dynamics365CheckRequirements',
    'Dynamics365DataConnector',
    'Dynamics365DataConnectorDataTypes',
    'Dynamics365DataConnectorDataTypesDynamics365CdsActivities',
    'Entity',
    'EntityAnalytics',
    'EntityCommonProperties',
    'EntityExpandParameters',
    'EntityExpandResponse',
    'EntityExpandResponseValue',
    'EntityGetInsightsParameters',
    'EntityGetInsightsResponse',
    'EntityInsightItem',
    'EntityInsightItemQueryTimeInterval',
    'EntityKind1',
    'EntityQuery',
    'EntityQueryItem',
    'EntityQueryItemProperties',
    'EntityQueryItemPropertiesDataTypesItem',
    'EntityQueryKind1',
    'EntityTimelineItem',
    'EntityTimelineParameters',
    'EntityTimelineResponse',
    'EventGroupingSettings',
    'ExpansionEntityQuery',
    'ExpansionResultAggregation',
    'ExpansionResultsMetadata',
    'EyesOn',
    'FileEntity',
    'FileHashEntity',
    'FusionAlertRule',
    'FusionAlertRuleTemplate',
    'GeoLocation',
    'GetInsightsError',
    'GetInsightsResultsMetadata',
    'GetQueriesResponse',
    'GroupingConfiguration',
    'HostEntity',
    'HuntingBookmark',
    'Incident',
    'IncidentAdditionalData',
    'IncidentAlertList',
    'IncidentBookmarkList',
    'IncidentComment',
    'IncidentConfiguration',
    'IncidentEntitiesResponse',
    'IncidentEntitiesResultsMetadata',
    'IncidentInfo',
    'IncidentLabel',
    'IncidentOwnerInfo',
    'InsightQueryItem',
    'InsightQueryItemProperties',
    'InsightQueryItemPropertiesAdditionalQuery',
    'InsightQueryItemPropertiesDefaultTimeRange',
    'InsightQueryItemPropertiesReferenceTimeRange',
    'InsightQueryItemPropertiesTableQuery',
    'InsightQueryItemPropertiesTableQueryColumnsDefinitionsItem',
    'InsightQueryItemPropertiesTableQueryQueriesDefinitionsItem',
    'InsightQueryItemPropertiesTableQueryQueriesDefinitionsItemLinkColumnsDefinitionsItem',
    'InsightsTableResult',
    'InsightsTableResultColumnsItem',
    'IoTDeviceEntity',
    'IpEntity',
    'MailboxEntity',
    'MailClusterEntity',
    'MailMessageEntity',
    'MalwareEntity',
    'MCASCheckRequirements',
    'MCASDataConnector',
    'MCASDataConnectorDataTypes',
    'MCASDataConnectorDataTypesDiscoveryLogs',
    'MDATPCheckRequirements',
    'MDATPDataConnector',
    'MicrosoftSecurityIncidentCreationAlertRule',
    'MicrosoftSecurityIncidentCreationAlertRuleCommonProperties',
    'MicrosoftSecurityIncidentCreationAlertRuleTemplate',
    'OfficeATPCheckRequirements',
    'OfficeATPDataConnector',
    'OfficeConsent',
    'OfficeDataConnector',
    'OfficeDataConnectorDataTypes',
    'OfficeDataConnectorDataTypesExchange',
    'OfficeDataConnectorDataTypesSharePoint',
    'OfficeDataConnectorDataTypesTeams',
    'Operation',
    'OperationDisplay',
    'ProcessEntity',
    'RegistryKeyEntity',
    'RegistryValueEntity',
    'Relation',
    'RelationBase',
    'RelationNode',
    'RelationsModelInput',
    'Resource',
    'ResourceWithEtag',
    'ScheduledAlertRule',
    'ScheduledAlertRuleCommonProperties',
    'ScheduledAlertRuleTemplate',
    'SecurityAlert',
    'SecurityAlertPropertiesConfidenceReasonsItem',
    'SecurityAlertTimelineItem',
    'SecurityGroupEntity',
    'SettingList',
    'Settings',
    'SettingsKind',
    'SubmissionMailEntity',
    'ThreatIntelligence',
    'ThreatIntelligenceAppendTags',
    'ThreatIntelligenceFilteringCriteria',
    'ThreatIntelligenceGranularMarkingModel',
    'ThreatIntelligenceIndicatorModel',
    'ThreatIntelligenceIndicatorModelForRequestBody',
    'ThreatIntelligenceInformation',
    'ThreatIntelligenceKillChainPhase',
    'ThreatIntelligenceMetric',
    'ThreatIntelligenceMetricEntity',
    'ThreatIntelligenceMetrics',
    'ThreatIntelligenceMetricsList',
    'ThreatIntelligenceResourceKind1',
    'ThreatIntelligenceSortingCriteria1',
    'TICheckRequirements',
    'TIDataConnector',
    'TIDataConnectorDataTypes',
    'TIDataConnectorDataTypesIndicators',
    'TimelineAggregation',
    'TimelineError',
    'TimelineResultsMetadata',
    'TiTaxiiCheckRequirements',
    'TiTaxiiDataConnector',
    'TiTaxiiDataConnectorDataTypes',
    'TiTaxiiDataConnectorDataTypesTaxiiClient',
    'Ueba',
    'UrlEntity',
    'UserInfo',
    'Watchlist',
    'WatchlistItem',
    'OperationPaged',
    'AlertRulePaged',
    'ActionResponsePaged',
    'AlertRuleTemplatePaged',
    'CasePaged',
    'CaseCommentPaged',
    'BookmarkPaged',
    'CaseRelationPaged',
    'RelationPaged',
    'DataConnectorPaged',
    'EntityPaged',
    'OfficeConsentPaged',
    'EntityQueryPaged',
    'IncidentPaged',
    'IncidentCommentPaged',
    'WatchlistPaged',
    'ThreatIntelligenceInformationPaged',
    'AlertRuleKind',
    'TemplateStatus',
    'TriggerOperator',
    'AlertSeverity',
    'AttackTactic',
    'RelationTypes',
    'RelationNodeKind',
    'CaseSeverity',
    'EntityKind',
    'CloseReason',
    'CaseStatus',
    'DataConnectorAuthorizationState',
    'DataConnectorLicenseState',
    'DataTypeState',
    'DataConnectorKind',
    'EntityTimelineKind',
    'EntityType',
    'EntityQueryKind',
    'FileHashAlgorithm',
    'OSFamily',
    'IncidentClassification',
    'IncidentClassificationReason',
    'IncidentLabelType',
    'IncidentSeverity',
    'IncidentStatus',
    'ConfidenceLevel',
    'ConfidenceScoreStatus',
    'KillChainIntent',
    'AlertStatus',
    'AntispamMailDirection',
    'DeliveryAction',
    'DeliveryLocation',
    'MicrosoftSecurityProductName',
    'ElevationToken',
    'RegistryHive',
    'RegistryValueKind',
    'EntitiesMatchingMethod',
    'GroupingEntityType',
    'EventGroupingAggregationKind',
    'SettingKind',
    'UebaDataSources',
    'Source',
    'ThreatIntelligenceResourceKind',
    'ThreatIntelligenceSortingCriteria',
]
