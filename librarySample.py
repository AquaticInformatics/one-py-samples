from one_py_sdk.clientsdk import ClientSdk

client =ClientSdk(cacheTimeout=50)#creates client targeting production with 50 second in memory cache for REST requests 
client.Authentication.GetToken("userName", "password")
units =client.Library.GetUnits()#Gets all units
i18n=client.Library.Geti18nKeys("AQI_FOUNDATION_LIBRARY", "en") #gets I18N information for particular module for particular language
quantityTypes =client.Library.GetQuantityTypes() #Gets all quantity types
parameters =client.Library.GetParameters() #gets all parameters

print(units, i18n, quantityTypes, parameters)
