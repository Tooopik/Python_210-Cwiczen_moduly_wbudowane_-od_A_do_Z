from string import Template

names = ['John', 'Paul', 'Lisa', 'Michael']
email = """Hello $name,
Thank you for visiting our website.
Team, XYZ"""
t = Template(email)

for name in names:
    print(t.substitute(name=name))
    print('-'*35)
