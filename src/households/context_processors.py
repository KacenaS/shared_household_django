from .models import Membership

def current_household(request):
    if request.user.is_authenticated:
        membership = Membership.objects.filter(user=request.user).select_related('household').first()
        if membership:
            return {'current_household': membership.household}
    return {'current_household': None}