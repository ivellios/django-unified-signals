import typing

from django.dispatch import Signal

from .exceptions import UnifiedSignalMessageTypeError


class UnifiedSignal(Signal):
    """

    Example of defining the signal

        @dataclasses.dataclass
        SomeSignalMessage:
            some_field: int

        some_signal = UnifiedSignal(SomeSignalMessage)

    Example of sending the signal:

        some_signal.send(
            sender=SomeSenderClass,
            message=SomeSignalMessage(
                some_field=5
            )
        )

    Example of receiving the signal data:

        @receiver(some_signal)
        def handle_some_signal(sender, message: SomeSignalMessage, **kwargs):
            print(message.some_field)

    """

    def __init__(self, message_class: typing.Type, use_caching=False):
        # NOTE: In pre 4.0 Django versions you would need
        #       to add providing_args param also.
        super().__init__(use_caching=use_caching)
        self.message_class = message_class

    def _check_message_class(self, message):
        if not isinstance(message, self.message_class):
            raise UnifiedSignalMessageTypeError(
                f"Wrong message dataclass passed to the signal send: {message.__class__}. Expected {self.message_class}"
            )

    def send(
        self, sender: typing.Any, message: typing.Optional[typing.Type] = None, **named
    ):
        self._check_message_class(message)
        return super().send(sender, message=message, **named)

    def send_robust(
        self,
        sender: typing.Any,
        message: typing.Optional[typing.Type] = None,
        **named: typing.Any,
    ):
        self._check_message_class(message)
        return super().send_robust(sender, **named)
