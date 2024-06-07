from flask import Blueprint, current_app, render_template, request
from sqlalchemy import create_engine , ForeignKey , Column , String , Integer , CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

insert_bp = Blueprint('insert', __name__,static_folder="templates/static" , template_folder="templates")

@insert_bp.route("", methods=['GET', 'POST'])
@insert_bp.route("/", methods=['GET', 'POST'])
def people():
    Base = declarative_base()

    class Person (Base) :
        __tablename__ = "people"

        id = Column ("id" , Integer , primary_key=True)
        first_name = Column ("first_name" , String)
        last_name = Column ("last_name" , String)

        def __init__ (self, id , first_name , last_name) :
            self.id = id
            self.first_name = first_name
            self.last_name = last_name
        
        def __repr__ (self) : 
            return f"id : {self.id} , first_name : {self.first_name} , last_name : {self.last_name}"

    engine = create_engine('postgresql+psycopg2://postgres:QaZxcv54321@localhost/test' , echo=True)

    
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    if request.method == "POST":
        try :
            id = request.form['insert_id']
            firstname = request.form['insert_firstname']
            lastname = request.form['insert_lastname']
        except :
            id = "insert id" 
            firstname = "insert first name" 
            lastname = "insert last name"
        finally :
            if id !=  "insert id":
                print (id , firstname , lastname)
                person = Person(int(id) , str(firstname) , str(lastname))
                session.add(person)
                session.commit()
                id_list = list() 
                firstname_list = list()
                lastname_list = list()
                results = session.query(Person).all()
                print(len(results))
                print(type(results))
                print(results)
                for_loop = 0
                for result in results : 
                    for_loop +=1
                    result = str(result)
                    changed_results = result.split(",")
                    id_list.append(changed_results[0])
                    firstname_list.append(changed_results[1])
                    lastname_list.append(changed_results[2])

            id_list = list() 
            firstname_list = list()
            lastname_list = list()
            results = session.query(Person).all()
            print(len(results))
            print(type(results))
            print(results)
            for_loop = 0
            for result in results : 
                for_loop +=1
                result = str(result)
                changed_results = result.split(",")
                id_list.append(changed_results[0])
                firstname_list.append(changed_results[1])
                lastname_list.append(changed_results[2])
    else :
        id_list = list() 
        firstname_list = list()
        lastname_list = list()
        results = session.query(Person).all()
        print(len(results))
        print(type(results))
        print(results)
        for_loop = 0
        for result in results : 
            for_loop +=1
            result = str(result)
            changed_results = result.split(",")
            id_list.append(changed_results[0])
            firstname_list.append(changed_results[1])
            lastname_list.append(changed_results[2])


    return render_template (
        "insert.html",
        for_loop = for_loop ,
        id_result = id_list ,
        firstname_result = firstname_list,
        lastname_result = lastname_list 
    )

