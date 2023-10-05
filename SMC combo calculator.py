#calculate possible answers
def get_score():
    while True:
        score = int(input("Enter SMC score: "))
        if 0 <= score <= 125:
            return score
        else:
            print('enter a score bwetween 0 and 125')
        

def calculate_combo(score):
    possible_combos = []
    for correct in range(26):
        for incorrect in range(26):
            mark = 25 + (correct * 4 - incorrect)
            if mark == score:
                if (correct+incorrect) <= 25:
                    possible_combos.append([correct, incorrect])
    if  len(possible_combos) == 0:
        print("No combinations found for the given score.")
    else:
        for pair in possible_combos:
            correct = pair[0]
            incorrect = pair[1]
            answered = correct + incorrect
            print(f"answered:{answered}/25 correct:{correct}/25 incorrect:{incorrect}/25")
            print()
                

if __name__ == "__main__":
    while True:
        score = get_score()
        calculate_combo(score)
