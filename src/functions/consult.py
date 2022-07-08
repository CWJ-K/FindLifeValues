from typing import List, Mapping
import random


class User:
    def __init__(self):
        self.responses = 'No Responses'


class Inquirer:
    def __init__(self):
        self.LIFE_VALUES_REFERENCE = 'No references of life values'
        self.data = 'No organized data from user responses!'
        self.comparion_questions = 'No comparison questions now!'
        self.response_summary = 'No response summary now!'


    def create_life_values_table(self):
        self.LIFE_VALUES_REFERENCE = [
            '公平', '敏感', '公正', '務實', '耐心', '專業', '獨立', '信任',
            '自律', '志願', '溫暖', '堅持', '能量', '誠實', '流行', '教育',
            '利他', '名氣', '安全', '穩定', '友誼', '強烈', '希望', '無懼',
            '健康', '力量', '忠誠', '啟發', '毅力', '靈活', '守諾', '控制',
            '魅力', '長壽', '透明', '智慧', '探索', '細心', '奇蹟', '自由',
            '平衡', '意義', '和諧', '多元', '負責', '善良', '快樂', '權威',
            '團隊', '競爭', '努力', '直覺', '熱情', '真理', '敏銳', '冒險',
            '美德', '效率', '開放', '美麗', '同理', '獨特', '活力', '和平',
            '樂觀', '權力', '溫柔', '創造', '家庭', '忠貞', '性感', '挑戰',
            '平安', '滿足', '愛', '創新', '同情', '速度', '高貴', '影響力',
        ]
        
        life_values_table = []
        break_ = 1
        for value in self.LIFE_VALUES_REFERENCE:

            if break_ == 8:
                if len(value) == 3:
                    row =  value + '| \n'
                else:
                    row = '  ' + value + '| \n' 
                break_ = 1
            else:
                if len(value) == 1:
                    row = '    '+ value + '|'
                    
                else:
                    row = '  ' + value + '|'
                break_ += 1
            life_values_table.append(row)


        life_values_table = ('').join(life_values_table)

        print(life_values_table)


    def ask_users_life_values_question(self) -> None:
        print(
            'Type in your 10 life values in the format of:',
            'value1, value2, value3, ..., value10',
        )
        User.responses = input('Your 10 most important life values are: ')


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