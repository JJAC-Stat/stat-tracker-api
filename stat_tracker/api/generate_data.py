from django.contrib.auth.models import User
from api.models import Activity, DataPoint


def generate_users():
    from faker import Faker
    fake = Faker()
    for _ in range(50):
        user = User.objects.create_user(username=fake.user_name(),password='password',email=fake.email())
        user.save()
        print(user)



def generate_activities():
    import json
    from faker import Faker
    import random
    fake = Faker()
    activities=[]
    activity_list = ['running', 'biking', 'walking',
                'double dutch', 'cook a meal', 'have a snack',
                'walk the dog', 'watch a movie', 'bake a cake',
                'order pizza']
    for x in range(100):
    #     activity = {'fields':{'title':random.choice(activity_list),
    #                         'timestamp':str(fake.date_time_this_year())[:10],
    #                         'user': random.choice(User.objects.all())
    #                         },
    #                 'model':'api.Activity',}
    #     activities.append(activity)
    #     print(activity)
    # with open('activities.json', 'w') as f:
    #     f.write(json.dumps(activities))
        activity = Activity(title=random.choice(activity_list),
                             timestamp=str(fake.date_time_this_year())[:10],
                             user= random.choice(User.objects.all()))
        activity.save()
        print(activity)

def generate_datapoints():
    import json
    from faker import Faker
    import random
    fake = Faker()
    datapoints = []
    for _ in range(500):
    #     datapoint = {'fields':{'value':random.randint(1,100),
    #                         'timestamp':str(fake.date_time_this_year())[:10],
    #                         'activity': random.choice(range(1,100))
    #                         },
    #                 'model':'api.DataPoint',}
    #     print(datapoint)
    #     datapoints.append(datapoint)
    # with open('datapoints.json', 'w') as f:
    #     f.write(json.dumps(datapoints))
        datapoint = DataPoint(value=random.randint(1,100),
                          timestamp=str(fake.date_time_this_year())[:10],
                          activity = random.choice(Activity.objects.all()))
        datapoint.save()
        print(datapoint)

def get_all():
    User.objects.all().delete()
    Activity.objects.all().delete()
    DataPoint.objects.all().delete()
    
    generate_users()
    generate_activities()
    generate_datapoints()
