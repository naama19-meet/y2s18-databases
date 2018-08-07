from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class knowledge(Base):
    # Create a table with 4 columns
    # The first column will be the primary key
    # The second column should be a string representing
    # the name of the Wiki article that you're referencing
    # The third column will be a string representing the 
    # topic of the article. The last column will be
    # an integer, representing your rating of the article.

    #def (self, id, namearticel, topic,rating):
    __tablename__ ='knowledge'
    
    student_id = Column(Integer, primary_key=True)
    namearticel = Column(String)
    topic = Column(String)
    rating = Column(Integer)

    def __repr__(self):
        return ("knowledge student_id : {}\n"
               "knowledge namearticel If you want to learn about: {} \n"
               "knowledge topic you should look at the Wikipedia article called: {} \n"
               "knowledge rating We gave this article a rating of: {} \n" ).format(
                self.student_id, self.namearticel, self.topic, self.rating)


    

articel1 = knowledge( namearticel="wether", topic="rainbow", rating=9 )
print(articel1)

articel2 = knowledge( namearticel="basketball", topic="hobbis", rating=7 )
print(articel2)


articel3 = knowledge( namearticel="howtopizza", topic="food", rating=4 )
print(articel3)


