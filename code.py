import random
import time

print('WELCOME TO KAUN BANEGA CROREPATI\n'.center(60))

# Questions
questions = [
    {"q": "Bharat ki rajdhani kya hai?", "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"], "ans": "B"},
    {"q": "2 + 2 kitna hota hai?", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "ans": "B"},
    {"q": "Suraj kis disha me ugta hai?", "options": ["A. West", "B. North", "C. East", "D. South"], "ans": "C"},
    {"q": "5 x 5 kitna hota hai?", "options": ["A. 20", "B. 25", "C. 30", "D. 15"], "ans": "B"},
    {"q": "1 week me kitne din hote hain?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "ans": "C"},
    {"q": "Pani ka formula kya hai?", "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"], "ans": "B"},
    {"q": "India ka rashtriya pakshi?", "options": ["A. Mor", "B. Tota", "C. Kauwa", "D. Kabootar"], "ans": "A"},
    {"q": "Computer ka brain?", "options": ["A. Monitor", "B. CPU", "C. Mouse", "D. Keyboard"], "ans": "B"},
]

money = [1000,2000,3000,5000,10000,20000,40000,80000]

safe_level = 10000

lifeline_5050 = True
lifeline_audience = True

random.shuffle(questions)

win = 0

for i in range(len(questions)):
    q = questions[i]

    print(f"\nQuestion {i+1} for ₹{money[i]}")
    print(q["q"])

    for opt in q["options"]:
        print(opt)

    print("\nLifelines:")
    if lifeline_5050:
        print("Type 50 to use 50-50")
    if lifeline_audience:
        print("Type AUD to use Audience Poll")

    start = time.time()

    ans = input("\nYour Answer (A/B/C/D): ").upper()

    end = time.time()

    # Timer (10 sec limit)
    if end - start > 10:
        print("⏰ Time up!")
        break

    # 50-50 Lifeline
    if ans == "50" and lifeline_5050:
        lifeline_5050 = False
        print("50-50 Lifeline used!")
        
        correct = q["ans"]
        options = ["A", "B", "C", "D"]
        options.remove(correct)
        remove = random.sample(options, 2)

        for opt in q["options"]:
            if opt[0] not in remove:
                print(opt)

        ans = input("Now answer: ").upper()

    # Audience Poll Lifeline
    if ans == "AUD" and lifeline_audience:
        lifeline_audience = False
        print("Audience Poll:")
        
        correct = q["ans"]
        for opt in ["A","B","C","D"]:
            if opt == correct:
                print(f"{opt}: {random.randint(50,80)}%")
            else:
                print(f"{opt}: {random.randint(5,30)}%")

        ans = input("Now answer: ").upper()

    # Check answer
    if ans == q["ans"]:
        print("✅ Correct Answer!")
        win = money[i]
    else:
        print("❌ Wrong Answer!")
        print("Correct was:", q["ans"])

        if win >= safe_level:
            win = safe_level
        else:
            win = 0
        break

print("\n🎉 You won ₹", win)
print("GAME OVER")
