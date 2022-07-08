from typing import Union
import pandas as pd
from collections import Counter

class Writer:
    def __init__(self):
        self.report = 'No report now!'
    
    def generate_report(self, responses) -> pd.DataFrame:
        report = pd.DataFrame(list(responses.items()), columns=['Life Value', 'Times'])
        
        report['Rank'] = (
            report['Times']
            .rank(method='min', ascending=False)
            .astype(int)
        )
        
        self.report = (
            report
            .sort_values(by=['Rank'], ascending=True)
            .reset_index(drop=True)
            .drop(['Times'], axis=1)
        )
        
        return self.report
    
    def transform_responses_to_report(self, responses) -> pd.DataFrame:
        splited_responses = list(responses.split(','))
        rank_list = [rank for rank in range(1, len(splited_responses) + 1)]

        report = pd.DataFrame(
            data={
                'Life Value': splited_responses,
                'Rank': rank_list,
            }
        )
        report['Life Value'] = report['Life Value'].str.strip()

        return report
    
    def rerank_report_if_duplicated_ranks(self) -> pd.DataFrame:
        if len(self.report['Rank']) != len(set(self.report['Rank'])):
            print(
                'Please resort the life values with the same ranks.\n',
                'Type in the new order of your life values in the format:', 
                'the most important value, the second important value, ..., the least important value: '
            )
            responses = input('New order of your life values: ')
            self.report = self.transform_responses_to_report(responses)

    
        return self.report

    def calculate_similarity(self, results):
        round_one_result = results[0]
        round_two_result = results[1]
        
        round_one_word_occurrency = Counter(round_one_result)
        round_two_word_occurrency = Counter(round_two_result)
        
        all_words = list(round_one_word_occurrency.keys() | round_two_word_occurrency.keys())
        
        round_one_word_vector = [round_one_word_occurrency.get(word, 0) for word in all_words]
        round_two_word_vector = [round_two_word_occurrency.get(word, 0) for word in all_words]
        
        len_round_one  = sum(vector*vector for vector in round_one_word_vector) ** 0.5
        len_round_two  = sum(vector*vector for vector in round_two_word_vector) ** 0.5

        dot = sum(vector_one*vector_two for vector_one, vector_two in zip(round_one_word_vector, round_two_word_vector)) 

        cosine = round(dot / (len_round_one * len_round_two), 2)
        return cosine

    def make_similarity_report(self, results) -> Union[pd.DataFrame, int]:
        
        report = pd.DataFrame(
            {
                'Round 1': results[0],
                'Round 2': results[1]
            }
        )
        
        similarity = self.calculate_similarity(results)

        return report, similarity