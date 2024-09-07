from django.db import models

class skillList(models.Model):
    
    skillName = [
        ("Opcion1","Opcion1"),
        ("Opcion2","Opcion2")
    ]

    skillChoices = [
        ("Opcion1","Opcion1"),
        ("Opcion2","Opcion2"),
    ]

    skillID = models.BigAutoField(primary_key=True)
    skillName= models.CharField(skillName,blank=False,null=False,max_length=50)
    skillCategory = models.CharField(skillChoices,blank=False,null=False,max_length=30)
