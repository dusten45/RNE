import requests

def get_gene_length(ensembl_gene_id):
    ensembl_url = f"https://rest.ensembl.org/sequence/id/{ensembl_gene_id}?content-type=application/json&type=genomic"

    try:
        response = requests.get(ensembl_url)
        data = response.json()

        # Gene 정보에서 gene length 추출
        gene_length = len(data.get('seq', ''))

        return gene_length

    except Exception as e:
        print(f"오류 발생: {e}")
        return None

def Run(ensembl_gene_id):
    gene_length = get_gene_length(ensembl_gene_id)
    
    if gene_length is not None:
        return gene_length
    else:
        return None