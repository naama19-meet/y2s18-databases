from knowledge_model import Base, knowledge

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


def query_all_articles():
	pass
	

def query_article_by_topic(topic):
	return session.query( 
       knowledge).filter_by(
       topic=topic).all()
    




	

def delete_article_by_topic():
	pass

def delete_all_articles():
	 pass

def edit_article_rating():
	
	add_article("climbing","sports", 10)
	add_article("basketball", "hobbis", 7)
	add_article("howtopizza", "food", 4)


print(query_article_by_topic("hobbis"))