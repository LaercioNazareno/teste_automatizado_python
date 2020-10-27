# teste_automatizado_python
Esse repositório tem como objetivo aplicar os conhecimento de teste de mutação e mock teste em Python 

Para executar basta instalar o mutpy e rodar o comando de execução, segue os comandos:

instalar o mutpy:
	pip3 install MutPy

executar na pasta normalize
	mut.py --target main --unit-test teste_mock.py -m

Os testes implementados foram:
   teste_normalize_menor_igual_menor:
      Reproduz o fluxo para vetores com um unico valor.
      valores de entrada:
         main.my_min = 3
         main.my_max = 3
         
   teste_normalize:
      Reprouz o fluxo esperado da função.
      valores de entrada:
         main.my_min = 3
         main.my_max = 4
         
   teste_normalize_maior_que_100:
      Reproduz os valores para os casos maiores que 100.
      valores de entrada:
         main.my_min = 100
         main.my_max = 1000
         
	teste_normalize_menor_que_1:
      Reproduz os valores limites para casos menores que 1.
      valores de entrada:
         main.my_min = 0.4
         main.my_max = 10
         
   teste_normalize_erro: 
      Induz ao erro com o my_min mior que my_max, 
      teoricamente isso não pode acontecer.
      valores de entrada:
         main.my_min = 20
         main.my_max = 10

Os metodos que passaram pelo mock foram: 
   main.my_min;
   main.my_max;

Resultado: 
[*] Start mutation process:
   - targets: main
   - tests: teste_mock.py
[*] 5 tests passed:
   - teste_mock [0.00419 s]
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
   8:         return new_vet
   9:     
--------------------------------------------------------------------------------
[0.01811 s] killed by teste_normalize_menor_igual_menor (teste_mock.teste_mock)
   - [#   2] AOR main: 
--------------------------------------------------------------------------------
   7:             new_vet.append(100)
   8:         return new_vet
   9:     
  10:     for n in range(len(vet)):
- 11:         a = vet[n] - vet_min
+ 11:         a = vet[n] + vet_min
  12:         b = vet_max - vet_min
  13:         new_vet.append((a / b) * 100)
  14:     
  15:     return new_vet
--------------------------------------------------------------------------------
[0.01216 s] killed by teste_normalize (teste_mock.teste_mock)
   - [#   3] AOR main: 
--------------------------------------------------------------------------------
   8:         return new_vet
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
[0.01866 s] killed by teste_normalize (teste_mock.teste_mock)
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
[0.01963 s] killed by teste_normalize_erro (teste_mock.teste_mock)
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
[0.01696 s] killed by teste_normalize_erro (teste_mock.teste_mock)
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
[0.00935 s] killed by teste_normalize (teste_mock.teste_mock)
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
[0.01254 s] killed by teste_normalize (teste_mock.teste_mock)
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
[0.01820 s] killed by teste_normalize (teste_mock.teste_mock)
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
   8:         return new_vet
   9:     
--------------------------------------------------------------------------------
[0.01381 s] killed by teste_normalize (teste_mock.teste_mock)
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
   8:         return new_vet
   9:     
--------------------------------------------------------------------------------
[0.02154 s] killed by teste_normalize (teste_mock.teste_mock)
[*] Mutation score [0.55794 s]: 100.0%
   - all: 10
   - killed: 10 (100.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
