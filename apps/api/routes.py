
from rest_framework.routers import DefaultRouter
from apps.api.views import UserModelView
from apps.api.views import CondominioView, SubAreaModelView, HouseModelView, PublicationModelView, CommuniqueModelView, CommonAreaModelView, ReservationModelView, AdminHistoryModelView




router = DefaultRouter()

router.register(r'users',UserModelView,basename = 'users')
router.register(r'cond',CondominioView,basename = 'cond')
router.register(r'sub',SubAreaModelView,basename = 'sub')
router.register(r'hom',HouseModelView,basename = 'hom')
router.register(r'pub',PublicationModelView,basename = 'pub')
router.register(r'com',CommuniqueModelView,basename = 'com')
router.register(r'are',CommonAreaModelView,basename = 'are')
router.register(r'res',ReservationModelView,basename = 'res')
router.register(r'adh',AdminHistoryModelView,basename = 'adh')


urlpatterns = router.urls