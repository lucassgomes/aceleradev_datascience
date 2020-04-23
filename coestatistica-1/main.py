import pandas as pd


def main():
    df = pd.read_csv('desafio1.csv')
    pts_credit = df.groupby('estado_residencia').pontuacao_credito.agg([
        pd.Series.mode,
        'median',
        'mean',
        'std'
    ])
    pts_credit.columns = [
        'moda',
        'mediana',
        'media',
        'desvio_padrao'
    ]
    pts_credit.to_json('submission.json', orient='index')


if __name__ == '__init__':
    main()
