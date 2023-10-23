def test_pesquisa_sem_resultados():
    nome_hotel = "trivago"
    base_de_dados_hoteis = ["Hotel A", "Hotel B", "Hotel C"]
    if nome_hotel not in base_de_dados_hoteis:
        print(f"O hotel '{nome_hotel}' foi encontrado na busca.")
    else:
        print(f"Desculpe, não encontramos resultados para o hotel '{nome_hotel}'.")

test_pesquisa_sem_resultados()
