# Module 3: Software Design Patterns

## Module introduction

### What are design patterns?

- Reusable solutions to common problems in software design.
- Outline standard ways to structure and organize code for specific scenarios.

### Design Patterns: Elements of Reusable Object-Oriented Software

- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (1994)
- Known as the "Gang of Four"

### Gang of Four design pattern groups

- **Creational**  
  Outline object creation mechanisms.

- **Structural**  
  Deal with the composition of classes or objects.

- **Behavioral**  
  Characterize the ways in which classes or objects interact and distribute responsibility.

## Gang of Four patterns overview

### Creational design patterns

- Singleton
- Builder
- Prototypes
- Factory Methods
- Abstract Factories

### Structural design patterns

- Adapter
- Bridges
- Composites
- Decorators
- Facades
- Flyweights
- Proxies

### Behavioral design patterns

- Iterator
- Strategy
- Template Method

## Singletons

## Patterns advice from an LLM

### Requesting design pattern advice

**Prompt:**  
You are an expert in software design patterns, particularly those from the Gang of Four, designed to make coding and maintenance more efficient. Please analyze the following code and suggest some changes that I could make based on good software engineering practice with these design patterns.

### Requesting design pattern advice iteratively

**Follow up:**  
Instead of making all the changes at once, please do them one at a time, going in order from Singleton to Factory to Template Method to Strategy, and explain in detail why you made the changes and what impact they may have.

## Singleton for database connection manager

### Requesting design pattern advice iteratively

**Follow up:**  
Enhance the following code to use the Singleton Gang-of-Four pattern. Strictly follow the common conventions for the pattern.

Start by explaining the conventions for the Singleton pattern and then describe how the code modifications you made strictly follow the conventions.

## Factory Patterns

### Implementing the Factory Pattern

**Prompt:**  
Enhance the following code to use the Factory Gang-of-Four pattern. Strictly follow the common conventions for the pattern. Start by explaining the conventions for the Factory pattern and why it makes sense to use it here. Then describe how the code modifications you made strictly follow the conventions of the pattern.

**YOUR CODE HERE...**

### Factory Pattern elements

- A **factory class** handles overall production of objects.
- **Concrete classes** provide specific instructions to make variations of those objects.

### Multiple company types using the Factory Pattern

**Prompt:**  
Go back to the code that adds data to the database and synthesize some foreign companies (which will have a unique ID, but the ticker is always 'ZZZZ') and the data for them, both in the companies table and in the time series table.

Then fully explain the Factory pattern by having multiple company types—a Domestic Company that is denoted by its ticker, and a Foreign Company that is denoted by its ID.

Create code that shows how...

## Template Method Pattern

### Benefits of the Template Method Pattern

- **Code Reuse**: Common steps are implemented in the base class, reducing code duplication.
- **Flexibility**: Allows subclasses to customize certain steps of the algorithm without changing its overall structure.
- **Control of Algorithm Execution**: The base class controls the execution order, ensuring the algorithm runs consistently.

### When to Use

- When multiple classes share a common algorithm but some steps vary.
- When you want to enforce a certain sequence of method execution.

The Template Method Pattern is great for defining the "skeleton" of an algorithm and letting subclasses fill in the details.

### Requesting Information on the Template Pattern

**Prompt:**  
Great – the third pattern you mentioned was the Template Method pattern. Can you demonstrate where, how, and why you would use it in this code? What advantages would it bring?

### Applying the Template Method Pattern

In the context of our `Company` class, we can use the Template Method pattern to define the process of loading and processing time series data, which might have some common steps and some steps that can vary for different types of companies.

### Exploring more advanced functions

**Prompt:**  
The example of how to use the `postprocess_data` method is very simple right now. What are some interesting examples of ways I could actually make use of the flexibility provided by that `postprocess_data` method?

## Strategy Pattern

### Learning more about the Strategy Pattern

**Prompt:**  
Ok, so next let's explore the Strategy pattern. What is it, how does it work, why would you use it, and demonstrate and clearly explain the code for it.

Also, please give me some scenarios where additions to this code might be made easier with this pattern.

## Comparison of the Design Patterns

Here are the examples in English, showcasing classic scenarios for each design pattern to illustrate their usage clearly.

### 1. Singleton Pattern

**Purpose**: Ensures that a class has only one instance and provides a global access point to that instance.

**Use Case**: When you need to control access to a shared resource or ensure only one instance of an object exists, such as a configuration manager or database connection.

**Example**:

- **Scenario**: Suppose we have a configuration manager in an application, where only one instance is needed to manage settings.

```python
class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = "Default Settings"
        return cls._instance

# Using Singleton Pattern
settings1 = Settings()
settings2 = Settings()

print(settings1 is settings2)  # Output: True
```

In this example, no matter how many times you create `Settings`, they all point to the same instance.

### 2. Factory Patterns

**Purpose**: Defines a method for creating objects, allowing subclasses to decide which class to instantiate. It makes the creation process more flexible.

**Use Case**: When the program needs to create different types of objects based on certain conditions, such as creating various types of vehicles (car, boat, airplane).

**Example**:

- **Scenario**: A transport factory that creates different types of transport based on the user’s choice.

```python
class Car:
    def move(self):
        print("The car is driving.")

class Boat:
    def move(self):
        print("The boat is sailing.")

class TransportFactory:
    @staticmethod
    def create_transport(transport_type):
        if transport_type == "car":
            return Car()
        elif transport_type == "boat":
            return Boat()
        else:
            raise ValueError("Unknown transport type")

# Using Factory Pattern
transport = TransportFactory.create_transport("car")
transport.move()  # Output: The car is driving.
```

In this example, the factory method is responsible for creating the appropriate transport object.

### 3. Template Method Pattern

**Purpose**: Defines the skeleton of an algorithm in a base class, allowing subclasses to override specific steps without changing the algorithm’s structure.

**Use Case**: When several classes share a common process, but some steps differ, such as making different types of beverages (tea or coffee).

**Example**:

- **Scenario**: Suppose we want to make a beverage. The process involves boiling water, adding the main ingredient (tea or coffee), pouring into a cup, and adding condiments.

```python
from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

class Tea(Beverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

class Coffee(Beverage):
    def brew(self):
        print("Brewing the coffee")

    def add_condiments(self):
        print("Adding sugar and milk")

# Using Template Method Pattern
tea = Tea()
tea.prepare_recipe()
# Output:
# Boiling water
# Steeping the tea
# Pouring into cup
# Adding lemon
```

This example shows how the Template Method Pattern defines the process for making a beverage.

### 4. Strategy Pattern

**Purpose**: Allows a program to choose from different behaviors dynamically. These behaviors are encapsulated in a strategy interface and can be swapped during runtime.

**Use Case**: When a program needs to use different algorithms to solve the same problem, such as applying various discount strategies.

**Example**:

- **Scenario**: Suppose we have different discount strategies (no discount, percentage discount, fixed amount discount) and users can choose which discount to apply.

```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price

class PercentageDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9  # 10% off

class FixedAmountDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price - 10

class ShoppingCart:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_discount_strategy(self, strategy):
        self.strategy = strategy

    def calculate_total(self, price):
        return self.strategy.apply_discount(price)

# Using Strategy Pattern
cart = ShoppingCart(NoDiscount())
print(cart.calculate_total(100))  # Output: 100

cart.set_discount_strategy(PercentageDiscount())
print(cart.calculate_total(100))  # Output: 90

cart.set_discount_strategy(FixedAmountDiscount())
print(cart.calculate_total(100))  # Output: 90
```

This example demonstrates how the Strategy Pattern allows changing the discount strategy dynamically.

### Summary

- **Singleton**: Ensures that a class has only one instance, suitable for global settings or resources.
- **Factory Patterns**: Flexible creation of objects based on conditions, useful when the type of object is decided at runtime.
- **Template Method Pattern**: Defines the steps of an algorithm in a base class, with some steps implemented in subclasses, useful for processes with a fixed sequence.
- **Strategy Pattern**: Allows dynamic changes of behavior, useful for cases where different algorithms are needed for the same task.

These design patterns offer different solutions for common software development problems, making the code more flexible, maintainable, and scalable.

## Course conclusion
