from django.core.management.base import BaseCommand
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(name='Thor', email='thor@asgard.com'),
            User(name='Iron Man', email='ironman@starkindustries.com'),
            User(name='Hulk', email='hulk@smash.com'),
            User(name='Black Widow', email='blackwidow@shield.com'),
            User(name='Captain America', email='cap@avengers.com'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Avengers')
        team1.save()
        team1.members.set(users)

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60, date='2025-04-01'),
            Activity(user=users[1], activity_type='Running', duration=45, date='2025-04-02'),
            Activity(user=users[2], activity_type='Swimming', duration=30, date='2025-04-03'),
            Activity(user=users[3], activity_type='Yoga', duration=50, date='2025-04-04'),
            Activity(user=users[4], activity_type='Weightlifting', duration=40, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, points=500),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Morning Run', description='A quick morning run', duration=30),
            Workout(name='Evening Yoga', description='Relaxing yoga session', duration=60),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
