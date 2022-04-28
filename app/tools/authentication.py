from app.models import Comercio, Empleado
from app.tools.exceptions import AuthenticationFailedError


class BasicAuthentication:
    def authenticate_credentials(self, db, username, password, request=None):
        try:
            api_key = UUID(username)
        except ValueError:
            return AuthenticationFailedError, False

        try:
            comercio = db.query(Comercio).filter(Comercio.api_key==api_key).first()
            if comercio is None:
                return AuthenticationFailedError, False
        except Exception:
            return AuthenticationFailedError, False

        return comercio, None
    
    def get_user(self, username):
        try:
            return Comercio.objects.get(pk=user_id)
        except Comercio.DoesNotExist:
            return None