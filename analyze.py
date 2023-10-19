from os import error
import find_length_by_ensembl as f_ensembl
import find_length_by_symbol as f_symbol
import pandas as pd

def Run(FilePath : str, data_sheet_name : str, info_sheet_name : str, ensembl_exist : bool, col : int, kind : int):
    data_df = pd.read_excel(FilePath, engine="openpyxl", sheet_name=data_sheet_name, index_col=0)
    info_df = pd.DataFrame()

    if ensembl_exist == True:
        a = pd.read_excel(FilePath, engine="openpyxl", sheet_name=info_sheet_name, index_col=col)
        info_df = a

    elif kind == 1:
        temp = data_df.index.to_series()
        a = pd.Series()
        cnt = 0

        for i in temp:
            try:
                a[cnt] = f_symbol.Run(i)
                cnt+=1
            except:
                return error

        info_df = info_df.set_axis(temp, axis=0)
        info_df.insert(0, 'Length', a.to_list())

    else:
        temp = data_df.index.to_series()
        a = pd.Series()
        cnt = 0

        for i in temp:
            try:
                a[cnt] = f_ensembl.Run(i)
                print(a)
                cnt+=1
            except:
                return error

        info_df = info_df.set_axis(temp, axis=0)
        info_df.insert(0, 'Length', a.to_list())

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