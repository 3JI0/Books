# -*- coding: utf-8 -*-
from flask import render_template
from app import app, db
from app.forms import BookForm
from flask import flash, redirect,url_for
from app.models import User
from flask import Flask,jsonify,request 



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


@app.route('/')
@app.route('/index')
def index():
    content = {'Book': 'books'}
    #list_books = [{'author':'a', 'book':'b'}, {'author': 'c', 'book':'d'}]

    user = User.query.all()

        
    return render_template('index.html', title='Home', content=content, user=user)

@app.route('/books', methods = ['GET', 'POST'])
def books():
    list_books = {}
    form = BookForm()
    if form.validate_on_submit():
        user = User(author=form.author.data, books=form.books.data)
        db.session.add(user)
        db.session.commit()
    #    list_books[form.author.data] = form.books.data
        flash('Book  {}, by author {} is added'.format(
             form.author.data, form.books.data))
        return redirect(url_for('index'))
    return render_template('books.html', title='Add Books', form=form, list_books=list_books)  


@app.route('/json', methods = ['GET'])
def json(): 
    if(request.method == 'GET'): 
        user = User.query.all()
        list_books = []
        for u in user:
            dict_books = {'Author':u.author, 'Books':u.books}  
            list_books.append(dict_books)
        return  jsonify( list_books) 
    return render_template('json.html', title='JSON')  


 
  