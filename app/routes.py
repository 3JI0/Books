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
    list_books = [{'author':'a', 'book':'b'}, {'author': 'c', 'book':'d'}]
    return render_template('index.html', title='Home', content=content, list_books=list_books)

@app.route('/books', methods = ['GET', 'POST'])
def books():
    list_books = {}
    form = BookForm()
    if form.validate_on_submit():
        user = User(author=form.author.data, books=form.books.data)
        list_books[form.author.data] = form.books.data
        flash('Book  {}, by author {} is added'.format(
             form.author.data, form.books.data))
        return redirect(url_for('index'))
    return render_template('books.html', title='Add Books', form=form, list_books=list_books)  


@app.route('/json', methods = ['GET'])
def json(): 
    if(request.method == 'GET'): 
        list_books = {}
        form = BookForm()
       # user = User(author=form.author.data, books=form.books.data)
        list_books[form.author.data] = form.books.data
        #connection = lite.connect('app.db')
        #cursor = connection.cursor()
        #cursor.execute('SELECT * FROM User')
        #users = cursor.fetchall()
        #for row in users:
        #    name = str(row[1])
        #    book = str(row[0])
        #   return name, book
        list_books = [{'a':'a', 'b':'b'}, {'a': 'c', 'b':'d'}]
        return  jsonify( list_books) 
    return render_template('json.html', title='JSON')  


 
  