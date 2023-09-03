from rest_framework import routers

from article import views

urlpatterns = []
app_name = 'article'
router = routers.SimpleRouter()
router.register('', views.ArticleView)
urlpatterns += router.urls
