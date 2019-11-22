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


class APIError(Model):
    """Error information returned by the API.

    :param code: The error code.
    :type code: object
    :param message: A message explaining the error reported by the service.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'object'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code=None, message: str=None, **kwargs) -> None:
        super(APIError, self).__init__(**kwargs)
        self.code = code
        self.message = message


class APIErrorException(HttpOperationError):
    """Server responsed with exception of type: 'APIError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(APIErrorException, self).__init__(deserialize, response, 'APIError', *args)


class ChangePointDetectRequest(Model):
    """ChangePointDetectRequest.

    All required parameters must be populated in order to send to Azure.

    :param series: Required. Time series data points. Points should be sorted
     by timestamp in ascending order to match the change point detection
     result.
    :type series: list[~azure.cognitiveservices.anomalydetector.models.Point]
    :param granularity: Required. Can only be one of yearly, monthly, weekly,
     daily, hourly or minutely. Granularity is used for verify whether input
     series is valid. Possible values include: 'yearly', 'monthly', 'weekly',
     'daily', 'hourly', 'minutely'
    :type granularity: str or
     ~azure.cognitiveservices.anomalydetector.models.Granularity
    :param custom_interval: Custom Interval is used to set non-standard time
     interval, for example, if the series is 5 minutes, request can be set as
     {"granularity":"minutely", "customInterval":5}.
    :type custom_interval: int
    :param period: Optional argument, periodic value of a time series. If the
     value is null or does not present, the API will determine the period
     automatically.
    :type period: int
    :param stable_trend_window: Optional argument, advanced model parameter, a
     default stableTrendWindow will be used in detection.
    :type stable_trend_window: int
    :param threshold: Optional argument, advanced model parameter, between
     0.0-1.0, the lower the value is, the larger the trend error will be which
     means less change point will be accepted.
    :type threshold: float
    """

    _validation = {
        'series': {'required': True},
        'granularity': {'required': True},
    }

    _attribute_map = {
        'series': {'key': 'series', 'type': '[Point]'},
        'granularity': {'key': 'granularity', 'type': 'Granularity'},
        'custom_interval': {'key': 'customInterval', 'type': 'int'},
        'period': {'key': 'period', 'type': 'int'},
        'stable_trend_window': {'key': 'stableTrendWindow', 'type': 'int'},
        'threshold': {'key': 'threshold', 'type': 'float'},
    }

    def __init__(self, *, series, granularity, custom_interval: int=None, period: int=None, stable_trend_window: int=None, threshold: float=None, **kwargs) -> None:
        super(ChangePointDetectRequest, self).__init__(**kwargs)
        self.series = series
        self.granularity = granularity
        self.custom_interval = custom_interval
        self.period = period
        self.stable_trend_window = stable_trend_window
        self.threshold = threshold


class ChangePointDetectResponse(Model):
    """ChangePointDetectResponse.

    All required parameters must be populated in order to send to Azure.

    :param period: Required. Frequency extracted from the series, zero means
     no recurrent pattern has been found.
    :type period: int
    :param is_change_point: Required. isChangePoint contains change point
     properties for each input point. True means an anomaly either negative or
     positive has been detected. The index of the array is consistent with the
     input series.
    :type is_change_point: list[bool]
    :param confidence_scores: Required. the change point confidence of each
     point
    :type confidence_scores: list[float]
    """

    _validation = {
        'period': {'required': True},
        'is_change_point': {'required': True},
        'confidence_scores': {'required': True},
    }

    _attribute_map = {
        'period': {'key': 'period', 'type': 'int'},
        'is_change_point': {'key': 'isChangePoint', 'type': '[bool]'},
        'confidence_scores': {'key': 'confidenceScores', 'type': '[float]'},
    }

    def __init__(self, *, period: int, is_change_point, confidence_scores, **kwargs) -> None:
        super(ChangePointDetectResponse, self).__init__(**kwargs)
        self.period = period
        self.is_change_point = is_change_point
        self.confidence_scores = confidence_scores


class EntireDetectResponse(Model):
    """EntireDetectResponse.

    All required parameters must be populated in order to send to Azure.

    :param period: Required. Frequency extracted from the series, zero means
     no recurrent pattern has been found.
    :type period: int
    :param expected_values: Required. ExpectedValues contain expected value
     for each input point. The index of the array is consistent with the input
     series.
    :type expected_values: list[float]
    :param upper_margins: Required. UpperMargins contain upper margin of each
     input point. UpperMargin is used to calculate upperBoundary, which equals
     to expectedValue + (100 - marginScale)*upperMargin. Anomalies in response
     can be filtered by upperBoundary and lowerBoundary. By adjusting
     marginScale value, less significant anomalies can be filtered in client
     side. The index of the array is consistent with the input series.
    :type upper_margins: list[float]
    :param lower_margins: Required. LowerMargins contain lower margin of each
     input point. LowerMargin is used to calculate lowerBoundary, which equals
     to expectedValue - (100 - marginScale)*lowerMargin. Points between the
     boundary can be marked as normal ones in client side. The index of the
     array is consistent with the input series.
    :type lower_margins: list[float]
    :param is_anomaly: Required. IsAnomaly contains anomaly properties for
     each input point. True means an anomaly either negative or positive has
     been detected. The index of the array is consistent with the input series.
    :type is_anomaly: list[bool]
    :param is_negative_anomaly: Required. IsNegativeAnomaly contains anomaly
     status in negative direction for each input point. True means a negative
     anomaly has been detected. A negative anomaly means the point is detected
     as an anomaly and its real value is smaller than the expected one. The
     index of the array is consistent with the input series.
    :type is_negative_anomaly: list[bool]
    :param is_positive_anomaly: Required. IsPositiveAnomaly contain anomaly
     status in positive direction for each input point. True means a positive
     anomaly has been detected. A positive anomaly means the point is detected
     as an anomaly and its real value is larger than the expected one. The
     index of the array is consistent with the input series.
    :type is_positive_anomaly: list[bool]
    """

    _validation = {
        'period': {'required': True},
        'expected_values': {'required': True},
        'upper_margins': {'required': True},
        'lower_margins': {'required': True},
        'is_anomaly': {'required': True},
        'is_negative_anomaly': {'required': True},
        'is_positive_anomaly': {'required': True},
    }

    _attribute_map = {
        'period': {'key': 'period', 'type': 'int'},
        'expected_values': {'key': 'expectedValues', 'type': '[float]'},
        'upper_margins': {'key': 'upperMargins', 'type': '[float]'},
        'lower_margins': {'key': 'lowerMargins', 'type': '[float]'},
        'is_anomaly': {'key': 'isAnomaly', 'type': '[bool]'},
        'is_negative_anomaly': {'key': 'isNegativeAnomaly', 'type': '[bool]'},
        'is_positive_anomaly': {'key': 'isPositiveAnomaly', 'type': '[bool]'},
    }

    def __init__(self, *, period: int, expected_values, upper_margins, lower_margins, is_anomaly, is_negative_anomaly, is_positive_anomaly, **kwargs) -> None:
        super(EntireDetectResponse, self).__init__(**kwargs)
        self.period = period
        self.expected_values = expected_values
        self.upper_margins = upper_margins
        self.lower_margins = lower_margins
        self.is_anomaly = is_anomaly
        self.is_negative_anomaly = is_negative_anomaly
        self.is_positive_anomaly = is_positive_anomaly


class LastDetectResponse(Model):
    """LastDetectResponse.

    All required parameters must be populated in order to send to Azure.

    :param period: Required. Frequency extracted from the series, zero means
     no recurrent pattern has been found.
    :type period: int
    :param suggested_window: Required. Suggested input series points needed
     for detecting the latest point.
    :type suggested_window: int
    :param expected_value: Required. Expected value of the latest point.
    :type expected_value: float
    :param upper_margin: Required. Upper margin of the latest point.
     UpperMargin is used to calculate upperBoundary, which equals to
     expectedValue + (100 - marginScale)*upperMargin. If the value of latest
     point is between upperBoundary and lowerBoundary, it should be treated as
     normal value. By adjusting marginScale value, anomaly status of latest
     point can be changed.
    :type upper_margin: float
    :param lower_margin: Required. Lower margin of the latest point.
     LowerMargin is used to calculate lowerBoundary, which equals to
     expectedValue - (100 - marginScale)*lowerMargin.
    :type lower_margin: float
    :param is_anomaly: Required. Anomaly status of the latest point, true
     means the latest point is an anomaly either in negative direction or
     positive direction.
    :type is_anomaly: bool
    :param is_negative_anomaly: Required. Anomaly status in negative direction
     of the latest point. True means the latest point is an anomaly and its
     real value is smaller than the expected one.
    :type is_negative_anomaly: bool
    :param is_positive_anomaly: Required. Anomaly status in positive direction
     of the latest point. True means the latest point is an anomaly and its
     real value is larger than the expected one.
    :type is_positive_anomaly: bool
    """

    _validation = {
        'period': {'required': True},
        'suggested_window': {'required': True},
        'expected_value': {'required': True},
        'upper_margin': {'required': True},
        'lower_margin': {'required': True},
        'is_anomaly': {'required': True},
        'is_negative_anomaly': {'required': True},
        'is_positive_anomaly': {'required': True},
    }

    _attribute_map = {
        'period': {'key': 'period', 'type': 'int'},
        'suggested_window': {'key': 'suggestedWindow', 'type': 'int'},
        'expected_value': {'key': 'expectedValue', 'type': 'float'},
        'upper_margin': {'key': 'upperMargin', 'type': 'float'},
        'lower_margin': {'key': 'lowerMargin', 'type': 'float'},
        'is_anomaly': {'key': 'isAnomaly', 'type': 'bool'},
        'is_negative_anomaly': {'key': 'isNegativeAnomaly', 'type': 'bool'},
        'is_positive_anomaly': {'key': 'isPositiveAnomaly', 'type': 'bool'},
    }

    def __init__(self, *, period: int, suggested_window: int, expected_value: float, upper_margin: float, lower_margin: float, is_anomaly: bool, is_negative_anomaly: bool, is_positive_anomaly: bool, **kwargs) -> None:
        super(LastDetectResponse, self).__init__(**kwargs)
        self.period = period
        self.suggested_window = suggested_window
        self.expected_value = expected_value
        self.upper_margin = upper_margin
        self.lower_margin = lower_margin
        self.is_anomaly = is_anomaly
        self.is_negative_anomaly = is_negative_anomaly
        self.is_positive_anomaly = is_positive_anomaly


class Point(Model):
    """Point.

    All required parameters must be populated in order to send to Azure.

    :param timestamp: Required. Timestamp of a data point (ISO8601 format).
    :type timestamp: datetime
    :param value: Required. The measurement of that point, should be float.
    :type value: float
    """

    _validation = {
        'timestamp': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(self, *, timestamp, value: float, **kwargs) -> None:
        super(Point, self).__init__(**kwargs)
        self.timestamp = timestamp
        self.value = value


class Request(Model):
    """Request.

    All required parameters must be populated in order to send to Azure.

    :param series: Required. Time series data points. Points should be sorted
     by timestamp in ascending order to match the anomaly detection result. If
     the data is not sorted correctly or there is duplicated timestamp, the API
     will not work. In such case, an error message will be returned.
    :type series: list[~azure.cognitiveservices.anomalydetector.models.Point]
    :param granularity: Required. Possible values include: 'yearly',
     'monthly', 'weekly', 'daily', 'hourly', 'minutely'
    :type granularity: str or
     ~azure.cognitiveservices.anomalydetector.models.Granularity
    :param custom_interval: Custom Interval is used to set non-standard time
     interval, for example, if the series is 5 minutes, request can be set as
     {"granularity":"minutely", "customInterval":5}.
    :type custom_interval: int
    :param period: Optional argument, periodic value of a time series. If the
     value is null or does not present, the API will determine the period
     automatically.
    :type period: int
    :param max_anomaly_ratio: Optional argument, advanced model parameter, max
     anomaly ratio in a time series.
    :type max_anomaly_ratio: float
    :param sensitivity: Optional argument, advanced model parameter, between
     0-99, the lower the value is, the larger the margin value will be which
     means less anomalies will be accepted.
    :type sensitivity: int
    """

    _validation = {
        'series': {'required': True},
        'granularity': {'required': True},
    }

    _attribute_map = {
        'series': {'key': 'series', 'type': '[Point]'},
        'granularity': {'key': 'granularity', 'type': 'Granularity'},
        'custom_interval': {'key': 'customInterval', 'type': 'int'},
        'period': {'key': 'period', 'type': 'int'},
        'max_anomaly_ratio': {'key': 'maxAnomalyRatio', 'type': 'float'},
        'sensitivity': {'key': 'sensitivity', 'type': 'int'},
    }

    def __init__(self, *, series, granularity, custom_interval: int=None, period: int=None, max_anomaly_ratio: float=None, sensitivity: int=None, **kwargs) -> None:
        super(Request, self).__init__(**kwargs)
        self.series = series
        self.granularity = granularity
        self.custom_interval = custom_interval
        self.period = period
        self.max_anomaly_ratio = max_anomaly_ratio
        self.sensitivity = sensitivity
