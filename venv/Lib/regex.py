import re

def regexCNPJ():
    return re.compile(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b|\b\d{2}\.\d{3}\.\d{3}/\d{4}\s-\d{2}\b')

def regexAno():
    return re.compile(r'\b\d{4}\b')

def regexAnoEOutubro():
    return re.compile(r'10\s*/\s*2023|01\s*a\s*31/10/2023|OUTUBRO\s*/\s*2023|31\s*/\s*10\s*/\s*2023|OUTUBRO|OUT\s*2023|OUTUBRO\s*DE\s*2023', re.IGNORECASE)
            
def regexAnoEAgosto():
    return re.compile(r'08\s*/\s*2023|01\s*a\s*30/08/2023|AGOSTO\s*/\s*2023|30\s*/\s*08\s*/\s*2023|AGOSTO|AGO\s*2023|AGOSTO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEJulho():
    return re.compile(r'07\s*/\s*2023|01\s*a\s*31/07/2023|JULHO\s*/\s*2023|31\s*/\s*07\s*/\s*2023|JULHO|JUL\s*2023|JULHO\s*DE\s*2023', re.IGNORECASE)

def regexAnoENovembro():
    return re.compile(r'11\s*/\s*2023|01\s*a\s*30/11/2023|NOVEMBRO\s*/\s*2023|31\s*/\s*11\s*/\s*2023|NOVEMBRO|NOV\s*2023|NOVEMBRO\s*DE\s*2023', re.IGNORECASE)

def regexAnoEMarco():
    return re.compile(r'03\s*/\s*2023|03\s*a\s*31/11/2023|MARÇO\s*/\s*2023|31\s*/\s*03\s*/\s*2023|MARÇO|MARÇO\s*2023|MARÇO\s*DE\s*2023', re.IGNORECASE)



