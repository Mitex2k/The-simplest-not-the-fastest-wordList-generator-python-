import time
def generate(letters, word_length, file):
    amount_of_letters = len(letters)
    total_combinations = amount_of_letters ** word_length
    current_indices = [0] * word_length

    for _ in range(total_combinations):
        word = ""
        for position in range(word_length):
            letter_index = current_indices[position]
            word += letters[letter_index]

        file.write(word + "\n")

        position = word_length - 1
        while position >= 0:
            current_indices[position] += 1
            if current_indices[position] < amount_of_letters:
                break
            current_indices[position] = 0
            position -= 1

def main():
    letters_input = input("Enter letters: ")  
    length_input = int(input("Enter max length: ")) 
    name = input("Name the output file: ")
    
    amount_of_letters = len(letters_input)
    total_combinations = amount_of_letters ** length_input
    print(f"total_combinations: {total_combinations}")
    
    confirmation = input("Do you want to proceed?(Y/N): ")
    
    if confirmation.lower() != 'y':
        return
          
    start = time.time()
    
    with open(f"{name}.txt", "w") as file:
        for i in range(1, length_input + 1):
            generate(letters_input, i, file)
    
    print(f"Saved to {name}.txt")
    
    end = time.time()
    print(f"Execution time: {end - start:.4f} seconds")   

if __name__ == "__main__":
    main()
