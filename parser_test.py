from .parser import parse


def test_parser():
    assert parse("abc") == ["abc"]
    assert parse("") == []
    assert parse("(abc) def") == [["abc"], "def"]
    assert parse("(abc (def ghi) jjj bbb) ccc"
                 ) == [["abc", ["def", "ghi"], "jjj", "bbb"], "ccc"]
