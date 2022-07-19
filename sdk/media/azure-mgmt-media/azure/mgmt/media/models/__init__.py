# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AacAudio
from ._models_py3 import AbsoluteClipTime
from ._models_py3 import AccessControl
from ._models_py3 import AccountEncryption
from ._models_py3 import AccountFilter
from ._models_py3 import AccountFilterCollection
from ._models_py3 import AkamaiAccessControl
from ._models_py3 import AkamaiSignatureHeaderAuthenticationKey
from ._models_py3 import ArmStreamingEndpointCapacity
from ._models_py3 import ArmStreamingEndpointCurrentSku
from ._models_py3 import ArmStreamingEndpointSku
from ._models_py3 import ArmStreamingEndpointSkuInfo
from ._models_py3 import Asset
from ._models_py3 import AssetCollection
from ._models_py3 import AssetContainerSas
from ._models_py3 import AssetFileEncryptionMetadata
from ._models_py3 import AssetFilter
from ._models_py3 import AssetFilterCollection
from ._models_py3 import AssetStreamingLocator
from ._models_py3 import AssetTrack
from ._models_py3 import AssetTrackCollection
from ._models_py3 import AssetTrackOperationStatus
from ._models_py3 import AsyncOperationErrorDetail
from ._models_py3 import AsyncOperationResult
from ._models_py3 import Audio
from ._models_py3 import AudioAnalyzerPreset
from ._models_py3 import AudioOverlay
from ._models_py3 import AudioTrack
from ._models_py3 import AudioTrackDescriptor
from ._models_py3 import BuiltInStandardEncoderPreset
from ._models_py3 import CbcsDrmConfiguration
from ._models_py3 import CencDrmConfiguration
from ._models_py3 import CheckNameAvailabilityInput
from ._models_py3 import ClipTime
from ._models_py3 import Codec
from ._models_py3 import CommonEncryptionCbcs
from ._models_py3 import CommonEncryptionCenc
from ._models_py3 import ContentKeyPolicy
from ._models_py3 import ContentKeyPolicyClearKeyConfiguration
from ._models_py3 import ContentKeyPolicyCollection
from ._models_py3 import ContentKeyPolicyConfiguration
from ._models_py3 import ContentKeyPolicyFairPlayConfiguration
from ._models_py3 import ContentKeyPolicyFairPlayOfflineRentalConfiguration
from ._models_py3 import ContentKeyPolicyOpenRestriction
from ._models_py3 import ContentKeyPolicyOption
from ._models_py3 import ContentKeyPolicyPlayReadyConfiguration
from ._models_py3 import ContentKeyPolicyPlayReadyContentEncryptionKeyFromHeader
from ._models_py3 import ContentKeyPolicyPlayReadyContentEncryptionKeyFromKeyIdentifier
from ._models_py3 import ContentKeyPolicyPlayReadyContentKeyLocation
from ._models_py3 import ContentKeyPolicyPlayReadyExplicitAnalogTelevisionRestriction
from ._models_py3 import ContentKeyPolicyPlayReadyLicense
from ._models_py3 import ContentKeyPolicyPlayReadyPlayRight
from ._models_py3 import ContentKeyPolicyProperties
from ._models_py3 import ContentKeyPolicyRestriction
from ._models_py3 import ContentKeyPolicyRestrictionTokenKey
from ._models_py3 import ContentKeyPolicyRsaTokenKey
from ._models_py3 import ContentKeyPolicySymmetricTokenKey
from ._models_py3 import ContentKeyPolicyTokenClaim
from ._models_py3 import ContentKeyPolicyTokenRestriction
from ._models_py3 import ContentKeyPolicyUnknownConfiguration
from ._models_py3 import ContentKeyPolicyUnknownRestriction
from ._models_py3 import ContentKeyPolicyWidevineConfiguration
from ._models_py3 import ContentKeyPolicyX509CertificateTokenKey
from ._models_py3 import CopyAudio
from ._models_py3 import CopyVideo
from ._models_py3 import CrossSiteAccessPolicies
from ._models_py3 import DefaultKey
from ._models_py3 import Deinterlace
from ._models_py3 import EdgePolicies
from ._models_py3 import EdgeUsageDataCollectionPolicy
from ._models_py3 import EdgeUsageDataEventHub
from ._models_py3 import EnabledProtocols
from ._models_py3 import EntityNameAvailabilityCheckOutput
from ._models_py3 import EnvelopeEncryption
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import FaceDetectorPreset
from ._models_py3 import FilterTrackPropertyCondition
from ._models_py3 import FilterTrackSelection
from ._models_py3 import Filters
from ._models_py3 import FirstQuality
from ._models_py3 import Format
from ._models_py3 import FromAllInputFile
from ._models_py3 import FromEachInputFile
from ._models_py3 import H264Layer
from ._models_py3 import H264Video
from ._models_py3 import H265Layer
from ._models_py3 import H265Video
from ._models_py3 import H265VideoLayer
from ._models_py3 import Hls
from ._models_py3 import HlsSettings
from ._models_py3 import IPAccessControl
from ._models_py3 import IPRange
from ._models_py3 import Image
from ._models_py3 import ImageFormat
from ._models_py3 import InputDefinition
from ._models_py3 import InputFile
from ._models_py3 import Job
from ._models_py3 import JobCollection
from ._models_py3 import JobError
from ._models_py3 import JobErrorDetail
from ._models_py3 import JobInput
from ._models_py3 import JobInputAsset
from ._models_py3 import JobInputClip
from ._models_py3 import JobInputHttp
from ._models_py3 import JobInputSequence
from ._models_py3 import JobInputs
from ._models_py3 import JobOutput
from ._models_py3 import JobOutputAsset
from ._models_py3 import JpgFormat
from ._models_py3 import JpgImage
from ._models_py3 import JpgLayer
from ._models_py3 import KeyDelivery
from ._models_py3 import KeyVaultProperties
from ._models_py3 import Layer
from ._models_py3 import ListContainerSasInput
from ._models_py3 import ListContentKeysResponse
from ._models_py3 import ListEdgePoliciesInput
from ._models_py3 import ListPathsResponse
from ._models_py3 import ListStreamingLocatorsResponse
from ._models_py3 import LiveEvent
from ._models_py3 import LiveEventActionInput
from ._models_py3 import LiveEventEncoding
from ._models_py3 import LiveEventEndpoint
from ._models_py3 import LiveEventInput
from ._models_py3 import LiveEventInputAccessControl
from ._models_py3 import LiveEventInputTrackSelection
from ._models_py3 import LiveEventListResult
from ._models_py3 import LiveEventOutputTranscriptionTrack
from ._models_py3 import LiveEventPreview
from ._models_py3 import LiveEventPreviewAccessControl
from ._models_py3 import LiveEventTranscription
from ._models_py3 import LiveOutput
from ._models_py3 import LiveOutputListResult
from ._models_py3 import LogSpecification
from ._models_py3 import MediaService
from ._models_py3 import MediaServiceCollection
from ._models_py3 import MediaServiceIdentity
from ._models_py3 import MediaServiceOperationStatus
from ._models_py3 import MediaServiceUpdate
from ._models_py3 import MetricDimension
from ._models_py3 import MetricSpecification
from ._models_py3 import Mp4Format
from ._models_py3 import MultiBitrateFormat
from ._models_py3 import NoEncryption
from ._models_py3 import Operation
from ._models_py3 import OperationCollection
from ._models_py3 import OperationDisplay
from ._models_py3 import OutputFile
from ._models_py3 import Overlay
from ._models_py3 import PngFormat
from ._models_py3 import PngImage
from ._models_py3 import PngLayer
from ._models_py3 import PresentationTimeRange
from ._models_py3 import Preset
from ._models_py3 import PresetConfigurations
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import Properties
from ._models_py3 import ProxyResource
from ._models_py3 import Rectangle
from ._models_py3 import Resource
from ._models_py3 import ResourceIdentity
from ._models_py3 import SelectAudioTrackByAttribute
from ._models_py3 import SelectAudioTrackById
from ._models_py3 import SelectVideoTrackByAttribute
from ._models_py3 import SelectVideoTrackById
from ._models_py3 import ServiceSpecification
from ._models_py3 import StandardEncoderPreset
from ._models_py3 import StorageAccount
from ._models_py3 import StorageEncryptedAssetDecryptionData
from ._models_py3 import StreamingEndpoint
from ._models_py3 import StreamingEndpointAccessControl
from ._models_py3 import StreamingEndpointListResult
from ._models_py3 import StreamingEndpointSkuInfoListResult
from ._models_py3 import StreamingEntityScaleUnit
from ._models_py3 import StreamingLocator
from ._models_py3 import StreamingLocatorCollection
from ._models_py3 import StreamingLocatorContentKey
from ._models_py3 import StreamingPath
from ._models_py3 import StreamingPolicy
from ._models_py3 import StreamingPolicyCollection
from ._models_py3 import StreamingPolicyContentKey
from ._models_py3 import StreamingPolicyContentKeys
from ._models_py3 import StreamingPolicyFairPlayConfiguration
from ._models_py3 import StreamingPolicyPlayReadyConfiguration
from ._models_py3 import StreamingPolicyWidevineConfiguration
from ._models_py3 import SyncStorageKeysInput
from ._models_py3 import SystemData
from ._models_py3 import TextTrack
from ._models_py3 import TrackBase
from ._models_py3 import TrackDescriptor
from ._models_py3 import TrackPropertyCondition
from ._models_py3 import TrackSelection
from ._models_py3 import TrackedResource
from ._models_py3 import Transform
from ._models_py3 import TransformCollection
from ._models_py3 import TransformOutput
from ._models_py3 import TransportStreamFormat
from ._models_py3 import UserAssignedManagedIdentity
from ._models_py3 import UtcClipTime
from ._models_py3 import Video
from ._models_py3 import VideoAnalyzerPreset
from ._models_py3 import VideoLayer
from ._models_py3 import VideoOverlay
from ._models_py3 import VideoTrack
from ._models_py3 import VideoTrackDescriptor

from ._azure_media_services_enums import AacAudioProfile
from ._azure_media_services_enums import AccountEncryptionKeyType
from ._azure_media_services_enums import ActionType
from ._azure_media_services_enums import AnalysisResolution
from ._azure_media_services_enums import AssetContainerPermission
from ._azure_media_services_enums import AssetStorageEncryptionFormat
from ._azure_media_services_enums import AsyncOperationStatus
from ._azure_media_services_enums import AttributeFilter
from ._azure_media_services_enums import AudioAnalysisMode
from ._azure_media_services_enums import BlurType
from ._azure_media_services_enums import ChannelMapping
from ._azure_media_services_enums import Complexity
from ._azure_media_services_enums import ContentKeyPolicyFairPlayRentalAndLeaseKeyType
from ._azure_media_services_enums import ContentKeyPolicyPlayReadyContentType
from ._azure_media_services_enums import ContentKeyPolicyPlayReadyLicenseType
from ._azure_media_services_enums import ContentKeyPolicyPlayReadyUnknownOutputPassingOption
from ._azure_media_services_enums import ContentKeyPolicyRestrictionTokenType
from ._azure_media_services_enums import CreatedByType
from ._azure_media_services_enums import DefaultAction
from ._azure_media_services_enums import DeinterlaceMode
from ._azure_media_services_enums import DeinterlaceParity
from ._azure_media_services_enums import EncoderNamedPreset
from ._azure_media_services_enums import EncryptionScheme
from ._azure_media_services_enums import EntropyMode
from ._azure_media_services_enums import FaceRedactorMode
from ._azure_media_services_enums import FilterTrackPropertyCompareOperation
from ._azure_media_services_enums import FilterTrackPropertyType
from ._azure_media_services_enums import H264Complexity
from ._azure_media_services_enums import H264RateControlMode
from ._azure_media_services_enums import H264VideoProfile
from ._azure_media_services_enums import H265Complexity
from ._azure_media_services_enums import H265VideoProfile
from ._azure_media_services_enums import InsightsType
from ._azure_media_services_enums import InterleaveOutput
from ._azure_media_services_enums import JobErrorCategory
from ._azure_media_services_enums import JobErrorCode
from ._azure_media_services_enums import JobRetry
from ._azure_media_services_enums import JobState
from ._azure_media_services_enums import LiveEventEncodingType
from ._azure_media_services_enums import LiveEventInputProtocol
from ._azure_media_services_enums import LiveEventResourceState
from ._azure_media_services_enums import LiveOutputResourceState
from ._azure_media_services_enums import MetricAggregationType
from ._azure_media_services_enums import MetricUnit
from ._azure_media_services_enums import OnErrorType
from ._azure_media_services_enums import Priority
from ._azure_media_services_enums import PrivateEndpointConnectionProvisioningState
from ._azure_media_services_enums import PrivateEndpointServiceConnectionStatus
from ._azure_media_services_enums import ProvisioningState
from ._azure_media_services_enums import PublicNetworkAccess
from ._azure_media_services_enums import Rotation
from ._azure_media_services_enums import StorageAccountType
from ._azure_media_services_enums import StorageAuthentication
from ._azure_media_services_enums import StreamOptionsFlag
from ._azure_media_services_enums import StreamingEndpointResourceState
from ._azure_media_services_enums import StreamingLocatorContentKeyType
from ._azure_media_services_enums import StreamingPolicyStreamingProtocol
from ._azure_media_services_enums import StretchMode
from ._azure_media_services_enums import TrackAttribute
from ._azure_media_services_enums import TrackPropertyCompareOperation
from ._azure_media_services_enums import TrackPropertyType
from ._azure_media_services_enums import VideoSyncMode
from ._azure_media_services_enums import Visibility
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AacAudio",
    "AbsoluteClipTime",
    "AccessControl",
    "AccountEncryption",
    "AccountFilter",
    "AccountFilterCollection",
    "AkamaiAccessControl",
    "AkamaiSignatureHeaderAuthenticationKey",
    "ArmStreamingEndpointCapacity",
    "ArmStreamingEndpointCurrentSku",
    "ArmStreamingEndpointSku",
    "ArmStreamingEndpointSkuInfo",
    "Asset",
    "AssetCollection",
    "AssetContainerSas",
    "AssetFileEncryptionMetadata",
    "AssetFilter",
    "AssetFilterCollection",
    "AssetStreamingLocator",
    "AssetTrack",
    "AssetTrackCollection",
    "AssetTrackOperationStatus",
    "AsyncOperationErrorDetail",
    "AsyncOperationResult",
    "Audio",
    "AudioAnalyzerPreset",
    "AudioOverlay",
    "AudioTrack",
    "AudioTrackDescriptor",
    "BuiltInStandardEncoderPreset",
    "CbcsDrmConfiguration",
    "CencDrmConfiguration",
    "CheckNameAvailabilityInput",
    "ClipTime",
    "Codec",
    "CommonEncryptionCbcs",
    "CommonEncryptionCenc",
    "ContentKeyPolicy",
    "ContentKeyPolicyClearKeyConfiguration",
    "ContentKeyPolicyCollection",
    "ContentKeyPolicyConfiguration",
    "ContentKeyPolicyFairPlayConfiguration",
    "ContentKeyPolicyFairPlayOfflineRentalConfiguration",
    "ContentKeyPolicyOpenRestriction",
    "ContentKeyPolicyOption",
    "ContentKeyPolicyPlayReadyConfiguration",
    "ContentKeyPolicyPlayReadyContentEncryptionKeyFromHeader",
    "ContentKeyPolicyPlayReadyContentEncryptionKeyFromKeyIdentifier",
    "ContentKeyPolicyPlayReadyContentKeyLocation",
    "ContentKeyPolicyPlayReadyExplicitAnalogTelevisionRestriction",
    "ContentKeyPolicyPlayReadyLicense",
    "ContentKeyPolicyPlayReadyPlayRight",
    "ContentKeyPolicyProperties",
    "ContentKeyPolicyRestriction",
    "ContentKeyPolicyRestrictionTokenKey",
    "ContentKeyPolicyRsaTokenKey",
    "ContentKeyPolicySymmetricTokenKey",
    "ContentKeyPolicyTokenClaim",
    "ContentKeyPolicyTokenRestriction",
    "ContentKeyPolicyUnknownConfiguration",
    "ContentKeyPolicyUnknownRestriction",
    "ContentKeyPolicyWidevineConfiguration",
    "ContentKeyPolicyX509CertificateTokenKey",
    "CopyAudio",
    "CopyVideo",
    "CrossSiteAccessPolicies",
    "DefaultKey",
    "Deinterlace",
    "EdgePolicies",
    "EdgeUsageDataCollectionPolicy",
    "EdgeUsageDataEventHub",
    "EnabledProtocols",
    "EntityNameAvailabilityCheckOutput",
    "EnvelopeEncryption",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "FaceDetectorPreset",
    "FilterTrackPropertyCondition",
    "FilterTrackSelection",
    "Filters",
    "FirstQuality",
    "Format",
    "FromAllInputFile",
    "FromEachInputFile",
    "H264Layer",
    "H264Video",
    "H265Layer",
    "H265Video",
    "H265VideoLayer",
    "Hls",
    "HlsSettings",
    "IPAccessControl",
    "IPRange",
    "Image",
    "ImageFormat",
    "InputDefinition",
    "InputFile",
    "Job",
    "JobCollection",
    "JobError",
    "JobErrorDetail",
    "JobInput",
    "JobInputAsset",
    "JobInputClip",
    "JobInputHttp",
    "JobInputSequence",
    "JobInputs",
    "JobOutput",
    "JobOutputAsset",
    "JpgFormat",
    "JpgImage",
    "JpgLayer",
    "KeyDelivery",
    "KeyVaultProperties",
    "Layer",
    "ListContainerSasInput",
    "ListContentKeysResponse",
    "ListEdgePoliciesInput",
    "ListPathsResponse",
    "ListStreamingLocatorsResponse",
    "LiveEvent",
    "LiveEventActionInput",
    "LiveEventEncoding",
    "LiveEventEndpoint",
    "LiveEventInput",
    "LiveEventInputAccessControl",
    "LiveEventInputTrackSelection",
    "LiveEventListResult",
    "LiveEventOutputTranscriptionTrack",
    "LiveEventPreview",
    "LiveEventPreviewAccessControl",
    "LiveEventTranscription",
    "LiveOutput",
    "LiveOutputListResult",
    "LogSpecification",
    "MediaService",
    "MediaServiceCollection",
    "MediaServiceIdentity",
    "MediaServiceOperationStatus",
    "MediaServiceUpdate",
    "MetricDimension",
    "MetricSpecification",
    "Mp4Format",
    "MultiBitrateFormat",
    "NoEncryption",
    "Operation",
    "OperationCollection",
    "OperationDisplay",
    "OutputFile",
    "Overlay",
    "PngFormat",
    "PngImage",
    "PngLayer",
    "PresentationTimeRange",
    "Preset",
    "PresetConfigurations",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "Properties",
    "ProxyResource",
    "Rectangle",
    "Resource",
    "ResourceIdentity",
    "SelectAudioTrackByAttribute",
    "SelectAudioTrackById",
    "SelectVideoTrackByAttribute",
    "SelectVideoTrackById",
    "ServiceSpecification",
    "StandardEncoderPreset",
    "StorageAccount",
    "StorageEncryptedAssetDecryptionData",
    "StreamingEndpoint",
    "StreamingEndpointAccessControl",
    "StreamingEndpointListResult",
    "StreamingEndpointSkuInfoListResult",
    "StreamingEntityScaleUnit",
    "StreamingLocator",
    "StreamingLocatorCollection",
    "StreamingLocatorContentKey",
    "StreamingPath",
    "StreamingPolicy",
    "StreamingPolicyCollection",
    "StreamingPolicyContentKey",
    "StreamingPolicyContentKeys",
    "StreamingPolicyFairPlayConfiguration",
    "StreamingPolicyPlayReadyConfiguration",
    "StreamingPolicyWidevineConfiguration",
    "SyncStorageKeysInput",
    "SystemData",
    "TextTrack",
    "TrackBase",
    "TrackDescriptor",
    "TrackPropertyCondition",
    "TrackSelection",
    "TrackedResource",
    "Transform",
    "TransformCollection",
    "TransformOutput",
    "TransportStreamFormat",
    "UserAssignedManagedIdentity",
    "UtcClipTime",
    "Video",
    "VideoAnalyzerPreset",
    "VideoLayer",
    "VideoOverlay",
    "VideoTrack",
    "VideoTrackDescriptor",
    "AacAudioProfile",
    "AccountEncryptionKeyType",
    "ActionType",
    "AnalysisResolution",
    "AssetContainerPermission",
    "AssetStorageEncryptionFormat",
    "AsyncOperationStatus",
    "AttributeFilter",
    "AudioAnalysisMode",
    "BlurType",
    "ChannelMapping",
    "Complexity",
    "ContentKeyPolicyFairPlayRentalAndLeaseKeyType",
    "ContentKeyPolicyPlayReadyContentType",
    "ContentKeyPolicyPlayReadyLicenseType",
    "ContentKeyPolicyPlayReadyUnknownOutputPassingOption",
    "ContentKeyPolicyRestrictionTokenType",
    "CreatedByType",
    "DefaultAction",
    "DeinterlaceMode",
    "DeinterlaceParity",
    "EncoderNamedPreset",
    "EncryptionScheme",
    "EntropyMode",
    "FaceRedactorMode",
    "FilterTrackPropertyCompareOperation",
    "FilterTrackPropertyType",
    "H264Complexity",
    "H264RateControlMode",
    "H264VideoProfile",
    "H265Complexity",
    "H265VideoProfile",
    "InsightsType",
    "InterleaveOutput",
    "JobErrorCategory",
    "JobErrorCode",
    "JobRetry",
    "JobState",
    "LiveEventEncodingType",
    "LiveEventInputProtocol",
    "LiveEventResourceState",
    "LiveOutputResourceState",
    "MetricAggregationType",
    "MetricUnit",
    "OnErrorType",
    "Priority",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "PublicNetworkAccess",
    "Rotation",
    "StorageAccountType",
    "StorageAuthentication",
    "StreamOptionsFlag",
    "StreamingEndpointResourceState",
    "StreamingLocatorContentKeyType",
    "StreamingPolicyStreamingProtocol",
    "StretchMode",
    "TrackAttribute",
    "TrackPropertyCompareOperation",
    "TrackPropertyType",
    "VideoSyncMode",
    "Visibility",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
