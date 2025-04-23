from django.contrib import admin
from .recommendations import get_recommendations

def create_recommendation_admin_action():
    """Create an admin action for movie recommendations"""
    
    @admin.action(description="Get movie recommendations")
    def get_user_recommendations(modeladmin, request, queryset):
        """Action to get recommendations for selected users"""
        for profile in queryset:
            user = profile.user
            recommendations = get_recommendations(user, limit=5)
            recommendation_list = ", ".join([movie.title for movie in recommendations])
            modeladmin.message_user(
                request, 
                f"Recommendations for {user.username}: {recommendation_list}"
            )
    
    return get_user_recommendations

# Update the UserProfileAdmin in movies/admin.py
# Add this import at the top of the file:
# from .utils import create_recommendation_admin_action

# Then update the UserProfileAdmin class:
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for user profiles"""
    list_display = ('user', 'favorite_genre_count', 'rating_count')
    search_fields = ('user__username',)
    filter_horizontal = ('favorite_genres', 'favorite_movies')
    actions = [create_recommendation_admin_action()]
    
    def favorite_genre_count(self, obj):
        """Count favorite genres"""
        return obj.favorite_genres.count()
    favorite_genre_count.short_description = "Favorite Genres"
    
    def rating_count(self, obj):
        """Count ratings"""
        return obj.user.ratings.count()
    rating_count.short_description = "Ratings"

# Create a superuser to access the admin interface:
# python3 manage.py createsuperuser
# Then run the development server:
# python3 manage.py runserver
# Access the admin interface at http://127.0.0.1:8000/admin/

## Testing 🧪

# movies/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from .models import Director, Actor, Genre, Movie, MovieActor, Rating, UserProfile
from .recommendations import get_genre_recommendations, get_collaborative_recommendations

class MovieModelTest(TestCase):
    """Test cases for the Movie model"""
    
    def setUp(self):
        """Set up test data"""
        # Create director
        self.director = Director.objects.create(
            name="Christopher Nolan",
            birth_date=date(1970, 7, 30)
        )
        
        # Create genres
        self.genre1 = Genre.objects.create(name="Sci-Fi")
        self.genre2 = Genre.objects.create(name="Thriller")
        
        # Create movie
        self.movie = Movie.objects.create(
            title="Inception",
            release_date=date(2010, 7, 16),
            director=self.director,
            runtime=148,
            plot="A thief who steals corporate secrets through the use of dream-sharing technology."
        )
        self.movie.genres.add(self.genre1, self.genre2)
        
        # Create actor
        self.actor = Actor.objects.create(
            name="Leonardo DiCaprio",
            birth_date=date(1974, 11, 11)
        )
        
        # Create movie-actor relationship
        self.movie_actor = MovieActor.objects.create(
            movie=self.movie,
            actor=self.actor,
            character_name="Dom Cobb",
            is_lead=True
        )
    
    def test_movie_creation(self):
        """Test movie creation and relationships"""
        self.assertEqual(self.movie.title, "Inception")
        self.assertEqual(self.movie.director.name, "Christopher Nolan")
        self.assertEqual(self.movie.genres.count(), 2)
        self.assertTrue(self.genre1 in self.movie.genres.all())
        self.assertTrue(self.genre2 in self.movie.genres.all())
        self.assertEqual(self.movie.runtime, 148)
    
    def test_actor_relationship(self):
        """Test movie-actor relationship"""
        self.assertEqual(self.movie.actors.count(), 1)
        self.assertEqual(self.movie.actors.first().name, "Leonardo DiCaprio")
        self.assertEqual(self.movie_actor.character_name, "Dom Cobb")
        self.assertTrue(self.movie_actor.is_lead)


class RatingTest(TestCase):
    """Test cases for the Rating model"""
    
    def setUp(self):
        """Set up test data"""
        # Create movie
        self.movie = Movie.objects.create(
            title="The Shawshank Redemption",
            release_date=date(1994, 9, 23),
            runtime=142
        )
        
        # Create users
        self.user1 = User.objects.create_user(username="user1", password="testpass123")
        self.user2 = User.objects.create_user(username="user2", password="testpass123")
        self.user3 = User.objects.create_user(username="user3", password="testpass123")
        
        # Create ratings
        self.rating1 = Rating.objects.create(movie=self.movie, user=self.user1, value=9)
        self.rating2 = Rating.objects.create(movie=self.movie, user=self.user2, value=10)
    
    def test_average_rating_calculation(self):
        """Test automatic average rating calculation"""
        # Check initial average rating with 2 ratings
        self.movie.refresh_from_db()
        self.assertEqual(float(self.movie.avg_rating), 9.5)
        
        # Add a new rating
        Rating.objects.create(movie=self.movie, user=self.user3, value=8)
        self.movie.refresh_from_db()
        
        # Check updated average rating with 3 ratings
        self.assertEqual(float(self.movie.avg_rating), 9.0)


class RecommendationTest(TestCase):
    """Test cases for the recommendation engine"""
    
    def setUp(self):
        """Set up test data"""
        # Create genres
        self.action = Genre.objects.create(name="Action")
        self.comedy = Genre.objects.create(name="Comedy")
        self.drama = Genre.objects.create(name="Drama")
        
        # Create movies
        self.movie1 = Movie.objects.create(title="Movie 1", avg_rating=8.5)
        self.movie1.genres.add(self.action, self.drama)
        
        self.movie2 = Movie.objects.create(title="Movie 2", avg_rating=7.0)
        self.movie2.genres.add(self.comedy)
        
        self.movie3 = Movie.objects.create(title="Movie 3", avg_rating=9.0)
        self.movie3.genres.add(self.action)
        
        self.movie4 = Movie.objects.create(title="Movie 4", avg_rating=6.5)
        self.movie4.genres.add(self.drama)
        
        # Create users
        self.user1 = User.objects.create_user(username="user1", password="testpass123")
        self.user2 = User.objects.create_user(username="user2", password="testpass123")
        
        # Create user profiles with favorite genres
        self.profile1 = UserProfile.objects.create(user=self.user1)
        self.profile1.favorite_genres.add(self.action)
        
        self.profile2 = UserProfile.objects.create(user=self.user2)
        self.profile2.favorite_genres.add(self.drama)
        
        # Create ratings
        Rating.objects.create(user=self.user1, movie=self.movie1, value=9)
        Rating.objects.create(user=self.user2, movie=self.movie1, value=8)
        Rating.objects.create(user=self.user2, movie=self.movie4, value=7)
    
    def test_genre_recommendations(self):
        """Test genre-based recommendations"""
        # User1 likes action, should get Movie3 (action movie they haven't rated)
        recs = get_genre_recommendations(self.user1)
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0], self.movie3)
        
        # User2 likes drama, should get no recommendations (as they've rated all drama movies)
        recs = get_genre_recommendations(self.user2)
        self.assertEqual(len(recs), 0)
    
    def test_collaborative_recommendations(self):
        """Test collaborative recommendations"""
        # User1 and User2 both rated Movie1 highly, so User1 might like Movie4 (which User2 liked)
        recs = get_collaborative_recommendations(self.user1)
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0], self.movie4)
