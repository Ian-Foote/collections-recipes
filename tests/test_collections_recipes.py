import pickle
from collections import Counter, OrderedDict

from hypothesis import given
from hypothesis.strategies import binary, booleans, integers, lists, one_of, text

from collections_recipes import OrderedCounter


hashable = one_of(binary(), booleans(), integers(), text())


def in_order(elements):
    seen = set()
    for element in elements:
        if element not in seen:
            seen.add(element)
            yield element


class TestOrderedCounter:
    @given(lists(hashable))
    def test_order(self, elements):
        ordered_counter = OrderedCounter(elements)

        assert tuple(ordered_counter.keys()) == tuple(in_order(elements))

    @given(lists(hashable))
    def test_counter(self, elements):
        counter = Counter(elements)
        ordered_counter = OrderedCounter(elements)

        assert dict(ordered_counter) == dict(counter)

    @given(lists(hashable))
    def test_repr(self, elements):
        ordered_counter = OrderedCounter(elements)

        ordered_repr = repr(OrderedDict(ordered_counter))
        assert repr(ordered_counter) == "OrderedCounter({})".format(ordered_repr)

    @given(lists(hashable))
    def test_pickle(self, elements):
        ordered_counter = OrderedCounter(elements)

        pickled_counter = pickle.dumps(ordered_counter)

        assert pickle.loads(pickled_counter) == ordered_counter
