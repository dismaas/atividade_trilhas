def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Avestruz")

def sem_parametro():
    print("Olá, não tenho variável.")

sem_parametro()

def somar(a, b):
    return a + b

resultado = somar(1, 2)
print(resultado)

try:
    numero = int("texto")
except Exception as e:
    print("Deu errado:", e)

pessoa = {
    "nome": "Davi",
    "idade": 24,
    "altura": 1.80,
    "professor": True,
    "alunos": ["Avestruz", "Itachi"]
}

print(pessoa["nome"])
print(pessoa.get("idade"))
print(pessoa["alunos"][0])

pessoa["nome"] = "Novo Nome"
del pessoa["idade"]

for chave in pessoa:
    print(chave, pessoa[chave])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

aluno = {
    "nome": "Itachi",
    "notas": {
        "matematica": 9,
        "portugues": 10
    }
}

print(aluno["notas"]["matematica"])

comandos_git = """
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
git add .
git commit -m "Adicionado assunto de dicionarios"
git push origin main
"""
print(comandos_git)
