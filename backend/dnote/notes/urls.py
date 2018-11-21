from django.conf.urls import url
from .views import NoteViewSet

note_list = NoteViewSet.as_view({'get' : 'list', 'post' : 'create'})

note_detail = NoteViewSet.as_view(
    {'get' : 'retrieve', 'patch' : 'partial_update', 'delete' : 'destory'}
)

urlpatterns = [
    url('notes/', note_list, name='note-list'),
    url('notes/<int:pk>/', note_detail, name='note-detail'),
]
