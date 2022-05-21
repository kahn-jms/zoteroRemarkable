import subprocess
import logging

# user config variables. set these in a .env
# Eventually want an install script that queries for these
REMARKABLE_IP = "10.11.99.1"
LOCAL_BACKUP_PATH = "/home/jkahn/Documents/Nextcloud/ReMarkable/"

# These should be constant, can stay hardcoded
RSYNC_CMD = "rsync -aruq --timeout=2"
STORAGE_BASE = ".local/share/remarkable/xochitl/"
MAX_RETRIES = 3


def syncFromRemarkable():
    ''' Actually execute rsync '''
    command = f"{RSYNC_CMD} root@{REMARKABLE_IP}:{STORAGE_BASE} {LOCAL_BACKUP_PATH}"

    # Try the sync
    for i in range(MAX_RETRIES):
        try:
            subprocess.run(command, capture_output=True, shell=True, check=True)
            return
        except subprocess.CalledProcessError as e:
            logging.error(e)

    # The rsync has failed, so sad
    logging.error("Max retries failed for ReMarkable rsync backup")
    return


if __name__ == "__main__":

    logging.info('ReMarkable connected, backup started')
    syncFromRemarkable()
    logging.info('ReMarkable backup complete')
