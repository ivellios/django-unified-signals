import dataclasses
from unittest import mock

import pytest
from django.dispatch import receiver

from unified_signals.exceptions import UnifiedSignalMessageTypeError
from unified_signals.signals import UnifiedSignal


@dataclasses.dataclass
class DataMock:
    required_field: int
    optional_field: int = 5


class SenderMock:
    pass


def test_event_signal():
    signal = UnifiedSignal(DataMock)
    assert signal.message_class is DataMock


def test_send_signal_without_data():
    # given
    signal = UnifiedSignal(DataMock)

    # when, then
    with pytest.raises(UnifiedSignalMessageTypeError):
        signal.send(SenderMock)


def test_send_signal_with_wrong_data_type():
    # given
    signal = UnifiedSignal(DataMock)

    @dataclasses.dataclass
    class OtherDataMock:
        pass

    # when, then
    with pytest.raises(UnifiedSignalMessageTypeError):
        signal.send(SenderMock, OtherDataMock())


def test_send_signal_with_proper_data_type():
    # given
    signal = UnifiedSignal(DataMock)

    @receiver(signal)
    def handle_signal(sender, message: DataMock, **kwargs):
        assert message.required_field == 10
        assert message.__class__ == DataMock

    # when
    signal.send(
        mock.Mock(),
        DataMock(
            required_field=10,
        ),
    )


def test_send_robust_signal():
    signal = UnifiedSignal(DataMock)

    @receiver(signal)
    def handle_signal(sender, message: DataMock, **kwargs):
        assert message.required_field == 10
        assert message.__class__ == DataMock

    responses = signal.send_robust(
        mock.Mock(),
        DataMock(
            required_field=10,
        ),
    )

    assert all(not isinstance(response, Exception) for _, response in responses)


def test_send_robust_signal_checks_for_wrong_type():
    signal = UnifiedSignal(DataMock)

    with pytest.raises(UnifiedSignalMessageTypeError):
        signal.send_robust(mock.Mock(), 10)


def test_signal_with_use_caching():
    signal = UnifiedSignal(DataMock, use_caching=True)

    handler = mock.Mock()
    receiver(signal)(handler)

    signal.send(mock.Mock(), DataMock(required_field=10))

    handler.assert_called_once()


def test_send_forwards_extra_kwargs():
    signal = UnifiedSignal(DataMock)
    handler = mock.Mock()
    receiver(signal)(handler)

    signal.send(mock.Mock(), DataMock(required_field=10), extra="value")

    _, kwargs = handler.call_args
    assert kwargs["extra"] == "value"


def test_send_robust_forwards_extra_kwargs():
    signal = UnifiedSignal(DataMock)
    handler = mock.Mock()
    receiver(signal)(handler)

    signal.send_robust(mock.Mock(), DataMock(required_field=10), extra="value")

    _, kwargs = handler.call_args
    assert kwargs["extra"] == "value"


def test_receiver_not_called_on_invalid_message():
    signal = UnifiedSignal(DataMock)
    handler = mock.Mock()
    receiver(signal)(handler)

    with pytest.raises(UnifiedSignalMessageTypeError):
        signal.send(mock.Mock(), "not a message")

    handler.assert_not_called()
