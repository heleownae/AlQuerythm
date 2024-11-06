SELECT Class
FROM Courses
GROUP BY Class
Having Count(Student) >= 5;
