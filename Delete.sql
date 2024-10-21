-- delete a product and all relations
DELETE FROM products
WHERE product_id = 'Enter Product ID Here';

DELETE FROM warranties
WHERE product_id = 'Enter Product ID Here';

DELETE FROM productscategoriesxref
WHERE product_id = 'Enter Product ID Here';

-- delete a category and all relations
DELETE FROM categories
WHERE category_id = 'Enter Category ID here';

DELETE FROM productscategoriesxref
WHERE category_id = 'Enter Category ID here';

-- to remove every record related to a company
DELETE FROM companies
WHERE company_id = 'Enter company name here';

DELETE FROM products
WHERE company_id = 'Enter company name here';

DELETE FROM productscategoriesxref
WHERE product_id IN (SELECT product_id FROM products WHERE company_id = 'Enter company name here');

-- delete by warranty id 
DELETE FROM warranties
WHERE warranty_id = 'warranty id';
