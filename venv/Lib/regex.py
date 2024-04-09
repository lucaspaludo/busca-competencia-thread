import re

def regexCNPJ():
    return re.compile(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b|\b\d{2}\.\d{3}\.\d{3}/\d{4}\s-\d{2}\b')

def regexAno():
    return re.compile(r'\b\d{4}\b')

def regexAnoEJaneiro():
    return re.compile(r'01\s*/\s*2023|01\s*a\s*31/01/2023|JANEIRO\s*/\s*2023|31\s*/\s*01\s*/\s*2023|JANEIRO|JAN\s*2023|JANEIRO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEFevereiro():
    return re.compile(r'02\s*/\s*2023|01\s*a\s*28/02/2023|FEVEREIRO\s*/\s*2023|28\s*/\s*02\s*/\s*2023|FEVEREIRO|FEV\s*2023|FEVEREIRO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEMarco():
    return re.compile(r'03\s*/\s*2023|01\s*a\s*31/03/2023|MARÇO\s*/\s*2023|31\s*/\s*03\s*/\s*2023|MARÇO|MAR\s*2023|MARÇO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEAbril():
    return re.compile(r'04\s*/\s*2023|01\s*a\s*30/04/2023|ABRIL\s*/\s*2023|30\s*/\s*04\s*/\s*2023|ABRIL|ABR\s*2023|ABRIL\s*DE\s*2023', re.IGNORECASE)

def regexAnoEMaio():
    return re.compile(r'05\s*/\s*2023|01\s*a\s*31/05/2023|MAIO\s*/\s*2023|31\s*/\s*05\s*/\s*2023|MAIO|MAI\s*2023|MAIO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEJunho():
    return re.compile(r'06\s*/\s*2023|01\s*a\s*30/06/2023|JUN\s*/\s*2023|30\s*/\s*06\s*/\s*2023|JUNHO|JUN\s*2023|JUNHO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEJulho():
    return re.compile(r'07\s*/\s*2023|01\s*a\s*31/07/2023|JULHO\s*/\s*2023|31\s*/\s*07\s*/\s*2023|JULHO|JUL\s*2023|JULHO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEAgosto():
    return re.compile(r'08\s*/\s*2023|01\s*a\s*31/08/2023|AGOSTO\s*/\s*2023|31\s*/\s*08\s*/\s*2023|AGOSTO|AGO\s*2023|AGOSTO\s*DE\s*2023', re.IGNORECASE)

def regexAnoESetembro():
    return re.compile(r'09\s*/\s*2023|01\s*a\s*30/09/2023|SETEMBRO\s*/\s*2023|30\s*/\s*09\s*/\s*2023|SETEMBRO|SET\s*2023|SETEMBRO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEOutubro():
    return re.compile(r'10\s*/\s*2023|01\s*a\s*31/10/2023|OUTUBRO\s*/\s*2023|31\s*/\s*10\s*/\s*2023|OUTUBRO|OUT\s*2023|OUTUBRO\s*DE\s*2023', re.IGNORECASE)
            
def regexAnoENovembro():
    return re.compile(r'11\s*/\s*2023|01\s*a\s*30/11/2023|NOVEMBRO\s*/\s*2023|30\s*/\s*11\s*/\s*2023|NOVEMBRO|NOV\s*2023|NOVEMBRO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEDezembro():
    return re.compile(r'12\s*/\s*2023|01\s*a\s*31/12/2023|DEZEMBRO\s*/\s*2023|31\s*/\s*12\s*/\s*2023|DEZEMBRO|DEZ\s*2023|DEZEMBRO\s*DE\s*2023', re.IGNORECASE)
