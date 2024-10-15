# Documentation

## Benefits of good code documentation

* Improves code readability
* Prevents technical debt
* Helps others learn to use your code
* Increases overall code quality

## Principles of good documentation writing

* Be clear and concise
* Avoid redundancy
* Think of your audience
* Follow language-specific conventions
* Keep documentation up to date

## Documentation comments

* Special comments to explain purpose and usage of code
* More detailed than inline comments
* Used to generate automated documentation

## Docstrings

1. **Google style**:

   ```python
   def add(a, b):
       """
       Add two numbers and return the result.

       Parameters:
       a (int, float): The first number.
       b (int, float): The second number.

       Returns:
       int, float: The sum of the two numbers.
       """
       return a + b
   ```

2. **NumPy/SciPy style**:

   ```python
   def add(a, b):
       """
       Add two numbers and return the result.

       Parameters
       ----------
       a : int or float
           The first number.
       b : int or float
           The second number.

       Returns
       -------
       int or float
           The sum of the two numbers.
       """
       return a + b
   ```

3. **reStructuredText (ReST) style**:

   ```python
   def add(a, b):
       """
       Add two numbers and return the result.

       :param a: The first number.
       :type a: int or float
       :param b: The second number.
       :type b: int or float
       :return: The sum of the two numbers.
       :rtype: int or float
       """
       return a + b
   ```

## Automated documentation tools

* [Sphinx](https://www.sphinx-doc.org/en/master/)
* [JSDoc](https://jsdoc.app/) (for Java)
