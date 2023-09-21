import pandas as pd

def Run(FilePath : str, data_sheet_name : str, info_sheet_name : str, ensembl_exist : bool):
    data_df = pd.read_excel(FilePath, engine="openpyxl", sheet_name=data_sheet_name, index_col=0)
    info_df = pd.read_excel(FilePath, engine="openpyxl", sheet_name=info_sheet_name, index_col=9, dtype=object)

    totalread = data_df.sum(axis=0)

    rpm = data_df.mul(1000000).div(totalread, axis=1)

    data_df = data_df.groupby(data_df.index).first()
    info_df = info_df.groupby(info_df.index).first()

    rpk = data_df.mul(1000).div(info_df['Length'], axis=0)
    rpktotal = rpk.sum().sum()

    rpkm = rpk.div(totalread / 1e6, axis=1)

    tpm = rpk.div(rpktotal).mul(1000000)

    new_sheet = pd.concat([rpm, rpk, rpkm, tpm], keys=['rpm', 'rpk', 'rpkm', 'tpm'], axis=1).swaplevel(axis=1).sort_index(axis=1)

    new_sheet.to_csv('result.csv')