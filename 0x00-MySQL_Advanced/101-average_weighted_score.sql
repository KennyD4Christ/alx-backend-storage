-- Stored procedure which computes and stores the average weighted score for all students.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;  -- Changed INT to FLOAT to match with the weighted score

    -- Cursor to iterate over each user
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Reset the totals for each user
        SET total_weighted_score = 0;
        SET total_weight = 0;

        -- Calculate the total weighted score for the current user
        SELECT IFNULL(SUM(c.score * p.weight), 0)
        INTO total_weighted_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the total weight for the current user
        SELECT IFNULL(SUM(p.weight), 0)
        INTO total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- If total_weight is 0, set average_score to 0 to avoid division by zero
        IF total_weight = 0 THEN
            UPDATE users
            SET average_score = 0
            WHERE id = user_id;
        ELSE
            -- Update the user's average_score with the computed weighted average
            UPDATE users
            SET average_score = (total_weighted_score / total_weight)
            WHERE id = user_id;
        END IF;

    END LOOP;

    CLOSE user_cursor;
END //

DELIMITER ;
