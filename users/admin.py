from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register
from .models import Profile
# Register your models here.
@register(Profile)
class ProfileAdmin(MaterialModelAdmin):
	pass
	
	