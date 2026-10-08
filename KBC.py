questions=[
    { "Question" : "Capital of India?",
      "Options": ["A.Delhi","B.Mumbai","C.Kolkata","D.Pune"],
       "Correct answer": "A",
        "prize" : 1000
        },
        {
        "Question": "Which language is used for Python programs?",
        "Options": ["A. Python", "B. Java", "C. C++", "D. HTML"],
        "Correct answer": "A",
        "prize": 2000
    },
    {
        "Question": "How many days are there in a week?",
        "Options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "Correct answer": "C",
        "prize": 5000
    },
    {
        "Question": "Which planet is known as the Red Planet?",
        "Options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Mercury"],
        "Correct answer": "C",
        "prize": 50000
    },
    {
        "Question": "Who wrote the Indian national anthem?",
        "Options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Mahatma Gandhi"],
        "Correct answer": "A",
        "prize": 60000
    },
    {
        "Question": "Which is the largest ocean in the world?",
        "Options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "Correct answer": "D",
        "prize": 70000
    },
    {
        "Question": "What is the chemical symbol for Gold?",
        "Options": ["A. Go", "B. Gd", "C. Au", "D. Ag"],
        "Correct answer": "C",
        "prize": 80000
    },
    {
        "Question": "Which country is famous for the Eiffel Tower?",
        "Options": ["A. Italy", "B. France", "C. Germany", "D. Spain"],
        "Correct answer": "B",
        "prize": 90000
    },
    {
        "Question": "How many bones are there in an adult human body?",
        "Options": ["A. 206", "B. 208", "C. 210", "D. 212"],
        "Correct answer": "A",
        "prize": 100000
    },
    {
        "Question": "Who was the first Prime Minister of India?",
        "Options": ["A. Mahatma Gandhi", "B. Sardar Patel", "C. Jawaharlal Nehru", "D. Rajendra Prasad"],
        "Correct answer": "C",
        "prize": 200000
    },
    {
        "Question": "Which gas do humans need to breathe for survival?",
        "Options": ["A. Carbon Dioxide", "B. Oxygen", "C. Nitrogen", "D. Hydrogen"],
        "Correct answer": "B",
        "prize": 300000
    },
    {
        "Question": "Which is the smallest continent in the world?",
        "Options": ["A. Europe", "B. Antarctica", "C. Australia", "D. South America"],
        "Correct answer": "C",
        "prize": 400000
    },
    {
        "Question": "What is the square root of 144?",
        "Options": ["A. 10", "B. 11", "C. 12", "D. 14"],
        "Correct answer": "C",
        "prize": 500000
    },
    {
        "Question": "Which Indian city is known as the Pink City?",
        "Options": ["A. Jaipur", "B. Jodhpur", "C. Udaipur", "D. Bikaner"],
        "Correct answer": "A",
        "prize": 600000
    }
]


print("=========================================")
print("            WELCOME TO KBC               ")
print("=========================================")

for q in questions:
    print("\n" + q["Question"])

    for Options in q['Options']:
        print("\n"+ Options)


    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q["Correct answer"]:
        money = q["prize"]
        print("✅ Correct answer!")
        print("You won ₹", money)
    else:
        print("❌ Wrong answer!")
        print("The correct answer was:", q["Correct answer"])
        continue

print("\nGame Over!")
print("Your total prize money: ₹", money)        
