"""Arquivo principal que será interpretado pelo interpretador."""
import math

def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    valor_mínimo = 200
    
    número_de_ligações = float(input('Digite o número de ligações que foram efetuadas durante o mês: '))

    diferença_ligações_100_mais = (número_de_ligações - 100) 
    diferença_ligações_150_mais = (número_de_ligações - 150)
    diferença_ligações_200_mais = (número_de_ligações - 200)
    diferença_valor_100_mais = diferença_ligações_100_mais * 0.6
    diferença_valor_150_mais = diferença_ligações_150_mais * 0.5
    diferença_valor_200_mais = diferença_ligações_200_mais * 0.4

    if número_de_ligações <= 100:
      print(f'O valor devido é R$ {valor_mínimo:.2f}.')
    elif 100 < número_de_ligações <= 150:
      print(f'O valor devido é R$ {valor_mínimo + diferença_valor_100_mais:.2f}.')
    elif 150 < número_de_ligações <= 200:
      print(f'O valor devido é R$ {valor_mínimo + diferença_valor_100_mais + diferença_valor_150_mais:.2f}.')
    else:
      print(f'O valor devido é R$ {valor_mínimo + diferença_valor_100_mais + diferença_valor_150_mais + diferença_valor_200_mais:.2f}.')


if __name__ == '__main__':
    main()
