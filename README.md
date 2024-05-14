# alertist

Alertist is a library that makes it as easy as possible to send a message to a target, without rewriting code. All configuration happens via environment variables.

-----

## Motivation

Sending alerts just needs to be easy. Code shouldn't need rewriting so that you can change the destination for a message, a deployment shouldn't have to happen, and CI changed just to send an email, when an SNS message will do.  Enter alertist.

Alertist makes is simple to send alerts. Configure environment variables, and run your python application. But maybe that doesn't work for you - alertist loads a .env by default, from your current working directory, making it as painless as possible to trigger alert sending, without application overhead.

## Installation

`pip install alertist`

## Usage

Create an alertist object, and call the `alert` method with the target and message. The alertist object, must be instantiated with the target, or alert type you'd like to send.

```python

from alertist import Alertist
from alertist.targets import Pushover

a = Alertist(Pushover)
a.alert("Hello, world!")
```

If you'd like to send a message asynchronously, you use the exact same code, except that the `alert` method is now called `aalert`, and must be awaited.

```python
from alertist import Alertist
from alertist.targets import Pushover

a = Alertist(Pushover)
await a.alert("Hello, world!")
```

Supported alert types can be found in the [targets folder](alertist/targets).

-----

## Contributing

### Writing a new alert target

Bug, features, or integrations? Feel free to contribute in whatever way you can! But below, let's highlight how to create a new alert target.

1. Create a new class subclassing `ABCTarget`
1. Implement the synchronous `alert` method, and asynchronous `aalert` method
1. Add all environment variables that can be configured to `CONFIG_KEYS` in your class.
1. Add your class to `targets.__all__` in `__init__.py`
1. Write two unit tests, probably mocking your connecting.
