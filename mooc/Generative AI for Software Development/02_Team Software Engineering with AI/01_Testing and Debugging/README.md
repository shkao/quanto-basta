# Module 1: Testing and Debugging

## Module introduction

## Testing and debugging strategies

### The discipline of software testing

- Manual testing
- Automated testing
- Performance testing
- Security testing

## Exploratory testing

### Developing exploratory test cases

**Prompt:** You are a software engineer and tester who is curious and who likes to go through code looking for edge cases. There’s some Python code here -- please explore it and find any issues that might cause bugs or poor functionality: {code}

## Functional testing

### Ask an LLM to create functional tests

**Prompt:** As an expert software tester, write code that converts the output of the exploratory testing into functional tests using the `unittest` module in Python.

## Automated Testing

### Write new test cases for updated code

**Prompt:** As an expert software tester, write code that converts the output of the exploratory testing into functional tests using the `unittest` module in Python.

### Automated Testing and Generating Tests

Framework suggested: [pytest](https://docs.pytest.org/en/stable/)

**Prompt:** You are an expert in PyTest for automated testing of Python code. Please amend this code with a comprehensive set of tests in PyTest to find bugs or other issues in the code.

## Software performance testing

### Software performance testing

**Using cProfile output in your prompt**

**Prompt:** Rewrite my `is_prime` function in the code below to be more optimized. Below the code is the output from a cProfile analysis of the function.

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_of_primes_naive(numbers):
    total = 0
    for number in numbers:
        if is_prime(number):
            total += number
    return total
```

_cProfile output:_

```
ncalls  tottime  percall  cumtime  percall  filename:lineno(function)
1       0.046    0.046    52.203   52.203   <ipython-input-3-ecbf73245c3a>:12(sum_of_primes_naive)
99999   52.156   0.001    52.156   0.001    <ipython-input-3-ecbf73245c3a>:4(is_prime)
1       0.000    0.000    52.203   52.203   <string>:1(<module>)
1       0.000    0.000    52.203   52.203   {built-in method builtins.exec}
1       0.000    0.000    52.203   52.203   {method 'disable' of '_lsprof.Profiler' objects}
```

## Security testing

## Analyzing code for security vulnerabilities

### Security testing

**Generating security tests**

**Prompt:** You are an expert in web security and in creating API endpoints. With the following code, there are likely many vulnerabilities. Can you create some test cases that test against these vulnerabilities?

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "password": user.password
        })
    return jsonify({"message": "User not found"}), 404
```
