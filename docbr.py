import re

def _clean(value):
    if not value:
        return ""
    return re.sub(r'\D', '', str(value))

def validate_cpf(cpf: str) -> bool:
    cpf = _clean(cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    
    # 1st digit
    s = sum(int(cpf[i]) * (10 - i) for i in range(9))
    d1 = 11 - (s % 11)
    d1 = 0 if d1 >= 10 else d1
    if int(cpf[9]) != d1:
        return False
    
    # 2nd digit
    s = sum(int(cpf[i]) * (11 - i) for i in range(10))
    d2 = 11 - (s % 11)
    d2 = 0 if d2 >= 10 else d2
    return int(cpf[10]) == d2

def validate_cnpj(cnpj: str) -> bool:
    cnpj = _clean(cnpj)
    if len(cnpj) != 14:
        return False
    if cnpj == cnpj[0] * 14:
        return False
    
    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    s = sum(int(cnpj[i]) * weights1[i] for i in range(12))
    d1 = 11 - (s % 11)
    d1 = 0 if d1 >= 10 else d1
    if int(cnpj[12]) != d1:
        return False
    
    weights2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    s = sum(int(cnpj[i]) * weights2[i] for i in range(13))
    d2 = 11 - (s % 11)
    d2 = 0 if d2 >= 10 else d2
    return int(cnpj[13]) == d2

def validate(value: str, doctype: str = 'cnpj', lazy: bool = False) -> bool:
    doc = _clean(value)
    doctype = doctype.lower()
    if doctype == 'cnpj':
        return validate_cnpj(doc)
    elif doctype == 'cpf':
        return validate_cpf(doc)
    return False
