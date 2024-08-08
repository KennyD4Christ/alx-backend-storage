-- Task: Create an index on the first letter of the 'name' column and the 'score' column in the 'names' table.

-- Import the table dump if not already done:
-- Execute: cat names.sql | mysql -uroot -p holberton

-- Create an index on the first letter of 'name' and the 'score' column
CREATE INDEX idx_name_first_score ON names (name(1), score);
