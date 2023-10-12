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

if __name__ == "__main__":
    while True:
        ensembl_gene_id = input("Ensembl Gene ID를 입력하세요 (빈 문자열을 입력하면 종료): ")
        
        if not ensembl_gene_id:
            break

        gene_length = get_gene_length(ensembl_gene_id)
    
        if gene_length is not None:
            print(f"Ensembl Gene ID: {ensembl_gene_id}")
            print(f"Gene Length: {gene_length} bp")
        else:
            print("Gene 정보를 검색할 수 없거나 gene length를 찾을 수 없습니다.")