# Define a classe Evento
# Define a classe chamada 'Evento'.
class Evento:
    
    # Define o método inicializador '__init__' da classe Evento.
    # Este método é chamado automaticamente ao criar uma nova instância da classe.
    def __init__(self, capacidade = 10):
        
        # Inicializa o atributo 'capacidade' da instância com o valor fornecido como argumento.
        # Se nenhum valor for fornecido, utiliza o valor padrão de 10.
        self.capacidade = capacidade
        
        # Inicializa o atributo 'lugares_disponiveis' com o mesmo valor da 'capacidade' inicial.
        # Isso é feito porque inicialmente todos os lugares estão disponíveis.
        self.lugares_disponiveis = capacidade
        
    # Define o método 'reservar', que é usado para reservar um lugar no evento.
    def reservar(self):
        
        # Verifica se o número de 'lugares_disponiveis' é maior que zero.
        if self.lugares_disponiveis > 0:
            
            # Diminui o atributo 'lugares_disponiveis' em 1 para representar a reserva de um lugar.
            self.lugares_disponiveis -= 1
            
            # Imprime uma mensagem informando que a reserva foi realizada com sucesso.
            print(f"A reserva foi feita com sucesso.")
            
        # Se for zero, isso significa que não há lugares disponíveis para reserva.
        else:
            
            # Imprime uma mensagem informando o usuário que não há lugares disponíveis para reserva.
            print(f"Não há reservas disponíveis.")
            
    # Define o método 'cancelar', que é usado para cancelar uma reserva existente.
    def cancelar(self):
        
        # Verifica se o número de 'lugares_disponiveis' é menor que a 'capacidade' total.
        if self.lugares_disponiveis < 10:
            
            # Aumenta o atributo 'lugares_disponiveis' em 1 para representar o cancelamento de uma reserva.
            self.lugares_disponiveis += 1
            
            # Imprime uma mensagem informando que a reserva foi cancelada com sucesso.
            print(f"A reserva foi cancelada com sucesso.")
            
        # Se for igual a 'capacidade' total, isso significa que não há reservas para cancelar.
        else:
            
            # Imprime uma mensagem informando que não há reservas para cancelar.
            print(f"Não há reservas para cancelar.")
            
    # Define o método 'mostrar_lugares_disponiveis', que é usado para mostrar o 
    # número de lugares disponíveis.
    def lugar_disponiveis(self):
        
        # Retorna uma string formatada que inclui o número atual de 'lugares_disponiveis'.
        print(f"Reservas disponíveis: {self.lugares_disponiveis}")
        
# Testando a classe
evento = Evento()

print("Reservas para um Evento")

# Enquanto verdadeiro, o menu ficará em execução
while True:
    
    print()
    
    # Imprime as opções do menu
    print("Menu")
    
    print()
    
    print("1 - Reservar um lugar")
    
    print("2 - Cancelar uma reserva")
    
    print("3 - Vagas disponíveis")
    
    print("4 - Sair")
    
    print()
    
    # Solicita ao usuário que escolha uma opção
    op = input("Escolha a opção desejada: ")
    
    print()
    
    if op == "1":
        
        # Chamando o método 'reservar' da instância 'evento'
        evento.reservar()
        
    elif op == "2":
        
        # Chamando o método 'cancelar' da instância 'evento'
        evento.cancelar()
        
    elif op == "3":
        
        # Chamando o método 'lugar_disponiveis' da instância 'evento'
        evento.lugar_disponiveis()
        
    elif op == "4":

        # Informa que o Programa está sendo Encerrado
        print(f"Encerrando o Programa")
        
        # Encerra o Programa
        break
        
    # Se não for digitada uma Opção Válida
    else:

        # Informa que foi digitada uma Opção Inválida
        print("Opção Inválida!")
