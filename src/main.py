from functions.create_life_values_table import create_life_values_table
from functions.ask_the_importance_of_values import ask_the_importance_of_values

def find_life_values():
    print('Hello, I am coming to help you find your life values. \nPlease select the 10 most important life values based on the table below: \n')
    life_values_table = create_life_values_table()
    
    print('Type your 10 life values by this format: value1, value2, value3, ..., value10')
    ten_life_values = input('Your 10 most important life values: ')
    #check_ten_life_values(ten_life_values)
    
    print('''
        Based on the 10 life values, you will be asked to select the most important values
        from two values randomly choosed. There are two rounds of the process.
    '''
    )
    raw_result = ask_the_importance_of_values()
    
    sort_result = _sort_values()
    sort_result = resort_values_if_same_order()
    final result = create_report()
    print('it is your result')
    
    
    
    #print('the similarity of the two rounds. below is the same values')

if __name__ == '__main__':
    find_life_values()