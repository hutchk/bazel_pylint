# Python rules from Bazel.
git_repository(
    name = "io_bazel_rules_python",
    commit = "49a434b1d920f9960d207d79ff7641ad75c0a04f",
    remote = "https://github.com/bazelbuild/rules_python.git",
)

# Utility for creating self-contained python executables.
git_repository(
    name = "subpar",
    remote = "https://github.com/google/subpar",
    tag = "1.0.0",
)

# Load Python rules.
load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")

pip_repositories()

pip_import(
    name = "pips",
    requirements = "//python:requirements.txt",
)

load("@pips//:requirements.bzl", "pip_install")

pip_install()
