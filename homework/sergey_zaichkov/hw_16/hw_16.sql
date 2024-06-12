INSERT INTO students (name, second_name, group_id) VALUES ('Peter', 'Parker', NULL)books
INSERT INTO books (title, taken_by_student_id) VALUES ('Spider-man', 66)
INSERT INTO books (title, taken_by_student_id) VALUES ('Spider-man2', 66)
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Avengers', '2012-05-08', '2019-08-05')

UPDATE students SET group_id = 30 WHERE id = 66

INSERT INTO subjects (title) VALUES ('Throw a web')
INSERT INTO subjects (title) VALUES ('Сlimb walls')

INSERT INTO lessons (title, subject_id) VALUES ('lesson1', 65);
INSERT INTO lessons (title, subject_id) VALUES ('lesson2', 65);
INSERT INTO lessons (title, subject_id) VALUES ('lesson1', 66);
INSERT INTO lessons (title, subject_id) VALUES ('lesson2', 66);

INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 125, 66);
INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 126, 66);
INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 127, 66);
INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 128, 66);

SELECT value FROM marks WHERE student_id = 66

SELECT title FROM books WHERE taken_by_student_id = 66

SELECT students.name AS 'Name', students.second_name AS 'Surname',
groups.title AS 'Group', subjects.title AS 'Subject',
lessons.title AS 'Lesson', marks.value AS 'Mark', books.title AS 'Book'
FROM marks JOIN lessons ON marks.lesson_id = lessons.id
JOIN students ON marks.student_id = students .id
JOIN books ON students.id = books.taken_by_student_id
JOIN `groups` ON students.group_id = groups.id
JOIN subjects ON lessons.subject_id = subjects.id
where student_id = 66
