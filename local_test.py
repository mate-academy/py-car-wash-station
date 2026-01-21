# local_test.py
# -*- coding: utf-8 -*-

# Importa as classes do seu ficheiro de solução
# Assumindo que o seu código está em app/main.py
from app.main import Car, CarWashStation


def check(label: str, got, expected) -> None:
    """Pequeno helper de asserção com mensagem amigável."""
    if isinstance(expected, float):
        # Comparação com arredondamento de 1 casa, igual ao enunciado
        got_r = round(got, 1)
        exp_r = round(expected, 1)
        assert got_r == exp_r, f"{label} -> obtido {got_r}, esperado {exp_r}"
        print(f"[OK] {label}: {got_r} (esperado: {exp_r})")
    else:
        assert got == expected, f"{label} -> obtido {got}, esperado {expected}"
        print(f"[OK] {label}: {got} (esperado: {expected})")


print("--- INICIANDO TESTE LOCAL ---")

# Criando as instâncias exatamente como no PDF
bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")
mercedes = Car(7, 1, "Mercedes")
ws = CarWashStation(6, 8, 3.9, 11)

# Mostra preços individuais ANTES de lavar (não altera clean_mark)
p_bmw = ws.calculate_washing_price(bmw)
p_audi = ws.calculate_washing_price(audi)
p_mer = ws.calculate_washing_price(mercedes)

print("\nPreços individuais (antes de lavar):")
print(f"  BMW: {p_bmw}")
print(f"  Audi: {p_audi}")
print(f"  Mercedes: {p_mer}")

# --- Testando o método serve_cars ---
print("\n1) Testando serve_cars...")
income = ws.serve_cars([bmw, audi, mercedes])
check("Rendimento total", income, 41.6)
check("Limpeza BMW", bmw.clean_mark, 8)
check("Limpeza Audi", audi.clean_mark, 9)
check("Limpeza Mercedes", mercedes.clean_mark, 8)

# --- Testando o método calculate_washing_price ---
print("\n2) Testando calculate_washing_price...")
ford = Car(2, 1, "Ford")
wash_cost = ws.calculate_washing_price(ford)
check("Custo de lavagem Ford", wash_cost, 9.1)
check("Limpeza Ford (não muda)", ford.clean_mark, 1)

# --- Testando o método rate_service ---
print("\n3) Testando rate_service...")
ws.rate_service(5)
check("Nova contagem de avaliações", ws.count_of_ratings, 12)
check("Nova avaliação média", ws.average_rating, 4.0)

print("\n--- TESTE LOCAL CONCLUÍDO ---")
