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
	knowledge44 = session.query(
	knowledge).all()
	return knowledge44



	

def query_article_by_topic(topic):
	return session.query( 
       knowledge).filter_by(
       topic=topic).all()



    




	

def delete_article_by_topic(topic):




   session.query(knowledge).filter_by(
       topic=topic).delete()
   session.commit()




	

def delete_all_articles():
	session.query(knowledge).all
	session.commit()


	
	add_article("climbing","sports", 10)
	add_article("basketball", "hobbis", 7)
	add_article("howtopizza", "food", 4)



#print(query_article_by_topic("hobbis")

print(query_all_articles())

print(query_article_by_topic("hobbis"))

delete_article_by_topic("food")

(delete_all_articles()):

# articel1 = knowledge( namearticel="wether", topic="rainbow", rating=9 )
# # print(articel1)

# articel2 = knowledge( namearticel="basketball", topic="hobbis", rating=7 )
# # print(articel2)


# articel3 = knowledge( namearticel="howtopizza", topic="food", rating=4 )
# # print(articel3)



# session.add(articel1)
# session.add(articel2)
# session.add(articel3)
# session.commit()


# print(query_all_articles())
# p

