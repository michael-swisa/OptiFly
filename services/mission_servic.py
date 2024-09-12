import csv
import json

from packege import file


# המיון הוא שהמטרה עם המרחק הכי גדול יהיה לה את הציון הכי גבוה
def distance_scores(targets, max_score_percentage):
    sorted_targets = sorted(targets, key=lambda x: x['distance'], reverse=True)

    max_distance = sorted_targets[0]['distance']
    targets_with_scores = []

    for target in sorted_targets:
        score = (target['distance'] / max_distance) * max_score_percentage
        new_score = {'City': target['City'], 'score': score}
        targets_with_scores.append(new_score)

    return targets_with_scores


# המיון של המטוסים הוא שמי שמגיע הכי רחוק יש לו את הציון הכי גבוה
def aircraft_type_scores(aircrafts, max_score_percentage):
    sorted_aircrafts = sorted(aircrafts, key=lambda x: x['fuel_capacity'], reverse=True)

    max_distance = sorted_aircrafts[0]['fuel_capacity']
    aircrafts_with_scores = []

    for aircraft in sorted_aircrafts:
        score = (aircraft['fuel_capacity'] / max_distance) * max_score_percentage
        new_score = {'type': aircraft['type'], 'score': score}
        aircrafts_with_scores.append(new_score)

    return aircrafts_with_scores


# מיון של הטייסים לפי המיומנות ככל שיש לטייס מיומנות יותר גבוה הציון שלו יותר גבה
def skill_level_scores(pilots, max_score_percentage):
    sorted_pilots = sorted(pilots, key=lambda x: x['skill_level'], reverse=True)

    max_distance = sorted_pilots[0]['skill_level']
    pilots_with_scores = []

    for pilot in sorted_pilots:
        score = (pilot['skill_level'] / max_distance) * max_score_percentage
        new_score = {'name': pilot['name'], 'score': score}
        pilots_with_scores.append(new_score)

    return pilots_with_scores


# מיון מטרות לפי מזג האויר
def weather_scores(targets, max_score_percentage):
    sorted_targets = sorted(targets, key=lambda x: x['wind_speed'], reverse=True)

    max_wind_speed = sorted_targets[0]['wind_speed']
    targets_with_scores = []

    for target in sorted_targets:
        max_clouds = 100
        cloud_score = max(0, 1 - (target["clouds"] / max_clouds))
        wind_score = max(0, 1 - (target["wind_speed"] / max_wind_speed))
        final_score = target['weather'] * cloud_score * wind_score
        normalized_score = final_score * 100
        adjusted_score = normalized_score * (max_score_percentage / 100)
        final_score = max(1, min(adjusted_score, max_score_percentage))
        new_score = {'City': target['City'], 'score': final_score}
        targets_with_scores.append(new_score)

    return targets_with_scores


def priority_scores(targets, max_score_percentage):
    sorted_targets = sorted(targets, key=lambda x: x['Priority'], reverse=True)

    max_distance = int(sorted_targets[0]['Priority'])
    targets_with_scores = []

    for target in sorted_targets:
        score = (int(target['Priority']) / max_distance) * max_score_percentage
        new_score = {'City': target['City'], 'score': score}
        targets_with_scores.append(new_score)

    return targets_with_scores


weights = {
    "distance": 0.20,
    "aircraft_type": 0.25,
    "pilot_skill": 0.25,
    "weather_conditions": 0.20,
    "priority": 0.10
}


def creating_proposals_for_tasks(url_target, url_aircraft, url_pilot, ):
    list_target = file.read_json(url_target)
    list_pilots = file.read_json(url_pilot)
    list_aircraft = file.read_json(url_aircraft)

    # יצירת ליסט של מטרות ממונינות ביחס עם אחוזים ביחס למרחק
    distance_scores_list = distance_scores(list_target, 20)

    # ליסט של מטוסים עם אחוזים ביחס למרחק שהם יכולים להגיע
    aircraft_type_scores_list = aircraft_type_scores(list_aircraft, 25)

    # ליסט של טייסים עם אחוזים ביחס למיומנות
    skill_level_scores_list = skill_level_scores(list_pilots, 25)

    # ליסט של מטרות ממוינות לפי החשיבות
    priority_scores_list = priority_scores(list_target, 10)

    # ליסט של מטרות ממוינות לפי מזג האויר
    weather_scores_list = weather_scores(list_target, 20)

    Task_suggestions_list = []


url_target = r'C:\_kodcode2\second half\Python\OptiFly\models\targets.json'
url_aircraft = r'C:\_kodcode2\second half\Python\OptiFly\files\aircrafts.json'
url_pilot = r'C:\_kodcode2\second half\Python\OptiFly\files\pilots.json'
creating_proposals_for_tasks(url_target, url_aircraft, url_pilot)

data_target = file.read_json(url_target)
data_pilot = file.read_json(url_pilot)
data_aircraft = file.read_json(url_aircraft)

data = [
    ["target_city", "priority", "assigned_pilot", "assigned_aircraft", "distance", "weather_conditions", "pilot_skill",
     "aircraft_speed", "fuel_capacity"]]
for i in range(len(data_target)):
    for j in range(len(data_pilot)):
        for k in range(len(data_aircraft)):
            data.append([data_target[i]['City'], int(data_target[i]['Priority']), data_pilot[j]['name'],
                         data_aircraft[k]['type'], data_target[i]['distance'], data_target[i]['weather'],
                         data_pilot[j]['skill_level'], data_aircraft[k]['speed'], data_aircraft[k]['fuel_capacity']])

print(data)
with open('data_semicolon.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=';')
    csv_writer.writerows(data)
