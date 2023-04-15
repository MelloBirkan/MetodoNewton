# Importa a biblioteca math para utilizar a função cos()
import math

# Função que implementa o Método de Newton
def newton(f, u, epsilon, N0=100):
    
    # Função para calcular a derivada da função f usando a fórmula das diferenças finitas
    def df(x):
        h = 1e-6  # Define um valor pequeno para h
        # Calcula a derivada usando a fórmula das diferenças finitas central
        return (f(x + h) - f(x - h)) / (2 * h) 
    
    # Iteração do método de Newton
    for i in range(N0):
        # Calcula a razão entre a função e sua derivada no ponto u
        du = f(u) / df(u) 
        # Atualiza o valor de v usando a fórmula de Newton
        v = u - du 
        
        # Verifica se a aproximação atual atende à tolerância epsilon
        if abs(v - u) < epsilon:
            return v  # Retorna o valor atual de v
        
        # Atualiza o valor de u para a próxima iteração
        u = v 
    
    # Se o método não convergir em N0 iterações, retorna None
    return None

def resolver_equacao(f, ponto_inicial, ep, raiz_string):
    # Encontra a raiz da função f com ponto inicial e tolerância especificados
    raiz = newton(f, ponto_inicial, ep)  
    if raiz is not None:
        # Imprime a raiz encontrada para a função
        print(f"A raiz de {raiz_string} é:", raiz)  
    else:
        # Imprime uma mensagem se o método não convergir para a função
        print("O método não convergiu para uma raiz de f")  
    
    # Imprime a tolerância utilizada
    print(f"Tolerância utilizada:{ep}\n")  

def main():
  # EXERCICIO 1 (
    print("EXERCICIO 1:")
    # Definindo as funções que se deseja encontrar raízes
    def f1(x):
        # Função f1(x) = x^3 + 4x^2 - 10
        return x**3 + 4*x**2 - 10  
    
    def f2(x):
        # Função f2(x) = cos(x) - x
        return math.cos(x) - x  
    
    # Encontrando as raízes de f1 e f2 utilizando o método de Newton
    resolver_equacao(f1, 1, 1e-1, "x**3 + 4*x**2 - 10")
    resolver_equacao(f2, 1, 1e-1, "cos(x) - x") 
  
#)

# EXERCICIO 2 (
    print("\nEXERCICIO 2:")
    def fc(x):
        # Função fc(x) = 𝑥ˆ3 − 2𝑥ˆ2 − 5
        return x**3 - 2*x**2 - 5
    
    def fd(x):
        # Função fd(x) = 𝑒𝑥 -3x2
        return 2.71828 - 3*x**2

# Encontrando as raízes de a,b,c e d utilizando o método de Newton
    print("A)")
    resolver_equacao(f1, 1, 1e-3, "x**3 + 4*x**2 - 10")
    print("B)")
    resolver_equacao(f2, 1, 1e-3, "cos(x) - x")
    print("C)")
    resolver_equacao(fc, 1, 1e-3, "x**3 - 2*x**2 - 5")
    print("D)")
    resolver_equacao(fd, 1, 1e-3, "x**3 - 2*x**2 - 5")
#)
main()  # Executa a função main()

