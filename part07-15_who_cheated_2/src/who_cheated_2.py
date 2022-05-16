import csv
from datetime import datetime, timedelta
 
def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        maxpts = {}
        sum = []
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            task = int(row[1])
            point = int(row[2])
    
            if name not in maxpts and (time - start_times[name]) < timedelta(hours = 3):
                maxpts[name] = []

            elif task not in maxpts[name] and (time - start_times[name]) < timedelta(hours = 3):
                maxpts[name].append(task, point)
                point += point
            
            elif point > maxpts[name][1] and (time - start_times[name]) < timedelta(hours = 3):
                maxpts[name] = max
            
            print(maxpts[name][task])
            
    # print(maxpts)

final_points()

# dict = {'matti': 43, 'erkki': 45, 'antti': 41, 'emilia': 42, 'henrik': 37, 'arto': 40, 'esko': 45, 'kjell': 47, 'jyrki': 41, 'teemu': 43, 'tiina': 36, 'jenna': 38, 'virpi': 39, 'kalle': 46, 'maija': 40, 'uolevi': 34, 'anna': 45, 'liisa': 42, 'kotivalo': 43, 'justiina': 44, 'matteus': 30, 'markus': 35, 'luukas': 40, 'johannes': 39}

# elif maxpts[name][0] == task and (time - start_times[name]) < timedelta(hours = 3) and max > maxpts[name][1]:
            #     maxpts[name][1] = max

            # elif max > maxpts[name][1] and task != maxpts[name][0] and (time - start_times[name]) < timedelta(hours = 3):
            #     maxpts[name][1] += max
            #     # print(maxpts[name][1])