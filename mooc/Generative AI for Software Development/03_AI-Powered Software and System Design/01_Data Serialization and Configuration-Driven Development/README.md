# Module 1: Data Serialization and Configuration-Driven Development

## Module introduction

### Configuration-driven development (CDD)

* Behavior, features and settings of an application are controlled by external configuration files
* More flexible software
* Non-technical teammates can modify the application

### Module overview

* Configuration-driven development overview
* Data serialization in Python and configuration file formats
* Design an app to use the DALL-E API using CDD
* Serialize output

## Configuration-driven development overview

### Design paradigms

* Structured approach to software architecture and organization
* Some are baked into popular tools
* Others are supported in tools, but optional

### Brainstorming design paradigms

**Prompt:** You are an expert on software design paradigms. I am working on building a simple Python-based app that will make calls to the DALL-E API and generate images for users.

The application will be deployed in many different contexts and configurations depending on the end users, and I want my less technical colleagues to be able to do some customization without editing the code itself.

What high-level software design paradigms should I consider for this project?

### Configuration-driven development overview

* Behavior controlled through external configuration files  
  * e.g. JSON or YAML

* Benefits  
  * Non-technical teammates can change application  
  * Flexible software for many environments  
  * Reduce bugs  

* Drawbacks  
  * Potential complexity from many configuration files  
  * Debugging is more complicated  
  * Potential security risks

## Choosing a configuration file format

### Prompting best practices

* **Be specific:** Provide detail and context about your problem
* **Assign a role:** Assign a role to tailor the output you receive
* **Request an expert opinion:** Assign an expert role and ask the LLM to evaluate the work you’ve already done to further refine it
* **Give feedback:** Iteratively prompt the LLM and provide feedback on the output you receive to get closer to your expected results

### JSON vs YAML

**JSON**  

* Support across many languages  
* No comment support  
* Verbose  

**YAML**  

* High readable  
* Supports comments  
* Potentially error-prone

## JSON and pickle

### Comparisons

* **JSON (JavaScript Object Notation)**
  * Text-based, human-readable format for data exchange.
  * Supported across multiple programming languages.
  * Common commands:
    * `json.dump()`: Serialize Python object to a file.
    * `json.load()`: Deserialize data from a file.
    * `json.dumps()`: Serialize to a JSON string.
    * `json.loads()`: Deserialize from a JSON string.

* **Pickle**
  * Python-specific binary format for serializing complex objects.
  * Can serialize custom objects, functions, and nested structures.
  * Common commands:
    * `pickle.dump()`: Serialize to a binary file.
    * `pickle.load()`: Deserialize from a binary file.
    * `pickle.dumps()`: Serialize to a byte stream.
    * `pickle.loads()`: Deserialize from a byte stream.
  * **Security Risk**: Avoid unpickling untrusted data, as it can execute malicious code.

* **When to Use?**
  * Use **JSON** for readability and cross-language compatibility.
  * Use **Pickle** for complex Python objects and internal Python applications.
