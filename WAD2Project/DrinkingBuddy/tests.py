from django.test import TestCase
from django.core.urlresolvers import reverse
from DrinkingBuddy.models import *


class PageMethodTests(TestCase):

    def test_page_slug_creation(self):
        owner = User.objects.create_user(username="Test Name", password=None, email=None)
        owner_profile = UserProfile(user=owner, owner=True, )
        owner_profile.save()
        page = Page(name ="Bar Name", description = "", address = "", owner=owner_profile)
        page.save()
        self.assertEquals(page.slug, "bar-name")


class IndexViewTests(TestCase):
    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_index_view_with_no_recent_bars(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no bars.")
        self.assertQuerysetEqual(response.context['recent'], [])

    def test_index_view_with_no_rated_bars(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no bars.")
        self.assertQuerysetEqual(response.context['highest_rated'], [])

    def test_index_view_without_login(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign Up")
        self.assertContains(response, "Login")

    def test_index_view_with_login(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Account")
        self.assertContains(response, "Log Out")


class BarPagesViewTest(TestCase):

    def test_bar_pages_no_bars(self):
        response = self.client.get(reverse('barPages'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no bars")
        self.assertQuerysetEqual(response.context['pages'], [])

    def test_bar_pages_with_bars(self):
        user1 = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        user2 = User.objects.create_user('temporary2', 'temporary2@gmail.com', 'temporary2')
        user3 = User.objects.create_user('temporary3', 'temporary3@gmail.com', 'temporary3')
        user1.save()
        user2.save()
        user3.save()
        profile1 = UserProfile(user=user1, owner=True)
        profile2 = UserProfile(user=user2, owner=True)
        profile3 = UserProfile(user=user3, owner=True)
        profile1.save()
        profile2.save()
        profile3.save()
        bar1 = Page(name ="bar1", description = "", address = "", owner=profile1)
        bar2 = Page(name ="bar2", description = "", address = "", owner=profile2)
        bar3 = Page(name ="bar3", description = "", address = "", owner=profile3)
        bar1.save()
        bar2.save()
        bar3.save()
        response = self.client.get(reverse('barPages'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "bar1")
        self.assertContains(response, "bar2")
        self.assertContains(response, "bar3")
        self.assertQuerysetEqual(response.context['pages'], ['<Page: bar1>','<Page: bar2>','<Page: bar3>'])


class BarViewTest(TestCase):

    def test_bar_no_comments(self):
        user1 = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        user1.save()
        profile1 = UserProfile(user=user1, owner=True)
        profile1.save()
        bar1 = Page(name ="bar1", description = "", address = "", owner=profile1)
        bar1.save()

        response = self.client.get(reverse('bar', args = [bar1.slug]))
        self.assertContains(response, "There are no comments on this bar yet.")
        self.assertQuerysetEqual(response.context['comments'], [])

    def test_bar_with_comments(self):
        user1 = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        user1.save()
        profile1 = UserProfile(user=user1, owner=True)
        profile1.save()
        bar1 = Page(name ="bar1", description = "", address = "", owner=profile1)
        bar1.save()
        comment1 = Comment(comment = 'New comment', commenter = profile1, page = bar1)
        comment1.save()

        response = self.client.get(reverse('bar', args = [bar1.slug]))
        self.assertContains(response, "New comment")
        self.assertQuerysetEqual(response.context['comments'], ['<Comment: temporary: "New comment...">'])

    def test_bar_with_login(self):
        user1 = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        user1.save()
        user2 = User.objects.create_user('temporary2', 'temporary2@gmail.com', 'temporary2')
        user2.save()
        profile1 = UserProfile(user=user1, owner=True)
        profile1.save()
        profile2 = UserProfile(user=user2, owner=True)
        profile2.save()
        bar1 = Page(name ="bar1", description = "", address = "", owner=profile1)
        bar1.save()

        self.client.login(username='temporary2', password='temporary2')
        response = self.client.get(reverse('bar', args = [bar1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Submit Comment")
        self.assertContains(response, "Submit Rating")

    def test_bar_with_owner_login(self):
        user1 = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        user1.save()
        profile1 = UserProfile(user=user1, owner=True)
        profile1.save()
        bar1 = Page(name ="bar1", description = "", address = "", owner=profile1)
        bar1.save()

        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('bar', args = [bar1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Change Picture")


class MyAccountViewTest(TestCase):

    def test_account_bar_owner(self):
        user1 = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        user1.save()
        profile1 = UserProfile(user=user1, owner=True)
        profile1.save()
        bar1 = Page(name ="bar1", description = "", address = "", owner=profile1)
        bar1.save()

        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('myAccount'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Your bar")

    def test_account_not_owner(self):
        user1 = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        user1.save()
        profile1 = UserProfile(user=user1, owner=True)
        profile1.save()

        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('myAccount'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Change Picture")