# Overview
This project is a Django REST API that consists of two applications: account and order. The account app handles user authentication, registration, and profile information, while the order app manages the creation, retrieval, update, and deletion of orders.

# Applications
## Account Application
### Serializers

SignUp Serializer:
Serializes user data for registration.
- Fields: first_name, last_name, email, password.
- Validators: Required, cannot be blank, minimum password length.

User Serializer:
- Serializes user data for API responses.
- Fields: first_name, last_name, email.
Views
Register User:

### Endpoints
- Endpoint: /register/
Method: POST
- Endpoint: /userinfo/
Method: GET
- Endpoint: /userinfo/update/
Method: PUT

### URLs
/register/: Register a new user.
/userinfo/: Get current user information.
/userinfo/update/: Update current user information.

view more details in the Account Documentation
## Order Application
### Models
- Order Model:
Attributes: id, title (unique), name, description, price, createdAt, status, user (Foreign Key), timestamp.
Status Choices: "Pending," "Processing," "Shipped," or "Delivered."

### Serializers
Order Serializer:
Serializes order data for API responses.
Fields: All model fields.

### Endpoints
Endpoint: /new/
Method: POST

Endpoint: /orders/
Method: GET

Endpoint: /orders/<int:pk>/
Method: GET

Endpoint: /orders/<int:pk>/update/
Method: PUT

Endpoint: /orders/<int:pk>/delete/
Method: DELETE

Endpoint: /search/
Method: GET

Endpoint: /search/<str:pk>/
Method: GET

### URLS 
/new/: Create a new order.
/orders/: Get all orders.
/orders/<int:pk>/: Get order by ID.
/orders/<int:pk>/update/: Update order.
/orders/<int:pk>/delete/: Delete order.
/search/: Get order by title.
/search/<str:pk>/: Get orders by title query.

### API Pagination
To retrieve paginated results, use the page parameter (e.g., /orders/?page=2). Each page contains 2 elements.

