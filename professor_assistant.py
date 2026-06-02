# Project Name: Professor Assistant
# Version: 1.0
# Description: Helps professors create automated, randomized exams from a question bank file.

import random

def main():
    print("Welcome to professor assistant version 1.0.\n")
    
    # 1. Capture professor's name and greet them
    prof_name = input("Please Enter Your Name: ")
    print(f"\nHello Professor. {prof_name}, I am here to help you create exams from a question bank.")
    
    # 2. Outer loop to allow creating multiple exams if requested
    keep_going = True
    while keep_going:
        proceed = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ")
        
        # Check user intent using case-insensitive validation
        if proceed.strip().lower() == 'yes':
            bank_path = input("Please Enter the Path to the Question Bank. ")
            
            try:
                # 3. Open and parse the question bank file safely
                # Each question is on its own line, immediately followed by its answer on the next line
                with open(bank_path, 'r', encoding='utf-8') as file:
                    lines = [line.strip() for line in file.readlines() if line.strip()]
                
                # Validation: Since lines are paired (Question \n Answer), the count must be even
                if len(lines) < 2 or len(lines) % 2 != 0:
                    print("\nError: The question bank file format is corrupt or empty.")
                    continue
                
                print("\nYes, indeed the path you provided includes questions and answers.\n")
                
                # 4. Group lines into explicit Question-Answer tuples
                qa_pairs = []
                for i in range(0, len(lines), 2):
                    question = lines[i]
                    answer = lines[i+1]
                    qa_pairs.append((question, answer))
                
                total_available = len(qa_pairs)
                
                # 5. Capture the desired number of questions with validation logic
                while True:
                    try:
                        num_requested = int(input(f"How many question-answer pairs do you want to include in your exam? (Available: {total_available}): "))
                        if 1 <= num_requested <= total_available:
                            break
                        else:
                            print(f"Please enter a number between 1 and {total_available}.")
                    except ValueError:
                        print("Invalid input! Please enter a valid whole integer number.")
                
                # 6. Capture the output storage destination filename
                output_path = input("\nWhere do you want to save your exam? ")
                
                # 7. Use random selection sampling to pick unique question-answer pairs
                # Using random.sample prevents identical questions from appearing twice in the same exam
                selected_exam = random.sample(qa_pairs, num_requested)
                
                # 8. Write the selected pairs out to the destination target file
                with open(output_path, 'w', encoding='utf-8') as out_file:
                    for idx, (q, a) in enumerate(selected_exam, start=1):
                        out_file.write(f"Question {idx}: {q}\n")
                        out_file.write(f"Answer: {a}\n")
                        out_file.write("-" * 40 + "\n")  # Visual separator between questions
                
                print(f"\nCongratulations Professor {prof_name}. Your exam is created and saved in {output_path}.\n")
                
            except FileNotFoundError:
                print(f"\nError: Could not locate the file at '{bank_path}'. Please check the filename or path and try again.\n")
            except Exception as e:
                print(f"\nAn unexpected runtime processing error occurred: {e}\n")
                
        elif proceed.strip().lower() == 'no':
            # Terminate the loop and exit gracefully
            keep_going = False
        else:
            print("Invalid input choice. Please explicitly type 'Yes' or 'No'.\n")
            
    # Final cleanup exit message
    print(f"Thank you professor {prof_name}. Have a good day!")

# Execute the program structure
if __name__ == '__main__':
    main()