# importando as bibilotecas

import firebase_admin
from firebase_admin import credentials, firestore


# criando uma variavel para armazer o arquivo json para podermos fazer a autenticaçao com o banco de dados
cred = credentials.Certificate(r'D:\projetocursodbpython\sistemacadastroderemedios-firebase-adminsdk-fbsvc-92f4744f05.json')

# agora iremos fazer a conexão do nosso sistema de gerenciamento de remedio com o banco de dados 
firebase_admin.initialize_app(cred)

db_sistema_de_gerenciamento_de_remedios = firestore.client()



# Sistema de gerenciamento de remedios usando o metódo Crud - U update (adicionando novos usuários)

remedio = input("Nome do medicamento/remedio :")

categoria = input("Categoria do medicamento/remedio ex (alnalgesico/antibiotico):")

formato = input("formato farmaceutico: ex: (comprimido , capsula, pomada ou liquido) :")

origem = input("Origem(Pais, estado ou região):")

quantidade = int(input("quantidade disponivel em estoque:"))

ano = int(input("ano de fabricaçao:"))

#  a tabela remedios no banco de dados(crud) nesse caso C - Create

remedios = {
    "Nome do Remedio/Medicaçao": remedio,
    "Categoria": categoria,
    "Forma do Remedio/Medicamento": formato,
    "Origem": origem,
    "Quantidade disponivel em estoque": quantidade,
    "Ano de Fabricação": ano

}

#salvando as informaçoes no banco de dados usando o collection
db_sistema_de_gerenciamento_de_remedios.collection("Gerenciador de Remedios").add(remedios)
print("Dados enviados com sucesso ao nosso sistema de Gerenciamento de Remedios!")

# Usando o crud novamente para vizualizar os dados cadastrados  R - Read

ver_remedios = db_sistema_de_gerenciamento_de_remedios.collection("Gerenciador de Remedios").stream()
for dado in ver_remedios:
    print("Remedios cadastrados no sistema:",dado.to_dict())

# Deletando dados usando o crud novamente D - delete atraves do id do Remédio
doc_id = ""
db_sistema_de_gerenciamento_de_remedios.collection("Gerenciador de Remedios").document(doc_id).delete()
print("Remedio deletado com sucesso!")