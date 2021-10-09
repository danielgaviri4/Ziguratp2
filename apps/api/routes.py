
from rest_framework.routers import DefaultRouter
from apps.api.views import UserModelView
from apps.api.views import CondominioView




router = DefaultRouter()

router.register(r'users',UserModelView,basename = 'users')
router.register(r'cond',CondominioView,basename = 'cond')



urlpatterns = router.urls