from faker import Faker


fake = Faker()


def provide(event, context):
    print(event, context)
    owner = fake.name()
    print("{} is here and would like a cat".format(owner))
    return {'cats': None}
