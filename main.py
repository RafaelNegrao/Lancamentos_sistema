import pandas as pd

def planilha():
    #nome da planilha
    nome_arquivo = "estoque.xlsx"
    #df que recebe a planilha
    df = pd.read_excel(nome_arquivo, sheet_name='Sheet1')
    
    #a propriedade shape[0]conta a quantidade de linhas usadas na planilha
    #a propriedade shape[1] conta a quantidade de colunas
    num_linhas = df.shape[0] 

    lista_px = []
    print("Itens a serem comprados:")

    for x in range(num_linhas):
    #A propriedade at esta buscando a célula x(que é um numero variável do loop) ,na coluna quantidade  
        valor_comprado = df.at[x, "quantidade"]
        item_lista = df.at[x,"peixe"]
        lista_px.append(item_lista) 
        
        if valor_comprado<=50:
            print(f"{item_lista}  {valor_comprado}")
            df.at[x,"compra?"]= "sim"

    print("novamente")
    for a in range(num_linhas):
        print(lista_px[a])
    #vai salvar os dados alterados na planilha

    df.to_excel(nome_arquivo,index=False)

