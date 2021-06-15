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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class AzureResourceBase(Model):
    """Common properties for all Azure resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy
     and modifiedBy information.
    :vartype system_data:
     ~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(self, **kwargs):
        super(AzureResourceBase, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorAdditionalInfo(Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorResponse(Model):
    """Error Response.

    Common error response for all Azure Resource Manager APIs to return error
    details for failed operations. (This also follows the OData error response
    format.).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details:
     list[~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorResponse]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class LinkedTemplateArtifact(Model):
    """Represents a Template Spec artifact containing an embedded Azure Resource
    Manager template for use as a linked template.

    All required parameters must be populated in order to send to Azure.

    :param path: Required. A filesystem safe relative path of the artifact.
    :type path: str
    :param template: Required. The Azure Resource Manager template.
    :type template: object
    """

    _validation = {
        'path': {'required': True},
        'template': {'required': True},
    }

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'template': {'key': 'template', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(LinkedTemplateArtifact, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
        self.template = kwargs.get('template', None)


class SystemData(Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource.
     Possible values include: 'User', 'Application', 'ManagedIdentity', 'Key'
    :type created_by_type: str or
     ~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the
     resource. Possible values include: 'User', 'Application',
     'ManagedIdentity', 'Key'
    :type last_modified_by_type: str or
     ~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.CreatedByType
    :param last_modified_at: The timestamp of resource last modification (UTC)
    :type last_modified_at: datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = kwargs.get('created_by', None)
        self.created_by_type = kwargs.get('created_by_type', None)
        self.created_at = kwargs.get('created_at', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.last_modified_by_type = kwargs.get('last_modified_by_type', None)
        self.last_modified_at = kwargs.get('last_modified_at', None)


class TemplateSpec(AzureResourceBase):
    """Template Spec object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy
     and modifiedBy information.
    :vartype system_data:
     ~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.SystemData
    :param location: Required. The location of the Template Spec. It cannot be
     changed after Template Spec creation. It must be one of the supported
     Azure locations.
    :type location: str
    :param description: Template Spec description.
    :type description: str
    :param display_name: Template Spec display name.
    :type display_name: str
    :param metadata: The Template Spec metadata. Metadata is an open-ended
     object and is typically a collection of key-value pairs.
    :type metadata: object
    :ivar versions: High-level information about the versions within this
     Template Spec. The keys are the version names. Only populated if the
     $expand query parameter is set to 'versions'.
    :vartype versions: dict[str,
     ~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.TemplateSpecVersionInfo]
    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
        'location': {'required': True},
        'description': {'max_length': 4096},
        'display_name': {'max_length': 64},
        'versions': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'versions': {'key': 'properties.versions', 'type': '{TemplateSpecVersionInfo}'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(TemplateSpec, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.description = kwargs.get('description', None)
        self.display_name = kwargs.get('display_name', None)
        self.metadata = kwargs.get('metadata', None)
        self.versions = None
        self.tags = kwargs.get('tags', None)


class TemplateSpecsError(Model):
    """Template Specs error response.

    :param error:
    :type error:
     ~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, **kwargs):
        super(TemplateSpecsError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class TemplateSpecsErrorException(HttpOperationError):
    """Server responsed with exception of type: 'TemplateSpecsError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(TemplateSpecsErrorException, self).__init__(deserialize, response, 'TemplateSpecsError', *args)


class TemplateSpecUpdateModel(AzureResourceBase):
    """Template Spec properties to be updated (only tags are currently supported).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy
     and modifiedBy information.
    :vartype system_data:
     ~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.SystemData
    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(TemplateSpecUpdateModel, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class TemplateSpecVersion(AzureResourceBase):
    """Template Spec Version object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy
     and modifiedBy information.
    :vartype system_data:
     ~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.SystemData
    :param location: Required. The location of the Template Spec Version. It
     must match the location of the parent Template Spec.
    :type location: str
    :param description: Template Spec version description.
    :type description: str
    :param linked_templates: An array of linked template artifacts.
    :type linked_templates:
     list[~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.LinkedTemplateArtifact]
    :param metadata: The version metadata. Metadata is an open-ended object
     and is typically a collection of key-value pairs.
    :type metadata: object
    :param main_template: The main Azure Resource Manager template content.
    :type main_template: object
    :param ui_form_definition: The Azure Resource Manager template UI
     definition content.
    :type ui_form_definition: object
    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
        'location': {'required': True},
        'description': {'max_length': 4096},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'linked_templates': {'key': 'properties.linkedTemplates', 'type': '[LinkedTemplateArtifact]'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'main_template': {'key': 'properties.mainTemplate', 'type': 'object'},
        'ui_form_definition': {'key': 'properties.uiFormDefinition', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(TemplateSpecVersion, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.description = kwargs.get('description', None)
        self.linked_templates = kwargs.get('linked_templates', None)
        self.metadata = kwargs.get('metadata', None)
        self.main_template = kwargs.get('main_template', None)
        self.ui_form_definition = kwargs.get('ui_form_definition', None)
        self.tags = kwargs.get('tags', None)


class TemplateSpecVersionInfo(Model):
    """High-level information about a Template Spec version.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar description: Template Spec version description.
    :vartype description: str
    :ivar time_created: The timestamp of when the version was created.
    :vartype time_created: datetime
    :ivar time_modified: The timestamp of when the version was last modified.
    :vartype time_modified: datetime
    """

    _validation = {
        'description': {'readonly': True},
        'time_created': {'readonly': True},
        'time_modified': {'readonly': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'time_created': {'key': 'timeCreated', 'type': 'iso-8601'},
        'time_modified': {'key': 'timeModified', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(TemplateSpecVersionInfo, self).__init__(**kwargs)
        self.description = None
        self.time_created = None
        self.time_modified = None


class TemplateSpecVersionUpdateModel(AzureResourceBase):
    """Template Spec Version properties to be updated (only tags are currently
    supported).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy
     and modifiedBy information.
    :vartype system_data:
     ~azure.mgmt.resource.templatespecs.v2021_03_01_preview.models.SystemData
    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(TemplateSpecVersionUpdateModel, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
