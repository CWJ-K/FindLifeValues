import pandas as pd


def create_report(answers):
    report = pd.DataFrame(list(answers.items()), columns=['Life Value', 'Times'])
    report['Rank'] = (
        report['Times']
        .rank(method='min', ascending=False)
        .astype(int)
    )
    sorted_report = (
        report
        .sort_values(by=['Rank'], ascending=True)
        .reset_index(drop=True)
        .drop(['Times'], axis=1)
    )
    return sorted_report