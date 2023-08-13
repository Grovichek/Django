from rest_framework.views import APIView

class SignInView(APIView):
    def post(self, request):
        ...
class SignUpView(APIView):
    def post(self, request):
        ...

class SignOutView(APIView):
    def post(self, request):
        ...

class ProfileView(APIView):
    def get(self, request):
        ...

    def post(self, request):
        ...

class UpdatePasswordView(APIView):
    def post(self, request):
        ...

class UpdateAvatarView(APIView):
    def post(self, request):
        ...
