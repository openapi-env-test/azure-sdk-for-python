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

from ._configuration import NetworkManagementClientConfiguration
from .operations import ApplicationGatewaysOperations
from .operations import ApplicationSecurityGroupsOperations
from .operations import AvailableDelegationsOperations
from .operations import AvailableResourceGroupDelegationsOperations
from .operations import AzureFirewallsOperations
from .operations import AzureFirewallFqdnTagsOperations
from .operations import BastionHostsOperations
from .operations import NetworkManagementClientOperationsMixin
from .operations import DdosCustomPoliciesOperations
from .operations import DdosProtectionPlansOperations
from .operations import AvailableEndpointServicesOperations
from .operations import ExpressRouteCircuitAuthorizationsOperations
from .operations import ExpressRouteCircuitPeeringsOperations
from .operations import ExpressRouteCircuitConnectionsOperations
from .operations import PeerExpressRouteCircuitConnectionsOperations
from .operations import ExpressRouteCircuitsOperations
from .operations import ExpressRouteServiceProvidersOperations
from .operations import ExpressRouteCrossConnectionsOperations
from .operations import ExpressRouteCrossConnectionPeeringsOperations
from .operations import ExpressRouteGatewaysOperations
from .operations import ExpressRouteConnectionsOperations
from .operations import ExpressRoutePortsLocationsOperations
from .operations import ExpressRoutePortsOperations
from .operations import ExpressRouteLinksOperations
from .operations import FirewallPoliciesOperations
from .operations import FirewallPolicyRuleGroupsOperations
from .operations import LoadBalancersOperations
from .operations import LoadBalancerBackendAddressPoolsOperations
from .operations import LoadBalancerFrontendIPConfigurationsOperations
from .operations import InboundNatRulesOperations
from .operations import LoadBalancerLoadBalancingRulesOperations
from .operations import LoadBalancerOutboundRulesOperations
from .operations import LoadBalancerNetworkInterfacesOperations
from .operations import LoadBalancerProbesOperations
from .operations import NatGatewaysOperations
from .operations import NetworkInterfacesOperations
from .operations import NetworkInterfaceIPConfigurationsOperations
from .operations import NetworkInterfaceLoadBalancersOperations
from .operations import NetworkInterfaceTapConfigurationsOperations
from .operations import NetworkProfilesOperations
from .operations import NetworkSecurityGroupsOperations
from .operations import SecurityRulesOperations
from .operations import DefaultSecurityRulesOperations
from .operations import NetworkWatchersOperations
from .operations import PacketCapturesOperations
from .operations import ConnectionMonitorsOperations
from .operations import Operations
from .operations import PrivateEndpointsOperations
from .operations import AvailablePrivateEndpointTypesOperations
from .operations import PrivateLinkServicesOperations
from .operations import PublicIPAddressesOperations
from .operations import PublicIPPrefixesOperations
from .operations import RouteFiltersOperations
from .operations import RouteFilterRulesOperations
from .operations import RouteTablesOperations
from .operations import RoutesOperations
from .operations import BgpServiceCommunitiesOperations
from .operations import ServiceEndpointPoliciesOperations
from .operations import ServiceEndpointPolicyDefinitionsOperations
from .operations import ServiceTagsOperations
from .operations import UsagesOperations
from .operations import VirtualNetworksOperations
from .operations import SubnetsOperations
from .operations import ResourceNavigationLinksOperations
from .operations import ServiceAssociationLinksOperations
from .operations import VirtualNetworkPeeringsOperations
from .operations import VirtualNetworkGatewaysOperations
from .operations import VirtualNetworkGatewayConnectionsOperations
from .operations import LocalNetworkGatewaysOperations
from .operations import VirtualNetworkTapsOperations
from .operations import VirtualWansOperations
from .operations import VpnSitesOperations
from .operations import VpnSiteLinksOperations
from .operations import VpnSitesConfigurationOperations
from .operations import VirtualHubsOperations
from .operations import HubVirtualNetworkConnectionsOperations
from .operations import VpnGatewaysOperations
from .operations import VpnConnectionsOperations
from .operations import VpnSiteLinkConnectionsOperations
from .operations import VpnLinkConnectionsOperations
from .operations import P2SVpnServerConfigurationsOperations
from .operations import P2SVpnGatewaysOperations
from .operations import WebApplicationFirewallPoliciesOperations
from . import models


class NetworkManagementClient(NetworkManagementClientOperationsMixin):
    """Network Client.

    :ivar application_gateways: ApplicationGatewaysOperations operations
    :vartype application_gateways: azure.mgmt.network.v2019_06_01.operations.ApplicationGatewaysOperations
    :ivar application_security_groups: ApplicationSecurityGroupsOperations operations
    :vartype application_security_groups: azure.mgmt.network.v2019_06_01.operations.ApplicationSecurityGroupsOperations
    :ivar available_delegations: AvailableDelegationsOperations operations
    :vartype available_delegations: azure.mgmt.network.v2019_06_01.operations.AvailableDelegationsOperations
    :ivar available_resource_group_delegations: AvailableResourceGroupDelegationsOperations operations
    :vartype available_resource_group_delegations: azure.mgmt.network.v2019_06_01.operations.AvailableResourceGroupDelegationsOperations
    :ivar azure_firewalls: AzureFirewallsOperations operations
    :vartype azure_firewalls: azure.mgmt.network.v2019_06_01.operations.AzureFirewallsOperations
    :ivar azure_firewall_fqdn_tags: AzureFirewallFqdnTagsOperations operations
    :vartype azure_firewall_fqdn_tags: azure.mgmt.network.v2019_06_01.operations.AzureFirewallFqdnTagsOperations
    :ivar bastion_hosts: BastionHostsOperations operations
    :vartype bastion_hosts: azure.mgmt.network.v2019_06_01.operations.BastionHostsOperations
    :ivar ddos_custom_policies: DdosCustomPoliciesOperations operations
    :vartype ddos_custom_policies: azure.mgmt.network.v2019_06_01.operations.DdosCustomPoliciesOperations
    :ivar ddos_protection_plans: DdosProtectionPlansOperations operations
    :vartype ddos_protection_plans: azure.mgmt.network.v2019_06_01.operations.DdosProtectionPlansOperations
    :ivar available_endpoint_services: AvailableEndpointServicesOperations operations
    :vartype available_endpoint_services: azure.mgmt.network.v2019_06_01.operations.AvailableEndpointServicesOperations
    :ivar express_route_circuit_authorizations: ExpressRouteCircuitAuthorizationsOperations operations
    :vartype express_route_circuit_authorizations: azure.mgmt.network.v2019_06_01.operations.ExpressRouteCircuitAuthorizationsOperations
    :ivar express_route_circuit_peerings: ExpressRouteCircuitPeeringsOperations operations
    :vartype express_route_circuit_peerings: azure.mgmt.network.v2019_06_01.operations.ExpressRouteCircuitPeeringsOperations
    :ivar express_route_circuit_connections: ExpressRouteCircuitConnectionsOperations operations
    :vartype express_route_circuit_connections: azure.mgmt.network.v2019_06_01.operations.ExpressRouteCircuitConnectionsOperations
    :ivar peer_express_route_circuit_connections: PeerExpressRouteCircuitConnectionsOperations operations
    :vartype peer_express_route_circuit_connections: azure.mgmt.network.v2019_06_01.operations.PeerExpressRouteCircuitConnectionsOperations
    :ivar express_route_circuits: ExpressRouteCircuitsOperations operations
    :vartype express_route_circuits: azure.mgmt.network.v2019_06_01.operations.ExpressRouteCircuitsOperations
    :ivar express_route_service_providers: ExpressRouteServiceProvidersOperations operations
    :vartype express_route_service_providers: azure.mgmt.network.v2019_06_01.operations.ExpressRouteServiceProvidersOperations
    :ivar express_route_cross_connections: ExpressRouteCrossConnectionsOperations operations
    :vartype express_route_cross_connections: azure.mgmt.network.v2019_06_01.operations.ExpressRouteCrossConnectionsOperations
    :ivar express_route_cross_connection_peerings: ExpressRouteCrossConnectionPeeringsOperations operations
    :vartype express_route_cross_connection_peerings: azure.mgmt.network.v2019_06_01.operations.ExpressRouteCrossConnectionPeeringsOperations
    :ivar express_route_gateways: ExpressRouteGatewaysOperations operations
    :vartype express_route_gateways: azure.mgmt.network.v2019_06_01.operations.ExpressRouteGatewaysOperations
    :ivar express_route_connections: ExpressRouteConnectionsOperations operations
    :vartype express_route_connections: azure.mgmt.network.v2019_06_01.operations.ExpressRouteConnectionsOperations
    :ivar express_route_ports_locations: ExpressRoutePortsLocationsOperations operations
    :vartype express_route_ports_locations: azure.mgmt.network.v2019_06_01.operations.ExpressRoutePortsLocationsOperations
    :ivar express_route_ports: ExpressRoutePortsOperations operations
    :vartype express_route_ports: azure.mgmt.network.v2019_06_01.operations.ExpressRoutePortsOperations
    :ivar express_route_links: ExpressRouteLinksOperations operations
    :vartype express_route_links: azure.mgmt.network.v2019_06_01.operations.ExpressRouteLinksOperations
    :ivar firewall_policies: FirewallPoliciesOperations operations
    :vartype firewall_policies: azure.mgmt.network.v2019_06_01.operations.FirewallPoliciesOperations
    :ivar firewall_policy_rule_groups: FirewallPolicyRuleGroupsOperations operations
    :vartype firewall_policy_rule_groups: azure.mgmt.network.v2019_06_01.operations.FirewallPolicyRuleGroupsOperations
    :ivar load_balancers: LoadBalancersOperations operations
    :vartype load_balancers: azure.mgmt.network.v2019_06_01.operations.LoadBalancersOperations
    :ivar load_balancer_backend_address_pools: LoadBalancerBackendAddressPoolsOperations operations
    :vartype load_balancer_backend_address_pools: azure.mgmt.network.v2019_06_01.operations.LoadBalancerBackendAddressPoolsOperations
    :ivar load_balancer_frontend_ip_configurations: LoadBalancerFrontendIPConfigurationsOperations operations
    :vartype load_balancer_frontend_ip_configurations: azure.mgmt.network.v2019_06_01.operations.LoadBalancerFrontendIPConfigurationsOperations
    :ivar inbound_nat_rules: InboundNatRulesOperations operations
    :vartype inbound_nat_rules: azure.mgmt.network.v2019_06_01.operations.InboundNatRulesOperations
    :ivar load_balancer_load_balancing_rules: LoadBalancerLoadBalancingRulesOperations operations
    :vartype load_balancer_load_balancing_rules: azure.mgmt.network.v2019_06_01.operations.LoadBalancerLoadBalancingRulesOperations
    :ivar load_balancer_outbound_rules: LoadBalancerOutboundRulesOperations operations
    :vartype load_balancer_outbound_rules: azure.mgmt.network.v2019_06_01.operations.LoadBalancerOutboundRulesOperations
    :ivar load_balancer_network_interfaces: LoadBalancerNetworkInterfacesOperations operations
    :vartype load_balancer_network_interfaces: azure.mgmt.network.v2019_06_01.operations.LoadBalancerNetworkInterfacesOperations
    :ivar load_balancer_probes: LoadBalancerProbesOperations operations
    :vartype load_balancer_probes: azure.mgmt.network.v2019_06_01.operations.LoadBalancerProbesOperations
    :ivar nat_gateways: NatGatewaysOperations operations
    :vartype nat_gateways: azure.mgmt.network.v2019_06_01.operations.NatGatewaysOperations
    :ivar network_interfaces: NetworkInterfacesOperations operations
    :vartype network_interfaces: azure.mgmt.network.v2019_06_01.operations.NetworkInterfacesOperations
    :ivar network_interface_ip_configurations: NetworkInterfaceIPConfigurationsOperations operations
    :vartype network_interface_ip_configurations: azure.mgmt.network.v2019_06_01.operations.NetworkInterfaceIPConfigurationsOperations
    :ivar network_interface_load_balancers: NetworkInterfaceLoadBalancersOperations operations
    :vartype network_interface_load_balancers: azure.mgmt.network.v2019_06_01.operations.NetworkInterfaceLoadBalancersOperations
    :ivar network_interface_tap_configurations: NetworkInterfaceTapConfigurationsOperations operations
    :vartype network_interface_tap_configurations: azure.mgmt.network.v2019_06_01.operations.NetworkInterfaceTapConfigurationsOperations
    :ivar network_profiles: NetworkProfilesOperations operations
    :vartype network_profiles: azure.mgmt.network.v2019_06_01.operations.NetworkProfilesOperations
    :ivar network_security_groups: NetworkSecurityGroupsOperations operations
    :vartype network_security_groups: azure.mgmt.network.v2019_06_01.operations.NetworkSecurityGroupsOperations
    :ivar security_rules: SecurityRulesOperations operations
    :vartype security_rules: azure.mgmt.network.v2019_06_01.operations.SecurityRulesOperations
    :ivar default_security_rules: DefaultSecurityRulesOperations operations
    :vartype default_security_rules: azure.mgmt.network.v2019_06_01.operations.DefaultSecurityRulesOperations
    :ivar network_watchers: NetworkWatchersOperations operations
    :vartype network_watchers: azure.mgmt.network.v2019_06_01.operations.NetworkWatchersOperations
    :ivar packet_captures: PacketCapturesOperations operations
    :vartype packet_captures: azure.mgmt.network.v2019_06_01.operations.PacketCapturesOperations
    :ivar connection_monitors: ConnectionMonitorsOperations operations
    :vartype connection_monitors: azure.mgmt.network.v2019_06_01.operations.ConnectionMonitorsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.network.v2019_06_01.operations.Operations
    :ivar private_endpoints: PrivateEndpointsOperations operations
    :vartype private_endpoints: azure.mgmt.network.v2019_06_01.operations.PrivateEndpointsOperations
    :ivar available_private_endpoint_types: AvailablePrivateEndpointTypesOperations operations
    :vartype available_private_endpoint_types: azure.mgmt.network.v2019_06_01.operations.AvailablePrivateEndpointTypesOperations
    :ivar private_link_services: PrivateLinkServicesOperations operations
    :vartype private_link_services: azure.mgmt.network.v2019_06_01.operations.PrivateLinkServicesOperations
    :ivar public_ip_addresses: PublicIPAddressesOperations operations
    :vartype public_ip_addresses: azure.mgmt.network.v2019_06_01.operations.PublicIPAddressesOperations
    :ivar public_ip_prefixes: PublicIPPrefixesOperations operations
    :vartype public_ip_prefixes: azure.mgmt.network.v2019_06_01.operations.PublicIPPrefixesOperations
    :ivar route_filters: RouteFiltersOperations operations
    :vartype route_filters: azure.mgmt.network.v2019_06_01.operations.RouteFiltersOperations
    :ivar route_filter_rules: RouteFilterRulesOperations operations
    :vartype route_filter_rules: azure.mgmt.network.v2019_06_01.operations.RouteFilterRulesOperations
    :ivar route_tables: RouteTablesOperations operations
    :vartype route_tables: azure.mgmt.network.v2019_06_01.operations.RouteTablesOperations
    :ivar routes: RoutesOperations operations
    :vartype routes: azure.mgmt.network.v2019_06_01.operations.RoutesOperations
    :ivar bgp_service_communities: BgpServiceCommunitiesOperations operations
    :vartype bgp_service_communities: azure.mgmt.network.v2019_06_01.operations.BgpServiceCommunitiesOperations
    :ivar service_endpoint_policies: ServiceEndpointPoliciesOperations operations
    :vartype service_endpoint_policies: azure.mgmt.network.v2019_06_01.operations.ServiceEndpointPoliciesOperations
    :ivar service_endpoint_policy_definitions: ServiceEndpointPolicyDefinitionsOperations operations
    :vartype service_endpoint_policy_definitions: azure.mgmt.network.v2019_06_01.operations.ServiceEndpointPolicyDefinitionsOperations
    :ivar service_tags: ServiceTagsOperations operations
    :vartype service_tags: azure.mgmt.network.v2019_06_01.operations.ServiceTagsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.network.v2019_06_01.operations.UsagesOperations
    :ivar virtual_networks: VirtualNetworksOperations operations
    :vartype virtual_networks: azure.mgmt.network.v2019_06_01.operations.VirtualNetworksOperations
    :ivar subnets: SubnetsOperations operations
    :vartype subnets: azure.mgmt.network.v2019_06_01.operations.SubnetsOperations
    :ivar resource_navigation_links: ResourceNavigationLinksOperations operations
    :vartype resource_navigation_links: azure.mgmt.network.v2019_06_01.operations.ResourceNavigationLinksOperations
    :ivar service_association_links: ServiceAssociationLinksOperations operations
    :vartype service_association_links: azure.mgmt.network.v2019_06_01.operations.ServiceAssociationLinksOperations
    :ivar virtual_network_peerings: VirtualNetworkPeeringsOperations operations
    :vartype virtual_network_peerings: azure.mgmt.network.v2019_06_01.operations.VirtualNetworkPeeringsOperations
    :ivar virtual_network_gateways: VirtualNetworkGatewaysOperations operations
    :vartype virtual_network_gateways: azure.mgmt.network.v2019_06_01.operations.VirtualNetworkGatewaysOperations
    :ivar virtual_network_gateway_connections: VirtualNetworkGatewayConnectionsOperations operations
    :vartype virtual_network_gateway_connections: azure.mgmt.network.v2019_06_01.operations.VirtualNetworkGatewayConnectionsOperations
    :ivar local_network_gateways: LocalNetworkGatewaysOperations operations
    :vartype local_network_gateways: azure.mgmt.network.v2019_06_01.operations.LocalNetworkGatewaysOperations
    :ivar virtual_network_taps: VirtualNetworkTapsOperations operations
    :vartype virtual_network_taps: azure.mgmt.network.v2019_06_01.operations.VirtualNetworkTapsOperations
    :ivar virtual_wans: VirtualWansOperations operations
    :vartype virtual_wans: azure.mgmt.network.v2019_06_01.operations.VirtualWansOperations
    :ivar vpn_sites: VpnSitesOperations operations
    :vartype vpn_sites: azure.mgmt.network.v2019_06_01.operations.VpnSitesOperations
    :ivar vpn_site_links: VpnSiteLinksOperations operations
    :vartype vpn_site_links: azure.mgmt.network.v2019_06_01.operations.VpnSiteLinksOperations
    :ivar vpn_sites_configuration: VpnSitesConfigurationOperations operations
    :vartype vpn_sites_configuration: azure.mgmt.network.v2019_06_01.operations.VpnSitesConfigurationOperations
    :ivar virtual_hubs: VirtualHubsOperations operations
    :vartype virtual_hubs: azure.mgmt.network.v2019_06_01.operations.VirtualHubsOperations
    :ivar hub_virtual_network_connections: HubVirtualNetworkConnectionsOperations operations
    :vartype hub_virtual_network_connections: azure.mgmt.network.v2019_06_01.operations.HubVirtualNetworkConnectionsOperations
    :ivar vpn_gateways: VpnGatewaysOperations operations
    :vartype vpn_gateways: azure.mgmt.network.v2019_06_01.operations.VpnGatewaysOperations
    :ivar vpn_connections: VpnConnectionsOperations operations
    :vartype vpn_connections: azure.mgmt.network.v2019_06_01.operations.VpnConnectionsOperations
    :ivar vpn_site_link_connections: VpnSiteLinkConnectionsOperations operations
    :vartype vpn_site_link_connections: azure.mgmt.network.v2019_06_01.operations.VpnSiteLinkConnectionsOperations
    :ivar vpn_link_connections: VpnLinkConnectionsOperations operations
    :vartype vpn_link_connections: azure.mgmt.network.v2019_06_01.operations.VpnLinkConnectionsOperations
    :ivar p2_svpn_server_configurations: P2SVpnServerConfigurationsOperations operations
    :vartype p2_svpn_server_configurations: azure.mgmt.network.v2019_06_01.operations.P2SVpnServerConfigurationsOperations
    :ivar p2_svpn_gateways: P2SVpnGatewaysOperations operations
    :vartype p2_svpn_gateways: azure.mgmt.network.v2019_06_01.operations.P2SVpnGatewaysOperations
    :ivar web_application_firewall_policies: WebApplicationFirewallPoliciesOperations operations
    :vartype web_application_firewall_policies: azure.mgmt.network.v2019_06_01.operations.WebApplicationFirewallPoliciesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
        self._config = NetworkManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.application_gateways = ApplicationGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application_security_groups = ApplicationSecurityGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.available_delegations = AvailableDelegationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.available_resource_group_delegations = AvailableResourceGroupDelegationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.azure_firewalls = AzureFirewallsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.azure_firewall_fqdn_tags = AzureFirewallFqdnTagsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.bastion_hosts = BastionHostsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.ddos_custom_policies = DdosCustomPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.ddos_protection_plans = DdosProtectionPlansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.available_endpoint_services = AvailableEndpointServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_circuit_authorizations = ExpressRouteCircuitAuthorizationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_circuit_peerings = ExpressRouteCircuitPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_circuit_connections = ExpressRouteCircuitConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.peer_express_route_circuit_connections = PeerExpressRouteCircuitConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_circuits = ExpressRouteCircuitsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_service_providers = ExpressRouteServiceProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_cross_connections = ExpressRouteCrossConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_cross_connection_peerings = ExpressRouteCrossConnectionPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_gateways = ExpressRouteGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_connections = ExpressRouteConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_ports_locations = ExpressRoutePortsLocationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_ports = ExpressRoutePortsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_links = ExpressRouteLinksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.firewall_policies = FirewallPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.firewall_policy_rule_groups = FirewallPolicyRuleGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.load_balancers = LoadBalancersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.load_balancer_backend_address_pools = LoadBalancerBackendAddressPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.load_balancer_frontend_ip_configurations = LoadBalancerFrontendIPConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.inbound_nat_rules = InboundNatRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.load_balancer_load_balancing_rules = LoadBalancerLoadBalancingRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.load_balancer_outbound_rules = LoadBalancerOutboundRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.load_balancer_network_interfaces = LoadBalancerNetworkInterfacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.load_balancer_probes = LoadBalancerProbesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.nat_gateways = NatGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_interfaces = NetworkInterfacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_interface_ip_configurations = NetworkInterfaceIPConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_interface_load_balancers = NetworkInterfaceLoadBalancersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_interface_tap_configurations = NetworkInterfaceTapConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_profiles = NetworkProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_security_groups = NetworkSecurityGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.security_rules = SecurityRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.default_security_rules = DefaultSecurityRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_watchers = NetworkWatchersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.packet_captures = PacketCapturesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.connection_monitors = ConnectionMonitorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoints = PrivateEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.available_private_endpoint_types = AvailablePrivateEndpointTypesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_services = PrivateLinkServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.public_ip_addresses = PublicIPAddressesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.public_ip_prefixes = PublicIPPrefixesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.route_filters = RouteFiltersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.route_filter_rules = RouteFilterRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.route_tables = RouteTablesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.routes = RoutesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.bgp_service_communities = BgpServiceCommunitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.service_endpoint_policies = ServiceEndpointPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.service_endpoint_policy_definitions = ServiceEndpointPolicyDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.service_tags = ServiceTagsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_networks = VirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subnets = SubnetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_navigation_links = ResourceNavigationLinksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.service_association_links = ServiceAssociationLinksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_peerings = VirtualNetworkPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_gateways = VirtualNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_gateway_connections = VirtualNetworkGatewayConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.local_network_gateways = LocalNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_taps = VirtualNetworkTapsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_wans = VirtualWansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vpn_sites = VpnSitesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vpn_site_links = VpnSiteLinksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vpn_sites_configuration = VpnSitesConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_hubs = VirtualHubsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.hub_virtual_network_connections = HubVirtualNetworkConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vpn_gateways = VpnGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vpn_connections = VpnConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vpn_site_link_connections = VpnSiteLinkConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vpn_link_connections = VpnLinkConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.p2_svpn_server_configurations = P2SVpnServerConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.p2_svpn_gateways = P2SVpnGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.web_application_firewall_policies = WebApplicationFirewallPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> NetworkManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
