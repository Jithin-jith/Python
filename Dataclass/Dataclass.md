# Dataclasses

Dataclasses were introduced in Python 3.7 to provide a convenient way to define classes that store data.  
They reduce boilerplate code by automatically adding special methods like `__init__`, `__repr__`, `__eq__`, and more.

## How to Use Dataclasses
To use dataclasses, you import the `dataclass` decorator from the `dataclasses` module.

## Key Properties
- **Automatic `__init__` Method** - Generates an initializer automatically based on class attributes.
- **Automatic `__repr__` Method** - Provides a readable string representation of the object.
- **Automatic `__eq__` Method** - Enables equality comparisons based on attribute values.
- **Default Values and Default Factories** - Allows setting default values.
- **Immutable Dataclasses** - Can be made immutable using `frozen=True`.
- **Ordering Support** - Enables comparison operators.