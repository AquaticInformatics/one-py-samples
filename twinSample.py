from one_py_sdk.clientsdk import ClientSdk

client =ClientSdk(cacheTimeout=50) #Use for Production environment with 50 second in memory cache
client.Authentication.GetToken("userName", "password") # Supply username and password here
client.LoadCurrentUser()
tenantId =client.Authentication.User.tenantId
tenantTwin =client.DigitalTwin.Get(tenantId)#Get a digital twin using its twin ref id
print(tenantTwin)
tenantTwinType =client.DigitalTwin.GetDigitalTwinType(tenantTwin[0].twinTypeId)#get twin type using twin type id
tenantSubtypeId =tenantTwin[0].twinSubTypeId.value
tenantDescendantsSameSubtype =client.DigitalTwin.GetDescendantsBySubType(tenantId, tenantSubtypeId)#get descendents of twin by subtype
allDescendants =client.DigitalTwin.GetDescendants(tenantId) # Use this sparingly, this is not a very performant call because it gets all descendants of the twin reference id that is passed in 
descendantsOfCategory =client.DigitalTwin.GetDescendantsByRefByCategory(tenantId, 1) # gets descedants of a twin that fall into the specified category
twinSubtypes =client.DigitalTwin.GetDigitalTwinSubtypes() # Retrieves all twin subtypes
twinTypes = client.DigitalTwin.GetDigitalTwinTypes() # Retrieves all twin types
