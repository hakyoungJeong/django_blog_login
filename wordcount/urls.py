
from django.contrib import admin
from django.urls import path,include
import wordcounts.urls
import blog.urls
import account.urls
from django.conf import settings
from django.conf.urls.static import static #이거랑 위에거 미디어파일쓸때 꼭넣어줘야함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.list, name = "list"),
    path('blog/',include(blog.urls)),
    path('wordcounts/',include(wordcounts.urls)),
    path('account/',include(account.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)