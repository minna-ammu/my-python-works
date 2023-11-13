rates={  
    "USD": 1,
    "AED": 3.6725,
    "AFN": 86.0330,
    "ALL": 97.5499,
    "AMD": 386.9256,
    "ANG": 1.7900,
    "AOA": 824.0658,
    "ARS": 254.7465,
    "AUD": 1.5099,
    "AWG": 1.7900,
    "AZN": 1.6979,
    "BAM": 1.7974,
    "INR": 82.0914}

amnt=int(input("enter amount you need to exchange : "))
frm_crncy_cd=input("enter source code currenccy :")
to_crncy_cd=input("enter the destination currency code :")

# equation= (amount/from currency code rate)*to currency code rate

from_crncy_cd_rate=rates.get(frm_crncy_cd)
to_crncy_cd_rate=rates.get(to_crncy_cd)
rslt=(amnt/from_crncy_cd_rate)*to_crncy_cd_rate
print(rslt)
