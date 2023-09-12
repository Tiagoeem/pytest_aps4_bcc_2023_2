import pytest
from funcoes import soma, subtracao, divisao, somatoria

@pytest.mark.simples
def test_soma_positiva():
    assert soma(5, 3) == 8

@pytest.mark.simples
def test_subtracao_resultado_negativo():
    assert subtracao(3, 5) == 0

# TODO: Escreva mais testes
