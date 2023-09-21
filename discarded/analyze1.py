import pandas as pd
from exe_R import exe

def Run(FilePath : str, data_sheet_name : str, info_sheet_name : str, ensembl_exist : bool):
    data_df = pd.read_excel(FilePath, engine="openpyxl", sheet_name=data_sheet_name, index_col=0)
    info_df = pd.read_excel(FilePath, engine="openpyxl", sheet_name=info_sheet_name, index_col=9, dtype=object)

    cnt2 = 0
    cnt = 'A'
    cnt1 = 0
    for i in data_df.index:
        cnt2 = cnt2 + 1
        if cnt2 == 27:
            if cnt == 'Z':
                cnt = 'A'
                cnt1 = cnt1 + 1
            else:
                cnt = chr(ord(cnt) + 1)

    cnt = chr(ord('A') + cnt1) + cnt

    exe(FilePath, data_sheet_name, info_sheet_name, ensembl_exist, len(data_df.columns), len(info_df.columns), cnt)