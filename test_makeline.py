#Testing the makeline function

def test_linemaker():
    from makeline import linemaker
    p_one = (0, 0)
    p_two = (8, 4)
    xval = 4.5
    expected = 2.25
    answer = linemaker(p_one, p_two, xval)
    assert answer==expected
