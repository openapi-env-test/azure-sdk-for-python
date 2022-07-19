# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ApplicationGroupType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource Type of ApplicationGroup."""

    REMOTE_APP = "RemoteApp"
    DESKTOP = "Desktop"


class ApplicationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Application type of application."""

    REMOTE_APP = "RemoteApp"
    DESKTOP = "Desktop"


class CommandLineSetting(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether this published application can be launched with command line arguments
    provided by the client, command line arguments specified at publish time, or no command line
    arguments at all.
    """

    DO_NOT_ALLOW = "DoNotAllow"
    ALLOW = "Allow"
    REQUIRE = "Require"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DayOfWeek(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Day of the week."""

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class HealthCheckName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the name of the health check operation performed."""

    #: Verifies the SessionHost is joined to a domain. If this check fails is classified as fatal as
    #: no connection can succeed if the SessionHost is not joined to the domain.
    DOMAIN_JOINED_CHECK = "DomainJoinedCheck"
    #: Verifies the SessionHost is not experiencing domain trust issues that will prevent
    #: authentication on SessionHost at connection time when session is created. If this check fails
    #: is classified as fatal as no connection can succeed if we cannot reach the domain for
    #: authentication on the SessionHost.
    DOMAIN_TRUST_CHECK = "DomainTrustCheck"
    #: Verifies the FSLogix service is up and running to make sure users' profiles are loaded in the
    #: session. If this check fails is classified as fatal as even if the connection can succeed, user
    #: experience is bad as the user profile cannot be loaded and user will get a temporary profile in
    #: the session.
    FS_LOGIX_HEALTH_CHECK = "FSLogixHealthCheck"
    #: Verifies that the SxS stack is up and running so connections can succeed. If this check fails
    #: is classified as fatal as no connection can succeed if the SxS stack is not ready.
    SX_S_STACK_LISTENER_CHECK = "SxSStackListenerCheck"
    #: Verifies that the required WVD service and Geneva URLs are reachable from the SessionHost.
    #: These URLs are: RdTokenUri, RdBrokerURI, RdDiagnosticsUri and storage blob URLs for agent
    #: monitoring (geneva). If this check fails, it is non fatal and the machine still can service
    #: connections, main issue may be that monitoring agent is unable to store warm path data (logs,
    #: operations ...).
    URLS_ACCESSIBLE_CHECK = "UrlsAccessibleCheck"
    #: Verifies that the required Geneva agent is running. If this check fails, it is non fatal and
    #: the machine still can service connections, main issue may be that monitoring agent is missing
    #: or running (possibly) older version.
    MONITORING_AGENT_CHECK = "MonitoringAgentCheck"
    #: Verifies the domain the SessionHost is joined to is still reachable. If this check fails is
    #: classified as fatal as no connection can succeed if the domain the SessionHost is joined is not
    #: reachable at the time of connection.
    DOMAIN_REACHABLE = "DomainReachable"
    #: Verifies whether the WebRTCRedirector component is healthy. The WebRTCRedirector component is
    #: used to optimize video and audio performance in Microsoft Teams. This checks whether the
    #: component is still running, and whether there is a higher version available. If this check
    #: fails, it is non fatal and the machine still can service connections, main issue may be the
    #: WebRTCRedirector component has to be restarted or updated.
    WEB_RTC_REDIRECTOR_CHECK = "WebRTCRedirectorCheck"
    #: Verifies the value of SecurityLayer registration key. If the value is 0 (SecurityLayer.RDP)
    #: this check fails with Error code = NativeMethodErrorCode.E_FAIL and is fatal. If the value is 1
    #: (SecurityLayer.Negotiate) this check fails with Error code =
    #: NativeMethodErrorCode.ERROR_SUCCESS and is non fatal.
    SUPPORTED_ENCRYPTION_CHECK = "SupportedEncryptionCheck"
    #: Verifies the metadata service is accessible and return compute properties.
    META_DATA_SERVICE_CHECK = "MetaDataServiceCheck"
    #: Verifies that the AppAttachService is healthy (there were no issues during package staging).
    #: The AppAttachService is used to enable the staging/registration (and eventual
    #: deregistration/destaging) of MSIX apps that have been set up by the tenant admin. This checks
    #: whether the component had any failures during package staging. Failures in staging will prevent
    #: some MSIX apps from working properly for the end user. If this check fails, it is non fatal and
    #: the machine still can service connections, main issue may be certain apps will not work for
    #: end-users.
    APP_ATTACH_HEALTH_CHECK = "AppAttachHealthCheck"


class HealthCheckResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the Health state of the health check we performed."""

    #: Health check result is not currently known.
    UNKNOWN = "Unknown"
    #: Health check passed.
    HEALTH_CHECK_SUCCEEDED = "HealthCheckSucceeded"
    #: Health check failed.
    HEALTH_CHECK_FAILED = "HealthCheckFailed"
    #: We received a Shutdown notification.
    SESSION_HOST_SHUTDOWN = "SessionHostShutdown"


class HostpoolPublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enabled allows this resource to be accessed from both public and private networks, Disabled
    allows this resource to only be accessed via private endpoints.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    ENABLED_FOR_SESSION_HOSTS_ONLY = "EnabledForSessionHostsOnly"
    ENABLED_FOR_CLIENTS_ONLY = "EnabledForClientsOnly"


class HostPoolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """HostPool type for desktop."""

    #: Users will be assigned a SessionHost either by administrators (PersonalDesktopAssignmentType =
    #: Direct) or upon connecting to the pool (PersonalDesktopAssignmentType = Automatic). They will
    #: always be redirected to their assigned SessionHost.
    PERSONAL = "Personal"
    #: Users get a new (random) SessionHost every time it connects to the HostPool.
    POOLED = "Pooled"
    #: Users assign their own machines, load balancing logic remains the same as Personal.
    #: PersonalDesktopAssignmentType must be Direct.
    BYO_DESKTOP = "BYODesktop"


class LoadBalancerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the load balancer."""

    BREADTH_FIRST = "BreadthFirst"
    DEPTH_FIRST = "DepthFirst"
    PERSISTENT = "Persistent"


class Operation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of operation for migration."""

    #: Start the migration.
    START = "Start"
    #: Revoke the migration.
    REVOKE = "Revoke"
    #: Complete the migration.
    COMPLETE = "Complete"
    #: Hide the hostpool.
    HIDE = "Hide"
    #: Unhide the hostpool.
    UNHIDE = "Unhide"


class PersonalDesktopAssignmentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PersonalDesktopAssignment type for HostPool."""

    AUTOMATIC = "Automatic"
    DIRECT = "Direct"


class PreferredAppGroupType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of preferred application group type, default to Desktop Application Group."""

    NONE = "None"
    DESKTOP = "Desktop"
    RAIL_APPLICATIONS = "RailApplications"


class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"


class PrivateEndpointServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private endpoint connection status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enabled allows this resource to be accessed from both public and private networks, Disabled
    allows this resource to only be accessed via private endpoints.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RegistrationTokenOperation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of resetting the token."""

    DELETE = "Delete"
    NONE = "None"
    UPDATE = "Update"


class RemoteApplicationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource Type of Application."""

    IN_BUILT = "InBuilt"
    MSIX_APPLICATION = "MsixApplication"


class ScalingHostPoolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """HostPool type for desktop."""

    #: Users get a new (random) SessionHost every time it connects to the HostPool.
    POOLED = "Pooled"


class SessionHostComponentUpdateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of maintenance for session host components."""

    #: Agent and other agent side components are delivery schedule is controlled by WVD Infra.
    DEFAULT = "Default"
    #: TenantAdmin have opted in for Scheduled Component Update feature.
    SCHEDULED = "Scheduled"


class SessionHostLoadBalancingAlgorithm(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Load balancing algorithm for ramp up period."""

    BREADTH_FIRST = "BreadthFirst"
    DEPTH_FIRST = "DepthFirst"


class SessionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of user session."""

    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    DISCONNECTED = "Disconnected"
    PENDING = "Pending"
    LOG_OFF = "LogOff"
    USER_PROFILE_DISK_MOUNTED = "UserProfileDiskMounted"


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This field is required to be implemented by the Resource Provider if the service has more than
    one tier, but is not required on a PUT.
    """

    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class SSOSecretType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of single sign on Secret Type."""

    SHARED_KEY = "SharedKey"
    CERTIFICATE = "Certificate"
    SHARED_KEY_IN_KEY_VAULT = "SharedKeyInKeyVault"
    CERTIFICATE_IN_KEY_VAULT = "CertificateInKeyVault"


class Status(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status for a SessionHost."""

    #: Session Host has passed all the health checks and is available to handle connections.
    AVAILABLE = "Available"
    #: Session Host is either turned off or has failed critical health checks which is causing service
    #: not to be able to route connections to this session host. Note this replaces previous
    #: 'NoHeartBeat' status.
    UNAVAILABLE = "Unavailable"
    #: Session Host is shutdown - RD Agent reported session host to be stopped or deallocated.
    SHUTDOWN = "Shutdown"
    #: The Session Host is unavailable because it is currently disconnected.
    DISCONNECTED = "Disconnected"
    #: Session Host is unavailable because currently an upgrade of RDAgent/side-by-side stack is in
    #: progress. Note: this state will be removed once the upgrade completes and the host is able to
    #: accept connections.
    UPGRADING = "Upgrading"
    #: Session Host is unavailable because the critical component upgrade (agent, side-by-side stack,
    #: etc.) failed.
    UPGRADE_FAILED = "UpgradeFailed"
    #: The Session Host is not heart beating.
    NO_HEARTBEAT = "NoHeartbeat"
    #: SessionHost is not joined to domain.
    NOT_JOINED_TO_DOMAIN = "NotJoinedToDomain"
    #: SessionHost's domain trust relationship lost
    DOMAIN_TRUST_RELATIONSHIP_LOST = "DomainTrustRelationshipLost"
    #: SxS stack installed on the SessionHost is not ready to receive connections.
    SX_S_STACK_LISTENER_NOT_READY = "SxSStackListenerNotReady"
    #: FSLogix is in an unhealthy state on the session host.
    FS_LOGIX_NOT_HEALTHY = "FSLogixNotHealthy"
    #: New status to inform admins that the health on their endpoint needs to be fixed. The
    #: connections might not fail, as these issues are not fatal.
    NEEDS_ASSISTANCE = "NeedsAssistance"


class StopHostsWhen(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies when to stop hosts during ramp down period."""

    ZERO_SESSIONS = "ZeroSessions"
    ZERO_ACTIVE_SESSIONS = "ZeroActiveSessions"


class UpdateState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Update state of a SessionHost."""

    INITIAL = "Initial"
    PENDING = "Pending"
    STARTED = "Started"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
