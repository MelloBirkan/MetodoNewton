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

def main():
    # Definindo as funções que se deseja encontrar raízes
    def f1(x):
        return x**3 + 4*x**2 - 10  # Função f1(x) = x^3 + 4x^2 - 10
    
    def f2(x):
        return math.cos(x) - x  # Função f2(x) = cos(x) - x
    
    # Encontrando as raízes de f1 e f2 utilizando o método de Newton
    raiz1 = newton(f1, 1, 1e-6)  # Encontra a raiz de f1() com ponto inicial 1 e tolerância 1e-6
    raiz2 = newton(f2, 1, 1e-6)  # Encontra a raiz de f2() com ponto inicial 1 e tolerância 1e-6
    
    # Imprimindo os resultados
    if raiz1 is not None:
        print("A raiz de f1 é:", raiz1)  # Imprime a raiz encontrada para f1
    else:
        print("O método não convergiu para uma raiz de f1")  # Imprime uma mensagem se o método não convergir para f1
    
    if raiz2 is not None:
        print("\nA raiz de f2 é:", raiz2)  # Imprime a raiz encontrada para f2
    else:
        print("O método não convergiu para uma raiz de f2")  # Imprime uma mensagem se o método não convergir para f2
    
    # Imprimindo a tolerância utilizada
    print("\nTolerância utilizada:", 1e-6)  # Imprime a tolerância utilizada

main()  # Executa a função main()
