-- This procedure computes and stores the average score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN in_user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = in_user_id;

    -- Update the average_score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = in_user_id;
END //

DELIMITER ;
