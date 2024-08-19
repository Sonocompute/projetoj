import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Funções de geração de código
def gerar_codigo(opcao):
    """Gera código Python baseado na opção escolhida."""
    if opcao == 'Criar Função':
        return ("def minha_funcao(param1, param2):\n"
                "    # TODO: Adicione seu código aqui\n"
                "    pass")
    elif opcao == 'Ola mundo':
        return "print('Olá, Mundo!')"
    elif opcao == 'Soma':
        return ("def soma(a, b):\n"
                "    return a + b")
    elif opcao == 'Loop':
        return ("while True:\n"
                "    # Seu código aqui\n"
                "    pass")
    elif opcao == 'Condição':
        return ("if condicao:\n"
                "    print('Condição satisfeita')\n"
                "else:\n"
                "    print('Condição não satisfeita')")
    elif opcao == 'Array Soma':
        return ("def somar_array(arr):\n"
                "    soma = 0\n"
                "    for num in arr:\n"
                "        soma += num\n"
                "    return soma\n\n"
                "# Exemplo de uso:\n"
                "arr = [1, 2, 3, 4, 5]\n"
                "print(somar_array(arr))")
    elif opcao == 'Painel de Login':
        return ("import PySimpleGUI as sg\n\n"
                "def painel_login():\n"
                "    layout = [\n"
                "        [sg.Text('Usuário'), sg.Input(key='-USER-')],\n"
                "        [sg.Text('Senha'), sg.Input(key='-PASS-', password_char='*')],\n"
                "        [sg.Button('Login'), sg.Button('Cancelar')]\n"
                "    ]\n\n"
                "    window = sg.Window('Painel de Login', layout)\n\n"
                "    while True:\n"
                "        event, values = window.read()\n"
                "        if event in (sg.WIN_CLOSED, 'Cancelar'):\n"
                "            break\n"
                "        elif event == 'Login':\n"
                "            usuario = values['-USER-']\n"
                "            senha = values['-PASS-']\n"
                "            print(f'Usuário: {usuario}, Senha: {senha}')\n\n"
                "    window.close()\n\n"
                "painel_login()")
    elif opcao == 'Gerenciador de Tarefas':
        return ("import PySimpleGUI as sg\n\n"
                "def gerenciador_tarefas():\n"
                "    layout = [\n"
                "        [sg.Text('Gerenciador de Tarefas')],\n"
                "        [sg.Input(key='-TAREFA-', size=(25, 1)), sg.Button('Adicionar')],\n"
                "        [sg.Listbox([], size=(40, 10), key='-LISTA-')],\n"
                "        [sg.Button('Remover Selecionado'), sg.Button('Sair')]\n"
                "    ]\n\n"
                "    window = sg.Window('Gerenciador de Tarefas', layout)\n\n"
                "    tarefas = []\n"
                "    while True:\n"
                "        event, values = window.read()\n"
                "        if event == sg.WIN_CLOSED or event == 'Sair':\n"
                "            break\n"
                "        elif event == 'Adicionar':\n"
                "            tarefa = values['-TAREFA-']\n"
                "            if tarefa:\n"
                "                tarefas.append(tarefa)\n"
                "                window['-LISTA-'].update(tarefas)\n"
                "        elif event == 'Remover Selecionado':\n"
                "            selecionado = values['-LISTA-']\n"
                "            if selecionado:\n"
                "                tarefas.remove(selecionado[0])\n"
                "                window['-LISTA-'].update(tarefas)\n\n"
                "    window.close()\n\n"
                "gerenciador_tarefas()")
    elif opcao == 'Envio de Email':
        return ("import smtplib\n"
                "from email.mime.text import MIMEText\n"
                "from email.mime.multipart import MIMEMultipart\n\n"
                "def enviar_email():\n"
                "    remetente = 'seuemail@example.com'\n"
                "    destinatario = 'destinatario@example.com'\n"
                "    senha = 'sua_senha'\n\n"
                "    assunto = 'Assunto do Email'\n"
                "    corpo = 'Este é o corpo do email.'\n\n"
                "    mensagem = MIMEMultipart()\n"
                "    mensagem['From'] = remetente\n"
                "    mensagem['To'] = destinatario\n"
                "    mensagem['Subject'] = assunto\n\n"
                "    mensagem.attach(MIMEText(corpo, 'plain'))\n\n"
                "    with smtplib.SMTP('smtp.example.com', 587) as servidor:\n"
                "        servidor.starttls()\n"
                "        servidor.login(remetente, senha)\n"
                "        texto = mensagem.as_string()\n"
                "        servidor.sendmail(remetente, destinatario, texto)\n\n"
                "    print('Email enviado com sucesso!')\n\n"
                "# Execute o envio de email\n"
                "enviar_email()")
    elif opcao == 'Jogo Pac-Man':
        return ("import pygame\n"
                "import sys\n\n"
                "# Inicializar o Pygame\n"
                "pygame.init()\n\n"
                "# Configurações da tela\n"
                "SCREEN_WIDTH = 600\n"
                "SCREEN_HEIGHT = 600\n"
                "GRID_SIZE = 30\n"
                "SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))\n"
                "pygame.display.set_caption('Pac-Man')\n\n"
                "# Cores\n"
                "BLACK = (0, 0, 0)\n"
                "YELLOW = (255, 255, 0)\n"
                "WHITE = (255, 255, 255)\n\n"
                "# FPS\n"
                "FPS = 10\n"
                "clock = pygame.time.Clock()\n\n"
                "# Classe para o Pac-Man\n"
                "class PacMan:\n"
                "    def __init__(self):\n"
                "        self.x = SCREEN_WIDTH // 2\n"
                "        self.y = SCREEN_HEIGHT // 2\n"
                "        self.size = GRID_SIZE\n"
                "        self.color = YELLOW\n"
                "        self.direction = 'RIGHT'\n\n"
                "    def draw(self):\n"
                "        # Desenha o Pac-Man como um arco (face incompleta)\n"
                "        pygame.draw.arc(SCREEN, self.color, (self.x, self.y, self.size, self.size), 0.2, 2.8, 0)\n\n"
                "    def move(self):\n"
                "        if self.direction == 'UP':\n"
                "            self.y -= GRID_SIZE\n"
                "        elif self.direction == 'DOWN':\n"
                "            self.y += GRID_SIZE\n"
                "        elif self.direction == 'LEFT':\n"
                "            self.x -= GRID_SIZE\n"
                "        elif self.direction == 'RIGHT':\n"
                "            self.x += GRID_SIZE\n\n"
                "        # Restringir o movimento dentro da tela\n"
                "        if self.x < 0: self.x = SCREEN_WIDTH - GRID_SIZE\n"
                "        if self.x >= SCREEN_WIDTH: self.x = 0\n"
                "        if self.y < 0: self.y = SCREEN_HEIGHT - GRID_SIZE\n"
                "        if self.y >= SCREEN_HEIGHT: self.y = 0\n\n"
                "# Função para desenhar o labirinto\n"
                "def draw_maze():\n"
                "    for x in range(0, SCREEN_WIDTH, GRID_SIZE):\n"
                "        pygame.draw.line(SCREEN, WHITE, (x, 0), (x, SCREEN_HEIGHT))\n"
                "    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):\n"
                "        pygame.draw.line(SCREEN, WHITE, (0, y), (SCREEN_WIDTH, y))\n\n"
                "# Função principal do jogo\n"
                "def main():\n"
                "    pacman = PacMan()\n"
                "    while True:\n"
                "        for event in pygame.event.get():\n"
                "            if event.type == pygame.QUIT:\n"
                "                pygame.quit()\n"
                "                sys.exit()\n"
                "            elif event.type == pygame.KEYDOWN:\n"
                "                if event.key == pygame.K_UP:\n"
                "                    pacman.direction = 'UP'\n"
                "                elif event.key == pygame.K_DOWN:\n"
                "                    pacman.direction = 'DOWN'\n"
                "                elif event.key == pygame.K_LEFT:\n"
                "                    pacman.direction = 'LEFT'\n"
                "                elif event.key == pygame.K_RIGHT:\n"
                "                    pacman.direction = 'RIGHT'\n\n"
                "        SCREEN.fill(BLACK)\n"
                "        draw_maze()\n"
                "        pacman.move()\n"
                "        pacman.draw()\n\n"
                "        pygame.display.update()\n"
                "        clock.tick(FPS)\n\n"
                "if __name__ == '__main__':\n"
                "    main()")
    elif opcao == 'Calculadora Simples':
        return ("def calculadora():\n"
                "    while True:\n"
                "        print('Escolha a operação:')\n"
                "        print('1. Adição')\n"
                "        print('2. Subtração')\n"
                "        print('3. Multiplicação')\n"
                "        print('4. Divisão')\n"
                "        print('5. Sair')\n"
                "        opcao = input('Digite a opção (1/2/3/4/5): ')\n\n"
                "        if opcao == '5':\n"
                "            break\n\n"
                "        if opcao in ['1', '2', '3', '4']:\n"
                "            num1 = float(input('Digite o primeiro número: '))\n"
                "            num2 = float(input('Digite o segundo número: '))\n\n"
                "            if opcao == '1':\n"
                "                resultado = num1 + num2\n"
                "                print(f'Resultado: {resultado}')\n"
                "            elif opcao == '2':\n"
                "                resultado = num1 - num2\n"
                "                print(f'Resultado: {resultado}')\n"
                "            elif opcao == '3':\n"
                "                resultado = num1 * num2\n"
                "                print(f'Resultado: {resultado}')\n"
                "            elif opcao == '4':\n"
                "                if num2 != 0:\n"
                "                    resultado = num1 / num2\n"
                "                    print(f'Resultado: {resultado}')\n"
                "                else:\n"
                "                    print('Erro: Divisão por zero!')\n\n"
                "        else:\n"
                "            print('Opção inválida!')\n\n"
                "# Execute a calculadora\n"
                "calculadora()")
    elif opcao == 'Leitura de Arquivo e Contagem de Palavras':
        return ("def count_words(filename): \n \n"
                "try:\n"
                "with open(filename, 'r') as file: \n"
                "text = file.read()\n"
                "words = text.split()\n"
                "return len(words)\n"
                "except FileNotFoundError:\n"  
                "return 'Arquivo não encontrado'\n"              
                "filename = input('Digite o nome do arquivo: ')\n"
                "print('Número de palavras:'', count_words(filename))\n"
                
                
                
                
                
                
                )  
    elif opcao == 'Fatorial de um Número':
        return ("def factorial(n):\n"
                "if n == 0:\n"
                "return 1\n"
                "else:\n"
                "return n * factorial(n-1)\n"
                "number = int(input('Digite um número para calcular o fatorial: '))\n"
                "if number >= 0:\n"
                "print(f'O fatorial de {number} é {factorial(number)}')\n"
                "else:\n"
                " print('Número deve ser não-negativo.')\n"
                )    
    elif opcao == 'Contar Palavras em uma String' :
        return ('texto = input("Digite uma string: ")\n'
                'palavras = texto.split()\n'
                'print(f"Número de palavras: {len(palavras)}")\n'
                )
    elif opcao == 'Verificar Número Primo':
        return ("def is_prime(n):\n"
                "if n <= 1:\n"
                "return False\n"                
                "for i in range(2, int(n**0.5) + 1):\n"
                "if n % i == 0:\n"
                "return False\n"
                "return True\n"
                "num = int(input('Digite um número: '))\n"
                "if is_prime(num):\n"
                "print(f'{num} é um número primo.')\n"
                "else:\n"
                " print(f'{num} não é um número primo.')\n"
                )                      
    elif opcao == 'Jogo da Forca':
        return ("import random\n\n"
                "def jogar_forca():\n"
                "    palavras = ['python', 'programacao', 'desenvolvimento', 'computador']\n"
                "    palavra = random.choice(palavras).upper()\n"
                "    letras_erradas = []\n"
                "    letras_corretas = []\n\n"
                "    while True:\n"
                "        palavra_oculta = ''.join([letra if letra in letras_corretas else '_' for letra in palavra])\n"
                "        print(f'Palavra: {palavra_oculta}')\n"
                "        print(f'Letras erradas: {', '.join(letras_erradas)}')\n\n"
                "        if '_' not in palavra_oculta:\n"
                "            print('Parabéns! Você venceu!')\n"
                "            break\n\n"
                "        tentativa = input('Digite uma letra: ').upper()\n\n"
                "        if tentativa in letras_erradas or tentativa in letras_corretas:\n"
                "            print('Você já tentou essa letra.')\n"
                "            continue\n\n"
                "        if tentativa in palavra:\n"
                "            letras_corretas.append(tentativa)\n"
                "        else:\n"
                "            letras_erradas.append(tentativa)\n\n"
                "        if len(letras_erradas) >= 6:\n"
                "            print('Você perdeu!')\n"
                "            print(f'A palavra era: {palavra}')\n"
                "            break\n\n"
                "# Iniciar o jogo\n"
                "jogar_forca()")
    # Novas opções adicionadas
    elif opcao == 'Ordenar Lista':
        return ("def ordenar_lista(lista):\n"
                "    return sorted(lista)\n\n"
                "# Exemplo de uso:\n"
                "lista = [3, 1, 4, 1, 5, 9]\n"
                "print(ordenar_lista(lista))")
    elif opcao == 'Conversão de Temperatura':
        return ("def converter_temperatura(celsius):\n"
                "    fahrenheit = (celsius * 9/5) + 32\n"
                "    return fahrenheit\n\n"
                "# Exemplo de uso:\n"
                "celsius = 25\n"
                "print(f'{celsius}°C em Fahrenheit é {converter_temperatura(celsius)}°F')")
    elif opcao == 'Verificar Palíndromo':
        return ("def verificar_palindromo(palavra):\n"
                "    palavra = palavra.lower()\n"
                "    return palavra == palavra[::-1]\n\n"
                "# Exemplo de uso:\n"
                "print(verificar_palindromo('arara'))")
    elif opcao == 'Contar Palavras':
        return ("def contar_palavras(texto):\n"
                "    return len(texto.split())\n\n"
                "# Exemplo de uso:\n"
                "texto = 'Olá, quantas palavras há aqui?'\n"
                "print(contar_palavras(texto))")
    elif opcao == 'Converter Texto para Maiúsculas':
        return ("def converter_maiusculas(texto):\n"
                "    return texto.upper()\n\n"
                "# Exemplo de uso:\n"
                "texto = 'texto para maiúsculas'\n"
                "print(converter_maiusculas(texto))")
        
   
    else:
        return "Código não disponível para a opção selecionada."
    

# Função para abrir a janela de código
def mostrar_codigo(opcao):
    """Cria uma janela para exibir o código baseado na opção escolhida."""
    codigo = gerar_codigo(opcao)
    
    # Cria uma nova janela para mostrar o código
    janela_codigo = tk.Toplevel()
    janela_codigo.title(f"Código para: {opcao}")
    janela_codigo.config(bg='black')

    # Adiciona um widget de rolagem de texto
    texto_codigo = scrolledtext.ScrolledText(janela_codigo, wrap=tk.WORD, width=90, height=25, bg='black', fg='green')
    texto_codigo.insert(tk.END, codigo)
    texto_codigo.config(state=tk.DISABLED)
    texto_codigo.pack(expand=True, fill=tk.BOTH)

# Função para abrir a janela principal
def janela_principal():
    """Cria a janela principal com a lista de opções."""
    janela = tk.Tk()
    janela.title("Selecione um Código")
    janela.config(bg='black')

    opcoes = [
        'Criar Função',
        'Imprimir',
        'Soma',
        'Loop',
        'Condição',
        'Array Soma',
        'Painel de Login',
        'Gerenciador de Tarefas',
        'Envio de Email',
        'Jogo Pac-Man',
        'Calculadora Simples',
        'Jogo da Forca',
        'Ordenar Lista',
        'Conversão de Temperatura',
        'Verificar Palíndromo',
        'Contar Palavras',
        'Converter Texto para Maiúsculas',
        'Leitura de Arquivo e Contagem de Palavras',
        'Contar Palavras em uma String',
        'Verificar Número Primo'
    ]
    

    def opcao_selecionada(event):
    
        opcao = lista_opcoes.get(tk.ACTIVE)
        if opcao:
            mostrar_codigo(opcao)

    # Adiciona um widget Listbox para exibir as opções
    lista_opcoes = tk.Listbox(janela, width=80, height=15, bg='black', fg='white', selectmode=tk.SINGLE)
    lista_opcoes.pack(padx=30, pady=30)
    
    # Preenche a Listbox com as opções
    for opcao in opcoes:
        lista_opcoes.insert(tk.END, opcao)
    
    # Adiciona um botão para exibir o código
    botao_mostrar = tk.Button(janela, text="Mostrar Código", command=lambda: opcao_selecionada(None), bg='gray', fg='white')
    botao_mostrar.pack(pady=10)
    
    # Configura o evento de clique na Listbox para mostrar o código
    lista_opcoes.bind('<Double-1>', opcao_selecionada)
    
    janela.mainloop()

# Executa a função principal para iniciar a aplicação
if __name__ == "__main__":
    janela_principal()
                
                
                
                
