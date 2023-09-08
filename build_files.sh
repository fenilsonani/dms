 echo "BUILD START"
 mkdir dist
 echo "DIST CREATED"
 echo "INSTALLING REQUIREMENTS"
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"