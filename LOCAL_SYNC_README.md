# Instructions for setting up local auto sync.

## Settting up SSH access

The ReMarkable has an SSH server running constantly.
Go into the Help/Copyright info and you'll see your devices IP (same as the web 
USB server).

Add your SSH public key to `.ssh/authorized_keys` on the ReMarkable.
It only works with RSA keys, ecdsa won't work.
