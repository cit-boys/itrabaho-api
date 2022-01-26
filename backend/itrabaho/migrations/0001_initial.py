# Generated by Django 3.2.7 on 2021-10-18 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=11, unique=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('lastLogin', models.DateField(blank=True, null=True)),
                ('userType', models.CharField(blank=True, choices=[('R', 'Recruiter'), ('A', 'Applicant'), ('L', 'LGU Representative')], max_length=1, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearsOfExperience', models.PositiveSmallIntegerField()),
                ('highesteducationAttained', models.CharField(choices=[('N', 'None'), ('E', 'Elementary'), ('H', 'High School'), ('U', 'College Undergraduate'), ('B', "Bachelor's Degree"), ('A', 'Associate Degree'), ('M', "Master's Degree"), ('D', 'Doctorate Degree')], max_length=1)),
            ],
            options={
                'verbose_name': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='ApplicantModel',
            fields=[
                ('usermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='itrabaho.usermodel')),
                ('address', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('E', 'Employed'), ('U', 'Unemployed')], max_length=1)),
            ],
            options={
                'verbose_name': 'Applicant',
            },
            bases=('itrabaho.usermodel',),
        ),
        migrations.CreateModel(
            name='LGURepresentativeModel',
            fields=[
                ('usermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='itrabaho.usermodel')),
                ('barangay', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'LGU Representative',
            },
            bases=('itrabaho.usermodel',),
        ),
        migrations.CreateModel(
            name='RecruiterModel',
            fields=[
                ('usermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='itrabaho.usermodel')),
                ('address', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Recruiter',
            },
            bases=('itrabaho.usermodel',),
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itrabaho.categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField()),
                ('comment', models.CharField(blank=True, max_length=250, null=True)),
                ('fromUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('toUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Review',
            },
        ),
        migrations.CreateModel(
            name='JobPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('barangay', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, choices=[('H', 'Hiring'), ('A', 'Active'), ('D', 'Done')], default='H', max_length=1, null=True)),
                ('description', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=50)),
                ('datetimeCreated', models.DateTimeField(auto_now_add=True)),
                ('datetimeEnded', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=250)),
                ('applicantReviewId', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='itrabaho.reviewmodel')),
                ('recruiterReviewId', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_job_post', to='itrabaho.reviewmodel')),
                ('applicantId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepted_jobs', to='itrabaho.applicantmodel')),
                ('recruiterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_jobs', to='itrabaho.recruitermodel')),
            ],
            options={
                'verbose_name': 'Job Model',
            },
        ),
        migrations.CreateModel(
            name='ExperienceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(max_length=250)),
                ('startMonth', models.CharField(max_length=10)),
                ('startYear', models.CharField(max_length=10)),
                ('endMonth', models.CharField(max_length=10)),
                ('endYear', models.CharField(max_length=10)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='itrabaho.profilemodel')),
            ],
            options={
                'verbose_name': 'Experience',
            },
        ),
        migrations.CreateModel(
            name='ExperienceDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='itrabaho.experiencemodel')),
            ],
            options={
                'verbose_name': 'Experience Detail',
            },
        ),
        migrations.CreateModel(
            name='ActivityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('M', 'Match'), ('R', 'Review'), ('A', 'Accepted')], max_length=1)),
                ('datetimeCreated', models.DateTimeField(auto_now_add=True)),
                ('objectId', models.PositiveSmallIntegerField()),
                ('contentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='MatchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveSmallIntegerField()),
                ('percentage', models.PositiveSmallIntegerField()),
                ('jobPostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itrabaho.jobpostmodel')),
                ('applicantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itrabaho.applicantmodel')),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='ApplicantsListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobPostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='itrabaho.jobpostmodel')),
                ('applicantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='itrabaho.applicantmodel')),
            ],
            options={
                'verbose_name': 'ApplicantsList',
                'default_related_name': 'job_applications',
            },
        ),
        migrations.AddField(
            model_name='applicantmodel',
            name='LGURepresentativeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itrabaho.lgurepresentativemodel'),
        ),
        migrations.AddField(
            model_name='applicantmodel',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='itrabaho.profilemodel'),
        ),
    ]
