
-- inserts sample companies into the companies table
INSERT INTO companies (company_id, company_name) 
VALUES (gen_random_uuid(), 'Tech Innovators Inc.'),(gen_random_uuid(), 'Green Energy Solutions'),(gen_random_uuid(), 'Global Manufacturing Ltd.');

-- inserts sample data into categories 
INSERT INTO categories (category_id, category_name) 
VALUES (gen_random_uuid(), 'Electronics'),(gen_random_uuid(), 'Renewable Energy'),(gen_random_uuid(), 'Industrial Equipment');

-- insert sample data into products 
INSERT INTO products (product_id, company_id, company_name, price, description, active) 
VALUES (gen_random_uuid(), 'id-1', 'Tech Innovators Inc.', 500, 'Laptop', true),(gen_random_uuid(), 'id-2', 'Green Energy Solutions', 300, 'Solar panels', true),(gen_random_uuid(), 'id-3', 'Global Manufacturing Ltd.', 1000, 'Industrial machinery', false);

-- insert sample data into warranties 
--this also creates a random uuid to act as an warranty id
INSERT INTO warranties (warranty_id, product_id, warranty_months) 
VALUES (gen_random_uuid(), 'id-1', '24'),(gen_random_uuid(), 'id-2', '36'),(gen_random_uuid(), 'id-3', '12');

--insert sample data into products_categories_xref 
INSERT INTO productscategoriesxref (product_id, category_id) 
VALUES ('id-1', 'id-1'), ('id-2', 'id-2'), ('id-3', 'id-3'); 
