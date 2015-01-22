__author__ = 'Lokesh'

tableDictionary={
    'partner':'programs_partner',
    'country':'geographies_country',
    'state':'geographies_state',
    'district':'geographies_district',
    'block':'geographies_block',
    'village':'geographies_village',
    'animator':'people_animator_wise_data',
    'person':'people_person',
    'persongroup':'people_persongroup',
    'video':'videos_video_wise_data',
    'language':'videos_language',
    'sector':'videos_practicesector',
    'practice':'videos_practice',
    'topic':'videos_practicetopic',
    'numScreening':'activities_screeningwisedata',
#    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
#    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
    'numAdoption':'activities_personadoptpractice',
#    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
#    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
    'attendance':'activities_personmeetingattendance',
    'numPeople':'people_person',
    'numAnimator':'people_animatorwisedata',
    'listPeople':'people_person',
    'listAnimator':'people_animatorwisedata',
    'listVideoScreened':'videos_videowisedata',
    'numVideoScreened':'videos_videowisedata',
    'listVideoProduces':'Videos_videowisedata',
    'numVideoProduced':'videos_videowisedata',
}

whereDictionary={
    'partner':'id',
    'country':'id',
    'state':'id',
    'district':'id',
    'block':'id',
    'village':'id',
    'animator':'animator_id',
    'person':'id',
    'persongroup':'id',
    'video':'id',
    'language':'id',
    'sector':'id',
    'practice':'id',
    'topic':'id',
    'numScreening':'screening_date',
#    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
#    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
    'numAdoption':'date_of_adoption',
#    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
#    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
    'attendance':'',
    'numPeople':'',
    'numAnimator':'',
    'listPeople':'',
    'listAnimator':'',
    'listVideoScreened':'date',
    'numVideoScreened':'date',
    'listVideoProduces':'video_production_end_date',
    'numVideoProduced':'video_production_end_date',
}


categoryDictionary={
    'geographies':['country','state','district','block','village']
}

groupbyDictionary={
    'partner':'id',
    'country':'id',
    'state':'id',
    'district':'id',
    'block':'id',
    'village':'id',
    'animator':'animator_id',
    'person':'id',
    'persongroup':'id',
    'video':'id',
    'language':'id',
    'sector':'id',
    'practice':'id',
    'topic':'id',
    'numScreening':'',
#    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
#    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
    'numAdoption':'',
#    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
#    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
    'attendance':'',
    'numPeople':'',
    'numAnimator':'',
    'listPeople':'',
    'listAnimator':'',
    'listVideoScreened':'',
    'numVideoScreened':'',
    'listVideoProduces':'',
    'numVideoProduced':'',
}

selectDictionary={
    'partner':{'id':True,'partner_name':True},
    'country':{'id':True,'country_name':True},
    'state':{'id':True,'state_name':True},
    'district':{'id':True,'district_name':True},
    'block':{'id':True,'block_name':True},
    'village':{'id':True,'village_name':True},
    'animator':{'animator_id':True,'animator_name':True,'gender':True},
    'person':{'id':True,'person_name':True,'gender':True},
    'persongroup':{'id':True,'group_name':True},
    'video':{'id':True,'title':True},
    'language':{'id':True,'language_name':True},
    'sector':{'id':True,'name':True},
    'practice':{'id':True,'practice_name':True},
    'topic':{'id':True,'name':True},
    'numScreening':{'count(screening_id)':True,'count(distinct screening_id)':True},
#    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
#    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
    'numAdoption':{'count(id)':True,'count(distinct id)':True},
#    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
#    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
    'attendance':{'count(id)':True,'count(distinct id)':True},
    'numPeople':{'count(id)':True,'count(distinct id)':True},
    'numAnimator':{'count(id)':True,'count(distinct id)':True},
    'listPeople':{'person_name':True,'gender':True},
    'listAnimator':{'name':True,'gender':True},
    'listVideoScreened':{'id':True,'title':True},
    'numVideoScreened':{'count(id)':True,'count(distinct id)':True},
    'listVideoProduces':{'id':True,'title':True},
    'numVideoProduced':{'count(id)':True,'count(distinct id)':True},
}


#
# generalDictionary = {
#     'partner':{'table':'programs_partner','column':'partner_name','function':'partner_func()'},
#     'country':{'table':'geographies_country','column':'country_name','function':'country_func()'},
#     'state':{'table':'geographies_state','column':'state_name','function':'state_func()'},
#     'district':{'table':'geographies_district','column':'district_name','function':'district_func()'},
#     'block':{'table':'geographies_block','column':'block_name','function':'block_func()'},
#     'village':{'table':'geographies_village','column':'village_name','function':'village_func()'},
#     'animator':{'table':'people_animator_wise_data','column':'animator_name','function':'animator_func()'},
#     'person':{'table':'people_person','column':'person_name','function':'person_func()'},
#     'persongroup':{'table':'people_persongroup','column':'group_name_name','function':'persongroup_func()'},
#     'video':{'table':'videos_video_wise_data','column':'title','function':'video_func()'},
#     'language':{'table':'videos_language','column':'language_name','function':'language_func()'},
#     'sector':{'table':'videos_practicesector','column':'name','function':'practicesector_func()'},
#     'practice':{'table':'videos_practice','column':'practice_name','function':'practice_func()'},
#     'numScreening':{'table':'people_animator_wise_data','column':'nScreenings','function':'animator_screening_func()'},
# #    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
# #    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
#     'numAdoption':{'table':'people_animator_wise_data','column':'nAdoptions','function':'animator_adoption_func()'},
# #    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
# #    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
#     'screening':{'table':'activities_screening','column':'id','function':'screening_func()'},
#     'adoption':{'table':'activities_personadoptpractice','column':'id','function':'adoption_func()'},
#     'meetingAttendance':{'table':'activities_personmeetingattendance','column':'id','function':'meetingAttendance_func()'},
#     'adoption':{'table':'activities_personadoptpractice','column':'id','function':'adoption_func()'},
#
# }
#