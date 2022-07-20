# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._azure_ad_only_authentications_operations import AzureADOnlyAuthenticationsOperations
from ._operations import Operations
from ._ip_firewall_rules_operations import IpFirewallRulesOperations
from ._keys_operations import KeysOperations
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._private_link_resources_operations import PrivateLinkResourcesOperations
from ._private_link_hub_private_link_resources_operations import PrivateLinkHubPrivateLinkResourcesOperations
from ._private_link_hubs_operations import PrivateLinkHubsOperations
from ._private_endpoint_connections_private_link_hub_operations import (
    PrivateEndpointConnectionsPrivateLinkHubOperations,
)
from ._sql_pools_operations import SqlPoolsOperations
from ._sql_pool_metadata_sync_configs_operations import SqlPoolMetadataSyncConfigsOperations
from ._sql_pool_operation_results_operations import SqlPoolOperationResultsOperations
from ._sql_pool_geo_backup_policies_operations import SqlPoolGeoBackupPoliciesOperations
from ._sql_pool_data_warehouse_user_activities_operations import SqlPoolDataWarehouseUserActivitiesOperations
from ._sql_pool_restore_points_operations import SqlPoolRestorePointsOperations
from ._sql_pool_replication_links_operations import SqlPoolReplicationLinksOperations
from ._sql_pool_maintenance_windows_operations import SqlPoolMaintenanceWindowsOperations
from ._sql_pool_maintenance_window_options_operations import SqlPoolMaintenanceWindowOptionsOperations
from ._sql_pool_transparent_data_encryptions_operations import SqlPoolTransparentDataEncryptionsOperations
from ._sql_pool_blob_auditing_policies_operations import SqlPoolBlobAuditingPoliciesOperations
from ._sql_pool_operations_operations import SqlPoolOperationsOperations
from ._sql_pool_usages_operations import SqlPoolUsagesOperations
from ._sql_pool_sensitivity_labels_operations import SqlPoolSensitivityLabelsOperations
from ._sql_pool_recommended_sensitivity_labels_operations import SqlPoolRecommendedSensitivityLabelsOperations
from ._sql_pool_schemas_operations import SqlPoolSchemasOperations
from ._sql_pool_tables_operations import SqlPoolTablesOperations
from ._sql_pool_table_columns_operations import SqlPoolTableColumnsOperations
from ._sql_pool_connection_policies_operations import SqlPoolConnectionPoliciesOperations
from ._sql_pool_vulnerability_assessments_operations import SqlPoolVulnerabilityAssessmentsOperations
from ._sql_pool_vulnerability_assessment_scans_operations import SqlPoolVulnerabilityAssessmentScansOperations
from ._sql_pool_security_alert_policies_operations import SqlPoolSecurityAlertPoliciesOperations
from ._sql_pool_vulnerability_assessment_rule_baselines_operations import (
    SqlPoolVulnerabilityAssessmentRuleBaselinesOperations,
)
from ._extended_sql_pool_blob_auditing_policies_operations import ExtendedSqlPoolBlobAuditingPoliciesOperations
from ._data_masking_policies_operations import DataMaskingPoliciesOperations
from ._data_masking_rules_operations import DataMaskingRulesOperations
from ._sql_pool_columns_operations import SqlPoolColumnsOperations
from ._sql_pool_workload_group_operations import SqlPoolWorkloadGroupOperations
from ._sql_pool_workload_classifier_operations import SqlPoolWorkloadClassifierOperations
from ._workspace_managed_sql_server_blob_auditing_policies_operations import (
    WorkspaceManagedSqlServerBlobAuditingPoliciesOperations,
)
from ._workspace_managed_sql_server_extended_blob_auditing_policies_operations import (
    WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations,
)
from ._workspace_managed_sql_server_security_alert_policy_operations import (
    WorkspaceManagedSqlServerSecurityAlertPolicyOperations,
)
from ._workspace_managed_sql_server_vulnerability_assessments_operations import (
    WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations,
)
from ._workspace_managed_sql_server_encryption_protector_operations import (
    WorkspaceManagedSqlServerEncryptionProtectorOperations,
)
from ._workspace_managed_sql_server_usages_operations import WorkspaceManagedSqlServerUsagesOperations
from ._workspace_managed_sql_server_recoverable_sql_pools_operations import (
    WorkspaceManagedSqlServerRecoverableSqlPoolsOperations,
)
from ._workspace_managed_sql_server_dedicated_sql_minimal_tls_settings_operations import (
    WorkspaceManagedSqlServerDedicatedSQLMinimalTlsSettingsOperations,
)
from ._workspaces_operations import WorkspacesOperations
from ._workspace_aad_admins_operations import WorkspaceAadAdminsOperations
from ._workspace_sql_aad_admins_operations import WorkspaceSqlAadAdminsOperations
from ._workspace_managed_identity_sql_control_settings_operations import (
    WorkspaceManagedIdentitySqlControlSettingsOperations,
)
from ._restorable_dropped_sql_pools_operations import RestorableDroppedSqlPoolsOperations
from ._big_data_pools_operations import BigDataPoolsOperations
from ._library_operations import LibraryOperations
from ._libraries_operations import LibrariesOperations
from ._integration_runtimes_operations import IntegrationRuntimesOperations
from ._integration_runtime_node_ip_address_operations import IntegrationRuntimeNodeIpAddressOperations
from ._integration_runtime_object_metadata_operations import IntegrationRuntimeObjectMetadataOperations
from ._integration_runtime_nodes_operations import IntegrationRuntimeNodesOperations
from ._integration_runtime_credentials_operations import IntegrationRuntimeCredentialsOperations
from ._integration_runtime_connection_infos_operations import IntegrationRuntimeConnectionInfosOperations
from ._integration_runtime_auth_keys_operations import IntegrationRuntimeAuthKeysOperations
from ._integration_runtime_monitoring_data_operations import IntegrationRuntimeMonitoringDataOperations
from ._integration_runtime_status_operations import IntegrationRuntimeStatusOperations
from ._spark_configuration_operations import SparkConfigurationOperations
from ._spark_configurations_operations import SparkConfigurationsOperations
from ._kusto_operations_operations import KustoOperationsOperations
from ._kusto_pools_operations import KustoPoolsOperations
from ._kusto_pool_child_resource_operations import KustoPoolChildResourceOperations
from ._kusto_pool_attached_database_configurations_operations import KustoPoolAttachedDatabaseConfigurationsOperations
from ._kusto_pool_databases_operations import KustoPoolDatabasesOperations
from ._kusto_pool_data_connections_operations import KustoPoolDataConnectionsOperations
from ._kusto_pool_principal_assignments_operations import KustoPoolPrincipalAssignmentsOperations
from ._kusto_pool_database_principal_assignments_operations import KustoPoolDatabasePrincipalAssignmentsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureADOnlyAuthenticationsOperations",
    "Operations",
    "IpFirewallRulesOperations",
    "KeysOperations",
    "PrivateEndpointConnectionsOperations",
    "PrivateLinkResourcesOperations",
    "PrivateLinkHubPrivateLinkResourcesOperations",
    "PrivateLinkHubsOperations",
    "PrivateEndpointConnectionsPrivateLinkHubOperations",
    "SqlPoolsOperations",
    "SqlPoolMetadataSyncConfigsOperations",
    "SqlPoolOperationResultsOperations",
    "SqlPoolGeoBackupPoliciesOperations",
    "SqlPoolDataWarehouseUserActivitiesOperations",
    "SqlPoolRestorePointsOperations",
    "SqlPoolReplicationLinksOperations",
    "SqlPoolMaintenanceWindowsOperations",
    "SqlPoolMaintenanceWindowOptionsOperations",
    "SqlPoolTransparentDataEncryptionsOperations",
    "SqlPoolBlobAuditingPoliciesOperations",
    "SqlPoolOperationsOperations",
    "SqlPoolUsagesOperations",
    "SqlPoolSensitivityLabelsOperations",
    "SqlPoolRecommendedSensitivityLabelsOperations",
    "SqlPoolSchemasOperations",
    "SqlPoolTablesOperations",
    "SqlPoolTableColumnsOperations",
    "SqlPoolConnectionPoliciesOperations",
    "SqlPoolVulnerabilityAssessmentsOperations",
    "SqlPoolVulnerabilityAssessmentScansOperations",
    "SqlPoolSecurityAlertPoliciesOperations",
    "SqlPoolVulnerabilityAssessmentRuleBaselinesOperations",
    "ExtendedSqlPoolBlobAuditingPoliciesOperations",
    "DataMaskingPoliciesOperations",
    "DataMaskingRulesOperations",
    "SqlPoolColumnsOperations",
    "SqlPoolWorkloadGroupOperations",
    "SqlPoolWorkloadClassifierOperations",
    "WorkspaceManagedSqlServerBlobAuditingPoliciesOperations",
    "WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations",
    "WorkspaceManagedSqlServerSecurityAlertPolicyOperations",
    "WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations",
    "WorkspaceManagedSqlServerEncryptionProtectorOperations",
    "WorkspaceManagedSqlServerUsagesOperations",
    "WorkspaceManagedSqlServerRecoverableSqlPoolsOperations",
    "WorkspaceManagedSqlServerDedicatedSQLMinimalTlsSettingsOperations",
    "WorkspacesOperations",
    "WorkspaceAadAdminsOperations",
    "WorkspaceSqlAadAdminsOperations",
    "WorkspaceManagedIdentitySqlControlSettingsOperations",
    "RestorableDroppedSqlPoolsOperations",
    "BigDataPoolsOperations",
    "LibraryOperations",
    "LibrariesOperations",
    "IntegrationRuntimesOperations",
    "IntegrationRuntimeNodeIpAddressOperations",
    "IntegrationRuntimeObjectMetadataOperations",
    "IntegrationRuntimeNodesOperations",
    "IntegrationRuntimeCredentialsOperations",
    "IntegrationRuntimeConnectionInfosOperations",
    "IntegrationRuntimeAuthKeysOperations",
    "IntegrationRuntimeMonitoringDataOperations",
    "IntegrationRuntimeStatusOperations",
    "SparkConfigurationOperations",
    "SparkConfigurationsOperations",
    "KustoOperationsOperations",
    "KustoPoolsOperations",
    "KustoPoolChildResourceOperations",
    "KustoPoolAttachedDatabaseConfigurationsOperations",
    "KustoPoolDatabasesOperations",
    "KustoPoolDataConnectionsOperations",
    "KustoPoolPrincipalAssignmentsOperations",
    "KustoPoolDatabasePrincipalAssignmentsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
