# Generate the code for new endpoints

This script allows you to generate new endpoints for the WebexPythonSDK. Before we go into the 
usage let's quickly describe what exactly we are generating here. 

In order to add a new endpoint to the SDK we need two different classes. 

* The `BasicPropertiesMixin` defines the properties of the endpoint (i.e. the id or the name). In other words this Mixin defines the properties and defines how you read them from the json retrieved by a request.
* The `API` class defines the general functions (think `.get()`, `.list()` etc) for the endpoint.

Both of these classes can be written by hand but it can be easier to generate them from a definition format and this is exactly what this generator does. 





# Q&A

### Why the intermediate format?

There is no swagger doc for the webex APIs publically available (at least to my knowledge - please correct me if I am wrong here). The docs on developer.webex.com are generated from API Blueprint files but these are also not publically available. To keep the project community-driven this intermediate format is introduced. This way we can all create new endpoints without relying on non-public information while cutting down the time needed. 
