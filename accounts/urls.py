
from django.urls import path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('cambiar-datos/', views.update_user, name='update_user'),
    path('cambiar-contraseña/', views.update_password, name='update_password'),
    path('registro/', views.register, name='register'),
    path('entrar/', views.login, name='login'),
    path('salir/', views.logout, name='logout'),
    path('recuperar-contraseña/',
        views.password_reset_request,
        name='password_reset'
    ),
    path('recuperar-contraseña-ok/', 
        auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password/password_reset_done.html'
        ),
        name='password_reset_done',
    ),
    path('recuperar-contraseña-completo/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password/password_reset_complete.html'
            ),
            name='password_reset_complete',
    ),
    path('recuperar-contraseña-confirmar/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password/password_reset_confirm.html',
        success_url=reverse_lazy("accounts:password_reset_complete")
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_confirm',
        views.password_reset_request,
        name="password_reset"
    )

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
