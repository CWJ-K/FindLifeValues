import pandas as pd


def transform_answers_to_report(new_answers):
    splited_answers = list(new_answers.split(','))
    rank_list = [rank for rank in range(1, len(splited_answers) + 1)]
    
    report = pd.DataFrame(
        data={
            'Life Value': splited_answers,
            'Rank': rank_list,
        }
    )
    report['Life Value'] = report['Life Value'].str.strip()
    
    return report


def resort_values_if_same_grades(sort_report):
    if len(sort_report['Rank']) != len(set(sort_report['Rank'])):
        print('''This is your results. Please sort the identical ranks by yourself. Type the new order of your life values in the format: the most important value, the second important value, ..., the least important value:
        ''')
        new_answers = input('Type your answers: ')
        sort_report = transform_answers_to_report(new_answers)

    
    return sort_report