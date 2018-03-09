'''
A college maintains academic information about students in three separate lists.

1. Course details: A list of pairs of form (coursecode,coursename), where both entries are strings.
For instance, [("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")]

2. Student details: A list of pairs of form (rollnumber,name), where both entries are strings.
For instance, [("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar")]

3. Grades: A list of triples of the form (rollnumber,coursecode,grade), where all entries are strings.
For instance, [("UGM2018001", "MA101", "AB"), ("UGP2018132", "PH101", "B"), ("UGM2018001", "PH101", "B")].

You may assume that each roll number and course code in the grade list appears in the student details and course details, respectively.

Your task is to write a function transcript(coursedetails,studentdetails,grades) that takes these three lists as input and
produces consolidated grades for each student. Each of the input lists may have its entries listed in arbitrary order.
Each entry in the returned list should be a tuple of the form

(rollnumber, name,[(coursecode_1,coursename_1,grade_1),...,(coursecode_k,coursename_k,grade_k)])

where the student has grades for k >= 1 courses reported in the input list grades.
The output list should be organized as follows.

1. The tuples shold sorted in ascending order by rollnumber
2. Each student's grades should sorted in ascending order by coursecode

For instance:
>>> transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar")],[("UGM2018001","MA101","AB"),("UGP2018132","PH101","B"),("UGM2018001","PH101","B")])
[('UGM2018001', 'Rohit Grewal', [('MA101', 'Calculus', 'AB'), ('PH101', 'Mechanics', 'B')]), ('UGP2018132', 'Neha Talwar', [('PH101', 'Mechanics', 'B')])]

>>> transcript([("T1","Test 1"),("T2","Test 2"),("T3","Test 3")],[("Opener","Murali Vijay"),("Captain","Virat Kohli"),("No3","Cheteshwar Pujara")],[("Opener","T1","14"),("Captain","T1","33"),("No3","T1","30"),("Opener","T2","55") ,("Captain","T2","158"),("No3","T2","19"), ("Opener","T3","33"),("Captain","T3","95"),("No3","T3","51")])
[('Captain', 'Virat Kohli', [('T1', 'Test 1', '33'), ('T2', 'Test 2', '158'), ('T3', 'Test 3', '95')]), ('No3', 'Cheteshwar Pujara', [('T1', 'Test 1', '30'), ('T2', 'Test 2', '19'), ('T3', 'Test 3', '51')]), ('Opener', 'Murali Vijay', [('T1', 'Test 1', '14'), ('T2', 'Test 2', '55'), ('T3', 'Test 3', '33')])]

'''


def transcript(coursedetails, studentdetails, grades):
    ans = []
    student_grades = {}

    for x in range(len(studentdetails)):
        temp = []
        for y in range(len(grades)):
            for z in range(len(coursedetails)):
                if studentdetails[x][0] == grades[y][0] and grades[y][1] == coursedetails[z][0]:
                    temp.append((grades[y][1], coursedetails[z][1], grades[y][2]))
                student_grades[studentdetails[x][0]] = sorted(temp)

    [ans.append((studentdetails[a][0], studentdetails[a][1], student_grades[b])) for a in range(len(studentdetails)) for b in sorted(student_grades.keys()) if studentdetails[a][0] == b]

    return sorted(ans)


print(transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar")],[("UGM2018001","MA101","AB"),("UGP2018132","PH101","B"),("UGM2018001","PH101","B")]))

print('*' * 356)

print(transcript([("T1","Test 1"),("T2","Test 2"),("T3","Test 3")],[("Opener","Murali Vijay"),("Captain","Virat Kohli"),("No3","Cheteshwar Pujara")],[("Opener","T1","14"),("Captain","T1","33"),("No3","T1","30"),("Opener","T2","55") ,("Captain","T2","158"),("No3","T2","19"), ("Opener","T3","33"),("Captain","T3","95"),("No3","T3","51")]))
