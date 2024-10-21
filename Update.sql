-- Update Company 
UPDATE companies
SET company_name = 'Updated Company Name'
WHERE company_id = 'example-company-id';

-- Update Category
UPDATE categories
SET category_name = 'Updated Category Name'
WHERE category_id = 'example-category-id';

-- Update Product
UPDATE products
SET price = 150, description = 'Updated product description'
WHERE product_id = 'example-product-id';

-- Update Warranty
UPDATE warranties
SET warranty_months = '24'
WHERE warranty_id = 'example-warranty-id';

-- Update relationship between categories and products
UPDATE productscategoriesxref
SET category_id = 'new-category-id'
WHERE product_id = 'example-product-id';
