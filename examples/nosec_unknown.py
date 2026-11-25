def f(x):
    assert x  # nosec B999
    assert x  # nosec not_a_real_test
    assert x  # nosec B101
    assert x  # nosec B101, B999
    assert x
