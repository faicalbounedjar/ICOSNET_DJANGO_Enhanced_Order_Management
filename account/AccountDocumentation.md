# Serializers
# SignUp Serializer
The SignUpSerializer serializes user data for the registration process.

- Attributes:
    first_name (String, required).
    last_name (String, required).
    email (String, required).
    password (String, required).
- Validators:
    first_name: Required, cannot be blank.
    last_name: Required, cannot be blank.
    email: Required, cannot be blank.
    password: Required, cannot be blank, minimum length of 8 characters.

# User Serializer
The UserSerializer serializes user data for API responses.

- Attributes:
first_name
last_name
email
 

# register
Endpoint: /register/
Method: POST
Authentication: NOT Required 
Response:
    - Success: HTTP 200 OK
    - Error: HTTP 400 BAD REQUEST
# userinfo
Endpoint: /userinfo/
Method: GET
Authentication: Required (Bearer token)
Response:
    - Success: HTTP 200 OK
    - Error: HTTP 400 BAD REQUEST
# userinfo/update
Endpoint: /userinfo/update/
Method: PUT
Authentication: Required (Bearer token) 
Response:
    - Success: HTTP 200 OK
    - Error: HTTP 400 BAD REQUEST