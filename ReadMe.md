**** IMPORTANT *****
you will need to enter the info in the config file.

In the Psycopg assignment you created the endpoints to CRUD the four tables and their relationships in our inventory database. For this assignment, you will refactor the SQL queries and use SQLAlchemy and Flask_SQLAlchemy to be done through using objects.

By the end of this assignment, your application should have each API endpoint utilizing SQLAlchemy objects to execute each of the PSQL queries created in the assignment PSQL CRUD. This means your code should have flask endpoints that can create, read, update and delete a record in the companies, categories, products, and productscategoriesxref tables of your database. Make sure to return whatever values were affected in a json message in the server response.

You will notice some routes are used for several CRUD actions. Conditional statements should be used to determine which method has been sent (and which action should take place).


Files and Folder Structure
Your application should include the following files:
models folder with each table created in its own file (for example, the products.py file holds the fields for the Products table)
app.py
db.py that holds the creation of our tables if they do not exist
.gitignore that ignores the .pipfile.lock file
.env (though this is not web standard, this will allow the reviewer to quickly create and access the database)
pipfile file ONLY. This will allow the reviewer to grade your assignment quickly. (add pipfile.lock to the .gitignore file)
As a refresher, CRUD stands for:

CREATE (each route uses the POST request method)
/company route to create a new company
/category route to create a new category
/product route to create a new product
/warranty route to create a new warranty
/product/category route to create a new association between a product and category
READ (each route uses the GET request method)
/companies route to return all the companies in our companies table
/categories route to return all the categories in our categories table
/products route to return all the products in our products table (include the single warranty in the warranies table and all categories in the xref table that are connected)
/products/active route to return all products that have the active field set to the boolean true
/company/<id> route to read one company based on the company_id provided
/category/<id> route to read one category based on the category_id provided
/product/<id> route to read one product based on the product_id provided (including the associated categories)
/warranty/<id> route to read one warranty based on the warranty_id provided
/product/company/<id> route to return all products with the provided company_id
UPDATE (each route uses the PUT request method)
/company/<id> route to update one or more fields in one company record
/category/<id> route to update one or more fields in one category record
/product/<id> route to update one or more fields in one product record
/warranty/<id> route to update one or more fields in one warranty record
DELETE
/company/delete route that uses the DELETE request method to remove a record from the companies table (make sure all associated records in the products table and each associated records in the xref are also deleted)
/product/delete route that uses the DELETE request method to remove a record from the products table (make sure the warranty record and all associated records in the xref table are also deleted)
/category/delete route that uses the DELETE request method to remove a record from the categories table (make sure all associated records in the xref table are also deleted)
/warranty/deleteroute that uses the DELETE request method to remove a record from the warranties table (make sure the association to its product is also deleted)