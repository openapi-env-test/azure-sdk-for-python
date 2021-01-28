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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import SecurityInsightsConfiguration
from .operations import Operations
from .operations import AlertRulesOperations
from .operations import ActionsOperations
from .operations import AlertRuleTemplatesOperations
from .operations import CasesOperations
from .operations import CommentsOperations
from .operations import CaseCommentsOperations
from .operations import BookmarksOperations
from .operations import CaseRelationsOperations
from .operations import BookmarkRelationsOperations
from .operations import BookmarkOperations
from .operations import DataConnectorsOperations
from .operations import DataConnectorsCheckRequirementsOperations
from .operations import EntitiesOperations
from .operations import EntitiesGetTimelineOperations
from .operations import EntitiesRelationsOperations
from .operations import EntityRelationsOperations
from .operations import OfficeConsentsOperations
from .operations import ProductSettingsOperations
from .operations import CasesAggregationsOperations
from .operations import EntityQueriesOperations
from .operations import IncidentsOperations
from .operations import IncidentCommentsOperations
from .operations import IncidentRelationsOperations
from .operations import WatchlistsOperations
from .operations import WatchlistItemOperations
from .operations import ThreatIntelligenceIndicatorOperations
from .operations import ThreatIntelligenceIndicatorsOperations
from .operations import ThreatIntelligenceIndicatorMetricsOperations
from . import models


class SecurityInsights(SDKClient):
    """API spec for Microsoft.SecurityInsights (Azure Security Insights) resource provider

    :ivar config: Configuration for client.
    :vartype config: SecurityInsightsConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.contoso.mgmt.securityinsight.operations.Operations
    :ivar alert_rules: AlertRules operations
    :vartype alert_rules: azure.contoso.mgmt.securityinsight.operations.AlertRulesOperations
    :ivar actions: Actions operations
    :vartype actions: azure.contoso.mgmt.securityinsight.operations.ActionsOperations
    :ivar alert_rule_templates: AlertRuleTemplates operations
    :vartype alert_rule_templates: azure.contoso.mgmt.securityinsight.operations.AlertRuleTemplatesOperations
    :ivar cases: Cases operations
    :vartype cases: azure.contoso.mgmt.securityinsight.operations.CasesOperations
    :ivar comments: Comments operations
    :vartype comments: azure.contoso.mgmt.securityinsight.operations.CommentsOperations
    :ivar case_comments: CaseComments operations
    :vartype case_comments: azure.contoso.mgmt.securityinsight.operations.CaseCommentsOperations
    :ivar bookmarks: Bookmarks operations
    :vartype bookmarks: azure.contoso.mgmt.securityinsight.operations.BookmarksOperations
    :ivar case_relations: CaseRelations operations
    :vartype case_relations: azure.contoso.mgmt.securityinsight.operations.CaseRelationsOperations
    :ivar bookmark_relations: BookmarkRelations operations
    :vartype bookmark_relations: azure.contoso.mgmt.securityinsight.operations.BookmarkRelationsOperations
    :ivar bookmark: Bookmark operations
    :vartype bookmark: azure.contoso.mgmt.securityinsight.operations.BookmarkOperations
    :ivar data_connectors: DataConnectors operations
    :vartype data_connectors: azure.contoso.mgmt.securityinsight.operations.DataConnectorsOperations
    :ivar data_connectors_check_requirements: DataConnectorsCheckRequirements operations
    :vartype data_connectors_check_requirements: azure.contoso.mgmt.securityinsight.operations.DataConnectorsCheckRequirementsOperations
    :ivar entities: Entities operations
    :vartype entities: azure.contoso.mgmt.securityinsight.operations.EntitiesOperations
    :ivar entities_get_timeline: EntitiesGetTimeline operations
    :vartype entities_get_timeline: azure.contoso.mgmt.securityinsight.operations.EntitiesGetTimelineOperations
    :ivar entities_relations: EntitiesRelations operations
    :vartype entities_relations: azure.contoso.mgmt.securityinsight.operations.EntitiesRelationsOperations
    :ivar entity_relations: EntityRelations operations
    :vartype entity_relations: azure.contoso.mgmt.securityinsight.operations.EntityRelationsOperations
    :ivar office_consents: OfficeConsents operations
    :vartype office_consents: azure.contoso.mgmt.securityinsight.operations.OfficeConsentsOperations
    :ivar product_settings: ProductSettings operations
    :vartype product_settings: azure.contoso.mgmt.securityinsight.operations.ProductSettingsOperations
    :ivar cases_aggregations: CasesAggregations operations
    :vartype cases_aggregations: azure.contoso.mgmt.securityinsight.operations.CasesAggregationsOperations
    :ivar entity_queries: EntityQueries operations
    :vartype entity_queries: azure.contoso.mgmt.securityinsight.operations.EntityQueriesOperations
    :ivar incidents: Incidents operations
    :vartype incidents: azure.contoso.mgmt.securityinsight.operations.IncidentsOperations
    :ivar incident_comments: IncidentComments operations
    :vartype incident_comments: azure.contoso.mgmt.securityinsight.operations.IncidentCommentsOperations
    :ivar incident_relations: IncidentRelations operations
    :vartype incident_relations: azure.contoso.mgmt.securityinsight.operations.IncidentRelationsOperations
    :ivar watchlists: Watchlists operations
    :vartype watchlists: azure.contoso.mgmt.securityinsight.operations.WatchlistsOperations
    :ivar watchlist_item: WatchlistItem operations
    :vartype watchlist_item: azure.contoso.mgmt.securityinsight.operations.WatchlistItemOperations
    :ivar threat_intelligence_indicator: ThreatIntelligenceIndicator operations
    :vartype threat_intelligence_indicator: azure.contoso.mgmt.securityinsight.operations.ThreatIntelligenceIndicatorOperations
    :ivar threat_intelligence_indicators: ThreatIntelligenceIndicators operations
    :vartype threat_intelligence_indicators: azure.contoso.mgmt.securityinsight.operations.ThreatIntelligenceIndicatorsOperations
    :ivar threat_intelligence_indicator_metrics: ThreatIntelligenceIndicatorMetrics operations
    :vartype threat_intelligence_indicator_metrics: azure.contoso.mgmt.securityinsight.operations.ThreatIntelligenceIndicatorMetricsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = SecurityInsightsConfiguration(credentials, subscription_id, base_url)
        super(SecurityInsights, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-01-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alert_rules = AlertRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.actions = ActionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alert_rule_templates = AlertRuleTemplatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cases = CasesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.comments = CommentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.case_comments = CaseCommentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bookmarks = BookmarksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.case_relations = CaseRelationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bookmark_relations = BookmarkRelationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bookmark = BookmarkOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_connectors = DataConnectorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_connectors_check_requirements = DataConnectorsCheckRequirementsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.entities = EntitiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.entities_get_timeline = EntitiesGetTimelineOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.entities_relations = EntitiesRelationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.entity_relations = EntityRelationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.office_consents = OfficeConsentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.product_settings = ProductSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cases_aggregations = CasesAggregationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.entity_queries = EntityQueriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.incidents = IncidentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.incident_comments = IncidentCommentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.incident_relations = IncidentRelationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.watchlists = WatchlistsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.watchlist_item = WatchlistItemOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.threat_intelligence_indicator = ThreatIntelligenceIndicatorOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.threat_intelligence_indicators = ThreatIntelligenceIndicatorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.threat_intelligence_indicator_metrics = ThreatIntelligenceIndicatorMetricsOperations(
            self._client, self.config, self._serialize, self._deserialize)
