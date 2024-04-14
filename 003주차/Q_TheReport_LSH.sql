SELECT  if( Grades.Grade >7, Students.Name , 'NULL' ), Grades.Grade, Students.Marks
FROM Students 
JOIN Grades 
on Students.Marks between Grades.Min_Mark and Grades.MAX_Mark
order by Grades.Grade desc, Students.Name;