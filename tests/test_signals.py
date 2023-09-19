import dataclasses
from unittest import mock

import pytest
from django.dispatch import receiver

from unified_signals.signals import UnifiedSignal
from unified_signals.exceptions import UnifiedSignalMessageTypeError


@dataclasses.dataclass
class DataMock:
    required_field: int
    optional_field: int = 5


class SenderMock:
    pass


def test_event_signal():
    signal = UnifiedSignal(DataMock)
    assert True


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

    signal.send_robust(
        mock.Mock(),
        DataMock(
            required_field=10,
        ),
    )


def test_send_robus_signal_checks_for_wrong_type():
    signal = UnifiedSignal(DataMock)

    with pytest.raises(UnifiedSignalMessageTypeError):
        signal.send_robust(mock.Mock(), 10)
