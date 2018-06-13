import os

listcmd = 'gcloud compute instances list'
os.system(listcmd)

vmname = raw_input("Enter vm name: ")
deletecmd = 'gcloud compute instances delete %s' % vmname
print 'Deleting VM...'
os.system(deletecmd)