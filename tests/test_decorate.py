import pytest
from typing import List
from project.decorate import Evaluated, Isolated, smart_args, cache_results


from typing import List


def test_smart_args_Evaluated():
    with pytest.raises(ValueError):
        Evaluated(lambda x: x)


def test_smart_args_isol():
    @smart_args
    def check_isolation(*, d=Isolated()):
        d["a"] = 0
        return d

    no_mutable = {"a": 10}

    assert check_isolation(d=no_mutable) == {"a": 0}
    assert no_mutable == {"a": 10}


def test_smart_args_eval():
    count = [0]

    def get_count():
        count[0] += 1
        return count[0]

    @smart_args
    def check_evaluation(*, x=get_count(), y=Evaluated(get_count)):
        return (x, y)

    assert check_evaluation() == (1, 2)
    assert count[0] == 2  # call get_count for x and y
    assert check_evaluation() == (1, 3)
    assert count[0] == 3  # call get_count for y
    assert check_evaluation(y=150) == (1, 150)
    assert count[0] == 3  # don't call get_count


def test_smart_args_isol_positional_argument():
    @smart_args
    def increment(l=Isolated()):
        for el in l:
            el += 1
        return l

    with pytest.raises(AssertionError):
        increment(Isolated())


def test_smart_args_eval_positional_argument():
    @smart_args
    def add(a, b):
        return a + b

    with pytest.raises(AssertionError):
        add(Evaluated(lambda: 1), 4)


def test_smart_args_eval_isol_combination():
    @smart_args
    def add(*, a, b=Evaluated(Isolated)):
        return a + b

    with pytest.raises(ValueError):
        add(a=1)
    with pytest.raises(ValueError):
        add(a=1, b=3)


def test_smart_args_isol_without_argument():
    @smart_args
    def check_isolation(*, d=Isolated()):
        d["a"] = 0
        return d

    with pytest.raises(ValueError):
        check_isolation()


def test_smart_args_eval_isol_together():
    count = [0]

    def get_count():
        count[0] += 1
        return count[0]

    @smart_args
    def check_isol_eval(*, x=Isolated(), y=Evaluated(get_count)):
        x["a"] = 0
        return (x, y)

    no_mutable = {"a": 10}

    assert check_isol_eval(x=no_mutable) == ({"a": 0}, 1)
    assert check_isol_eval(x=no_mutable) == ({"a": 0}, 2)
    assert no_mutable == {"a": 10}


def test_cache():
    @cache_results(2)
    def add(x: int, y: int):
        return x + y

    assert add(3, 6) == 9
    assert add(2, 9) == 11
    assert add(8, 4) == 12


def test_cache_with_count():
    count = [0]

    @cache_results(2)
    def add_with_count(x: int, y: int):
        count[0] += 1
        return x + y

    f = add_with_count
    assert f(1, 2) == 3
    assert count[0] == 1  # calculate

    assert f(3, 4) == 7
    assert count[0] == 2  # calculate

    assert f(1, 2) == 3
    assert count[0] == 2  # take from cache

    assert f(5, 7) == 12
    assert count[0] == 3  # calculate

    assert f(3, 4) == 7
    assert count[0] == 4  # calculate


def test_cache_built_in():
    divmod_cache = cache_results(1)(divmod)

    assert divmod_cache(7, 3) == (2, 1)
    assert divmod_cache(8, 2) == (4, 0)
    assert divmod_cache(8, 2) == (4, 0)


def test_cache_non_hashable():
    count = [0]

    @cache_results(2)
    def addl_with_count(l: List[int]):
        count[0] += 1
        return sum(l)

    f = addl_with_count
    assert f([1, 2]) == 3
    assert count[0] == 1  # calculate

    assert f([6, 3, 1]) == 10
    assert count[0] == 2  # calculate

    assert f([1, 2]) == 3
    assert count[0] == 2  # take from cache

    assert f([2, 8, 4]) == 14
    assert count[0] == 3  # calculate

    assert f([6, 3, 1]) == 10
    assert count[0] == 4  # calculate
