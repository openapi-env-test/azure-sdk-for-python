# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class CollectionModel(_model_base.Model):
    """Identifier for collections.

    All required parameters must be populated in order to send to Azure.

    :ivar collection_id: Required.
    :vartype collection_id: str
    """

    collection_id: str = rest_field(name="collectionId")
    """Required. """

    @overload
    def __init__(
        self,
        *,
        collection_id: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ConfidentialLedgerCreateLedgerEntryRequest(_model_base.Model):
    """ConfidentialLedgerCreateLedgerEntryRequest.

    All required parameters must be populated in order to send to Azure.

    :ivar contents: Contents of the ledger entry. Required.
    :vartype contents: str
    """

    contents: str = rest_field()
    """Contents of the ledger entry. Required. """

    @overload
    def __init__(
        self,
        *,
        contents: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Error(_model_base.Model):
    """The error object.

    All required parameters must be populated in order to send to Azure.

    :ivar code: One of a server-defined set of error codes. Required.
    :vartype code: str
    :ivar message: A human-readable representation of the error. Required.
    :vartype message: str
    :ivar target: The target of the error.
    :vartype target: str
    :ivar details: An array of details about specific errors that led to this reported error.
     Required.
    :vartype details: list[~azure.security.confidentialledger.models.Error]
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~azure.security.confidentialledger.models.InnerError
    """

    code: str = rest_field()
    """One of a server-defined set of error codes. Required. """
    message: str = rest_field()
    """A human-readable representation of the error. Required. """
    target: Optional[str] = rest_field()
    """The target of the error. """
    details: List["_models.Error"] = rest_field()
    """An array of details about specific errors that led to this reported error. Required. """
    innererror: Optional["_models.InnerError"] = rest_field()
    """An object containing more specific information than the current object about the error. """

    @overload
    def __init__(
        self,
        *,
        code: str,
        message: str,
        details: List["_models.Error"],
        target: Optional[str] = None,
        innererror: Optional["_models.InnerError"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ErrorResponse(_model_base.Model):
    """A response containing error details.

    All required parameters must be populated in order to send to Azure.

    :ivar error: The error object. Required.
    :vartype error: ~azure.security.confidentialledger.models.Error
    """

    error: "_models.Error" = rest_field()
    """The error object. Required. """

    @overload
    def __init__(
        self,
        *,
        error: "_models.Error",
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InnerError(_model_base.Model):
    """An object containing more specific information about the error. As per Microsoft One API guidelines - https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    All required parameters must be populated in order to send to Azure.

    :ivar code: One of a server-defined set of error codes. Required.
    :vartype code: str
    :ivar innererror: Inner error.
    :vartype innererror: ~azure.security.confidentialledger.models.InnerError
    """

    code: str = rest_field()
    """One of a server-defined set of error codes. Required. """
    innererror: Optional["_models.InnerError"] = rest_field()
    """Inner error. """

    @overload
    def __init__(
        self,
        *,
        code: str,
        innererror: Optional["_models.InnerError"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LedgerEntry(_model_base.Model):
    """LedgerEntry.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar contents: Contents of the ledger entry. Required.
    :vartype contents: str
    :ivar collection_id: Required.
    :vartype collection_id: str
    :ivar transaction_id: Required.
    :vartype transaction_id: str
    """

    contents: str = rest_field()
    """Contents of the ledger entry. Required. """
    collection_id: str = rest_field(name="collectionId", readonly=True)
    """Required. """
    transaction_id: str = rest_field(name="transactionId", readonly=True)
    """Required. """

    @overload
    def __init__(
        self,
        *,
        contents: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LedgerUser(_model_base.Model):
    """LedgerUser.

    All required parameters must be populated in order to send to Azure.

    :ivar user_id: The user id, either an AAD object ID or certificate fingerprint. Required.
    :vartype user_id: str
    :ivar assigned_role: The user's assigned role. Required. Known values are: "Administrator",
     "Contributor", and "Reader".
    :vartype assigned_role: str or ~azure.security.confidentialledger.models.LedgerUserRole
    """

    user_id: str = rest_field(name="userId")
    """The user id, either an AAD object ID or certificate fingerprint. Required. """
    assigned_role: Union[str, "_models.LedgerUserRole"] = rest_field(name="assignedRole")
    """The user's assigned role. Required. Known values are: \"Administrator\", \"Contributor\", and \"Reader\"."""

    @overload
    def __init__(
        self,
        *,
        user_id: str,
        assigned_role: Union[str, "_models.LedgerUserRole"],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PagedLedgerEntries(_model_base.Model):
    """Paginated ledger entries returned in response to a query.

    All required parameters must be populated in order to send to Azure.

    :ivar entries: Array of ledger entries. Required.
    :vartype entries: list[~azure.security.confidentialledger.models.LedgerEntry]
    :ivar state: State of the ledger query. Required. Known values are: "Loading" and "Ready".
    :vartype state: str or ~azure.security.confidentialledger.models.LedgerQueryState
    :ivar next_link: Path from which to retrieve the next page of results.
    :vartype next_link: str
    """

    entries: List["_models.LedgerEntry"] = rest_field()
    """Array of ledger entries. Required. """
    state: Union[str, "_models.LedgerQueryState"] = rest_field()
    """State of the ledger query. Required. Known values are: \"Loading\" and \"Ready\"."""
    next_link: Optional[str] = rest_field(name="nextLink")
    """Path from which to retrieve the next page of results. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ReceiptContents(_model_base.Model):
    """ReceiptContents."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ResourceCreatedResponse(_model_base.Model):
    """A  resource was successfully created.

    All required parameters must be populated in order to send to Azure.

    :ivar user_id: The user id, either an AAD object ID or certificate fingerprint. Required.
    :vartype user_id: str
    :ivar assigned_role: The user's assigned role. Required. Known values are: "Administrator",
     "Contributor", and "Reader".
    :vartype assigned_role: str or ~azure.security.confidentialledger.models.LedgerUserRole
    """

    user_id: str = rest_field(name="userId")
    """The user id, either an AAD object ID or certificate fingerprint. Required. """
    assigned_role: Union[str, "_models.LedgerUserRole"] = rest_field(name="assignedRole")
    """The user's assigned role. Required. Known values are: \"Administrator\", \"Contributor\", and \"Reader\"."""

    @overload
    def __init__(
        self,
        *,
        user_id: str,
        assigned_role: Union[str, "_models.LedgerUserRole"],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ResourceOkResponse(_model_base.Model):
    """ResourceOkResponse.

    All required parameters must be populated in order to send to Azure.

    :ivar user_id: The user id, either an AAD object ID or certificate fingerprint. Required.
    :vartype user_id: str
    :ivar assigned_role: The user's assigned role. Required. Known values are: "Administrator",
     "Contributor", and "Reader".
    :vartype assigned_role: str or ~azure.security.confidentialledger.models.LedgerUserRole
    """

    user_id: str = rest_field(name="userId")
    """The user id, either an AAD object ID or certificate fingerprint. Required. """
    assigned_role: Union[str, "_models.LedgerUserRole"] = rest_field(name="assignedRole")
    """The user's assigned role. Required. Known values are: \"Administrator\", \"Contributor\", and \"Reader\"."""

    @overload
    def __init__(
        self,
        *,
        user_id: str,
        assigned_role: Union[str, "_models.LedgerUserRole"],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TransactionReceipt(_model_base.Model):
    """A receipt certifying the transaction at the specified id.

    All required parameters must be populated in order to send to Azure.

    :ivar receipt: Required.
    :vartype receipt: ~azure.security.confidentialledger.models.ReceiptContents
    :ivar state: Required. Known values are: "Loading" and "Ready".
    :vartype state: str or ~azure.security.confidentialledger.models.LedgerQueryState
    :ivar transaction_id: Required.
    :vartype transaction_id: str
    """

    receipt: "_models.ReceiptContents" = rest_field()
    """Required. """
    state: Union[str, "_models.LedgerQueryState"] = rest_field()
    """Required. Known values are: \"Loading\" and \"Ready\"."""
    transaction_id: str = rest_field(name="transactionId")
    """Required. """

    @overload
    def __init__(
        self,
        *,
        receipt: "_models.ReceiptContents",
        state: Union[str, "_models.LedgerQueryState"],
        transaction_id: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TransactionStatus(_model_base.Model):
    """Response returned to a query for the transaction status.

    All required parameters must be populated in order to send to Azure.

    :ivar state: Required. Known values are: "Committed" and "Pending".
    :vartype state: str or ~azure.security.confidentialledger.models.TransactionState
    :ivar transaction_id: Required.
    :vartype transaction_id: str
    """

    state: Union[str, "_models.TransactionState"] = rest_field()
    """Required. Known values are: \"Committed\" and \"Pending\"."""
    transaction_id: str = rest_field(name="transactionId")
    """Required. """

    @overload
    def __init__(
        self,
        *,
        state: Union[str, "_models.TransactionState"],
        transaction_id: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
