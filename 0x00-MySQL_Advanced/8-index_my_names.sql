-- Task: Create an index on the first letter of the 'name' column in the 'names' table.

-- Import the table dump if not already done:
-- Execute: cat names.sql | mysql -uroot -p holberton

-- Create an index on the first letter of 'name' column
CREATE INDEX idx_name_first ON names (name(1));
