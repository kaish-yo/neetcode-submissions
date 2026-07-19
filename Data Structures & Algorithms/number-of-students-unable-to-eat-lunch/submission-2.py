class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while sandwiches and sandwiches[0] in students:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
            else:
                students.append(students.pop(0))
        
        return len(students)