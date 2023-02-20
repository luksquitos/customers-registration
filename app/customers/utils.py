r"""
File that contains util logic
for other files.
"""


def is_cpf_valid(cpf: str):
    """
    Function to check if a CPF is
    valid or not.
    Returns True if it is.
    CPF must be a string.
    """    
    
    if isinstance(cpf, int):
        cpf = str(cpf)
    
    cpf_only_numbers = cpf.replace('.', '').replace('-', '')
    cpf_multiplier_digits = cpf_only_numbers[:9]
    
    if not cpf_only_numbers.isnumeric():
        return False
    
    
    def get_sum(start: int, cpf: str):
        """
        Function that multiple the numbers 
        of the cpf with the current 'start' 
        and returns the sum.
        """
        sum_ = 0
        multiplier = start
        
        for number in cpf:
            sum_ += int(number) * multiplier
            multiplier -= 1
        
        return sum_
    
    
    # Calculus of first digit
    
    rest_first_division = get_sum(10, cpf_multiplier_digits) % 11
    
    if rest_first_division < 2:
        cpf_multiplier_digits += '0'
    else: 
        cpf_multiplier_digits += str(11 - rest_first_division)
    
    # Calculus of second digit
    
    rest_second_division = get_sum(11, cpf_multiplier_digits) % 11
    
    if rest_second_division < 2:
        cpf_multiplier_digits += '0'
    else:
        cpf_multiplier_digits += str(11 - rest_second_division)
        
    # Is cpf valid ?
    
    if cpf_multiplier_digits == cpf_only_numbers:
        return True
    else:
        return False
