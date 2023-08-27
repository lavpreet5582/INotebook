from rest_framework_simplejwt.tokens import RefreshToken


def get_user_token(user):
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    return access_token