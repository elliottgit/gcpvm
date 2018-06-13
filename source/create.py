import os

createcmd = 'gcloud compute instances create myvm --image-family ubuntu-1604-lts --image-project ubuntu-os-cloud --boot-disk-size 30GB --boot-disk-type pd-ssd --machine-type n1-highmem-2 --min-cpu-platform "Intel Skylake"'
print 'Creating VM...'
os.system(createcmd)