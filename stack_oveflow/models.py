from django.db import models

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=10)
#     password = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.name
    
# class Answer(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)

#     title = models.CharField(max_length=50)
#     content = models.CharField(max_length = 250)
    
#     def __str__(self):
#         return self.title
    
# class Questions(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE) 
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE) 

#     title = models.CharField(max_length=50)
#     content = models.CharField(max_length = 250)
                              
#     def __str__(self):
#         return self.title

class User(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Answer(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    content = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.title
    
class Questions(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) 

    # esta me tiene en jaque
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE) 
    #

    title = models.CharField(max_length=50)
    content = models.CharField(max_length = 250)
                              
    def __str__(self):
        return self.title
    

    