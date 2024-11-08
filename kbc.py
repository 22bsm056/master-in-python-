import random

# Define questions, options, and correct answers
questions_and_options = [
    {
        "question": "What is the capital of India?",
        "options": ["A: Patna", "B: Gaya", "C: Delhi", "D: Mumbai"],
        "answer": "C"
    },
    {
        "question": "Who is the Prime Minister of India?",
        "options": ["A: Narendra Modi", "B: Rahul Gandhi", "C: Arvind Kejriwal", "D: Manmohan Singh"],
        "answer": "A"
    },
    {
        "question": "What is the national animal of India?",
        "options": ["A: Lion", "B: Elephant", "C: Peacock", "D: Tiger"],
        "answer": "D"
    },
    {
        "question": "What is the national bird of India?",
        "options": ["A: Sparrow", "B: Parrot", "C: Peacock", "D: Crow"],
        "answer": "C"
    },
    {
        "question": "What is the national sport of India?",
        "options": ["A: Cricket", "B: Football", "C: Kabaddi", "D: Hockey"],
        "answer": "D"
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["A: Earth", "B: Mars", "C: Jupiter", "D: Venus"],
        "answer": "C"
    },
    {
        "question": "Who wrote the Indian national anthem?",
        "options": ["A: Mahatma Gandhi", "B: Rabindranath Tagore", "C: Jawaharlal Nehru", "D: Subhash Chandra Bose"],
        "answer": "B"
    },
    {
        "question": "What is the smallest state in India by area?",
        "options": ["A: Goa", "B: Sikkim", "C: Tripura", "D: Nagaland"],
        "answer": "A"
    },
    {
        "question": "What is the official language of Brazil?",
        "options": ["A: Spanish", "B: English", "C: French", "D: Portuguese"],
        "answer": "D"
    },
    {
        "question": "Who is known as the father of the computer?",
        "options": ["A: Charles Babbage", "B: Alan Turing", "C: Bill Gates", "D: Steve Jobs"],
        "answer": "A"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["A: 10", "B: 12", "C: 14", "D: 16"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A: H2O", "B: O2", "C: CO2", "D: NaCl"],
        "answer": "A"
    },
    {
        "question": "How many continents are there?",
        "options": ["A: 5", "B: 6", "C: 7", "D: 8"],
        "answer": "C"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A: Vincent van Gogh", "B: Pablo Picasso", "C: Leonardo da Vinci", "D: Claude Monet"],
        "answer": "C"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A: 1945", "B: 1946", "C: 1947", "D: 1948"],
        "answer": "C"
    }
]

# Function to start the game
def start_game():
    print("Welcome to KBC! Enter '1' to start the game.")
    start = input("Enter 1 to start: ")
    
    if start != "1":
        print("Invalid input. Please enter 1 to start the game.")
        return
    
    print("Starting the game... Answer all questions correctly to win 7 crore rupees!")
    
    # Select 5 unique random questions
    selected_questions = random.sample(questions_and_options, 5)
    
    # Ask questions one by one
    for i, question_data in enumerate(selected_questions, 1):
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["answer"]
        
        print(f"\nQuestion {i}: {question}")
        for option in options:
            print(option)
        
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        # Check if the answer is correct
        if answer == correct_answer:
            print("Correct answer!")
        else:
            print("Incorrect answer. You are out! Try again.")
            return  # End the game if answer is incorrect
    
    # If player answers all 5 questions correctly
    print("Congratulations! You won 7 crore rupees!")

# Run the game
start_game()
