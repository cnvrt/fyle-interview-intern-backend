-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH teacher_grades AS (
    SELECT teacher_id, COUNT(*) AS total_graded
    FROM assignments
    WHERE state = 'GRADED'
    GROUP BY teacher_id
),
most_active_teacher AS (
    SELECT teacher_id
    FROM teacher_grades
    ORDER BY total_graded DESC
    LIMIT 1
)
SELECT COUNT(*) AS grade_a_count
FROM assignments
WHERE teacher_id = (SELECT teacher_id FROM most_active_teacher)
  AND grade = 'A'
  AND state = 'GRADED';
