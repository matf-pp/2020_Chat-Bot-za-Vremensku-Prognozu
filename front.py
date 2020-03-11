
from input_parser import (
    is_exit_command,
    determine_response,
)

def main():
    print('Ask me a question about the weather\n')

    while True:
        user_input = input()

        if is_exit_command(user_input):
            print('Program exiting...')
            break
        
        response = determine_response(user_input)
        print(response)
        
        

if __name__ == "__main__":
    main()