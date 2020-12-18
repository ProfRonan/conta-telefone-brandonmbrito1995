"""Arquivo principal que será interpretado pelo interpretador."""
import math

def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    número_ligações = int(input('Digite o número de ligações realizadas durante o mês: '))

    if 0 < número_ligações <= 100:
      print('O valor devido é R$ 200.00.')

    if 100 < número_ligações <= 150:
      valor = float(200 + (número_ligações-100) * 0.60)
      print('O valor devido é R$ {:.2f}.'.format(valor))

    if 150 < número_ligações <=200:
      valor = float(230 + (número_ligações - 150) * 0.50)
      print('O valor devido é R$ {:.2f}.'.format(valor))

    if número_ligações > 200:
      valor = float(255 + (número_ligações - 200)*0.40)
      print('O valor devido é R$ {:.2f}.'.format(valor))


if __name__ == '__main__':
    main()
