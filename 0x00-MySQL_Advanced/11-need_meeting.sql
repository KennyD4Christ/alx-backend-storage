-- Create a view need_meeting that lists all students who have a score under 80
-- and either no last_meeting date or a last_meeting date that is more than 1 month ago.

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
