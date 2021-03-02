from django.db import models
from datetime import date
from django.utils import timezone

class Users(models.Model):
	#pas besoin de gérer le user_id, django le crée pour nous en base nommé id
	nom = models.CharField(max_length=200)
	prenom = models.CharField(max_length=200)
	mail = models.EmailField(max_length=200)
	mdp = models.CharField(max_length=50)

	class Meta:
		constraints = [
        	models.UniqueConstraint(fields=['mail'], name='unique_user_mail'),
        	]

	def __str__(self):
		return str(self.id)+" "+self.nom+" "+self.prenom

class Categories(models.Model):
	titre = models.CharField(max_length=200)

	def __str__(self):
		return self.titre

class Scores(models.Model):
	date_score = models.DateTimeField()
	score = models.IntegerField()
	# si on supprime un user on supprime son historique de score
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	# on ne peut pas supprimer  une categories si des scores d'users existant pointent encore vers elle
	categorie = models.ForeignKey(Categories, on_delete=models.PROTECT)
	constraints = [
		models.UniqueConstraint(fields=['user', 'date_score', 'categorie'], name='unique_historic_score')
	]

class Challenges(models.Model):
	titre = models.CharField(max_length=200)
	description = models.CharField(max_length=254)
	categorie = models.ForeignKey(Categories, on_delete=models.PROTECT)
	score_max = models.IntegerField()
	duree = models.IntegerField()
	facile = models.BooleanField(default=False)
	ponctuel = models.BooleanField(default=False)
	def __str__(self):
		return str(self.id)+" "+self.titre

class Questions(models.Model):
	intitule = models.CharField(max_length=254)
	categorie = models.ForeignKey(Categories, on_delete=models.PROTECT)
	challenge = models.ForeignKey(Challenges, on_delete=models.PROTECT)

class Accepted_Challenges(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	defi = models.ForeignKey(Challenges, on_delete=models.CASCADE)
	date_defi_releve = models.DateTimeField(auto_now_add=True)	
	date_debut_prevu = models.DateTimeField()
	date_fin_effective = models.DateTimeField(default=None, null=True)
	fini = models.BooleanField(default=False)
	pourcentage_completion = models.FloatField(default=0)
	def __str__(self):
		return str(self.user)+" "+str(self.defi) + str(self.pourcentage_completion)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['user', 'defi', 'date_defi_releve'], name='unique_defi_releve'),
			models.CheckConstraint(check=models.Q(pourcentage_completion__gte=0), name="check_pourcentage_gte_1"),
			models.CheckConstraint(check=models.Q(pourcentage_completion__lte=1), name="check_pourcentage_lte_1")
		]
