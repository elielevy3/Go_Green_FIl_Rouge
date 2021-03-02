from .serializers import UserSerializer, ChallengeSerializer, CategorieSerializer, QuestionSerializer, AcceptedChallengesSerializer, ScoreSerializer
from .models import Users, Accepted_Challenges, Scores, Questions, Challenges, Categories
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, generics
from django.http import Http404, HttpResponse, JsonResponse
from django.views import View
from django.db.models import Sum, Max

class UserViewset(ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UserSerializer
	filter_backends = [DjangoFilterBackend]
	filter_fields = {
		'nom': ['exact'],
		'prenom': ['exact'],
		}

class ChallengeViewset(ModelViewSet):
	queryset = Challenges.objects.all()
	serializer_class = ChallengeSerializer
	filter_backends = [DjangoFilterBackend]
	filter_fields = {
		'duree': ['gte', 'lte'],
		'score_max': ['gte', 'lte'],
		'categorie': ['exact'],
		}

class CategorieViewset(ModelViewSet):
	queryset = Categories.objects.all()
	serializer_class = CategorieSerializer
	filter_backends = [DjangoFilterBackend]
	filter_fields = {
		'id': ['exact'],
		'titre': ['exact'],
		}

class QuestionViewset(ModelViewSet):
	queryset = Questions.objects.all()
	serializer_class = QuestionSerializer
	filter_backends = [DjangoFilterBackend]
	filter_fields = {
		'id': ['exact'],
		'intitule': ['exact'],
		'categorie': ['exact'],
		}

class ScoreList(APIView):
	def get(self, request, format=None):
		user_id = self.request.query_params.get("user_id", None)
		if user_id is not None:
			user = Users.objects.get(pk=user_id)
			scores = Scores.objects.all().filter(user=user)
		else:
			scores = Scores.objects.all()
		serializer = ScoreSerializer(scores, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ScoreSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScoreDetail(APIView):
	def get_object(self, pk):
		try:
			return Scores.objects.get(pk=pk)
		except Scores.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		score = self.get_object(pk)
		serializer = ScoreSerializer(score)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		score = self.get_object(pk)
		serializer = ScoreSerializer(score, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		score = self.get_object(pk)
		score.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class AcceptedChallengesList(generics.ListAPIView):
	queryset = Accepted_Challenges.objects.all().order_by('-pourcentage_completion')
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ["user", "defi", "fini", "defi__categorie__id"]
	serializer_class = AcceptedChallengesSerializer

	def post(self, request, format=None):
		serializer = AcceptedChallengesSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AcceptedChallengeDetail(APIView):
	def get_object(self, pk):
		try:
			return Accepted_Challenges.objects.get(pk=pk)
		except Accepted_Challenges.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		acceptedChallenge = self.get_object(pk)
		serializer = AcceptedChallengesSerializer(acceptedChallenge)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		acceptedChallenge = self.get_object(pk)
		serializer = AcceptedChallengesSerializer(acceptedChallenge, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		acceptedChallenge = self.get_object(pk)
		acceptedChallenge.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


def CalculateGrade(request):
	user = request.GET.get("user")
	categorie = request.GET.get("categorie")
	score_max = Challenges.objects.all().filter(categorie=categorie).aggregate(Sum('score_max'))
	done_challenges = Accepted_Challenges.objects.values('defi')\
												 .filter(user=user, defi__categorie__id=categorie, fini=True)\
												 .annotate(max_completion=Max('pourcentage_completion'))
	score_user = 0
	for elem in list(done_challenges):
		m = Challenges.objects.all().get(pk=elem["defi"]).score_max
		score_user += m*elem["max_completion"]
	#result = {"score_max" : score_max["score_max__sum"], "score_user": score_user}
	return HttpResponse(score_user / score_max["score_max__sum"])
	