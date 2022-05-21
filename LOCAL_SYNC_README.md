# Instructions for setting up local auto sync.

This works by setting up a trigger using udev to rsync our files from the 
ReMarkable to a folder on your local host.
The idea is that you can set the local directory to be somewhere 
cloud-synced (e.g. Nextcloud, Dropbox), and back up directly from
the ReMarkable to there without the need for the ReMarkable cloud.

This is usefuls if you don't have a subscription plan with them.

## Settting up SSH access

The ReMarkable has an SSH server running constantly.
Go into the Help/Copyright info and you'll see your devices IP (same as the web 
USB server).

Add your SSH public key to `.ssh/authorized_keys` on the ReMarkable.
It only works with RSA keys, ecdsa won't work.

## Configuring the backup script

1. First edit the script to set the backup path you want on the local host, and 
   the IP address of your remarkable.
   The IP address is the one you go to when using the USB web interface (you don't 
   need the web interface activated for this to work).
2. Then copy ``
