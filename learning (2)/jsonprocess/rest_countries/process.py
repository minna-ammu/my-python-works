from json import load
with open ("",encoding="UTF-8" ) as f :
    dta=load(f)
# print(len(dta))                                 # etra countries nte information unden ariyan


# all_country=[c.get("name")  for c in dta ]      #  all country name
# print(all_country)

# regions={r.get("region")for r in dta}                   #  all regions
# print(regions)


# asian_countries=[a.get("name")  for a in dta    if a.get("region")=="Asia"] # asian countries
# print(asian_countries)

# poltn_afgn=[p.get("population")    for p in dta    if p.get("name")=="Afganistan"]  # population of afganistan
# print(poltn_afgn)

# idn_brds=[ b.get("name")   for b in dta     if b.get("name")=="India"  ][0]    # ithil short name an kittuka. full name kittan 
# print(idn_brds)
# idn_brd_name=[ b.get("name")    for b in dta      if b.get("alpha3Code") in idn_brds]
# print(idn_brd_name)

crncy_cd_ind=[c.get("")     for c in dta       if c.get("name")=="India"]