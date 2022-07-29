from datetime import datetime, timedelta, timezone
from one_py_sdk.clientsdk import ClientSdk
from one_py_sdk.shared.constants import Environment 

client =ClientSdk() #Use for production environment with no cache
#client =ClientSdk(Environment.get('feature'), 50) #Use for feature environment with 50 second in memory cache of API requests
#client =ClientSdk(Environment.get('integration')) #Use for integration environment no cache
#client =ClientSdk(Environment.get('stage')) #Use for stage environment no cache
#client =ClientSdk(cacheTimeout=30) Use for production with 30 second in memory cache of requests

if (client.Authentication.GetToken("userName", "password")):  # Supply username and password here
    print("Authenticated successfully")
else:
    print("Authentication failed")
print(client.Authentication.UserName)
print(client.Authentication.Token)
client.LoadCurrentUser() #Loads full user object with email, username, first name, last name, id, tenants, tenantId, user status, password expiration, and record audit info.
print(client.Authentication.User)
client.Authentication.LoginResourceOwner("userName", "password") #Same as get token but returns true or false rather than a string value containing token
client.Authentication.Logout() #Logs user out
