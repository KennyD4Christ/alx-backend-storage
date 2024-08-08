-- Task: Create a function SafeDiv that divides the first number by the second number, or returns 0 if the second number is 0.

DELIMITER //

-- Creating the SafeDiv function
CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    -- Check if b is 0; if so, return 0; otherwise, return a / b
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //

DELIMITER ;
