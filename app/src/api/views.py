from rest_framework import viewsets, routers
from backend.models import Pokemon
from .serializers import UserSerializer


class UserApi(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = Pokemon.objects.all()
        L_id = self.request.query_params.get('id')

        if L_id:
            queryset = queryset.filter(user_id=L_id)
        return queryset

router = routers.DefaultRouter()
router.register(r'user', UserApi)