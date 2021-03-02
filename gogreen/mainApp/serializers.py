from rest_framework import serializers
from .models import Users, Challenges, Categories, Questions, Accepted_Challenges, Scores

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'nom', 'prenom', 'mail')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenges
        fields = ('id', 'titre', 'description', 'categorie', 'score_max', 'duree')

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'titre')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'intitule', 'categorie', 'challenge')

class AcceptedChallengesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accepted_Challenges
        fields = ('id', 'user', 'defi', 'date_defi_releve', 'date_debut_prevu', 'date_fin_effective', 'fini', 'pourcentage_completion')

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = ('id', 'date_score', 'score', 'user', 'categorie')
