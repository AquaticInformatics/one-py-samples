from one_py_sdk.clientsdk import ClientSdk
from one_py_sdk.shared.constants import Environment 

client =ClientSdk(cacheTimeout=50)#creates client targeting production with 50 second in memory cache for REST requests 
client.Authentication.GetToken("userName", "password")
units =client.Library.GetUnits()
i18n=client.Library.Geti18nKeys("AQI_FOUNDATION_LIBRARY")
quantityTypes =client.Library.GetQuantityTypes()
parameters =client.Library.GetParameters()
print(units, i18n, quantityTypes, parameters)
