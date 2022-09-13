def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    new_scores = []
    for score in student_scores:
        new_scores.append(round(score))
    return new_scores
    
def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    c = 0
    for score in student_scores:
        if score <= 40:
            c += 1
    return c
    
def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    great_scores = []
    for score in student_scores:
        if score >= threshold:
            great_scores.append(score)
    return great_scores
    
def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:
 
             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    gap = int(highest / 4) - 10
    results = []
    for i in range(4):
        results.append(41 + gap*i)
    return results
    
def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    ranking = []
    for i in range(len(student_scores)):
        ranking.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return ranking
    
def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect = []
    for name, score in student_info:
        if score == 100:
            perfect.append(name)
            perfect.append(score)
            break
        else:
            pass
    return perfect
