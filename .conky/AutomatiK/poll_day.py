"""import time, os



DateCommand='date +"%m-%d-%y"'
Date0=os.popen(DateCommand).read()


def job():
	global Date0
	DateNow=os.popen(DateCommand).read()
	if DateNow != Date0:
		os.system("./start")
		#os.system("conky -q -c clockfile")
		Date0=os.popen(DateCommand).read()
		
		
if __name__ == '__main__':
    while True:
        job()
        time.sleep(60)
"""


import subprocess
import time

while True:
    # Get current time
    current_time = time.strftime("%H:%M:%S", time.localtime())

    # Check if it's midnight
    if current_time == "00:00:00":
        # Execute bash script
        subprocess.Popen(["./bash.sh"])

    # Wait for 1 minute
    time.sleep(60)


"""
import time
import datetime

def job():
    print("Le script est exécuté à minuit !")
    os.system("./start")

def run_at_midnight():
    while True:
        # Récupérer la date et l'heure actuelles
        now = datetime.datetime.now()

        # Calculer le temps restant jusqu'à minuit
        midnight = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
        time_to_midnight = (midnight - now).total_seconds()

        # Si le temps restant est inférieur à 10 secondes, exécuter la tâche
        if time_to_midnight <= 10:
            job()
            # Attendre jusqu'à la fin de la journée pour éviter de relancer immédiatement
            time.sleep(24 * 3600 - 10)
        else:
            # Attendre 10 secondes avant de vérifier à nouveau
            time.sleep(10)

if __name__ == "__main__":
    run_at_midnight()
"""
