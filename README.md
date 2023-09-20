# Django Unified Signals

[![Continuous Integration](https://github.com/ivellios/django-unified-signals/actions/workflows/ci.yaml/badge.svg)](https://github.com/ivellios/django-unified-signals/actions/workflows/ci.yaml)

This package extends behavior of the Django Signals, by unifying the data passed
when the signal is sent. That way both: the sender and the receiver can be sure 
that the data passed is always of the same type.

Django Signals are not very strict on the data that can be passed with [send method](https://docs.djangoproject.com/en/4.2/topics/signals/#django.dispatch.Signal.send).
Basically anything can be passed as the arguments and receivers 
need to be aware of that from the project documentation. It gets even worse when on one
side the signal send params change and the receivers' maintainers may not be aware of that. 
It gets even worse, when using send_robust method, which ignores all exceptions 
and any errors may pass without being noticed.

Using this package you have to define the message type class which object  
is always expected to be passed when sending the signal. That way receiver 
knows what type of message will be received. This package automates the process
of checking if the send message is following the contract.

## Installation

The package is [available on PyPI](https://pypi.org/project/django-unified-signals/): 

```bash
pip install django-unified-signals
```

## Usage

Let's start by defining the message structure. It can be any class you want.
In the example we will use `dataclass`:

```python
import dataclasses

@dataclasses.dataclass
class UserMessage:
    name: str
    age: int
```

Now that we have the message structure defined, we can create the signal:

```python

from unified_signals import UnifiedSignal

user_deactivated_signal = UnifiedSignal(UserMessage)
```

It extends the standard `django.dispatch.Signal` class, 
so it can be used in the same way.

```python
user_deactivated_signal.send(sender, UserMessage(name='John', age=30))
```

The receiver can be defined in the same way as for the standard Django Signal:

```python
@receiver(user_deactivated_signal)
def handle_user_deactivated(sender, message: UserMessage, **kwargs):
    print(message.name)
    print(message.age)
    ...
```

The difference is that the message is always of the same type, so the receiver
can be sure that the message is always of the same type. If the message is not
of the expected type when sending the signal, the `unified_signals.exceptions.UnifiedSignalMessageTypeError` 
exception will be raised.

```python
user_deactivated_signal.send(sender, 'not a message') # raises UnifiedSignalMessageTypeError
```
