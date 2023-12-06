from unit_testing_sample_code import string_capitalizer, capitalize_list, integer_manipulator, manipulate_list

def test_string_capitalizer():
    # Test for String Capitalizer
    assert string_capitalizer("two") == "TwO"
    assert string_capitalizer("c") == "C"
    assert string_capitalizer(str(4)) == "FouR"  # Converting 4 to string
    assert string_capitalizer("") == ""

def test_capitalize_list():
    # Test for List Capitalizer
    assert capitalize_list(["two", "c", str(4), ""]) == ["TwO", "C", "FouR", ""]

def test_integer_manipulator():
    # Test for Integer Manipulator
    assert integer_manipulator(10) == 66
    assert integer_manipulator(2) == 2
    assert integer_manipulator(3) == 6
    assert integer_manipulator(0) == 0
    assert integer_manipulator("three") == 1

def test_manipulate_list():
    # Test for Manipulate List
    assert manipulate_list([10, 2, 3, 0, "three"]) == [66, 2, 6, 0, 1]
