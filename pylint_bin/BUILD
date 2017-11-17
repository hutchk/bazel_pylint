load("@subpar//:subpar.bzl", "par_binary")
load("@pips//:requirements.bzl", "requirement")

py_binary(
    name = "pylint_bin",
    srcs = ["pylint_bin.py"],
    deps = [
        requirement("astroid"),
        requirement("backports.functools-lru-cache"),
        requirement("certifi"),
        requirement("configparser"),
        requirement("enum34"),
        requirement("future"),
        requirement("isort"),
        requirement("lazy-object-proxy"),
        requirement("mccabe"),
        requirement("pylint"),
        requirement("singledispatch"),
        requirement("six"),
        requirement("textblob"),
        requirement("wrapt"),
    ],
)

par_binary(
    name = "pylint",
    srcs = ["pylint_bin.py"],
    deps = [":pylint_bin"],
)
