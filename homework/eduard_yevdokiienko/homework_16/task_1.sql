INSERT INTO students (name, second_name, group_id) VALUES ('Eduard', 'Yevdokiienko', NULL)

INSERT INTO books (title, taken_by_student_id) VALUES ('3 body problem', 21)
INSERT INTO books (title, taken_by_student_id) VALUES ('S_Q_L', 21)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('ST777', '2024-04-04', '2024-08-01')
UPDATE students SET group_id =9 WHERE id =21

INSERT INTO subjects (title) VALUES ('Math')
INSERT INTO subjects (title) VALUES ('Sciense')

INSERT INTO lessons (title, subject_id) VALUES ('Theory of mathematics', 12)
INSERT INTO lessons (title, subject_id) VALUES ('Practice of Math', 12)
INSERT INTO lessons (title, subject_id) VALUES ('Theory of Sciense', 13)
INSERT INTO lessons (title, subject_id) VALUES ('Practice of sciense', 13)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', 19, 21)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('B', 20, 21)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', 21, 21)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('B', 22, 21)

SELECT *
FROM marks
WHERE student_id =21

SELECT *
FROM books b
WHERE taken_by_student_id =21

SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title, m.value AS mark, l.title AS lesson_title, sub.title AS subject_title
FROM students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects sub ON sub.id = l.subject_id
WHERE s.id = 21
