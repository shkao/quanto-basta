# Module 2: Databases

## Module introduction

## Setting up a simple database

* SQLite
* SQLAlchemy

### Getting advice on setting up a database

**Prompt:** Suggest a lightweight but powerful Python setup that uses a file-based database so that I can practice working with databases. I want the code to be able to run in Google Colab.

The code snippet demonstrates how to create a connection to an SQLite database using SQLAlchemy in Python:

```python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///ecommerce.db', echo=True)
```

This code creates an SQLite database file named `ecommerce.db` in the current directory. The `echo=True` parameter enables logging of the generated SQL statements, which is helpful for debugging.

## Design and implement a database schema

### Prompting LLMs to design database schema

**Prompt:** I have an SQLite database set up in Python using SQLAlchemy. Help me implement tables for the following schema:

1. **Users:**
   * id (Primary Key)
   * name
   * email (Unique)

2. **Products:**
   * id (Primary Key)
   * name
   * price

3. **Orders:**
   * id (Primary Key)
   * user_id (Foreign Key referencing Users)

4. **Order_items:**
   * id (Primary Key)
   * order_id (Foreign Key referencing Orders)
   * product_id (Foreign Key referencing Products)
   * quantity

## Implementing CRUD operations

### The create operation

**Prompt:** How can I create a function to add a new user to the users table of this database?

```python
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String, unique=True)
)

products = Table('products', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', Integer)
)
...
```

This snippet sets up the database tables `users` and `products` using SQLAlchemy's `Table` and `Column` classes. To add a function for creating a new user, you would need to establish a connection to the database and execute an insert operation.

### Implementing read functionality

**Prompt:** Generate code that implements a read function for this database. It should return a list of all users currently in the database:

```python
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String, unique=True)
)

products = Table('products', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', Integer)
)
...
```

To implement a function that retrieves all users from the `users` table, you need to connect to the database and execute a `SELECT` query using SQLAlchemy's connection and execution model.

### Checking for vulnerabilities

**Prompt:** I’m using this code in a SQL database. Is there a chance that it’s vulnerable to SQL injection attack as SQLAlchemy appears to use SQL under-the-hood?

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def add_user(name, email):
    new_user = users.insert().values(name=name, email=email)
    session.execute(new_user)
    session.commit()
```

SQLAlchemy's `insert()` method with parameterized values (as shown in the code) uses bound parameters to safely handle user input, protecting against SQL injection attacks. By passing values through the `values()` method, the input is correctly parameterized, which avoids directly concatenating user input into the SQL query. Hence, the code is considered safe from SQL injection vulnerabilities in this context.

## Advanced querying

### Asking an LLM to write SQL queries (new chat)

**Prompt:** Write a SQLAlchemy query to find all orders placed by a specific user in the following e-commerce database.

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the SQLite database
engine = create_engine('sqlite:///ecommerce.db')
Base = declarative_base()

# Define the Users table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
```

To write a query that retrieves all orders for a specific user, you would need to create relationships between the `User` and `Order` classes and join the tables accordingly using SQLAlchemy's querying capabilities.

## Databaset optimization

### Optimizing the database

* Schema Design
* Indexing
* Query Optimization
* Caching
  * dogpile.cache
* Connection Management
* Monitoring and Maintenance

## Debugging
