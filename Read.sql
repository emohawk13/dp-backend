-- Read all records from companies
SELECT * FROM companies;

-- Read all records from categories
SELECT * FROM categories;

-- Read all records from products
SELECT * FROM products;

-- Read all records from warranty
SELECT * FROM warranties;

-- Read a single warranty by warranty id
SELECT * FROM warranties WHERE warranty_id = 'example-warranty-id';

-- Read a single company by company id
SELECT * FROM companies WHERE company_id = 'example-company-id';

-- Read all products by company
SELECT * FROM products WHERE company_id = 'example-company-id';

-- Read all active products
SELECT * FROM products WHERE active = true;

-- Read a single Category and its relationships
SELECT c.*, p.* 
FROM categories c 
JOIN productscategoriesxref x ON c.category_id = x.category_id
JOIN products p ON x.product_id = p.product_id
WHERE c.category_id = 'example-category-id';

-- Read a single product and its relationships
SELECT p.*, w.*, c.* 
FROM products p
LEFT JOIN warranties w ON p.product_id = w.product_id
LEFT JOIN productscategoriesxref x ON p.product_id = x.product_id
LEFT JOIN categories c ON x.category_id = c.category_id
WHERE p.product_id = 'example-product-id';

