from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(nameartical,topic,rating):
	nameartical=nameartical
	topic=topic
	rating=rating
    session.add(add_article)
    session.commit()

	add_article("climbing",sports, 10)


add_student("Mayuri", 2, True)


def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
