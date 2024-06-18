from restaurante import Restaurante
from avaliacao import Avaliacao

restaurantes = []

def cadastrar_restaurante():
    nome = input ("Nome do restaurante:")
    tipo_cozinha = input ("Tipo de cozinha")
    restaurante = Restaurante(nome, tipo_cozinha)
    restaurantes.append(restaurante)
    print("Restaurante cadastrado com sucesso!")

    def listar_restaurantes():
     if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    for i, restaurante in enumerate(restaurantes):
        print(f"{i + 1}. {restaurante}")

    def avaliar_restaurantes():
       listar_restaurantes()
       escolha = int(input("Escolha o número do restauran te que deseja avaliar:")) -1 
       if 0 <= escolha < len(restaurantes):
          nota = int(input("Nota (1-5): "))
          comentario = input("Comentario:")
          avaliacao = Avaliacao(nota,comentario)
          restaurantes[escolha].adicionar_avaliacao(avaliacao)
          print("Avaliacao adicionada com secesso!")
       else:
          print("Escolha inválida.")

    def ativar_desativar_restaurante():
        listar_restaurantes()
    escolha = int(input("Escolha o número do restaurante que deseja ativar/desativar: ")) - 1
    if 0 <= escolha < len(restaurantes):
        if restaurantes[escolha].ativo:
            restaurantes[escolha].desativar()
            print("Restaurante desativado com sucesso!")
        else:
            restaurantes[escolha].ativar()
            print("Restaurante ativado com sucesso!")
    else:
        print("Escolha inválida.")

    def main():
       while True:
          print("\nRESTAURANTE EXPRESS")
          print("1)Cadastrar Restaurante")
          print("2)listar Restaurante")
          print("3)Avaliar Restaurante")
          print("4)Ativar/Desativar Restaurante")
          print("5)Sair")
          escolhas = input ("Escolha uma opção:")

          
          if escolha == '1':
            cadastrar_restaurante()
          elif escolha =='2':
             listar_restaurantes()
          elif escolha =='3':
             avaliar_restaurantes()
          elif escolha == '4': 
                ativar_desativar_restaurante()
          elif escolha =='5': 
             print("Saindo...")
             break
          else:
             print ("Saindo inválida. Tente novamente.")

          
          if __name__=="_main_":
            main()
