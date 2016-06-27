import factory
from factory.django import DjangoModelFactory 

from users.models import BasicUser, HostProfile, ClientProfile

class UserFactory(DjangoModelFactory):
    class Meta:
        model = BasicUser

    username = factory.Sequence(lambda n: 'user%d' % n)

class HostFactory(DjangoModelFactory):
    class Meta:
        model = HostProfile

    user = factory.SubFactory(UserFactory)

class ClientFactory(DjangoModelFactory):
    class Meta:
        model = ClientProfile

    user = factory.SubFactory(UserFactory)