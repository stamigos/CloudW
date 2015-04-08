def include_login_form(request):
    from django.contrib.auth.forms import AuthenticationForm
    form = AuthenticationForm()
    return {'login_form': form}


def user(request):
    """A context processor that adds the user to template context"""
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return {
                'user_fullname': request.user.username
            }
        else:
            return {
                'user_fullname': request.user.first_name + ' ' + request.user.last_name,
            }
    return {
        'user_fullname': ''
    }

