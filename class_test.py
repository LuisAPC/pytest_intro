from main import calculadora

# monkeypatch ignora cierta funcion y la cambia por un valor en especifico
# sirve para testear solo lo que te interesa


def test_class_monkey(monkeypatch):
    monkeypatch.setattr(calculadora, "sumar", lambda x: 4)
    c = calculadora()
    assert c.sumar() == 4
