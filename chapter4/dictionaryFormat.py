phonebook = {'Alice':'2341','Beth':'9102','Cecil':'3258'}

print(phonebook)

print("Cecil's phone number is %(Cecil)s." % phonebook)

template = '''<html> 
    <head><title>%(title)s</title></head>
    <body>
        <h1>%(title)s</h1>
        <p>%(text)s</p>
    </body>
</html>'''

data = {'title':'My Home Page','text':'Welcome to my home page!'}

print(template % data)