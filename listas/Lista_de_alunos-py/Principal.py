from Lista import Lista # Importa a classe Lista

if __name__ == "__main__":
    l1 = Lista() 

    l1.adicionar_inicio("12345", "9") 
    l1.adicionar_inicio("54321", "8") 

    l1.adicionar_fim("67890", "6") 
    l1.adicionar_fim("09876", "7") 

    l1.mostrar_lista() 
    print()
    l1.remover_inicio() 
    l1.mostrar_lista() 
    print()
    l1.remover_fim() 
    l1.mostrar_lista() 
    print()
    l1.mostrar_nota("12345")
