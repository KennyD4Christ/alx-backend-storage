-- This trigger resets the valid_email attribute to 0 if the email has been changed.

DELIMITER //

CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has been changed
    IF OLD.email <> NEW.email THEN
        -- Reset valid_email to 0 if email has been changed
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;
