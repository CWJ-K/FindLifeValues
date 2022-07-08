from functions.create_life_values_table import create_life_values_table
from functions.ask_the_importance_of_values import ask_the_importance_of_values
from functions.create_report import create_report
from functions.resort_values_if_same_grades import resort_values_if_same_grades

def find_life_values():
    
    
    print('Hello, I am coming to help you find your life values. \nPlease select the 10 most important life values based on the table below: \n')
    life_values_table = create_life_values_table()
    
    print('Type your 10 life values by this format: value1, value2, value3, ..., value10')
    ten_life_values = input('Your 10 most important life values: ')
    #check_ten_life_values(ten_life_values)
    
    print('''Based on the 10 life values, you will be asked to select the most important values 
    from two values randomly chosen. There are two rounds of the process.
    '''
    )
    answers = ask_the_importance_of_values(ten_life_values)
    
    sort_report = create_report(answers)
    sort_report = resort_values_if_same_grades(sort_report)
    
    print('it is your result \n', sort_report)
    
    
    
    #print('the similarity of the two rounds. below is the same values')

if __name__ == '__main__':
    find_life_values()