# Importa a biblioteca math para utilizar a função cos()
import math

# Função que implementa o Método de Newton
def newton(f, u, epsilon, N0=100):
    
    # Função para calcular a derivada da função f usando a fórmula das diferenças finitas
    def df(x):
        h = 1e-6  # Define um valor pequeno para h
        return (f(x + h) - f(x - h)) / (2 * h)  # Calcula a derivada usando a fórmula das diferenças finitas
    
    # Iteração do método de Newton
    for i in range(N0):
        du = f(u) / df(u)  # Calcula a razão entre a função e sua derivada no ponto u
        v = u - du  # Atualiza o valor de v usando a fórmula de Newton
        
        # Verifica se a aproximação atual atende à tolerância epsilon
        if abs(v - u) < epsilon:
            return v  # Retorna o valor atual de v
        
        u = v  # Atualiza o valor de u para a próxima iteração
    
    # Se o método não convergir em N0 iterações, retorna None
    return None


def resolver_equacao(f, ponto_inicial, ep, raiz_string):
  raiz = newton(f, ponto_inicial, ep)  # Encontra a raiz de f1() com ponto inicial 1 e tolerância 1e-6
  if raiz is not None:
      print(f"A raiz de {raiz_string} é:", raiz)  # Imprime a raiz encontrada para f1
  else:
      print("O método não convergiu para uma raiz de f")  # Imprime uma mensagem se o método não convergir para f1
  # Imprimindo a tolerância utilizada
  print(f"Tolerância utilizada:{ep}\n")  # Imprime a tolerância utilizada

def main():
  # EXERCICIO 1 (
  
    # Definindo as funções que se deseja encontrar raízes
    def f1(x):
        return x**3 + 4*x**2 - 10  # Função f1(x) = x^3 + 4x^2 - 10
    
    def f2(x):
        return math.cos(x) - x  # Função f2(x) = cos(x) - x
    
    # Encontrando as raízes de f1 e f2 utilizando o método de Newton
    resolver_equacao(f1, 1, 1e-1, "x**3 + 4*x**2 - 10")  # Encontra a raiz de f1() com ponto inicial 1 e tolerância 1e-6
    resolver_equacao(f2, 1, 1e-1, "cos(x) - x")  # Encontra a raiz de f2() com ponto inicial 1 e tolerância 1e-6
    
    
    
  
    
  
#)
main()  # Executa a função main()
