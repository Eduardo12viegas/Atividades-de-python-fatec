curso_a = {("Ana", 101),("Carlos", 102),("João",103)}
curso_b = {("João",103),("Marina",104), ("Carlos", 102)}

print("Exclusivos do curso A:")
for nome, codigo in curso_a.difference(curso_b):
    print(f"{nome} ({codigo})")
print("")

print("Exclusivos do curso B:")
for nome, codigo in curso_b.difference(curso_a):
    print(f"{nome} ({codigo})")
print("")

print("Em ambos os cursos:")
for nome, codigo in curso_a.intersection(curso_b):
    print(f"{nome} ({codigo})")