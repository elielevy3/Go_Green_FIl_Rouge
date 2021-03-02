#!/usr/bin/env python
import datetime, pytz
from mainApp.models import Users, Challenges, Categories, Accepted_Challenges, Scores, Questions, Categories
from django.utils import timezone
# ON NETTOIE LA BDD
#attention à l'ordre de suppression : il faut supprimer les tables référençant avant de supprimer celles référencés (donc score avant user, challenges et questions avant categories...)
Scores.objects.all().delete()
Users.objects.all().delete()
#on doit d'abord supprimer les defis liés à une categories avant de supprimer celle-ci
Accepted_Challenges.objects.all().delete()
Questions.objects.all().delete()
Challenges.objects.all().delete()
Categories.objects.all().delete()

u1 = Users(id=1, nom="Levy", prenom="Elie", mail="elie.levy@mail.com", mdp="1234")
u2 = Users(id=2, nom="Dupont", prenom="Pierre", mail="pierre.dupont@mail.com", mdp="1234")
u3 = Users(id=3, nom="Fadili", prenom="Zineb", mail="zineb.fadili@mail.com", mdp="1234")

c1 = Categories(titre="Alimentation")
c2 = Categories(titre="EnergieEtEau")
c3 = Categories(titre="Dechets")
c4 = Categories(titre="Loisir")
c5 = Categories(titre="Menage/Hygiene")
c6 = Categories(titre="Numerique")


d1 = Challenges(titre="Mangez moins de viande", description="Sur une semaine entière, réduire de moitié sa consommation de viande rouge", categorie=c1, score_max=40, duree=7, facile=False, ponctuel=False)
d2 = Challenges(titre="Utiliser plus souvent le vélo", description="Sur une semaine entière, utiliser au moins 3 fois son vélo", categorie=c2, score_max=60, duree=7, facile=False, ponctuel=False)
d3 = Challenges(titre="Utiliser des produits de beauté éco-responsables", description="Durant vos prochaines courses, achetez des produits de beauté labellisés éco-responsables", categorie=c5, score_max=50, duree=14, facile=False, ponctuel=True)
d4 = Challenges(titre="Mangez plus souvent à l'éco-ligne", description="Sur une semaine entière, manger au moins 3 fois à l'éco-ligne", categorie=c1, score_max=60, duree=7, facile=False, ponctuel=False)
d5 = Challenges(titre="Achetez de saison local AMAP", description="Au prochaine course acheter local", categorie=c1, score_max=60, duree=7, facile=False, ponctuel=False)
d6 = Challenges(titre="Composter ses aliments", description="La prochaine fois composter", categorie=c3, score_max=60, duree=7, facile=True, ponctuel=False)

dr1 = Accepted_Challenges(user=u1, defi=d1, date_defi_releve=timezone.now(),date_debut_prevu=datetime.datetime(2020, 4, 6, 9, 0, 0, 0, pytz.UTC), fini=False)
dr2 = Accepted_Challenges(user=u1, defi=d2, date_defi_releve=timezone.now(),date_debut_prevu=datetime.datetime(2020, 4, 6, 9, 0, 0, 0, pytz.UTC), fini=False)
dr3 = Accepted_Challenges(user=u3, defi=d3, date_defi_releve=timezone.now(),date_debut_prevu=datetime.datetime(2020, 4, 4, 9, 0, 0, 0, pytz.UTC), fini=True)

q1 = Questions(intitule="A quelle fréquence consommez-vous de la chaire animale? (0-régime végétarien, 5-consommation de viande à tous les repas)", categorie=c1, challenge=d1)
q2 = Questions(intitule="A quelle fréquence consommez-vous des produits locaux? (0-jamais, 5-pour tous)", categorie=c3, challenge=d5)
q3 = Questions(intitule="Quelle part de votre alimentation conmpostez vous", categorie=c3, challenge=d6)

s1=Scores(date_score=datetime.datetime(2020, 4, 5, 9, 0, 0, 0, pytz.UTC),score=50, user=u3, categorie=c5)

u1.save()
u2.save()
u3.save()

c1.save()
c2.save()
c3.save()
c4.save()
c5.save()
c6.save()


d1.save()
d2.save()
d3.save()
d4.save()
d5.save()
d6.save()

dr1.save()
dr2.save()
dr3.save()

q1.save()
q2.save()
q3.save()

s1.save()
