import os
from config import *


userinput = raw_input(inputmsg)
while (userinput != 'exit'):

	if (userinput == 'create'):
		print 'Creating VM...'
		os.system(createcmd)
		userinput = raw_input(inputmsg)
		
	elif (userinput == 'stop'):
		print 'Stopping VM...'
		os.system(stopcmd)
		userinput = raw_input(inputmsg)
		
		
	elif (userinput == 'start'):
		print 'Starting VM...'
		os.system(startcmd)
		userinput = raw_input(inputmsg)
		
	elif (userinput == 'list'):
		print 'Listing VM...'
		os.system(listcmd)
		userinput = raw_input(inputmsg)

	elif (userinput == 'delete'):
		# listvmcmd = 'gcloud compute instances list'
		# os.system(listvmcmd)
		# vmname = raw_input("Enter vm name: ")
		print 'Deleting VM...'
		# deletecmd = 'gcloud compute instances delete %s' % vmname
		os.system(deletecmd)
		userinput = raw_input(inputmsg)

	else:
		print 'Invalid option '
		userinput = raw_input(inputmsg)
