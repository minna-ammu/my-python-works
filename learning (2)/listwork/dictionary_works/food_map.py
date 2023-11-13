items=[{"name":"biriyani","price":130,"category":"non veg"},
       {"name":"puttu kadala","price":60,"category":"veg"},
       {"name":"fried rice","price":14,"category":"non veg"},
       {"name":" mutton biriyani","price":190,"category":"non veg"},
       {"name":"burger","price":90,"category":"veg"}]

# item_names=list(map(lambda m:m.get("name"),items))    # all names using map
# print(item_names)

# item_names=[ i.get("name") for i in items]                   # all items names  using list comprehension
# print(item_names)


# price_items=list(map(lambda p:p.get("price"),items))     # price using map
# print(price_items)

# price_items=[p.get("price")  for p in items ]                  #  price using list comprehension
# print(price_items)

# filter_veg=list(filter(lambda v:v.get("category")=="veg",items)) # veg using filter
# print(filter_veg)

filter_veg=[v.get("name")      for v in items   if v.get("category")=="veg"]  # veg using list comprehension
print(filter_veg)