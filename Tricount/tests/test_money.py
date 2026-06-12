from decimal import Decimal, ROUND_HALF_UP 

def test_add_two_amount(): 
    first_amount = "1456.56"
    second_amount = "4563.49"
    assert(Decimal("6020.05") == add_two_amounts(first_amount, second_amount))

def test_substract_two_amount(): 
    first_amount = "1456.56"
    second_amount = "4563.49"
    assert(Decimal("-3106.93") == substract_two_amount(first_amount, second_amount))

def test_multiply_two_amount(): 
    first_amount = "1456.56"
    second_amount = "4563.49"
    assert(Decimal("6646996.99") == multiply_two_amount(first_amount, second_amount))

def test_divide_two_amount(): 
    first_amount = 1456.56
    second_amount = 4563.49
    assert(Decimal("0.32") == divide_two_amount(first_amount, second_amount))


def add_two_amounts(first_amount, second_amount):
    return Decimal(first_amount) + Decimal(second_amount)

def substract_two_amount(first_amount, second_amount):
    return Decimal(first_amount) - Decimal(second_amount)

def multiply_two_amount(first_amount, second_amount):
    first_amount_bigger = Decimal(first_amount)*100
    second_amount_bigger = Decimal(second_amount) *100
    bigger_multiply = first_amount_bigger * second_amount_bigger
    first_step_to_normal = bigger_multiply / 100
    result_remove_useless_futur_decimal = first_step_to_normal.quantize(Decimal("1"), rounding= ROUND_HALF_UP )
    final_result = result_remove_useless_futur_decimal / 100
    return final_result

def divide_two_amount(first_amount, second_amount): 
    result_divided = Decimal(first_amount) /Decimal(second_amount)
    first_step_to_normal = result_divided*100
    result_remove_useless_futur_decimal = first_step_to_normal.quantize(Decimal("1"), rounding= ROUND_HALF_UP )
    final_result = result_remove_useless_futur_decimal / 100
    return final_result