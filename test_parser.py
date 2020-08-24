import parser as ps

def test_parse_data():
    """
    Test for parser
    """
    P = ps.Parser()
    data = P.read_data('./testData/data.txt')
    row_list = P.parse_data(data)
    assert row_list[0] == P.col_names
    for item in row_list[1:-1]:
        assert len(item) == len(P.col_names)
        for sub_id, sub_item in enumerate(item):
            assert len(sub_item) == int(P.offsets[sub_id])
