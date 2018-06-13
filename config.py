# vm name
vmname = 'myvm'

# disk size
disksize = '10GB'

# vm type
vmtype = 'n1-standard-8'

# commands to be excuted
inputmsg = 'start, stop, create, list, delete, or exit: '

createcmd = 'gcloud compute instances create %s --image-family ubuntu-1604-lts --image-project ubuntu-os-cloud --boot-disk-size %s --boot-disk-type pd-ssd --machine-type %s --min-cpu-platform "Intel Skylake"' % (vmname, disksize, vmtype)

listcmd = 'gcloud compute instances list'

deletecmd = 'gcloud compute instances delete %s' % vmname

stopcmd = 'gcloud compute instances stop %s' % vmname

startcmd = 'gcloud compute instances start %s' % vmname
