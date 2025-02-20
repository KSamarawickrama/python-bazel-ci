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
