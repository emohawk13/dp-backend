Assignment - Flask API CRUD
Create an application that uses the Flask API to CRUD to a list of dictionaries named product_records, provided below:

product_records = [
{
"product_id": "1",
"product_name": "Hasbro Gaming Clue Game",
"description": "One murder... 6 suspects...",
"price": 9.95,
"active" : True
},
{
"product_id": "2",
"product_name": "Monopoly Board Game The Classic Edition, 2-8 players",
"description" : "Relive the Monopoly experiences...",
"price": 35.50
"active": False
}
]

Files and Folder Structure
As a minimum, your application should include an app.py file that holds the entire application. Additionally, feel free to organize your application further with routes and controllers.

Your application should include a pipfile file ONLY. This will allow the reviewer to grade your assignment quickly. (Add pipfile.lock to the .gitignore file).

Routes
Include the following routes and their actions in your application:

CREATE (each route uses a POST request)
/product route to create a new product

READ (each route uses a GET request)
/products route to return all the products in our list of dictionaries
/product/active route to return all products that have the active status set to the boolean True.

/products/<product_id> route to read one product based on the product_id provided

UPDATE (each route uses a PUT request)

/product/<product_id> route to update one or more key-value pairs in one product.

/product/activity/<product_id> route to toggle active status between True and False.

DELETE (each route uses a DELETE request)
/product/delete route to remove a product from our list of dictionaries.
