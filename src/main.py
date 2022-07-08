import time

from functions.writer import Writer
from functions.consult import Inquirer, User

def find_life_values() -> None:
    
    print(
        'Hello, I am coming to help you find your life values.\n',
        'The whole process will be conducted in two rounds.\n', 
    )

    MAX_ROUNDS = 2
    current_round = 1

    while current_round <= MAX_ROUNDS:
        print(
            f'Round {current_round}.\n',
            'Please select the 10 most important life values based on the table below: \n',
        )
        
        time.sleep(2)

        inquirer = Inquirer()
        inquirer.create_life_values_table()

        time.sleep(2)
        
        inquirer.ask_users_life_values_question()

        time.sleep(2)
        
        print(
            'Based on your 10 life values,\n',
            'you are going to compare the importance of two values randomly chosen.',
        )

        time.sleep(2)

        print('Start to compare them!')

        time.sleep(1)

        inquirer.organize_user_responses(User.responses)
        inquirer.make_comparison_questions()
        inquirer.ask_users_comparison_questions()
        
        writer = Writer()
        writer.generate_report(inquirer.response_summary)
        writer.rerank_report_if_duplicated_ranks()
        
        User.responses_in_rounds.append(list(writer.report['Life Value']))

        print(f'{current_round} finish!')
        current_round += 1

    print(
        'Your results:\n',
        f'Round 1: {User.responses_in_rounds[0]}\n',
        f'Round 2: {User.responses_in_rounds[1]}',

    )

    #print('the similarity of the two rounds. below is the same values')


if __name__ == '__main__':
    find_life_values()