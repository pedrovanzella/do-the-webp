from do_the_webp.traverser import traverse


def test_traverse_tree():
    assert set(traverse('samples/tree')) == set([
        ('samples/tree/a', '0'),
        ('samples/tree/a', '4'),
        ('samples/tree/b/ba', '1'),
        ('samples/tree/b/ba', '5'),
        ('samples/tree/b/bb', '2'),
        ('samples/tree/b/bb/bba', '6'),
        ('samples/tree/c', '3'),
    ]), "Traverses a tree properly"
