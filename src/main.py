import time

from functions.create_life_values_table import create_life_values_table
from functions.ask_the_importance_of_values import ask_the_importance_of_values
from functions.writer import Writer


def find_life_values():
    
    print(
        'Hello, I am coming to help you find your life values.\n',
        'The whole process will be conducted in two rounds.\n', 
        'Please select the 10 most important life values based on the table below: \n',
    )
    
    time.sleep(2)

    create_life_values_table()
    
    time.sleep(2)
    
    print('Type in your 10 life values in the format of: value1, value2, value3, ..., value10')
    ten_life_values = input('Your 10 most important life values are: ')

    time.sleep(2)
    
    print(
        'Based on your 10 life values,\n',
        'you are going to compare the importance of two values randomly chosen.',
    )

    time.sleep(2)

    print('Start to compare them!')

    time.sleep(1)

    responses = ask_the_importance_of_values(ten_life_values)
    
    writer = Writer()
    writer.generate_report(responses)
    writer.rerank_report_if_duplicated_ranks()
    
    print('This is your result: \n', writer.report)
    
    #print('the similarity of the two rounds. below is the same values')

if __name__ == '__main__':
    find_life_values()