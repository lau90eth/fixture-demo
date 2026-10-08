from app import parse

def test_parse_fixture():
    with open("fixtures/parser.txt") as f:
        assert "hello" in parse(f.read())
