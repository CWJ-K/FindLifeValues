import random


def transform_values_to_list(ten_life_values):
    results = list(ten_life_values.split(','))
    cleaned_results = [result.strip() for result in results]
    return cleaned_results


def create_two_value_pairs(ten_life_values):
    
    results = []
    for first in range(len(ten_life_values)-1):
        for second in range(first+1, len(ten_life_values)):
            result = [ten_life_values[first], ten_life_values[second]]
            results.append(result)
    return results
            

def randomize_pairs(two_value_pairs):
    random.seed(61)
    random.shuffle(two_value_pairs)


def compare_two_pairs(two_value_pairs, ten_life_values):
    results = {value:0 for value in ten_life_values}
    while two_value_pairs:
        random_number = random.randint(0, len(two_value_pairs)-1)
        selected_value = input(
            f'''
                {two_value_pairs[random_number][0]} vs {two_value_pairs[random_number][1]} : 
            '''
        ).strip()
        
       
        results[selected_value] += 1
        two_value_pairs.pop(random_number)
    return results


def ask_the_importance_of_values(ten_life_values):
    ten_life_values = transform_values_to_list(ten_life_values)
    two_value_pairs = create_two_value_pairs(ten_life_values)
    randomize_pairs(two_value_pairs)
    result = compare_two_pairs(two_value_pairs, ten_life_values)
    
    return result