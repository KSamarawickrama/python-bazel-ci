[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sBLwuAYj)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18290937&assignment_repo_type=AssignmentRepo)
# **CSC 7135: Python Build & Test System with Bazel**

**Topic:** Automating Builds, Testing, Linting, and Formatting with **Bazel**  


---

## **Objective**
This assignment will help you practice:
- Writing Python functions and unit tests.
- Using **Bazel** as a build system for Python projects.
- Automating linting and formatting within **Bazel**.

---

## **Task 1: Setting Up Your Project Repository**
1. Create a new **GitHub repository** named `python-bazel-ci`.
2. Clone the repository to your local machine.
3. Inside the repository, create the following directory structure:

    ```
    project-root/
    ├── src/
    │   ├── math_utils.py
    │   ├── string_utils.py
    ├── tests/
    │   ├── test_math_utils.py
    │   ├── test_string_utils.py
    ├── scripts/
    │   ├── lint.sh
    │   ├── format.sh
    ├── requirements.txt
    ├── WORKSPACE
    ├── BUILD
    ├── README.md
    ```

4. **Commit and push** the initial structure.

---

## **Task 2: Implement Python Utility Functions**
1. Implement **math-related functions** in `src/math_utils.py`.
2. Implement **string-related functions** in `src/string_utils.py`.

Each function should have a **docstring** describing its purpose.

---

## **Task 3: Write Unit Tests**
1. Implement unit tests for **math functions** in `tests/test_math_utils.py`.
2. Implement unit tests for **string functions** in `tests/test_string_utils.py`.

Tests should be written using **pytest**.

---

## **Task 4: Configure Bazel Build System**
1. Create a **WORKSPACE** file at the root of your project.
2. Create a **BUILD** file at the root of your project.
3. The `BUILD` file should define:
   - Python **libraries** for the utility functions.
   - Python **test targets** for unit tests.
   - Shell script **targets** for linting and formatting.

---

## **Task 5: Automate Linting & Formatting**
1. In the `scripts/` directory, create:
   - `lint.sh` → Runs **pylint** on all Python files.
   - `format.sh` → Runs **black** to check formatting.
2. Modify the `BUILD` file to include Bazel rules for:
   - Running `lint.sh` as a **Bazel test**.
   - Running `format.sh` as a **Bazel test**.

Make sure the scripts are **executable**.

---

## **Task 6: Run & Validate Your Bazel Setup**
Run the following Bazel commands to validate your setup:

### **Run Unit Tests**
```sh
bazel test //tests:test_math_utils
bazel test //tests:test_string_utils
```

### **Run Linter**
```sh
bazel test //:lint
```

### **Run Formatter**
```sh
bazel test //:format
```

## **Task 7: Setup GitHub Action**

Setup GitHub actions for each of the above tasks (unit tests, linter, and formatter), such that these action execute for each push or pull-request on the `main` branch. 

## **Pointers**

- `src/math_utils.py` 

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

```

- `src/string_utils.py`

```python
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s 

def count_vowels(s):
    return sum(1 for char in s.lower())

```
- `tests/test_math_utils.py`

```python
import pytest
from src.math_utils import add, subtract, multiply, divide


def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
```
- Bazel `BUILD` File
```python
# Define Python libraries
py_library(
    name = "math_utils",
    srcs = ["src/math_utils.py"],
    visibility = ["//visibility:public"],
)

...

# Define unit tests
py_test(
    name = "test_math_utils",
    srcs = ["tests/test_math_utils.py"],
    deps = [
        ":math_utils",
    ],
)

...

# Linting with pylint
sh_test(
    name = "lint",
    srcs = ["scripts/lint.sh"],
)

... 
```
- `scripts/lint.sh`
```sh
#!/bin/bash
set -e

pip install pylint
pylint src/*.py tests/*.py --fail-under=8.0
```

- `scripts/format.sh`

```sh
#!/bin/bash
set -e

pip install black
black --check src/ tests/
```

# Happy Coding! 🚀

  
