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
