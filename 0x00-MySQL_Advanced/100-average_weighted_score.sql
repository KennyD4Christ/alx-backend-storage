-- Create a stored procedure ComputeAverageWeightedScoreForUser that calculates
-- the average weighted score for a user based on their corrections and stores it in users.average_score.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;

    -- Calculate the total weighted score for the user
    SELECT SUM(c.score * p.weight)
    INTO total_weighted_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the total weight for the user
    SELECT SUM(p.weight)
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
END //

DELIMITER ;
