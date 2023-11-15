# Order Model

Attributes:
id (Auto-incremented)
title (String)(unique).
name (String).
description (Text).
price (Decimal).
createdAt (DateTime).
status (String): "Pending," "Processing," "Shipped," or "Delivered."
user (Foreign Key).
timestamp (DateTime).
Status Choices
The Status enumeration provides predefined choices for the status field in the Order model.


# Create a New Order
Endpoint: /new
Method: POST
Authentication: Required (Bearer Token)
Response:
    - Success: HTTP 201 Created
    - Error: HTTP 400 Bad Request
        {'Err': 'Order with the same title alredy exists .'}

# Get All Orders
Endpoint: /orders/
Method: GET
Authentication: NOT Required
- you can specify the pages i set the number of ellements to 2 items per page 
Response:
    - Success: HTTP 200 OK
    
# Get Order by ID
Endpoint: /orders/<int:pk>/
Method: GET
Authentication: NOT Required 
Parameters:
    - id 
Response:
    - Success: HTTP 200 OK
    - Error: HTTP 404 Not Found
    
# Update Order
Endpoint: /orders/<int:pk>/update/
Method: PUT
Authentication: Required (Bearer Token)
Response:
    - Success: HTTP 200 OK
    - Error: HTTP 400 Bad Request
    
# Delete Order
Endpoint: /orders/<int:pk>/delete/
Method: DELETE
Authentication: Required (Bearer Token)
Response:
    - Success: HTTP 200 OK
    - Error: HTTP 400 Bad Request
    
#  Get Order by Title
Endpoint: /search/
Method: GET
Authentication: NOT Required 
Parameters:
    - title 
Response:
    - Success: HTTP 200 OK
    
# Get Orders by Title Query
Endpoint: /search/<str:pk>
Method: GET
Authentication: NOT Required 
Response:
    - Success: HTTP 200 OK
    