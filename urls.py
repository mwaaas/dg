from django.conf.urls.defaults import *
from dg.views import *
from django.contrib.auth.views import login, logout
from dg.output.views import common, overviewAnalytics, videoAnalytics, screeningAnalytics, others
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dg/', include('dg.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^feeds/persons/$', feed_person_html_on_person_group),
    (r'^feeds/person_pract/$',feed_person_prac_pg_anim),
	(r'^feeds/persons_village/(\d+)/$', feeds_persons_village),
	(r'^feeds/test/(\d+)/$', test),
	(r'^feeds/test_gwt/(\d+)/$', test_gwt),
#    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
	(r'^animators-by-village-id/(\d+)/$', feed_animators),
    (r'/search/', search),
    (r'^dashboard/getkey/$', get_key_for_user),
    (r'^dashboard/setkey/$', set_key_for_user),
	(r'^dashboard/login/$', login_view),
    (r'^dashboard/saveregiononline/((?P<id>\d*)/)?$', save_region_online),
    (r'^dashboard/getregionsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_regions_online),
    (r'^dashboard/saveregionoffline/$', save_region_offline),
    (r'^dashboard/savestateonline/((?P<id>\d*)/)?$', save_state_online),
    (r'^dashboard/getstatesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_states_online),
    (r'^dashboard/savestateoffline/$', save_state_offline),
    (r'^dashboard/savefieldofficeronline/((?P<id>\d*)/)?$', save_fieldofficer_online),
    (r'^dashboard/getfieldofficersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_fieldofficers_online),
    (r'^dashboard/savefieldofficeroffline/$', save_fieldofficer_offline),
    (r'^dashboard/savepracticeonline/((?P<id>\d*)/)?$', save_practice_online),
    (r'^dashboard/getpracticesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_practices_online),
    (r'^dashboard/savepracticeoffline/$', save_practice_offline),
    (r'^dashboard/savelanguageonline/((?P<id>\d*)/)?$', save_language_online),
    (r'^dashboard/getlanguagesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_languages_online),
    (r'^dashboard/savelanguageoffline/$', save_language_offline),
    (r'^dashboard/savepartneronline/((?P<id>\d*)/)?$', save_partner_online),
    (r'^dashboard/getpartnersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_partners_online),
    (r'^dashboard/savepartneroffline/$', save_partner_offline),
    (r'^dashboard/savevideoonline/((?P<id>\d*)/)?$', save_video_online),
    (r'^dashboard/getvideosonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_videos_online),
    (r'^dashboard/savevideooffline/$', save_video_offline),
    (r'^dashboard/getvideorelatedagriculturalpracticesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_videoagriculturalpractices_online),
    (r'^dashboard/savevideorelatedagriculturalpracticesonline/$', save_videoagriculturalpractices_online),
    (r'^dashboard/savevideorelatedagriculturalpracticesoffline/$', save_videoagriculturalpractices_offline),
    (r'^dashboard/savevideofarmersonline/', save_personshowninvideo_online),
    (r'^dashboard/getvideofarmersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?', get_personshowninvideo_online),
    (r'^dashboard/savevideofarmersoffline/', save_personshowninvideo_offline),
    (r'^dashboard/savedevelopmentmanageronline/((?P<id>\d*)/)?$', save_developmentmanager_online),
    (r'^dashboard/getdevelopmentmanagersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_developmentmanagers_online),
    (r'^dashboard/savedevelopmentmanageroffline/$', save_developmentmanager_offline),
    (r'^dashboard/saveequipmentonline/((?P<id>\d*)/)?$', save_equipment_online),
    (r'^dashboard/getequipmentsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_equipments_online),
    (r'^dashboard/saveequipmentoffline/$', save_equipment_offline),    
    (r'^dashboard/savedistrictonline/((?P<id>\d*)/)?$', save_district_online),
    (r'^dashboard/getdistrictsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_districts_online),
    (r'^dashboard/savedistrictoffline/$', save_district_offline),
    (r'^dashboard/saveblockonline/((?P<id>\d*)/)?$', save_block_online),
    (r'^dashboard/getblocksonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_blocks_online),
    (r'^dashboard/saveblockoffline/$', save_block_offline),
    (r'^dashboard/savevillageonline/((?P<id>\d*)/)?$', save_village_online ),
    (r'^dashboard/getvillagesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_villages_online),
    (r'^dashboard/savevillageoffline/$', save_village_offline),
    (r'^dashboard/saveanimatoronline/((?P<id>\d*)/)?$', save_animator_online),
    (r'^dashboard/getanimatorsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_animators_online),
    (r'^dashboard/saveanimatoroffline/$', save_animator_offline),
    (r'^dashboard/saveanimatorassignedvillageonline/((?P<id>\d*)/)?$', save_animatorassignedvillage_online),
    (r'^dashboard/getanimatorassignedvillagesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_animatorassignedvillages_online),
    (r'^dashboard/saveanimatorassignedvillageoffline/$', save_animatorassignedvillage_offline),
    (r'^dashboard/savepersongrouponline/((?P<id>\d*)/)?$', save_persongroup_online),
    (r'^dashboard/getpersongroupsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_persongroups_online),
    (r'^dashboard/savepersongroupoffline/$', save_persongroup_offline),
    (r'^dashboard/savepersononline/((?P<id>\d*)/)?$', save_person_online),
    (r'^dashboard/getpersonsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_persons_online),
    (r'^dashboard/savepersonoffline/$', save_person_offline),
    (r'^dashboard/savescreeningonline/((?P<id>\d*)/)?$', save_screening_online),
    (r'^dashboard/getscreeningsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_screenings_online),
    (r'^dashboard/savescreeningoffline/$', save_screening_offline),
    (r'^dashboard/savescreeningfarmergroupstargetedsonline/',save_groupstargetedinscreening_online),
    (r'^dashboard/getscreeningfarmergroupstargetedsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?',get_groupstargetedinscreening_online),
    (r'^dashboard/savescreeningfarmergroupstargetedsoffline/',save_groupstargetedinscreening_offline),
    (r'^dashboard/savescreeningvideosscreenedsonline/', save_videosscreenedinscreening_online),
    (r'^dashboard/getscreeningvideosscreenedsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?', get_videosscreenedinscreening_online),
    (r'^dashboard/savescreeningvideosscreenedsoffline/', save_videosscreenedinscreening_offline),
    (r'^dashboard/savetrainingonline/((?P<id>\d*)/)?$', save_training_online),
    (r'^dashboard/gettrainingsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_trainings_online),
    (r'^dashboard/savetrainingoffline/$', save_training_offline),
    (r'^dashboard/savetraininganimatorstrainedonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', save_traininganimatorstrained_online),
    (r'^dashboard/gettraininganimatorstrainedonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_traininganimatorstrained_online),
    (r'^dashboard/savetraininganimatorstrainedoffline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', save_traininganimatorstrained_offline),
    (r'^dashboard/savemonthlycostpervillageonline/$', save_monthlycostpervillage_online),
    (r'^dashboard/getmonthlycostpervillagesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_monthlycostpervillages_online),
    (r'^dashboard/savemonthlycostpervillageoffline/$', save_monthlycostpervillage_offline),
    (r'^dashboard/saveanimatorsalarypermonthonline/$', save_animatorsalarypermonth_online),
    (r'^dashboard/getanimatorsalarypermonthsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_animatorsalarypermonths_online),
    (r'^dashboard/saveanimatorsalarypermonthoffline/$', save_animatorsalarypermonth_offline),
    (r'^dashboard/savepersonrelationonline/$', save_personrelation_online),
    (r'^dashboard/getpersonrelationsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_personrelations_online),
    (r'^dashboard/savepersonrelationoffline/$', save_personrelation_offline),
    (r'^dashboard/savepersonmeetingattendanceonline/$', save_personmeetingattendance_online),
    (r'^dashboard/getpersonmeetingattendancesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_personmeetingattendances_online),
    (r'^dashboard/savepersonmeetingattendanceoffline/$', save_personmeetingattendance_offline),
    (r'^dashboard/savepersonadoptpracticeonline/$', save_personadoptpractice_online),
    (r'^dashboard/getpersonadoptpracticesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_personadoptpractices_online),
    (r'^dashboard/savepersonadoptpracticeoffline/$', save_personadoptpractice_offline),
    (r'^dashboard/saveequipmentholderonline/$', save_equipmentholder_online),
    (r'^dashboard/getequipmentholdersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_equipmentholders_online),
    (r'^dashboard/saveequipmentholderoffline/$', save_equipmentholder_offline),
    (r'^dashboard/saverevieweronline/$', save_reviewer_online),
    (r'^dashboard/getreviewersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_reviewers_online),
    (r'^dashboard/saverevieweroffline/$', save_reviewer_offline),          
    (r'^dashboard/language/add/$', add_language),
	(r'^dashboard/languages/(?P<language>[^/]+)/$',language),
	(r'^dashboard/region/add/$',add_region),
	(r'^dashboard/regions/$',region),
	(r'^dashboard/state/add/$',add_state),
	(r'^dashboard/states/$',state),
	(r'^dashboard/district/add/$', add_district),
	(r'^dashboard/districts/$', district),
	(r'^dashboard/block/add/$', add_block),
	(r'^dashboard/blocks/$', block),
	(r'^dashboard/persongroup/add/$', add_person_group),
	(r'^dashboard/persongroups/$', person_group),
	(r'^dashboard/developmentmanager/add/$', add_development_manager),
	(r'^dashboard/developmentmanagers/$', development_manager),
	(r'^dashboard/animatorassignedvillage/add/$', add_animator_assigned_village),
	(r'^dashboard/animatorassignedvillages/$', animator_assigned_village),
	(r'^dashboard/animator/add/$', add_animator),
	(r'^dashboard/animators/$', animator),
	(r'^dashboard/fieldofficer/add/$', add_field_officer),
	(r'^dashboard/fieldofficers/$', field_officer),
	(r'^dashboard/partner/add/$', add_partner),
	(r'^dashboard/partners/$', partner),
	(r'^dashboard/person/add/$', add_person),
	(r'^dashboard/persons/$', person),
	(r'^dashboard/practice/add/$', add_practice),
	(r'^dashboard/practices/$', practice),
	(r'^dashboard/village/add/$', add_village),
	(r'^dashboard/villages/$', village),
	(r'^dashboard/video/add/$', add_video),
	(r'^dashboard/videos/', video),
	(r'^dashboard/screening/add/$', add_screening),
	(r'^dashboard/screenings/$', screening),
	(r'^dashboard/login/$', login),
	(r'^dashboard/logout/$', logout),
    (r'^home/$', others.base_home),    
    (r'^team/$', others.base_team),
    (r'^team_board/$', others.base_team_board),
    (r'^team_adviser/$', others.base_team_adviser),
    (r'^team_acclaw/$', others.base_team_acclaw),
    (r'^team_intern/$', others.base_team_intern),
    (r'^team_alumni/$', others.base_team_alumni),
    (r'^press/$', others.base_press),
    (r'^partner/$', others.base_partner),
    (r'^career/$', others.base_career),
    (r'^contact/$', others.base_contact),
    (r'^career_immediate/$', others.base_career_immediate),    
    (r'^output/dropdownval/$',common.overview_drop_down),
    (r'^output/overview/module/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',overviewAnalytics.new_overview),
    (r'^output/overview/line/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',common.overview_line_graph),
    (r'^output/video/module/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',videoAnalytics.video_module),
    (r'^output/video/mfpie/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',videoAnalytics.video_pie_graph_mf_ratio),
    (r'^output/video/actorpie/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',videoAnalytics.video_actor_wise_pie),
    (r'^output/video/typepie/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',videoAnalytics.video_type_wise_pie),
    (r'^output/video/geogpie/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',videoAnalytics.video_geog_pie_data),
    (r'^output/video/practicescatter/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',videoAnalytics.video_practice_wise_scatter),
    (r'^output/video/languagescatter/data/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',videoAnalytics.video_language_wise_scatter_data),
    (r'^output/video/monthbar/data/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',videoAnalytics.video_monthwise_bar_data),
    (r'^output/video/monthbar/settings/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',videoAnalytics.video_monthwise_bar_settings),
    (r'^output/screening/module/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',screeningAnalytics.screening_module),
    (r'^output/screening/mfpie/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',screeningAnalytics.screening_mf_ratio),
    (r'^output/screening/geogpie/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',screeningAnalytics.screening_geog_pie_data),
    (r'^output/screening/totlines/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',screeningAnalytics.screening_tot_lines),
    (r'^output/screening/percentlines/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',screeningAnalytics.screening_percent_lines),
    (r'^output/screening/monthbar/data/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',screeningAnalytics.screening_monthwise_bar_data),
    (r'^output/screening/monthbar/settings/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',screeningAnalytics.screening_monthwise_bar_settings),
    (r'^output/screening/practicescatter/(?P<geog>country|state|district|block|village)/(?P<id>\d+)/$',screeningAnalytics.screening_practice_wise_scatter_data),
)
