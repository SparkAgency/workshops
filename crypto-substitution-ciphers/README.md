
<!-- omit in toc -->
# Introdução à criptografia com cifras de substituição

- [Overview](#overview)
  - [Pré-requisitos](#pr%c3%a9-requisitos)
  - [Material necessário](#material-necess%c3%a1rio)
  - [Duração](#dura%c3%a7%c3%a3o)
  - [Conteúdos do workshop](#conte%c3%bados-do-workshop)
- [Workshop](#workshop)
  - [Introdução à cifra de César](#introdu%c3%a7%c3%a3o-%c3%a0-cifra-de-c%c3%a9sar)
  - [Aritmética modular](#aritm%c3%a9tica-modular)


# Overview

Neste workshop introdutório à criptografia com cifras de substituição, vamos usar Python para explorar as cifras [de César][caesar-cipher] e [afim][affine-cipher]. Durante o workshop vamos ver como encriptar mensagens com cifras de substituição, vamos implementá-las e vamos ainda implementar sistemas para as desencriptar. Vamos também perceber uma das principais fraquezas das cifras de substituição, e em particular das cifras de substituição monoalfabéticas.

## Pré-requisitos

 - Conhecimentos básicos de programação em Python.

## Material necessário

 - Computador com [Python 3][python3] instalado.

## Duração

Este workshop está desenhado para 1h30 com participantes do ensino superior, de nenhuma área em particular.

## Conteúdos do workshop

 - Introduzir a cifra de César [20 min];
   - Escolha do alfabeto;
   - Relacionar a cifra de César com aritmética modular;
   - Fazer algumas encriptações exemplo;
   - Implementar encriptação.
 - Desencriptar com aritmética modular [20 min];
   - Valores relativos entre caracteres;
   - Fazer desencriptações exemplo;
   - Implementar desencriptação;
   - Desencriptação por brute-force.
 - Estabelecer paralelo entre encriptação e desencriptação [10 min];
 - Introduzir a cifra afim [15 min];
   - Fórmula `ax + b mod L`;
   - Equivalência entre `a = 1` e cifra de César;
   - Implementação da encriptação.
 - Aritmética modular na cifra afim [25 min]
   - Escolha do parâmetro `a` em função de `L`;
   - Inversão de produtos com aritmética modular;
     - Caso particular em que `L` é primo.
   - Implementação da inversão da fórmula;
   - Implementação da desencriptação.


# Workshop

## Introdução à cifra de César

Começo por introduzir a [cifra de César](caesar-cipher), explicando que a "chave" consiste em escolher uma letra do alfabeto, por exemplo `D`, e depois criar uma correspondência entre duas cópias do alfabeto:

```
A -> D
B -> E
C -> F
D -> G
...
V -> Y
W -> Z
X -> A
Y -> B
Z -> C
```

e portanto a palavra `ABC` passa a ser `DEF` depois de encriptada com a chave `D`.

Logo de seguida numero as letras e mostro como a encriptação é extremamente simples quando vista como uma soma, se começarmos a numerar o alfabeto a partir do $0$ (correspondendo ao `A`) até ao $25$ (correspondendo ao `Z`).

```
 0 = A -> D =  3 =  0 + 3
 1 = B -> E =  4 =  1 + 3
 2 = C -> F =  5 =  2 + 3
 3 = D -> G =  6 =  3 + 3
...
21 = V -> Y = 24 = 21 + 3
22 = W -> Z = 25 = 22 + 3
23 = X -> A =  0 = 23 + 3
24 = Y -> B =  1 = 24 + 3
25 = Z -> C =  2 = 25 + 3
```

## Aritmética modular

Podemos ver, no caso em cima, que a letra `X` que tem o número $23$ está a ser encriptada como a letra `A`, que tem o número $0$, apesar de termos $23 + 3 = 26$.

[caesar-cipher]: https://en.wikipedia.org/wiki/Caesar_cipher
[affine-cipher]: https://en.wikipedia.org/wiki/Affine_cipher
[python3]: https://www.python.org/downloads/