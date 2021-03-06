from django.urls import path

from frontend.views import index
from frontend.views import home,activity,tracker,update_candidateprojects,sample,inprogress,projectinvites,update_finished,invites,\
    projectdetails,pendingproject,terms,dev,pricing,howitworks,privacy,report,credits
from accounts.views import update_profile

app_name = 'frontend'
urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('tracker/<int:id>', tracker, name='tracker'),
    path('dev', dev, name='dev'),
    path('howitworks', howitworks, name='howitworks'),
    path('pricing', pricing, name='pricing'),
    path('report/<str:email>/<int:transaction_id>', report, name='report'),
    path('privacy', privacy, name='privacy'),
    path('terms', terms, name='terms'),
    path('sample', sample, name='sample'),
    path('credits', credits, name='credits'),
    path('inprogress/<int:user_id>', inprogress, name='inprogress'),
    path('invites/', invites, name='invites'),
    path('pendingproject/<int:transaction_id>', pendingproject, name='pendingproject'),
    path('projectdetails/<int:id>', projectdetails, name='projectdetails'),
    path('activity/', activity, name='my-activity'),
    path('update_profile/', update_profile, name='update-profile'),
    path('projectinvites/<int:transaction_id>/<int:candidate_id>', projectinvites, name='update-profile'),
    path('update_finished/<int:candidateproject_id>/<int:transaction_id>', update_finished,
         name='update_finished'),
    path('update_candidateprojects/<int:candidateproject_id>/<int:transaction_id>', update_candidateprojects,
         name='update_candidateprojects'),
]
