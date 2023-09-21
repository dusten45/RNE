import subprocess

def exe(FilePath : str, data_sheet_name : str, info_sheet_name : str, ensembl_exist : bool, ng1, ng2, np_str):
    input = str(ng1) + '\n' + str(np_str) + '\n' + str(ng2) + '\n' + FilePath + '\n' + data_sheet_name + '\n' + info_sheet_name + '\n'
    
    f = open('input.txt', mode='w')
    f.write(input)

    subprocess.call('rscript D:\Personal\CODING\RNE\DTD.R')