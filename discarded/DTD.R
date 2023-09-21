#사용자가 입력해야할것들
input <- read.table("input.txt")
#첫번째 파일 유전자수
ng1 <- input[1, 1]

#첫번째 파일 환자수(알파벳으로)
np_str <- input[2, 1]
#두번째 파일 유전자수
ng2 <- input[3, 1]

# 엑셀 파일 경로를 지정합니다.
excel_file <- input[4, 1]
sht1 <- str(input[5, 1])
sht2 <- input[6, 1]

# readxl 패키지를 불러옵니다.
library(readxl)

range_pg <- paste0("B1:", np_str, as.character(ng1))
range_rowname <- paste0("A2:A", as.character(ng1))
range_colname <- paste0("B1:", np_str, "1")
range_len <- paste0("J1:K", as.character(ng2))

# 엑셀 파일의 데이터를 불러옵니다.
data_pg <- read_excel(excel_file, range <- range_pg, sheet <- sht1, col_names <- TRUE)
data_rowname <- read_excel(excel_file, range <- range_rowname, sheet <- sht1, col_names <- FALSE)
data_colname <- read_excel(excel_file, range <- range_colname, sheet <- sht1, col_names <- FALSE)

ng1 <- ng1 - 1

# 환자수 np
np <- ncol(data_pg) # 열의 수

# dim을 설정합니다.
dim <- c(ng1,  np)

# 배열을 생성합니다.
arr <- array(dim <- dim)

# 첫 번째 "면"에 data_pg 데이터를 할당합니다.
arr <- as.matrix(data_pg)

gene_id <- unlist(data_rowname)

dimnames(arr) <- list(
  unlist(data_rowname),     # 첫 번째 차원(행)의 이름
  unlist(data_colname)    # 두 번째 차원(열)의 이름)
)

# 데이터를 엑셀 파일에서 읽어옵니다.
data_len_2 <- read_excel(excel_file,  range <- range_len,  sheet <- sht2)
ng2 <- ng2 - 1

# 데이터를 배열에 저장합니다.
data_len_1 <- as.matrix(data_len_2)

# date 배열 생성
data_len <- matrix(as.integer(data_len_1[,  2]),  nrow <- ng2,  ncol <- 1)

data_len_name <- rep(0,  ng2)

for(i in 1:ng2)
{
	if(!is.na(data_len_1[i, 1]))
	{
		data_len_name[i] <- data_len_1[i, 1]
	}
	else
	{
		data_len_name[i] <- as.character(i+1000)
	}
}

# 열의 이름 지정

dimnames(data_len) <- list(
  unlist(data_len_name),     # 첫 번째 차원(행)의 이름
  c("len")    # 두 번째 차원(열)의 이름)
)

k <- 0

gene_out <- array(dim <- c(ng2,  np,  4))

out_row <- rep(0,  ng2)


total_rpk <- rep(0,  np)

gene_sum <- apply(arr, 2, sum)

for( i in data_len_1[,  1])
{
	if( i %in% gene_id)
	{
		k <- k + 1

		for(j in 1:np)
		{
			gene_out[k, j, 1] <- (arr[i, j]/gene_sum[j]) * 1000000
			gene_out[k, j, 2] <- gene_out[k, j, 1] * 1000 / data_len[i, ]
			gene_out[k, j, 3] <- arr[i,  j] * 1000 / data_len[i, ]
			
			total_rpk[j] <- total_rpk[j] + gene_out[k, j, 3]
			
			out_row[k] <- i
		}
	}
}

for( i in 1:k)
{
	for(j in 1:np)
	{
		gene_out[i, j, 4] <- gene_out[i, j, 3] * 1000000 / total_rpk[j]
	}
}

dimnames(gene_out) <- list(
  unlist(out_row),     # 첫 번째 차원(유전자)의 이름
  unlist(data_colname),     # 두 번째 차원(열)의 이름
  c("rpm",  "rpkm",  "rpk",  "tpm")
)

# 필요한 패키지 불러오기
library(openxlsx)

# 엑셀 파일 생성
wb <- createWorkbook()

# 시트 추가
addWorksheet(wb,  sheetName <- "Gene_Out")



# 유전자 이름 쓰기 (세로로 출력)
for(j in 1:np)
{
	writeData(wb,  sheet <- "Gene_Out",  x <- unlist(data_colname[1, j]),  startRow <- 1,  startCol <- 2+2*j)
}

# 유전자 값 쓰기
for(i in 1:k)
{
	writeData(wb,  sheet <- "Gene_Out",  x <- out_row[i],  startRow <- -3+6*i,  startCol <- 1)
	writeData(wb,  sheet <- "Gene_Out",  x <- "lead",  startRow <- -3+6*i,  startCol <- 2)
	writeData(wb,  sheet <- "Gene_Out",  x <- "RPM",  startRow <- -2+6*i,  startCol <- 2)
	writeData(wb,  sheet <- "Gene_Out",  x <- "RPKM",  startRow <- -1+6*i,  startCol <- 2)
	writeData(wb,  sheet <- "Gene_Out",  x <- "RPK",  startRow <- +6*i,  startCol <- 2)
	writeData(wb,  sheet <- "Gene_Out",  x <- "TPM",  startRow <- 1+6*i,  startCol <- 2)

	for(j in 1:np)
	{
		writeData(wb,  sheet <- "Gene_Out",  x <- arr[out_row[i], j],  startRow <- -3+6*i,  startCol <- 2+2*j)
		writeData(wb,  sheet <- "Gene_Out",  x <- gene_out[i,  j,  1],  startRow <- -2+6*i,  startCol <- 2+2*j)
		writeData(wb,  sheet <- "Gene_Out",  x <- gene_out[i,  j,  2],  startRow <- -1+6*i,  startCol <- 2+2*j)
		writeData(wb,  sheet <- "Gene_Out",  x <- gene_out[i,  j,  3],  startRow <- 6*i,  startCol <- 2+2*j)
		writeData(wb,  sheet <- "Gene_Out",  x <- gene_out[i,  j,  4],  startRow <- 1+6*i,  startCol <- 2+2*j)
	

	}
}

# 파일 저장
saveWorkbook(wb,  file <- "output.xlsx")