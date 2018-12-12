import dns.resolver

r = dns.resolver.Resolver()
r.timeout = 1
r.lifetime = 1

# AAAA, ip v6 address records
# A, address mapping records
# CNAME, Canonical Name Records
# HINFO, Host Information Records
# ISDN, Integrated Services Digital Network Records
# MX, Mail Exchanger Record
# NS, Name Server Records
# PTR, Reverse-lookup Pointer records
# SOA, Start of Authority Records
# TXT, Text Records

answers = r.query('petra.ac.id', 'MX')
for data in answers:
    print(data.to_text())

HOST='petra.ac.id'
for qtype in ['A', 'AAAA', 'CNAME', 'MX', 'NS']:
    answers = dns.resolver.query(HOST, qtype, raise_on_no_answer=False)
    print(answers.rrset)

import dns.reversename
REV = "203.189.120.4"
hrev = dns.reversename.from_address(REV)
domain = dns.resolver.query(hrev, "PTR")[0]
print(domain)
