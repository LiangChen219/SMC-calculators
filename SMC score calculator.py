def getting_inputs():
    while True:
        answered = int(input("Enter number of questions answered: "))
        correct = int(input("Enter number of questions correct: "))

        if (answered>=correct and 0<=answered<=25):
            return answered, correct
            

answered, correct = getting_inputs()

def return_score(answered, correct):
    score = 25
    score += (correct * 4)
    wrong = answered-correct
    score -= wrong
    return score

if __name__ == "__main__":
    score = return_score(answered, correct)
    print(f"score:{score}")
    
