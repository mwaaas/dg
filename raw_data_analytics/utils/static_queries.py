__author__ = 'Lokesh'
static_query = {
    'numAdoption' : {
        ('animator', ):'''SELECT
                            programs_partner.partner_name,
                            geographies_country.country_name,
                            geographies_state.state_name,
                            geographies_district.district_name,
                            geographies_block.block_name,
                            geographies_village.village_name,
                            people_animatorwisedata.animator_id,
                            people_animatorwisedata.animator_name,
                            COUNT(DISTINCT (activities_pmawisedata.pma_id)) AS 'Total Viewers',
                            COUNT(DISTINCT (activities_pmawisedata.person_id)) AS 'Unique Viewers'
                        FROM
                            people_animatorwisedata
                                JOIN
                            activities_screeningwisedata ON activities_screeningwisedata.animator_id = people_animatorwisedata.animator_id
                                JOIN
                            activities_pmawisedata ON activities_pmawisedata.screening_id = activities_screeningwisedata.screening_id
                                LEFT JOIN
                            geographies_village ON geographies_village.id = activities_screeningwisedata.village_id
                                LEFT JOIN
                            geographies_block ON geographies_block.id = geographies_village.block_id
                                LEFT JOIN
                            geographies_district ON geographies_district.id = geographies_block.district_id
                                LEFT JOIN
                            geographies_state ON geographies_state.id = geographies_district.state_id
                                LEFT JOIN
                            geographies_country ON geographies_country.id = geographies_state.country_id
                                LEFT JOIN
                            programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id;''',

        ('video', ):'''SELECT
                        programs_partner.partner_name,
                        geographies_country.country_name,
                        geographies_state.state_name,
                        geographies_district.district_name,
                        geographies_block.block_name,
                        geographies_village.village_name,
                        videos_video_wisedata.video_id,
                        videos_video_wisedata.title,
                        COUNT(DISTINCT (activities_personadoptpractice.id)) AS 'Total Adoptions',
                        COUNT(DISTINCT (activities_personadoptpractice.person_id)) AS 'Unique Adoptions'
                    FROM
                        activities_personadoptpractice
                            JOIN
                        videos_video_wisedata ON videos_video_wisedata.video_id = activities_personadoptpractice.video_id
                            JOIN
                        activities_screeningwisedata ON activities_screeningwisedata.video_id = videos_video_wisedata.video_id
                            LEFT JOIN
                        geographies_village ON geographies_village.id = activities_screeningwisedata.village_id
                            LEFT JOIN
                        geographies_block ON geographies_block.id = geographies_village.block_id
                            LEFT JOIN
                        geographies_district ON geographies_district.id = geographies_block.district_id
                            LEFT JOIN
                        geographies_state ON geographies_state.id = geographies_district.state_id
                            LEFT JOIN
                        geographies_country ON geographies_country.id = geographies_state.country_id
                            JOIN
                        programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id;''',

        ('person', ):'''SELECT
                            programs_partner.partner_name,
                            geographies_country.country_name,
                            geographies_state.state_name,
                            geographies_district.district_name,
                            geographies_block.block_name,
                            geographies_village.village_name,
                            people_person.person_name,
                            COUNT(DISTINCT (activities_personadoptpractice.id)) AS 'Total Adoptions'
                        FROM
                            people_person
                                JOIN
                            activities_personadoptpractice ON activities_personadoptpractice.person_id = people_person.id
                                LEFT JOIN
                            geographies_village ON geographies_village.id = people_person.village_id
                                LEFT JOIN
                            geographies_block ON geographies_block.id = geographies_village.block_id
                                LEFT JOIN
                            geographies_district ON geographies_district.id = geographies_block.district_id
                                LEFT JOIN
                            geographies_state ON geographies_state.id = geographies_district.state_id
                                LEFT JOIN
                            geographies_country ON geographies_country.id = geographies_state.country_id
                                LEFT JOIN
                            programs_partner ON programs_partner.id = people_person.partner_id;''',

        ('persongroup', ):'''yoyoyoyo''',

        ('animator','video'):'''SELECT
                                    programs_partner.partner_name,
                                    geographies_country.country_name,
                                    geographies_state.state_name,
                                    geographies_district.district_name,
                                    geographies_block.block_name,
                                    geographies_village.village_name,
                                    people_animatorwisedata.animator_name,
                                    videos_video_wisedata.title,
                                    COUNT(DISTINCT (activities_personadoptpractice.id)) AS 'Total Adoptions',
                                    COUNT(DISTINCT (activities_personadoptpractice.person_id)) AS 'Unique Adoptions'
                                FROM
                                    people_animatorwisedata
                                        JOIN
                                    activities_screeningwisedata ON activities_screeningwisedata.animator_id = people_animatorwisedata.animator_id
                                        JOIN
                                    activities_pmawisedata ON activities_pmawisedata.screening_id = activities_screeningwisedata.screening_id
                                        LEFT JOIN
                                    videos_video_wisedata ON videos_video_wisedata.video_id = activities_screeningwisedata.video_id
                                        LEFT JOIN
                                    activities_personadoptpractice ON activities_personadoptpractice.person_id = activities_pmawisedata.person_id
                                        AND videos_video_wisedata.video_id = activities_personadoptpractice.video_id
                                        LEFT JOIN
                                    geographies_village ON activities_screeningwisedata.village_id = geographies_village.id
                                        LEFT JOIN
                                    geographies_block ON geographies_village.block_id = geographies_block.id
                                        LEFT JOIN
                                    geographies_district ON geographies_district.id = geographies_block.district_id
                                        LEFT JOIN
                                    geographies_state ON geographies_state.id = geographies_district.state_id
                                        LEFT JOIN
                                    geographies_country ON geographies_country.id = geographies_state.country_id
                                        JOIN
                                    programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id;''',

        ('animator','persongroup'):"13456",

        ('animator','video','persongroup'):"1234567o",

        ('video','person'):'''SELECT
                                    programs_partner.partner_name,
                                    geographies_country.country_name,
                                    geographies_state.state_name,
                                    geographies_district.district_name,
                                    geographies_block.block_name,
                                    geographies_village.village_name,
                                    people_animatorwisedata.animator_name,
                                    video_video_wisedata.title,
                                    COUNT(DISTINCT (activities_personadoptpractice.id)) AS 'Total Adoptions',
                                    COUNT(DISTINCT (activities_personadoptpractice.person_id)) AS 'Unique Adoptions'
                                FROM
                                    people_animatorwisedata
                                        JOIN
                                    activities_screeningwisedata ON activities_screeningwisedata.animator_id = people_animatorwisedata.animator_id
                                        LEFT JOIN
                                    activities_pmawisedata ON activities_pmawisedata.screening_id = activities_screeningwisedata.screening_id
                                        LEFT JOIN
                                    videos_video_wisedata ON videos_video_wisedata.video_id = activities_screeningwisedata.video_id
                                        LEFT JOIN
                                    activities_personadoptpractice ON activities_personadoptpractice.person_id = activities_pmawisedata.person_id
                                        AND videos_video_wisedata.video_id = activities_personadoptpractice.video_id
                                        LEFT JOIN
                                    geographies_village ON activities_screeningwisedata.village_id = geographies_village.id
                                        LEFT JOIN
                                    geographies_block ON geographies_village.block_id = geographies_block.id
                                        LEFT JOIN
                                    geographies_district ON geographies_district.id = geographies_block.district_id
                                        LEFT JOIN
                                    geographies_state ON geographies_state.id = geographies_district.state_id
                                        LEFT JOIN
                                    geographies_country ON geographies_country.id = geographies_state.country_id
                                        JOIN
                                    programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id;''',

        ('video','persongroup'):"fjekvwlkngr",

        ('video','person','persongroup'):"egwegr",

        ('person','persongroup'):"gbgbgbgbgbgbggbgbgbgbgbgbgbg",
    },


    'attendance' : {
        ('animator', ):'''select
                            programs_partner.partner_name,
                            geographies_country.country_name,
                            geographies_state.state_name,
                            geographies_district.district_name,
                            geographies_block.block_name,
                            geographies_village.village_name,
                            people_animatorwisedata.animator_id,
                            people_animatorwisedata.animator_name,
                            count(distinct (activities_personmeetingattendance.id)) as 'Total Viewers',
                            count(distinct (activities_personmeetingattendance.person_id)) as 'Unique Viewers'
                        from
                            people_animatorwisedata
                                join
                            activities_screeningwisedata ON activities_screeningwisedata.animator_id = people_animatorwisedata.animator_id
                                join
                            activities_personmeetingattendance ON activities_personmeetingattendance.screening_id = activities_screeningwisedata.screening_id
                                left join
                            geographies_village ON geographies_village.id = activities_screeningwisedata.village_id
                                left join
                            geographies_block ON geographies_block.id = geographies_village.block_id
                                left join
                            geographies_district ON geographies_district.id = geographies_block.district_id
                                left join
                            geographies_state ON geographies_state.id = geographies_district.state_id
                                left join
                            geographies_country ON geographies_country.id = geographies_state.country_id
                                left join
                            programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id;''',

        ('video', ):'''select
                            programs_partner.partner_name,
                            geographies_country.country_name,
                            geographies_state.state_name,
                            geographies_district.district_name,
                            geographies_block.block_name,
                            geographies_village.village_name,
                            videos_video_wisedata.video_id,
                            videos_video_wisedata.title,
                            count(distinct (activities_personmeetingattendance.id)) as 'Total Viewers',
                            count(distinct (activities_personmeetingattendance.person_id)) as 'Unique Viewers'
                        from
                            videos_video_wisedata
                                left join
                            activities_screeningwisedata ON activities_screeningwisedata.video_id = videos_video_wisedata.video_id
                                left join
                            activities_personmeetingattendance ON activities_personmeetingattendance.screening_id = activities_screeningwisedata.screening_id
                                left join
                            geographies_village ON geographies_village.id = activities_screeningwisedata.village_id
                                left join
                            geographies_block ON geographies_block.id = geographies_village.block_id
                                left join
                            geographies_district ON geographies_district.id = geographies_block.district_id
                                left join
                            geographies_state ON geographies_state.id = geographies_district.state_id
                                left join
                            geographies_country ON geographies_country.id = geographies_state.country_id
                                left join
                            programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id;''',

        ('persongroup', ):'''select
                                programs_partner.partner_name,
                                geographies_country.country_name,
                                geographies_state.state_name,
                                geographies_district.district_name,
                                geographies_block.block_name,
                                geographies_village.village_name,
                                people_persongroup.id,
                                people_persongroup.group_name,
                                count(distinct (activities_personmeetingattendance.id)) as 'Total Viewers',
                                count(distinct (activities_personmeetingattendance.person_id)) as 'Unique Viewers'
                            from
                                activities_screeningwisedata
                                    left join
                                activities_personmeetingattendance ON activities_personmeetingattendance.screening_id = activities_screeningwisedata.screening_id
                                    left join
                                people_person ON people_person.id = activities_personmeetingattendance.person_id
                                    left join
                                people_persongroup ON people_persongroup.id = people_person.group_id
                                    left join
                                geographies_village ON geographies_village.id = activities_screeningwisedata.village_id
                                    left join
                                geographies_block ON geographies_block.id = geographies_village.block_id
                                    left join
                                geographies_district ON geographies_district.id = geographies_block.district_id
                                    left join
                                geographies_state ON geographies_state.id = geographies_district.state_id
                                    left join
                                geographies_country ON geographies_country.id = geographies_state.country_id
                                    left join
                                programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id;''',

        ('animator','video'):'''select
                                    programs_partner.partner_name,
                                    geographies_country.country_name,
                                    geographies_state.state_name,
                                    geographies_district.district_name,
                                    geographies_block.block_name,
                                    geographies_village.village_name,
                                    people_animatorwisedata.animator_id,
                                    people_animatorwisedata.animator_name,
                                    videos_video_wisedata.video_id,
                                    videos_video_wisedata.title,
                                    count(distinct (activities_personmeetingattendance.id)) as 'Total Viewers',
                                    count(distinct (activities_personmeetingattendance.person_id)) as 'Unique Viewers'
                                from
                                    people_animatorwisedata
                                        join
                                    activities_screeningwisedata ON activities_screeningwisedata.animator_id = people_animatorwisedata.id
                                        left join
                                    activities_personmeetingattendance ON activities_personmeetingattendance.screening_id = activities_screeningwisedata.screening_id
                                        left join
                                    videos_video_wisedata ON videos_video_wisedata.video_id = activities_screeningwisedata.video_id
                                        left join
                                    geographies_village ON geographies_village.id = activities_screeningwisedata.village_id
                                        left join
                                    geographies_block ON geographies_block.id = geographies_village.block_id
                                        left join
                                    geographies_district ON geographies_district.id = geographies_block.district_id
                                        left join
                                    geographies_state ON geographies_state.id = geographies_district.state_id
                                        left join
                                    geographies_country ON geographies_country.id = geographies_state.country_id
                                        left join
                                    programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id''',

        ('animator','persongroup'):'''select
                                            programs_partner.partner_name,
                                            geographies_country.country_name,
                                            geographies_state.state_name,
                                            geographies_district.district_name,
                                            geographies_block.block_name,
                                            geographies_village.village_name,
                                            people_animatorwisedata.animator_id,
                                            people_animatorwisedata.animator_name,
                                            people_persongroup.id,
                                            people_persongroup.group_name,
                                            count(distinct (activities_personmeetingattendance.id)) as 'Total Viewers',
                                            count(distinct (activities_personmeetingattendance.person_id)) as 'Unique Viewers'
                                        from
                                            people_animatorwisedata
                                                join
                                            activities_screeningwisedata ON activities_screeningwisedata.animator_id = people_animatorwisedata.id
                                                join
                                            activities_personmeetingattendance ON activities_personmeetingattendance.screening_id = activities_screeningwisedata.screening_id
                                                join
                                            activities_screening_farmer_groups_targeted ON activities_screening_farmer_groups_targeted.screening_id = activities_screeningwisedata.screening_id
                                                left join
                                            people_persongroup ON people_persongroup.id = activities_screening_farmer_groups_targeted.persongroup_id
                                                left join
                                            geographies_village ON geographies_village.id = activities_screeningwisedata.village_id
                                                left join
                                            geographies_block ON geographies_block.id = geographies_village.block_id
                                                left join
                                            geographies_district ON geographies_district.id = geographies_block.district_id
                                                left join
                                            geographies_state ON geographies_state.id = geographies_district.state_id
                                                left join
                                            geographies_country ON geographies_country.id = geographies_state.country_id
                                                left join
                                            programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id''',

        ('animator','video','persongroup'):'''select
                                                programs_partner.partner_name,
                                                geographies_country.country_name,
                                                geographies_state.state_name,
                                                geographies_district.district_name,
                                                geographies_block.block_name,
                                                geographies_village.village_name,
                                                people_animatorwisedata.animator_id,
                                                people_animatorwisedata.animator_name,
                                                people_persongroup.id,
                                                people_persongroup.group_name,
                                                videos_video_wisedata.video_id,
                                                videos_video_wisedata.title,
                                                count(distinct (activities_personmeetingattendance.id)) as 'Total Viewers',
                                                count(distinct (activities_personmeetingattendance.person_id)) as 'Unique Viewers'
                                            from
                                                people_animatorwisedata
                                                    join
                                                activities_screeningwisedata ON activities_screeningwisedata.animator_id = people_animatorwisedata.animator_id
                                                    left join
                                                videos_video_wisedata ON videos_video_wisedata.video_id = activities_screeningwisedata.video_id
                                                    join
                                                activities_screening_farmer_groups_targeted ON activities_screening_farmer_groups_targeted.screening_id = activities_screeningwisedata.screening_id
                                                    join
                                                activities_personmeetingattendance ON activities_personmeetingattendance.screening_id = activities_screeningwisedata.screening_id
                                                    left join
                                                people_persongroup ON people_persongroup.id = activities_screening_farmer_groups_targeted.persongroup_id
                                                    left join
                                                geographies_village ON geographies_village.id = activities_screeningwisedata.village_id
                                                    left join
                                                geographies_block ON geographies_block.id = geographies_village.block_id
                                                    left join
                                                geographies_district ON geographies_district.id = geographies_block.district_id
                                                    left join
                                                geographies_state ON geographies_state.id = geographies_district.state_id
                                                    left join
                                                geographies_country ON geographies_country.id = geographies_state.country_id
                                                    left join
                                                programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id''',

        ('video','persongroup'):'''select
                                        programs_partner.partner_name,
                                        geographies_country.country_name,
                                        geographies_state.state_name,
                                        geographies_district.district_name,
                                        geographies_block.block_name,
                                        geographies_village.village_name,
                                        videos_video_wisedata.video_id,
                                        videos_video_wisedata.title,
                                        people_persongroup.id,
                                        people_persongroup.group_name,
                                        count(distinct (activities_personmeetingattendance.id)) as 'Total Viewers',
                                        count(distinct (activities_personmeetingattendance.person_id)) as 'Unique Viewers'
                                    FROM
                                        activities_personadoptpractice
                                            join
                                        videos_video_wisedata ON videos_video_wisedata.video_id = activities_personadoptpractice.video_id
                                            join
                                        activities_screeningwisedata ON activities_screeningwisedata.video_id = videos_video_wisedata.video_id
                                            join
                                        activities_personmeetingattendance ON activities_personmeetingattendance.screening_id = activities_screeningwisedata.screening_id
                                            join
                                        activities_screening_farmer_groups_targeted ON activities_screening_farmer_groups_targeted.screening_id = activities_screeningwisedata.screening_id
                                            left join
                                        people_persongroup ON people_persongroup.id = activities_screening_farmer_groups_targeted.persongroup_id
                                            left join
                                        geographies_village ON geographies_village.id = people_persongroup.village_id
                                            left join
                                        geographies_block ON geographies_block.id = geographies_village.block_id
                                            left join
                                        geographies_district ON geographies_district.id = geographies_block.district_id
                                            left join
                                        geographies_state ON geographies_state.id = geographies_district.state_id
                                            left join
                                        geographies_country ON geographies_country.id = geographies_state.country_id
                                            left join
                                        programs_partner ON programs_partner.id = activities_screeningwisedata.partner_id''',
    }
}

#   'select M.id,M.name,St.state_name,D.district_name,B.block_name,V.village_name,count(distinct(S.id)) as \'Screenings\',count(distinct (PMA.id)) \'Total Viewers\',count(distinct (PMA.person_id)) as \'Distinct Viewers\',count(distinct (PAP.id)) as \'Total Adoptions\',count(distinct (PAP.person_id)) as \'Unique Adopters\' from  people_animator M join people_animatorassignedvillage AAV ON M.id = AAV.animator_id left join geographies_village V ON V.id = AAV.village_id left join geographies_block B ON B.id = V.block_id left join geographies_district D ON D.id = B.district_id left join geographies_state St ON St.id = D.state_id join activities_screening S ON S.animator_id = M.id join activities_screening_videoes_screened SVS ON SVS.screening_id = S.id join activities_personmeetingattendance PMA ON PMA.screening_id = S.id left join activities_personadoptpractice PAP ON PMA.person_id = PAP.person_id and PAP.video_id = SVS.video_id and PAP.date_of_adoption > \'2014-10-01\'where S.date between \'2014/09/01\' and \'2014/11/31\'group by M.id;'