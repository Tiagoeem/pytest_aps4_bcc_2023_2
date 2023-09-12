# Exercício Prático: Funções Matemáticas e Testes com pytest

## Objetivo:

Neste exercício, você implementará algumas funções matemáticas simples e escreverá testes para elas usando o `pytest`. Além disso, você tratará erros específicos e garantirá que certos requisitos sejam atendidos.

## Requisitos:

1. Implemente as seguintes funções matemáticas:
    - `soma(a, b)`: Retorna a soma de `a` e `b`. Se o resultado for negativo, retorne 0.
    - `subtracao(a, b)`: Retorna a subtração de `a` por `b`. Se o resultado for negativo, retorne 0.
    - `divisao(a, b)`: Retorna a divisão de `a` por `b`. Deve tratar a divisão por zero.
    - `somatoria(lista)`: Retorna a soma de todos os números em `lista`.

2. Escreva testes para essas funções usando o `pytest`. Alguns testes serão fornecidos para você, mas você deve escrever os adicionais conforme necessário.

3. Use marcadores do `pytest` para categorizar seus testes. Por exemplo, use `@pytest.mark.simples` para testes das funções `soma` e `subtracao`, e `@pytest.mark.lista` para testes da função `somatoria`.

## Estrutura do Projeto:

```bash
/projeto_matematico
    /tests
        test_funcoes.py
    funcoes.py
    pytest.ini
```


## Instruções:

1. Comece escrevendo seus testes em `test_funcoes.py`. Alguns testes serão fornecidos para você.
2. Em seguida, implemente as funções em `funcoes.py`.
3. Use o comando `pytest` para executar seus testes. Inicialmente, eles falharão.
4. Continue implementando e ajustando as funções até que todos os testes passem.
5. Lembre-se de tratar erros e garantir que os requisitos sejam atendidos.
6. A criação correta do `pytest.ini` é de sua responsabilidade.
 
## Como você deve testar seu código:

Para testar seu código, você usará o `pytest` juntamente com os marcadores definidos. Aqui estão os comandos que você pode usar para executar testes específicos:

   ```bash
   pytest -v -m simples
```

   ```bash
   pytest -v -m lista
```
