from simple_blogger import Journalist
from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from datetime import datetime

class Project(Journalist):
    def __init__(self, **kwargs):
        super().__init__(            
            review_chat_id=-1002374309134,
            first_post_date=datetime(2025, 1, 1),
            text_generator=OpenAITextGenerator(),
            topic_word_limit=100,
            **kwargs)

    def _get_category_folder(self, task):
        return task['country']
                    
    def _get_topic_folder(self, task):
        return task['topic']

    def _task_converter(self, item):
        return { 
            "topic": item['name'],
            "location": item['location'],
            "country": item['country'],
            "topic_prompt": f"Расскажи интересный факт про {item['name']}, который находятся в {item['location']} {item['country']}, используй не более {self.topic_word_limit} слов, используй смайлики",
            "topic_image": f"Нарисуй {item['name']}, который находятся в {item['location']} {item['country']}",
            "category": item['country'],
        }
    
    def _system_prompt(self, task):
        return f"Ты - блогер с 1000000 миллионном подписчиков"
    
   