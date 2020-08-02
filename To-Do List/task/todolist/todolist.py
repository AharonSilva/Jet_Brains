# Write your code here

# todo: Create Missed tasks
# todo: Create Delete task
# todo: Update Menu

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
import calendar

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Menu:
    def __init__(self):
        print("1) Today's tasks\n2) Week's tasks\n3) All tasks"
              "\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit")

    @staticmethod
    def tasks_at_date(query_date):
        task_rows = session.query(Table).filter(Table.deadline == query_date).all()
        if not task_rows:
            return []
        else:
            return [f"{x.task}" for x in task_rows]

    def choose_option(self):
        option = int(input())
        today = datetime.today()
        if option == 1:
            task_list = self.tasks_at_date(today.date())
            print(f'Today {datetime.today().strftime("%b")} {datetime.today().weekday()}:')
            if not task_list:
                print('Nothing to do!\n')
            else:
                for index, task in enumerate(task_list):
                    print(f'{index + 1}. {task}')
                print('')

        elif option == 2:
            print('')
            for x in range(7):
                this_week = (today + timedelta(days=x)).date()
                task_list = self.tasks_at_date(this_week)
                print(f'{calendar.day_name[this_week.weekday()]} {this_week.strftime("%b")} {this_week.day}:')
                if not task_list:
                    print('Nothing to do!')
                else:
                    for index, task in enumerate(task_list):
                        print(f'{index + 1}. {task}')
                print('')

        elif option == 3:
            todo_all = session.query(Table).order_by(Table.deadline).all()
            print('All tasks:')
            if not todo_all:
                print('Nothing to do!\n')
            else:
                for num, row in enumerate(todo_all, start=1):
                    date = row.deadline
                    text_format2 = '{0}. {1}. {2}'
                    date = f'{date.day} {date.strftime("%b")}'
                    print(text_format2.format(num, row, date))
                print('')

        elif option == 4:
            print('Missed tasks:')
            today = datetime.today()
            rows = session.query(Table).filter(Table.deadline < today.date()).order_by(Table.deadline).all()
            if len(rows) >= 1:
                text_format2 = '{0}. {1}. {2}'
                for num, row in enumerate(rows, start=1):
                    date = row.deadline
                    date = f'{date.day} {date.strftime("%b")}'
                    print(text_format2.format(num, row, date))
                print('')
            else:
                print("Nothing is missed!")

        elif option == 5:
            new_task = input('Enter task:\n')
            new_date = datetime.strptime(input('Enter deadline\n'), '%Y-%m-%d').date()
            session.add(Table(task=new_task, deadline=new_date))
            session.commit()
            print('The task has been added!\n')

        elif option == 6:
            print("Choose the number of the task you want to delete:")
            rows = session.query(Table).order_by(Table.deadline).all()
            text_format2 = '{0}. {1}. {2}'
            for num, row in enumerate(rows, start=1):
                date = row.deadline
                date = f'{date.day} {date.strftime("%b")}'
                print(text_format2.format(num, row, date))
            try:
                inp = int(input())
            except ValueError:
                print("Invalid Input")
                return
            session.delete(rows[inp - 1])
            session.commit()
            print("The task has been deleted!")

        elif option == 0:
            exit()

        else:
            print('You\'ve entered an invalid option!\n')


if __name__ == '__main__':
    while True:
        Menu().choose_option()
