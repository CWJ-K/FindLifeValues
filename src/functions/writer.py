import pandas as pd


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