from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile
from students.models import Student, FingerprintTemplate
from attendance.models import Course, Session, AttendanceRecord
from devices.models import Device, ScanLog
import datetime, random

class Command(BaseCommand):
    help='Seed demo data (admin/adminpass)'
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            u = User.objects.create_superuser('admin','admin@example.com','adminpass')
        # students
        for i in range(1,61):
            sid=f'STU{i:03}'; name=f'Student {i}'
            s,_=Student.objects.get_or_create(student_id=sid, defaults={'name':name,'department':'CSE','email':f'{sid}@example.com','photo':'/static/icons/avatar.svg'})
            FingerprintTemplate.objects.get_or_create(student=s, template_id=f'T-{i:04}', defaults={'quality':random.randint(70,95)})
        # course + sessions
        c,_=Course.objects.get_or_create(code='RDM503', title='Biometric Systems', lecturer='Dr. Research')
        today=datetime.date.today()
        for d in range(15):
            Session.objects.get_or_create(course=c, date=today-datetime.timedelta(days=d), start_time=datetime.time(9,0), end_time=datetime.time(10,0), is_open=False)
        # attendance
        students=list(Student.objects.all())
        for sess in Session.objects.all()[:12]:
            for s in random.sample(students, k=min(30,len(students))):
                AttendanceRecord.objects.get_or_create(session=sess, student=s, matched=True)
        # device + logs
        dev,_=Device.objects.get_or_create(name='ESP32-01')
        dev.status='connected'; dev.save()
        for i in range(50):
            ScanLog.objects.create(device=dev, template_id=f'T-{i+1:04}', result=random.choice(['matched','unrecognized']), note='demo')
        self.stdout.write(self.style.SUCCESS('Seeded demo data. Login: admin/adminpass'))
