from flask import Flask, escape, request

app=Flask(__name__)

#use below commands to fire up flask to start serving web pages
#Flask run
#export FLASK_ENV=development

#https://devcenter.heroku.com/articles/heroku-cli#download-and-install
#git..browse to project folder and execute below
#git init
#git status
#git add .
#git commit -m "initial release"
#git remote -v add 

# http://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes

#heroku
#heroku login -i
#<>@gmail.com
#
#heroku create
# after above cmd is executed, it generates a remote git
#git push https://git.heroku.com/mysterious-mountain-70470.git
#debug, see logs
#heroku logs -a=mysterious-mountain-70470



@app.route('/')
def hello_world():
    return 'jhinga la la?'

@app.route('/check')
def check():
    s = '<table><th> Col 1</th><th> Col 2</th><tr><td>asdf</td><td>1234</td></tr></table>'
    return (s)