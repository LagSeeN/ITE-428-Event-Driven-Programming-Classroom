wantedskill = {"C#", "Python", "Java", "PHP", "SQL", "Go"}
applicant1skill = {"VB", "C", "Ruby", "Java", "HTML"}
applicant2skill = {"C#", "HTML", "R", "PHP", "SQL", "Swift", "PHP"}
applicant3skill = {"Java", "C++", "Ruby", "JavaScript", "Objective-C", "Go"}
applicant4skill = {"Java", "Python", "Go", "SQL", "Swift"}
applicant5skill = {"C++", "C", "C#", "Objective-C", "JavaScript", "SQL"}


def calcMatch(applicant):
    return applicant.intersection(wantedskill).__len__() / wantedskill.__len__() * 100


print('Applicant 1 skill match : {:.2f}%'.format(calcMatch(applicant1skill)))
print('Applicant 2 skill match : {:.2f}%'.format(calcMatch(applicant2skill)))
print('Applicant 3 skill match : {:.2f}%'.format(calcMatch(applicant3skill)))
print('Applicant 4 skill match : {:.2f}%'.format(calcMatch(applicant4skill)))
print('Applicant 5 skill match : {:.2f}%'.format(calcMatch(applicant5skill)))
