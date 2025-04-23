from django.shortcuts import render
from .recommendations import get_recommendations

def movie_recommendations(request):
    user = request.user
    recommended_movies = get_recommendations(user, limit=10)
    return render(request, 'movies/recommendations.html', {'recommended_movies': recommended_movies})
