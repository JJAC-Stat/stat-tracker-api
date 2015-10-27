def generate_datapoints():
    from faker import Faker
    fake = Faker()
    for _ in range(50):
        user = User.objects.create_user(username=fake.user_name(),password='password',email=fake.email())
        user.save()
        print(user)



def generate_datapoints():
    import json
    from faker import Faker
    import random
    fake = Faker()
    activities=[]
    for x in range(100):
        activity = {'fields':{'title':fake.text(max_nb_chars=50),
                            'timestamp':str(fake.date_time_this_year()),
                            'user': random.choice(range(1,51)),
                            },
                    'model':'api.Activity',}
        activities.append(activity)
        print(activity)
    with open('./api/fixtures/activities.json', 'w') as f:
        f.write(json.dumps(activities))

def generate_datapoints():
    import json
    from faker import Faker
    import random
    fake = Faker()
    datapoints = []
    for _ in range(500):
        datapoint = {'fields':{'value':randint(1,100),
                            'timestamp':str(fake.date_time_this_year()),
                            'activity': random.choice(range(1,51)),
                            'question':random.choice(range(1,100))
                            },
                    'model':'api.DataPoint',}
        print(datapoint)
        answers.append(datapoint)
    with open('./api/fixtures/datapoints.json', 'w') as f:
        f.write(json.dumps(datapoints))
