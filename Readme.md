Assignment - PSQL CRUD
Completion requirements
Due: Tuesday, September 24, 2024, 1:00 PM
For this assignment, you will create CRUD SQL statements for the Products, and Categories tables and their relationships. Save these relationships in a file. Make sure all queries do the intended action by testing them in PSQL.

Products
PK
product_id
UUID4
FK
company_id
UUID4
U, NN
company_name
VARCHAR
price
INTEGER
description
VARCHAR
D=t
active
BOOLEAN

Companies
PK
company_id
UUID4
U, NN
company_name
VARCHAR

ProductsCategoriesXref
FK
product_id
UUID4
FK
category_id
UUID4

Categories
PK
category_id
UUID4
U, NN
category_name
VARCHAR

Warranties
PK
warranty_id
UUID4
FK
product_id
UUID4
NN
warranty_months
VARCHAR
As a refresher, CRUD stands for:

CREATE:
a single record in the companies table
a single record in the categories table
a single record in the products table
a single record in the warranties table
a single record in the products_categories table

READ:
all records in the companies table
all records in the categories table
all records in the products table
all records in the warranties table
all active products
all products with a particular company_id
a single company record by id
a single category record by id (and all its associated products)
a single product record by id (and its single associated warranty and its associated categories)
a single warranty record by id

UPDATE:
one or more fields in a record from the companies table
one or more fields in a record from the categories table
one or more fields in a record from the products table
one or more fields in a record from the warranties table
one or more fields in a record from the productscategoriesxref table

DELETE:
delete a record in the products table based on their id (make sure all associated records in the warranty table and xref table are also deleted)
delete a record in the categories table based on their id (make sure all associated records in the xref table are also deleted)
delete a record in the companies table based on their id (make sure all associated records in the products table, and the associated records in the xref table, are also deleted)
delete a record in the warranties table based on their id (make sure the associated id in the products table is also deleted)

to run this project:
pipenv install
pipeenv install --dev
pipenv run start
