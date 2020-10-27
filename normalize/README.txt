Para executar basta instalar o mutpy e rodar o comando de execução, segue os comandos:

instalar o mutpy:
	pip3 install MutPy

executar
	mut.py --target main --unit-test teste_mock.py -m

Os implementado foram:
	Retorno do primeiro if no teste: teste_normalize_menor_igual_menor
	Retorno no for: teste_normalize_menor_diferente_maior
	Quando a diferença entre o maior e o menor é positiva com números negativos: teste_normalize_diferenca_positiva
	Quanado a diferença entre o maior e o menor é negativa com um positivo e um negativo: teste_normalize_diferenca_negativa

As linhas que passaram pelo mock foram: 
  vet_max = my_max(vet)
  vet_min = my_min(vet)

obs.: O mutpy não executou corretamente em meu computador tendo falha ao mostrar os mutantes mortos, tive algumas duvidas
para verificar os resultados dos testes.

Resultado: 

[*] Start mutation process:
   - targets: main
   - tests: teste_mock.py
[*] 4 tests passed:
   - teste_mock [0.00549 s]
[*] Start mutants generation and execution:
   - [#   1] AOR main: 
--------------------------------------------------------------------------------
   1: def normalize(vet):
   2:     new_vet = []
   3:     vet_max = my_max(vet)
   4:     vet_min = my_min(vet)
-  5:     if vet_max - vet_min == 0:
+  5:     if vet_max + vet_min == 0:
   6:         for n in range(len(vet)):
   7:             new_vet.append(100)
   8:             return new_vet
   9:     
--------------------------------------------------------------------------------
[0.01724 s] survived
   - [#   2] AOR main: 
--------------------------------------------------------------------------------
   7:             new_vet.append(100)
   8:             return new_vet
   9:     
  10:     for n in range(len(vet)):
- 11:         a = vet[n] - vet_min
+ 11:         a = vet[n] + vet_min
  12:         b = vet_max - vet_min
  13:         new_vet.append((a / b) * 100)
  14:     
  15:     return new_vet
--------------------------------------------------------------------------------
[0.02676 s] survived
   - [#   3] AOR main: 
--------------------------------------------------------------------------------
   8:             return new_vet
   9:     
  10:     for n in range(len(vet)):
  11:         a = vet[n] - vet_min
- 12:         b = vet_max - vet_min
+ 12:         b = vet_max + vet_min
  13:         new_vet.append((a / b) * 100)
  14:     
  15:     return new_vet
  16: 
--------------------------------------------------------------------------------
[0.02972 s] survived
   - [#   4] AOR main: 
--------------------------------------------------------------------------------
   9:     
  10:     for n in range(len(vet)):
  11:         a = vet[n] - vet_min
  12:         b = vet_max - vet_min
- 13:         new_vet.append((a / b) * 100)
+ 13:         new_vet.append((a // b) * 100)
  14:     
  15:     return new_vet
  16: 
  17: def my_max(vet):
--------------------------------------------------------------------------------
[0.03500 s] survived
   - [#   5] AOR main: 
--------------------------------------------------------------------------------
   9:     
  10:     for n in range(len(vet)):
  11:         a = vet[n] - vet_min
  12:         b = vet_max - vet_min
- 13:         new_vet.append((a / b) * 100)
+ 13:         new_vet.append((a * b) * 100)
  14:     
  15:     return new_vet
  16: 
  17: def my_max(vet):
--------------------------------------------------------------------------------
[0.04672 s] survived
   - [#   6] AOR main: 
--------------------------------------------------------------------------------
   9:     
  10:     for n in range(len(vet)):
  11:         a = vet[n] - vet_min
  12:         b = vet_max - vet_min
- 13:         new_vet.append((a / b) * 100)
+ 13:         new_vet.append((a / b) / 100)
  14:     
  15:     return new_vet
  16: 
  17: def my_max(vet):
--------------------------------------------------------------------------------
[0.02588 s] survived
   - [#   7] AOR main: 
--------------------------------------------------------------------------------
   9:     
  10:     for n in range(len(vet)):
  11:         a = vet[n] - vet_min
  12:         b = vet_max - vet_min
- 13:         new_vet.append((a / b) * 100)
+ 13:         new_vet.append((a / b) // 100)
  14:     
  15:     return new_vet
  16: 
  17: def my_max(vet):
--------------------------------------------------------------------------------
[0.02549 s] survived
   - [#   8] AOR main: 
--------------------------------------------------------------------------------
   9:     
  10:     for n in range(len(vet)):
  11:         a = vet[n] - vet_min
  12:         b = vet_max - vet_min
- 13:         new_vet.append((a / b) * 100)
+ 13:         new_vet.append((a / b) ** 100)
  14:     
  15:     return new_vet
  16: 
  17: def my_max(vet):
--------------------------------------------------------------------------------
[0.02507 s] survived
   - [#   9] COI main: 
--------------------------------------------------------------------------------
   1: def normalize(vet):
   2:     new_vet = []
   3:     vet_max = my_max(vet)
   4:     vet_min = my_min(vet)
-  5:     if vet_max - vet_min == 0:
+  5:     if not (vet_max - vet_min == 0):
   6:         for n in range(len(vet)):
   7:             new_vet.append(100)
   8:             return new_vet
   9:     
--------------------------------------------------------------------------------
[0.02779 s] survived
   - [#  10] ROR main: 
--------------------------------------------------------------------------------
   1: def normalize(vet):
   2:     new_vet = []
   3:     vet_max = my_max(vet)
   4:     vet_min = my_min(vet)
-  5:     if vet_max - vet_min == 0:
+  5:     if vet_max - vet_min != 0:
   6:         for n in range(len(vet)):
   7:             new_vet.append(100)
   8:             return new_vet
   9:     
--------------------------------------------------------------------------------
[0.03691 s] survived
[*] Mutation score [0.70986 s]: 0.0%
   - all: 10
   - killed: 0 (0.0%)
   - survived: 10 (100.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
