# Define Python libraries
py_library(
    name = "math_utils_lib",
    srcs = ["//src:math_utils.py"],
    visibility = ["//visibility:public"],
)

py_library(
    name = "string_utils_lib",
    srcs = ["//src:string_utils.py"],
    visibility = ["//visibility:public"],
)


# Define unit tests
py_test(
    name = "test_math_utils",
    srcs = ["//tests:test_math_utils.py"],
    deps = [
        "//src:math_utils_lib",
    ],
)
'''
py_test(
    name = "test_math_utils",
    srcs = ["//tests:test_math_utils.py"],
    deps = [
        "//src:math_utils",
        "@pypi//pytest",  # Ensure pytest is available
    ],
)'''

py_test(
    name = "test_string_utils",
    srcs = ["//tests:test_string_utils.py"],
    deps = [
        "//src:math_utils_lib",
    ],
)


# Linting with pylint
sh_test(
    name = "lint",
    srcs = ["scripts/lint.sh"],
)

# Formatting check
sh_test(
    name = "format",
    srcs = ["scripts/format.sh"],
)