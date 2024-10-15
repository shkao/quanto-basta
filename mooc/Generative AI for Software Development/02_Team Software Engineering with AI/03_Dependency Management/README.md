# Dependency Management

## LLMs and dependencies

**Strengths:**

* Brainstorm libraries and packages to use for your project
* Learn more about a dependency
* Identify dependency conflicts
* Suggest solutions to issues with dependencies

**Weaknesses:**

* LLMs may not know about dependency changes past their training date (some models do search the web)
* May be less helpful or accurate with obscure libraries that are rarely in their training data

## Benefits of virtual environments

* **Isolation**: Each project has its own dependencies, avoiding conflicts
* **Reproducibility**: Ensures that the project runs with the same dependencies across different environments
* **Manageability**: Easier to manage and update dependencies for individual projects

## Managing dependencies in different languages

* Python: Poetry, pipreqs
* Javascript: npm
* C#: nuget

## Python: `pip`

* **`pip list`**: List installed packages.
* **`pip freeze`**: Output installed packages in `requirements.txt` format.
* **`pip-compile`**: Generate `requirements.txt` from `requirements.in`, resolving dependencies.
* **`pip-sync`**: Sync your environment to match `requirements.txt`, installing/removing packages as needed.

## Managing dependency conflicts

1. **Identify the conflict**: Determine which dependencies are causing the issue.
2. **Check compatibility**: Look for versions that are compatible with all packages.
3. **Update dependencies**: Update or modify your dependencies to resolve the conflict.

## Security issues with dependencies

* **Outdated packages**: Using old versions of packages with known vulnerabilities.
* **Transitive dependencies**: Security risks in dependencies of your dependencies.
* **Unmaintained packages**: Relying on packages that are no longer actively maintained.

## Python: `pip-audit`

* A tool to scan Python environments for packages with known security vulnerabilities.
* **Install**: `pip install pip-audit`
* **Basic Usage**: Run `pip-audit` to audit installed packages.
* **Options**:
  * `-r requirements.txt`: Audit packages from a requirements file.
  * `-f json -o file.json`: Output results in JSON format.
  * `--strict`: Exit with a non-zero status if vulnerabilities are found (useful for CI).

## Performing a security audit of your packages

**Prompt:** I am working on a simple web application in Python. Below are the dependencies currently listed for that project. Are there any known security issues for these libraries?

```
blinker==1.8.2
    # via flask
certifi==2024.6.2
    # via requests
charset-normalizer==3.3.2
    # via requests
click==8.1.7
    # via flask
flask==3.0.3
    # via -r requirements.in
idna==3.7
    # via requests
itsdangerous==2.2.0
    # via flask
...
```

## LLMs and dependency security

* LLMs are limited by the data they have access to:
  * Know the cutoff date of your model’s training data
  * Know whether your model can search the web

* Use LLMs in parallel with other tools:
  * Don’t rely exclusively on LLMs to **identify** vulnerabilities
  * LLMs can be very useful in **resolving** vulnerabilities

## LLMs and Dependencies

**Strengths:**

* Brainstorm libraries and packages to use for your project
* Learn more about a dependency
* Identify dependency conflicts
* Suggest solutions to issues with dependencies

**Weaknesses:**

* LLMs may not know about dependency changes past their training date (some models do search the web)
* May be less helpful or accurate with obscure libraries that are rarely in their training data
