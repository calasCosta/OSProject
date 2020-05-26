from django.db import models
from django.contrib.auth.models import User #importação da tabela do usuário 

# Tabela com nome Pet. 
class Pet(models.Model):
    #usamos sempre = models.Tipo da coluna(limite da coluna)
    city = models.CharField(max_length = 100) 
    description = models.TextField()
    phone = models.CharField(max_length = 11)
    email = models.EmailField() 

    #quando for inserida uma linha na tabela Pet automaticamente manda a data de inserçao
    begin_date = models.DateTimeField(auto_now_add = True) 

    #Imagem fica fora da base de dados(ex: numa pasta do projecto). usamos é só o caminho da imgem
    photo = models.ImageField(upload_to = 'pet')
    #se Pet tiver activo mosta no ecrã caso contrário não mosta 
    active = models.BooleanField(default = True)

    #se apagarmos um user, através do model cascade ele apaga todas as tabelas desse user
    user = models.ForeignKey(User, on_delete=models.CASCADE)# fk da tabela de user 


    #sempre que for chamado o pet, retorna o id
    def __str__(self): 
        return str(self.id) # os ids são criados automaticamente 

    #Funçao para colar nome da tabela na base de dados. no django pode ter um nome e na db um outro nome
    class Meta: 
        db_table = 'pet'