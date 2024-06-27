from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()
    
class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
      
	fieldsets = UserAdmin.fieldsets+ (
        (                      
            'Some heading', # you can also use None 
            {
                'fields': (
					"phd_year",
					"is_international_student",
					"is_first_gen",
					"phd_year_boundary",
					"international_student",
					"first_gen",
					"experience_tags",
					"other_info",
                ),
            },
        ),
    )

	list_display = [
		"email",
		"username",
		"is_superuser",
		"phd_year",
		"is_international_student",
		"is_first_gen",
		"phd_year_boundary",
		"international_student",
		"first_gen",
		"get_experience_tags",
		"other_info",
	]

admin.site.register(CustomUser, CustomUserAdmin)
