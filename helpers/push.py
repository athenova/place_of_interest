import json
import random
from datetime import date

TOPIC_WORD_LIMIT = 100

tasks_file = 'files/in_progress.json'

tasks = []
input_file = f"files/places_of_interest.json"
data = json.load(open(input_file, "rt", encoding="UTF-8"))
for item in data:
    task = { 
        "name": item['name'],
        "text_prompt": f"Расскажи интересный факт про {item['name']}, который находятся в {item['location']} {item['country']}, используй не более {TOPIC_WORD_LIMIT} слов, используй смайлики",
        "image_prompt": f"Нарисуй {item['name']}, который находятся в {item['location']} {item['country']}",
        "group": item['country'],
    }
    tasks.append(task)

random.seed(date.today().year)
random.shuffle(tasks)

for i, task in enumerate(tasks):
    task['index'] = i + 1

json.dump(tasks, open(tasks_file, 'wt', encoding='UTF-8'), indent=4, ensure_ascii=False)
print(f"{len(tasks)} tasks created")
