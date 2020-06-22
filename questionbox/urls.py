"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as questionbox_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', questionbox_views.homepage, name="homepage"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('questionbox/add_question', questionbox_views.add_question, name="add_question"),
    path('questionbox/<int:question_pk>/add_answer', questionbox_views.add_answer, name="add_answer"),
    path('questionbox/your_questions', questionbox_views.display_your_questions, name="your_questions"),
    path('questionbox/<int:question_pk>/show_question', questionbox_views.show_question, name="show_question"),
    path('questionbox/<int:question_pk>/delete_question', questionbox_views.delete_question, name="delete_question"),
    path('questionbox/<int:question_pk>/edit_question', questionbox_views.edit_question, name="edit_question"),
    # path('questionbox/search', questionbox_views.search, name="search")
    # path('user_profile', name="profile")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
