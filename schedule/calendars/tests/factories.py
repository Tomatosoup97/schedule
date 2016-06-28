import datetime
import factory

from factory.django import DjangoModelFactory 
from django.utils import timezone

from users.tests.factories import HostFactory, ClientFactory
from calendars.models import Meeting, Tag, Suggestion, Category

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'category%d' % n)

class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: 'tag%d' % n)

class MeetingFactory(DjangoModelFactory):
    class Meta:
        model = Meeting

    private = False
    public = False
    start = timezone.now()
    end = start + datetime.timedelta(days=1)

    @factory.post_generation
    def hosts(self, create, extracted, **kwargs):
        # Add hosts passed as an argument
        # syntax: Factory.create(host(host1, host2))
        if not create:
            self.hosts.add(HostFactory())

        if extracted:
            for host in extracted:
                self.hosts.add(host)

class SuggestionFactory(DjangoModelFactory):
    class Meta:
        model = Suggestion

    meeting = MeetingFactory()
    title = factory.Sequence(lambda n: 'suggestion%d' % n)