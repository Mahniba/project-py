currencies ={
    "USD" : 1.0,
    "EUR" : 0.85,
    "GBP" : 0.73,
    "JPY" : 110.0,
    "AUD" : 403.81,
    "HKD" : 76.22,
    "CZK" : 27.98,
    "CHF" : 670.19,
    "DKK" : 88.02,
    "BRL" : 119.47,
    "CNY" : 86.36,
    "BHD" : 1585.34,
    "ARS" : 2.62,
    "INR" : 7.28,
    "HUF" : 1.76,
    "BGN" : 334.77,
    "EGP" : 19.34,
    "GIP" : 1.26,
    "BAM" : 0.0030,
    "CLP" : 0.75,
    "IDR" : 0.041,
    "BBD" : 0.0
}
source_currency = input("enter the currency to be converted:")
destination_currency = input("enter the currency you want to convert to:")
if (source_currency and destination_currency)in currencies :
   amount = float(input("enter the amount to be converted :"))
   converted_currency = amount*currencies[destination_currency]/currencies[source_currency]
   print(converted_currency)