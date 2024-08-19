import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Funções de geração de código
def gerar_codigo(opcao):
    """Gera código JAVA baseado na opção escolhida."""
    if opcao == 'Soma de Dois Números':
        return ("import java.util.Scanner;\n"
                "\n"
                "   public class Soma {\n"
                "       public static void main(String[] args) {\n"
                "       Scanner scanner = new Scanner(System.in);\n"
                "       System.out.print('Digite o primeiro número: ');\n"
                "       int num1 = scanner.nextInt();\n"
                "       System.out.print('Digite o segundo número: ');\n"
                "       int num2 = scanner.nextInt();\n"
                "       int soma = num1 + num2;\n"
                "       System.out.println('A soma é: ' + soma);\n"
                "}\n"
                "}\n"
                "\n"
                "\n"
                "\n"
                "\n"
                )
    elif opcao == 'Ola mundo':
        return ("public class HelloWorld { \n"
                "   public static void main(String[] args) {\n"
                "       System.out.println('Olá, Mundo!'');\n"
                "}\n"
                "}\n"
                  )
    
    
    
    
    
    elif opcao == 'Gerenciador de Tarefas':
        return ("import java.util.ArrayList;\n"
                "import java.util.Scanner;\n"
                "\n"
                "public class GerenciadorDeTarefas {\n"
                "   private static ArrayList<String> tarefas = new ArrayList<>();\n"
                "\n"
                "   public static void main(String[] args) {\n"
                "       Scanner scanner = new Scanner(System.in);\n"
                "       int opcao;\n"
                "\n"
                "do {\n"
                "       System.out.println('Gerenciador de Tarefas');\n"
                "       System.out.println('1. Adicionar tarefa');\n"
                "       System.out.println('2. Listar tarefas');\n"
                "       System.out.println('3. Remover tarefa');\n"
                "       System.out.println('4. Sair');\n"
                "       opcao = scanner.nextInt();\n"
                "       scanner.nextLine(); // Limpar o buffer\n"
                "\n"
                "       switch (opcao) {\n"
                "           case 1:\n"
                "                  adicionarTarefa(scanner);\n"
                "                  break;\n"
                "           case 2:\n"
                "                  listarTarefas();\n"
                "                  break;\n"
                "           case 3:\n"
                "                  removerTarefa(scanner);\n"
                "                  break;\n"
                "           case 4:n"
                "                  System.out.println('Saindo...');\n"
                "                  break;\n"
                "                  default:\n"
                "                  System.out.println('Opção inválida. Tente novamente.');\n"
                "                  break;\n"
                "\n"
                "       }\n"
                "\n"
                " } while (opcao != 4);\n"
                "\n"
                "   scanner.close();\n"
                "\n"
                " }\n"
                "\n"
                "private static void adicionarTarefa(Scanner scanner) {\n"
                "   System.out.print('Digite a tarefa: ');\n"
                "   String tarefa = scanner.nextLine();\n"
                "   tarefas.add(tarefa);\n"
                "   System.out.println('Tarefa adicionada com sucesso!');\n"
                " }\n"
                " private static void listarTarefas() {\n"
                "   if (tarefas.isEmpty()) {\n"
                "   System.out.println('Nenhuma tarefa encontrada.');\n"
                "   } else {\n"
                "          System.out.println('Lista de Tarefas:'');\n"
                "          for (int i = 0; i < tarefas.size(); i++) {\n"
                "              System.out.println((i + 1) + '. ' + tarefas.get(i));\n"
                "           }\n"
                "       }\n"
                "}\n"
                "\n"
                "private static void removerTarefa(Scanner scanner) {\n"
                "   listarTarefas();\n"
                "   if (!tarefas.isEmpty()) {\n"
                "       System.out.print('Digite o número da tarefa a ser removida: ');\n"
                "       int indice = scanner.nextInt();\n"
                "       scanner.nextLine(); // Limpar o buffer\n"
                "\n"
                "   if (indice > 0 && indice <= tarefas.size()) {\n"
                "        tarefas.remove(indice - 1);\n"
                "       System.out.println('Tarefa removida com sucesso!');\n"
                " } else {\n"
                "           System.out.println('Número inválido. Nenhuma tarefa removida.');\n"
                "}\n"
                "}\n"
                "}\n"
                "}\n"
 )
    
    
    
    
    
    elif opcao == 'Painel de Login':
        return ("import javax.swing.*;\n"
                "import java.awt.*;\n"
                "import java.awt.event.ActionEvent;\n"
                "import java.awt.event.ActionListener;\n"
                "\n"
                "public class PainelDeLogin {\n"
                "\n"
                "public static void main(String[] args) {\n"
                " // Criação do JFrame (janela principal)\n"
                "JFrame frame = new JFrame('Painel de Login');\n"
                "frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\n"
                "frame.setSize(300, 200);\n"
                "frame.setLayout(new GridBagLayout());\n"
                "\n"
                "// Configuração do GridBagLayout\n"
                " GridBagConstraints gbc = new GridBagConstraints();\n"
                "gbc.insets = new Insets(10, 10, 10, 10); // Espaçamento entre os componentes\n"
                " gbc.anchor = GridBagConstraints.WEST; // Alinha os componentes à esquerda\n"
                "\n"
                " // Adicionando componentes à janela\n"
                "\n"
                "// Rótulo e campo de nome de usuário\n"
                "JLabel userLabel = new JLabel('Usuário:');\n"
                "gbc.gridx = 0;\n"
                "gbc.gridy = 0;\n"
                "frame.add(userLabel, gbc);\n"
                "\n"
                "JTextField userField = new JTextField(15);\n"
                "gbc.gridx = 1;\n"
                "gbc.gridy = 0;\n"
                "frame.add(userField, gbc);\n"
                "\n"
                "// Rótulo e campo de senha\n"
                "JLabel passwordLabel = new JLabel('Senha:');\n"
                "gbc.gridx = 0;\n"
                "gbc.gridy = 1;\n"
                "frame.add(passwordLabel, gbc);\n"
                "\n"
                "JPasswordField passwordField = new JPasswordField(15);\n"
                "gbc.gridx = 1;\n"
                "gbc.gridy = 1;\n"
                "frame.add(passwordField, gbc);\n"
                "\n"
                "// Botão de login\n"
                "JButton loginButton = new JButton('Login');\n"
                "gbc.gridx = 1;\n"
                "gbc.gridy = 2;\n"
                "gbc.anchor = GridBagConstraints.EAST;\n"
                "frame.add(loginButton, gbc);\n"
                "\n"
                "// Adicionando ação ao botão de login\n"
                "loginButton.addActionListener(new ActionListener() {\n"
                "       @Override\n"
                "       public void actionPerformed(ActionEvent e) \n"
                "          String usuario = userField.getText();\n"
                "          char[] senha = passwordField.getPassword();\n"
                "          // Aqui você pode adicionar a lógica de autenticação\n"
                "          if (autenticar(usuario, senha)) {\n"
                "              JOptionPane.showMessageDialog(frame, 'Login bem-sucedido!');\n"
                "           } else {\n"
                "               JOptionPane.showMessageDialog(frame, 'Usuário ou senha incorretos.');\n"
                "           }\n"
                "       }\n"
                "});\n"
                "\n"
                "// Exibir a janela\n"
                "frame.setVisible(true);\n"
                "}\n"
                "\n"
                "// Método de autenticação fictício\n"
                " private static boolean autenticar(String usuario, char[] senha) {\n"
                "    // Usuário e senha fictícios para teste\n"
                "    String usuarioCorreto = 'admin';\n"
                "    String senhaCorreta = 'senha123';\n"
                "\n"
                "    return usuarioCorreto.equals(usuario) && senhaCorreta.equals(new String(senha));\n"
                "   }\n"
                "}\n"
                
                )
        
        
        
        
        
        
        
    elif opcao == 'Imprimir Números de 1 a 10':
        return ("public class Contar {\n"
                    "public static void main(String[] args) {\n" 
                    "   for (int i = 1; i <= 10; i++) {\n" 
                    "       System.out.println(i);\n" 
               "        }\n" 
               "      }\n"      
               "}\n" 
            )
    
    
    
    
    elif opcao == 'Encontrar o Maior Elemento em um Array':
        return("public class MaiorElemento {\n"
               "   public static void main(String[] args) {\n"
               "        int[] array = {3, 5, 7, 2, 8};\n"
               "        int maior = array[0];\n"
               "        for (int i : array) {\n"
               "            if (i > maior) {\n"
               "                maior = i;\n"
               "            }\n"
               "        }\n"
               "        System.out.println('O maior elemento é: ' + maior);\n"
               "    }\n"
               "}n"
         )
    elif opcao == 'Array':
        return ("public class ExemploArray {\n"
                "   // Declaração e inicialização de um array de inteiros com 5 elementos\n"
                "   int[] numeros = new int[5];\n"
                "\n"
                "   // Atribuindo valores ao array\n"
                "\n"
                "   numeros[0] = 10;\n"
                "   numeros[1] = 20;\n"
                "   numeros[2] = 30;\n"
                "   numeros[3] = 40;\n"
                "   numeros[4] = 50;\n"
                "\n"
                "   // Exibindo os valores do array\n"
                "   System.out.println('Valores do array:');\n"
                "   for (int i = 0; i < numeros.length; i++) {\n"
                "       System.out.println('Elemento na posição ' + i + ': ' + numeros[i]);\n"
                "   }\n"
                "\n"
                "   // Inicialização direta do array com valores\n"
                "   int[] maisNumeros = {100, 200, 300, 400, 500};\n"
                "\n"
                "// Exibindo os valores do array inicializado diretamente\n"
                "System.out.println('Valores do array inicializado diretamente:');\n"
                "for (int num : maisNumeros) {\n"
                "   System.out.println(num);\n"
                "}\n"
                )                   
    elif opcao == 'Classe e Objeto Simples':
        return ("class Pessoa {\n"
                "   String nome;\n"
                "   int idade;\n"
                "\n"
                "\n"
                "   void apresentar() {\n"
                "        System.out.println('Olá, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos.');\n"
                " }\n"
                "\n"
                "void definirIdade(int novaIdade) {\n"
                "   idade = novaIdade;\n"
                "}\n"
                "\n"
                "void definirNome(String novoNome) {\n"
                "   nome = novoNome;\n"
                "  }\n"
                "}\n"
                "\n"
                "public class Main {\n"
                "    public static void main(String[] args) {\n"
                "\n"
                "   Pessoa pessoa1 = new Pessoa();\n"
                "\n"
                "   pessoa1.definirNome('João');\n"
                "\n"
                "   pessoa1.definirIdade(25);\n"
                "\n"
                "   pessoa1.apresentar();\n"
                "\n"
                "   Pessoa pessoa2 = new Pessoa();\n"
                "\n"
                "   pessoa2.definirNome('Maria');\n"
                "   pessoa2.definirIdade(30);\n"
                "\n"
                "   pessoa2.apresentar();\n"
                "   }\n"
                "}\n"
                "\n"
                "\n"
                "\n"
                "\n"
                "\n"
                )
    elif opcao == 'Leitura e Escrita em Arquivo':
        return ("import java.io.*;\n"
                "\n"
                "public class LeituraEscritaArquivo {\n"
                "   public static void main(String[] args) {\n"
                "   String texto = 'Olá, este é um texto de exemplo!';\n"
                "    try {\n"
                "         // Escrita em arquivo\n"
                "         FileWriter escritor = new FileWriter('exemplo.txt');\n"
                "         escritor.write(texto);\n"
                "         escritor.close();\n"
                "\n"
                "         // Leitura do arquivo\n"
                "         FileReader leitor = new FileReader('exemplo.txt');\n"
                "         BufferedReader bufferedReader = new BufferedReader(leitor);\n"
                "         String linha;\n"
                "         while ((linha = bufferedReader.readLine()) != null) {\n"
                "            System.out.println(linha);\n"
                "          }\n"
                "          bufferedReader.close();\n"
                "       } catch (IOException e) {\n"
                "            e.printStackTrace();\n"
                "       }\n"
                "   }\n"
                "}\n"
                )   
    elif opcao == 'Contagem Regressiva':
        return ("public class ContagemRegressiva {\n"
                "   public static void main(String[] args) {\n"
                "       for (int i = 10; i >= 0; i--) {\n"
                "       System.out.println(i);\n"
                "       try {\n"
                "           Thread.sleep(1000); // Pausa de 1 segundo\n"
                "       } catch (InterruptedException e) {\n"
                "            e.printStackTrace();\n"
                "       }\n"
                "      }\n"
                "      System.out.println('Fim!');\n"
                "   }\n"
                "}\n"
                )
    elif opcao == 'Tabela de Multiplicação':
        return ("public class TabelaMultiplicacao {\n"
                "    public static void main(String[] args) {\n"
                "        for (int i = 1; i <= 10; i++) {\n"
                "             for (int j = 1; j <= 10; j++) {\n"
                "                   System.out.printf('%4d', i * j);\n"
                "              }\n"
                "              System.out.println();\n"
                "           }\n"
                "        }\n"
                "}\n"
        )
    elif opcao == 'Calculadora Simples':
        return ("import java.util.Scanner;\n"
                "\n"
                "public class Calculadora {\n"
                "   public static void main(String[] args) {\n"
                "       Scanner scanner = new Scanner(System.in);\n"
                "       System.out.print('Digite o primeiro número: ');\n"
                "       double num1 = scanner.nextDouble();\n"
                "       System.out.print('Digite o segundo número: ');\n"
                "       double num2 = scanner.nextDouble();\n"
                "       System.out.print('Escolha a operação (+, -, *, /): ');\n"
                "       char operacao = scanner.next().charAt(0);\n"
                "\n"
                "       double resultado;\n"
                "       switch (operacao) {\n"
                "            case '+':\n"
                "                 resultado = num1 + num2;\n"
                "                 break;\n"
                "            case '-':\n"
                "                 resultado = num1 - num2;\n"
                "                  break;\n"
                "            case '*':\n"
                "                  resultado = num1 * num2;\n"
                "                  break;\n"
                "            case '/':\n"
                "                  if (num2 != 0) {\n"
                "                      resultado = num1 / num2;\n"
                "                   } else {\n"
                "                       System.out.println('Erro: Divisão por zero.');\n"
                "                       return;\n"
                "                   }\n"
                "                   break;\n"
                "                   default:\n"
                "                       System.out.println('Operação inválida.');\n"
                "                       return;\n"
                "               }\n"
                "                System.out.println('Resultado: ' + resultado);\n"
                "           }\n"
                "}\n"
                )            
    elif opcao == 'Tabuada de um número':
        return ("import java.util.Scanner;\n"
                "\n"
                "public class Tabuada {\n"
                "   public static void main(String[] args) {\n"
                "        Scanner scanner = new Scanner(System.in);\n"
                "        System.out.print('Digite um número para a tabuada: ');\n"
                "        int num = scanner.nextInt();\n"
                "        System.out.println('Tabuada de ' + num + ':');\n"
                "        for (int i = 1; i <= 10; i++) {\n"
                "             System.out.println(num + ' x ' + i + ' = ' + (num * i));\n"
                "        }\n"
                "   }\n"
                "}\n"
               
                )
    elif opcao == 'Reverter uma string' :
        return ("import java.util.Scanner;\n"
                "\n"
                "public class ReverterString {\n"
                "   public static void main(String[] args) {\n"
                "       Scanner scanner = new Scanner(System.in);\n"
                "       System.out.print('Digite uma string: ');\n"
                "       String str = scanner.nextLine();\n"
                "       String reverso = new StringBuilder(str).reverse().toString();\n"
                "       System.out.println('String revertida: '' + reverso);\n"
                "     }\n"
                "}\n"
                
                )  
    elif opcao == 'ArrayList':
        return ("import java.util.ArrayList;\n"
                "\n"
                "public class ArrayListExemplo {\n"
                "   public static void main(String[] args) {\n"
                "       ArrayList<String> lista = new ArrayList<>();\n"
                "       lista.add('Java');\n"
                "       lista.add('Python');\n"
                "       lista.add('C++');\n"
                "\n"
                "       System.out.println('Lista de linguagens: ' + lista);\n"
                "       }\n"
                "}\n"
                
                )      
    elif opcao == 'Manipulação de Datas':
        return ("import java.time.LocalDate;\n"
                "import java.time.format.DateTimeFormatter;\n"
                "\n"
                "public class ManipularData {\n"
                "   public static void main(String[] args) {\n"
                "       LocalDate dataAtual = LocalDate.now();\n"
                "       System.out.println('Data atual: ' + dataAtual);\n"
                "\n"
                "       DateTimeFormatter formatter = DateTimeFormatter.ofPattern('dd/MM/yyyy');\n"
                "       String dataFormatada = dataAtual.format(formatter);\n"
                "       System.out.println('Data formatada: ' + dataFormatada);\n"
                "     }\n"
                "}\n"
        )  
    elif opcao == 'Calcular a Distância Euclidiana entre Dois Pontos':
        return ("public class DistanciaEuclidiana {\n"
                "   public static void main(String[] args) {\n"
                "       double x1 = 1.0, y1 = 2.0;\n"
                "       double x2 = 4.0, y2 = 6.0;\n"
                "       double distancia = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));\n"
                "       System.out.println('Distância euclidiana: ' + distancia);   \n"
                "    }\n"
                "}\n"
        )
    elif opcao == 'ArrayList com Objetos':
        return ("import java.util.ArrayList;\n"
                "\n"
                "class Estudante {\n"
                "   String nome;\n"
                "    int idade;\n"
                "\n"
                "   Estudante(String nome, int idade) {\n"
                "       this.nome = nome;\n"
                "       this.idade = idade;\n"
                "   }\n"
                "\n"
                "   @Override\n"
                "   public String toString() {\n"
                "       return nome + ' (' + idade + ' anos)';\n"
                "   }\n"
                "}\n"
                "\n"
                "public class ArrayListObjetos {\n"
                "   public static void main(String[] args) {\n"
                "       ArrayList<Estudante> estudantes = new ArrayList<>();\n"
                "       estudantes.add(new Estudante('Ana', 20));\n"
                "       estudantes.add(new Estudante('Carlos', 22));\n"
                "\n"
                "        for (Estudante estudante : estudantes) {\n"
                "            System.out.println(estudante);\n"
                "        }\n"
                "    }\n"
                "}\n"
        )
    elif opcao == 'Implementar uma Pilha':
        return ("import java.util.Stack;\n"
                "\n"
                "public class PilhaExemplo {\n"
                "    public static void main(String[] args) {\n"
                "       Stack<String> pilha = new Stack<>();\n"
                "       pilha.push('A');\n"
                "       pilha.push('B');\n"
                "       pilha.push('C');\n"
                "\n"
                "       System.out.println('Topo da pilha: ' + pilha.peek());\n"
                "       System.out.println('Removendo: ' + pilha.pop());\n"
                "        System.out.println('Topo da pilha agora: ' + pilha.peek());\n"
                "       }\n"
                "}\n"
                )
    elif opcao == 'Criar e Manipular um HashMap':
        return ("import java.util.HashMap;\n"
                "\n"
                "public class ManipularHashMap {\n"
                "   public static void main(String[] args) {\n"
                "       HashMap<String, Integer> mapa = new HashMap<>();\n"
                "       mapa.put('Maçã', 10);\n"
                "       mapa.put('Banana', 20);\n"
                "       mapa.put('Laranja', 15);\n"
                "\n"
                "       System.out.println('Mapa de frutas:');\n"
                "       for (String chave : mapa.keySet()) {\n"
                "           System.out.println(chave + ': ' + mapa.get(chave));\n"
                "       }\n"
                "   }\n"
                "}\n"
                )
    elif opcao == 'Estrutura Condicional (if-else)':
        return ("import java.util.Scanner;\n"
                "\n"
                "public class CondicionalIfElse {\n"
                "\   public static void main(String[] args) {n"
                "       Scanner scanner = new Scanner(System.in);\n"
                "\n"
                "       // Solicitar entrada do usuário\n"
                "       System.out.print('Digite um número: ');\n"
                "       int numero = scanner.nextInt();\n"
                "\n"
                "       // Verificar se o número é positivo, negativo ou zero\n"
                "       if (numero > 0) {\n"
                "           System.out.println('O número é positivo.');\n"
                "       } else if (numero < 0) {\n"
                "           System.out.println('O número é negativo.');\n"
                "        } else {\n"
                "         }\n"
                "\n"
                "         scanner.close();\n"
                "       }\n"
                "}\n"
                )   
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

    # Adiciona rolagem de texto
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
        "Ola mundo",
        "Soma de Dois Números",
        "Gerenciador de Tarefas",
        "Painel de Login",
        "Imprimir Números de 1 a 10",
        "Encontrar o Maior Elemento em um Array",
        "Array",
        "Classe e Objeto Simples",
        "Leitura e Escrita em Arquivo",
        "Tabela de Multiplicação",
        "Contagem Regressiva",
        "Calculadora Simples",
        "Tabuada de um número",
        "Reverter uma string",
        "ArrayList",
        "Manipulação de Datas",
        "Implementar uma Pilha",
        "Calcular a Distância Euclidiana entre Dois Pontos",
        "ArrayList com Objetos",
        "Estrutura Condicional (if-else)"        
        
        
        
    ]
    

    def opcao_selecionada(event):
    
        opcao = lista_opcoes.get(tk.ACTIVE)
        if opcao:
            mostrar_codigo(opcao)

    # Adiciona exibir as opções
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
                
                
                
                
