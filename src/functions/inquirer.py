from typing import List, Mapping
import random


class Inquirer:
    def __init__(self):
        self.data = 'No organized data from user responses!'
        self.comparion_questions = 'No comparison questions now!'
        self.response_summary = 'No response summary now!'


    def organize_user_responses(self, responses) -> List:
        splitted_responses = list(responses.split(','))
        self.data = [response.strip() for response in splitted_responses]
        return self.data
    

    def make_comparison_questions(self) -> List:
        self.comparion_questions = []
        for first_value_index in range(len(self.data)-1):
            for second_value_index in range(first_value_index+1, len(self.data)):
                question = [self.data[first_value_index], self.data[second_value_index]]
                self.comparion_questions.append(question)
        
        self.randomize_questions(self.comparion_questions)
        
        return self.comparion_questions
    

    def randomize_questions(self, comparion_questions) -> None:
        random.seed(61)
        random.shuffle(comparion_questions)


    def ask_users_comparison_questions(self) -> Mapping[str, int]:
        response_summary = {response:0 for response in self.data}
        
        questions = self.comparion_questions
        
        while questions:
            number = random.randint(0, len(questions)-1)
            FIRST_ELEMENT = 0
            SECOND_ELEMENT = 1
            
            selected_response = (
                input(
                f'''
                    {questions[number][FIRST_ELEMENT]} vs {questions[number][SECOND_ELEMENT]} : 
                '''
                )
                .strip()
            )
            
            response_summary[selected_response] += 1
            questions.pop(number)
        
        self.response_summary = response_summary
        
        return self.response_summary