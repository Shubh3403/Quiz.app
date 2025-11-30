# questions = {}

# with open("questions.txt", "r") as file:
#     for line in file:
#         if "|" in line:
#             q, a = line.strip().split("|")
#             questions[q.strip()] = a.strip()

# score = 0

# for q, correct in questions.items():
#     print(q)
#     user = input("Your Answer: ")

#     if user.strip().lower() == correct.lower():
#         print("Correct!\n")
#         score += 1
#     else:
#         print("Wrong! Correct answer:", correct, "\n")

# print("Your final score:", score, "/", len(questions))
