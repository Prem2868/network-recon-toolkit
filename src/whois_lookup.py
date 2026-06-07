import whois

def get_whois(domain):
    return whois.whois(domain)