import requests

def fetch_gene_info(symorid, gene_symbol_or_id):
    base_url = "https://rest.ensembl.org/"
    
    if symorid == 0:
        endpoint = f"lookup/symbol/homo_sapiens/{gene_symbol_or_id}?content-type=application/json"
    else:
        endpoint = f"lookup/id/{gene_symbol_or_id}?content-type=application/json"

    response = requests.get(base_url + endpoint)
    
    if response.status_code == 200:
        return response.json()
    return None

def calculate_gene_length(gene_info):
    if gene_info and 'start' in gene_info and 'end' in gene_info:
        gene_length = gene_info['end'] - gene_info['start'] + 1
        return gene_length
    return None

def Run(gene_symbol_or_id):
    symorid = 0

    gene_info = fetch_gene_info(symorid, gene_symbol_or_id)
    gene_length = calculate_gene_length(gene_info)

    if gene_length:
        print("Gene Length:", gene_length)
        return gene_length
    else:
        print("Failed to fetch gene information.")
        return None