import os.path


from activities.models import PersonAdoptPractice
from people.models import Animator
from videos.models import Video
from activities.models import Screening
from django.core.management.base import BaseCommand, CommandError

import csv

class Command(BaseCommand):

	def handle(self, *args, **options):
	
		#transfering adoption for PersonAdoptPractice
		"""ids = {3418:3544, 3769:3972, 4075:4098, 4115:4102}

		
		for key, value  in ids.iteritems():
			file = 'C:\Users\Abhishek\Desktop\\'+str(key)+'.csv'
			csvfile = open(file, 'rb')
			reader = csv.reader(csvfile)
			for read in reader:
				
				print read
				pap = PersonAdoptPractice.objects.get(id=read[0])
				if pap.video_id == key:
					pap.video_id = value
					pap.save()
					print key, value, pap.video_id
				
	        csvfile.close()"""

	    #transfering screening for activities_screeningvideosscreened	
		sc = Screening.objects.filter(videoes_screened__id = 3973).values_list('id')
		print type(sc)
		s = sc[0]
		print type(s[0])
		print s[0]


			
