def percentage_to_letter(score=0):
    if score > 100 or score < 0:
        return "I"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "F"


def is_passing(letter=None):
    if letter == "A" or letter == "B" or letter == "C":
        return True
    elif letter == "D" or letter == "F":
        return False
    elif letter == "I":
        print("Invalid Score")


letterGrade = percentage_to_letter(float(input("Input Your Grade: ")))
print(is_passing(letterGrade))
