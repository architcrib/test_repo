from django.urls import path

from . import views

urlpatterns = {
    path('tenant/<int:tenant_id>', views.TenantViewSet.as_view(
        {
            'get': 'get_tenant'

        }
    )),
    path('operator/<int:operator_id>', views.OperatorViewSet.as_view(
        {
            'get': 'get_operator'
        }
    )),
    path('tenant/', views.SpecialOperatorViewSet.as_view(
        {
            'post': 'add_tenant'
        }
    ))
}
