from invoke import task

DOMAIN_NAME = ''
VENV_NAME = 'schedule'

@task
def migrate(context):
	print('-- Migrate database --')
	context.run('python manage.py migrate')

@task
def collectstatic(context):
	print('-- Collect static --')
	context.run('python manage.py collectstatic')

@task
def restart(context, domain=DOMAIN_NAME):
	print('-- Restart MyDevil server --')
	try:
		context.run('devil www restart {domain}'.format(domain=domain))
	except:
		print('Wrong domain name or not in mydevil server')

@task
def install_requirements(context):
	print('-- Install requirements via pip --')
	context.run('pip install -r requirements.txt')

@task
def clean(context, extension="pyc"):
	print("-- Clean {} files".format(extension))
	context.run("find . -name '*.{}' -delete".format(extension))

@task
def coverage(context, html=False):
	context.run("coverage run --source='.' manage.py test")
	context.run('coverage report -m')
	context.run('coverage report -m > coverage.txt')
	if html:
		context.run('coverage html')

@task(coverage)
def prepare(context):
	print("-- Prepare for deployment --")
	context.run("pip freeze > requirements.txt")
	context.run("git add --all")
	context.run("git status")

@task(
	install_requirements,
	migrate,
	collectstatic,
	restart)
def deploy(context):
	print('-- Deploy --')