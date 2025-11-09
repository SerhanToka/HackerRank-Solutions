# Given Code
if __name__ == '__main__':
    # Answer
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])
    
    scores_list = [student[1] for student in student_list] # List comprehension
    unique_scores = sorted(list(set(scores_list))) # No duplicate and sorted index 1 is second lowest score
    second_lowest_score = unique_scores[1]
    
    result_names = []
    for student in student_list:
        if student[1] == second_lowest_score:
            result_names.append(student[0])

    result_names.sort()
    for name in result_names:
        print(name)