# Set parent directory
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

# Import tables from files
from models import *
from app import *


s = db.session()

# Fake locations
l1 = Location(name='closet')
l2 = Location(name='cabinet')
l3 = Location(name='attic')

s.add_all([l1,l2,l3])
s.commit()


# Fake clothes
c1 = Clothes(location='1', category='dress', description='maxi red')
c2 = Clothes(location='1', category='shirt', description='blue')
c3 = Clothes(location='1', category='shirt', description='green')
c4 = Clothes(location='2', category='shirt', description='yellow')
c5 = Clothes(location='1', category='pants', description='short blue')
c6 = Clothes(location='2', category='pants', description='long khaki')
c7 = Clothes(location='3', category='dress', description='mini black')
c8 = Clothes(location='3', category='shirt', description='purple')

s.add_all([c1,c2,c3,c4,c5,c6,c7,c8])
s.commit()