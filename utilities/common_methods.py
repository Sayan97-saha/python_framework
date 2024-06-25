def hard_assert(variable_val, expected_val):
    try:
        assert variable_val == expected_val, 'yay'
    except:
        assert 1, 'nay'