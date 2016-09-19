#!/usr/bin/python
from __future__ import print_function
import sys, os
sys.path.append(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'lib'))
from bottle import run, route, request, template
import pymysql as db
import settings

#our connection function
def connection():
    ''' Use this function to create your connections '''
    con = db.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
    #    autocommit = True,   #we removed this, so that the changes in the database are not permanent
        charset = 'utf8')

    return con

#function that return the input in unicode
def make_unicode(input):
    if type(input) != unicode:
        input = input.decode('utf-8')
        return input
    else:
        return input

#connecting to our database
conn = connection()
cur = conn.cursor()
cur.execute("use songs;")

#our homepage
@route('/homepage')
def homepage():
    return template('templates/homepage')

#our Presentation of Artists page
@route('/presentation-of-artists')
def presentationOfArtists():
    return template('templates/presentation-of-artists')

#our View Artist Results page
@route('/view-artist-results', method='POST')
def viewArtistResults():
    query = " select distinct ar_taut, onoma, epitheto, etos_gen from kalitexnis a "
    if request.forms.get('type'):       # to see which radio button has been clicked
        subject = request.forms.get('type')
    else:
        subject = "No"
    print(subject)
    geniko = 1
    if(subject != "No"): # if a button was clicked
        geniko = 0
        if(subject == "Singer"):
            query += " ,singer_prod s where a.ar_taut = s.tragoudistis "
        if(subject == "SongWriter"):
            query  += " , tragoudi t where a.ar_taut = t.stixourgos "
        if(subject == "Composer"):
            query  += " , tragoudi t where a.ar_taut = t.sinthetis "
    else:
        geniko = 1
        query +=" where true"

    dict = {}#{'Name': '', 'Surname': '', 'birthYearFrom': '', 'birthYearTo': ''}    # we use dictionary with key values to have dynamic queries

    try:
        name = request.forms.get('name')
        name = make_unicode(name)       # converting string to unicode
        if(name):
            if(geniko == 1): # if a button wasn't clicked above
                query += " and a.onoma = %(Name)s "
                geniko = 0
            else:
                query += " and a.onoma = %(Name)s "
            dict["Name"] = name
        else:
            print("Name not given!")
    except:
        print("Name emptyyyyyyy\n")
        name = ""

    try:
        surname = request.forms.get('surname')
        surname = make_unicode(surname)
        if(surname):
            if(geniko == 1):     # we put geniko to see if we have to have an "and" in the string
                query += " and a.epitheto = %(Surname)s "
                geniko = 0
            else:
                query += " and a.epitheto = %(Surname)s "
            dict["Surname"] = surname
        else:
            print("Surname not given!")
    except:
        print("Surname emptyyyyyyy\n")
        surname = ""
    #we put try - exception because we couldn't parse from string to integer
    # and we had an error when you wouldn't put dates in the browser
    try :
        birthYearFrom = int(request.forms.get('birthYearFrom'))
        if(geniko == 1):
            query += " and a.etos_gen >= %(birthYearFrom)s "
            geniko = 0
        else:
            query += " and a.etos_gen >= %(birthYearFrom)s "
        dict["birthYearFrom"] = birthYearFrom
    except : # in case he leaves birthYearFrom empty
        print ("birthYearFrom emptyyyyyyyyyyyyy\n")
        birthYearFrom = None

    try :# in case he leaves birthYearTo empty
        birthYearTo = int(request.forms.get('birthYearTo'))
        if(geniko == 1):
            query += " and a.etos_gen <= %(birthYearTo)s "
            geniko = 0
        else :
            query += " and a.etos_gen <= %(birthYearTo)s"
        dict["birthYearTo"] = birthYearTo
    except:
        print("birthYearTo emptyyyyyyyyyyyyyyyy\n")
        birthYearTo = None

    print(query)
    #so we create a query that is a string and a dictionary with the values of name, surname , birthYearTo, birthYearFrom
    cur.execute(query,dict)
    print("APO TO QUERY EPESTREPSAN : ",cur.rowcount," ROWS" )
    data = cur.fetchall()
    output = template('templates/view-artist-results', rows=data)
    return output

#our Update Artist Information page
@route('/update-artist-information/<a_t:path>')
def updateArtistInformation(a_t):
    try:
        a_t = make_unicode(a_t)
        print ("%s" %(a_t))
    except:
        print("URL Varible ERROR!\n")

    dict = {}
    dict["ID"] = a_t

    cur.execute("select distinct onoma, epitheto, etos_gen from kalitexnis where ar_taut = %(ID)s", dict)
    data = cur.fetchall()
    name, surname, birthYear = data[0][0], data[0][1], data[0][2]
    print("%s %s %d" %(name, surname, birthYear))
    return template('templates/update-artist-information', id=a_t, name=name, surname=surname, birthYear=birthYear)

#our Artist Information Updated page
@route('/artist-information-updated/<id:path>', method='POST')
def artistInformationUpdated(id):
    try:
        print ("%s" %(id))
    except:
        print("URL Varible ERROR!\n")
    query = " update kalitexnis"
    dict = {} #{'ID': '', 'Name': '', 'Surname': '', 'Year': ''}
    geniko = 0
    flag = 0
    dict["ID"] = id

    try:
        name = request.forms.get('name')
        if(name):
            flag =1
            name = make_unicode(name)
            query += " set onoma = %(Name)s"
            dict["Name"] = name
            print ("Name given")
            geniko = 1
        else:
            geniko = 0
            print("Name not given!")
    except:
        geniko = 0
        print("Name Exception!")

    try:
        surname = request.forms.get('surname')
        if(surname):
            flag = 1
            surname = make_unicode(surname)
            if(geniko == 1):
                query+= " ,  epitheto = %(Surname)s"
            else:
                geniko = 1
                query += " set epitheto = %(Surname)s"
            dict["Surname"] = surname
        else:
            print("Surname not given!")
    except:
        print("Surname Exception!")

    try:
        year = request.forms.get('birthYear')
        if(year):
            flag = 1
            if(geniko == 1):
                query += " ,  etos_gen = %(Year)s "
            else:
                geniko = 1
                query += " set etos_gen = %(Year)s "
            dict["Year"] = year
        else:
            geniko =0
            print("Year not given!")
    except:
        print("Year Exception!")

    query += " where ar_taut = %(ID)s"
    print(id, name , surname, year)
    print(query,dict)
    if(flag == 1):     # the query never happens if EVERYTHING is empty
        cur.execute(query,dict)
    return template('templates/artist-information-updated')

#our Presentation of Songs page
@route('/presentation-of-songs')
def presentationOfSongs():
    return template('templates/presentation-of-songs')

#our View Song Results page
@route('/view-song-results', method = 'POST')
def viewSongsResults():
    query = "select  titlos, sinthetis, etos_par, stixourgos, etaireia "

    From = "from tragoudi t, singer_prod s, cd_production c"
    where = " where s.cd = c.code_cd and s.title = t.titlos"
    geniko, titleflag, yearflag, companyflag = 0, 0, 0, 0
    dict = {} #{'Title': '', 'Year': '', 'Company': ''}

    query2 = " union select  titlos, sinthetis, etos_par, stixourgos, etaireia "
    query2 += " from tragoudi t, group_prod g, cd_production c "
    where2 = " where g.cd = c.code_cd and g.title = t.titlos"

    try:
        title = request.forms.get('song-title')
        if(title):
            title = make_unicode(title)
            dict["Title"] = title
            titleflag = 1
            geniko = 1
            where += " and t.titlos = %(Title)s"
            where2 += " and t.titlos = %(Title)s"
        else:
            title = None
            print("No title given!")
    except:
        print("Title Exception!")

    try:
        year = int(request.forms.get('production-year'))
        if(year):
            yearflag = 1
            dict["Year"] = year
            where += " and etos_par = %(Year)s"
            where2 += " and etos_par = %(Year)s"
            geniko = 1
        else:
            print("No year given!")
    except:
        year = None
        print ("Year Exception!")

    try:
        company = request.forms.get('company')
        if(company):
            company = make_unicode(company)
            dict["Company"] = company
            companyflag = 1

            where += " and etaireia = %(Company)s "
            where2 += " and etaireia = %(Company)s "
            geniko = 1
        else:
            print("No company given!")
    except:
        company = None
        print ("Company Exception!")


    query += From + where
    query2 += where2
    query += query2
    print(query2)

    print("\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa\n")
    print(title, year, company)

    if(companyflag):
        query += query2
    print(query,dict)
    cur.execute(query,dict)
    print("APO TO QUERY EPESTREPSAN : ",cur.rowcount," ROWS" )
    print(query2)
    data = cur.fetchall()
    output = template('templates/view-song-results', rows=data)
    return output

#our Insert Artist page
@route('/insert-artist')
def insertArtist():
    return template('templates/insert-artist')

#our View Insert Artist Result page
@route('/view-insert-artist-result', method = 'POST')
def viewInsertArtistResults():
    query = "insert into kalitexnis (ar_taut,onoma,epitheto,etos_gen) values(%(Nationalid)s , %(Name)s, %(Surname)s, %(Birthyear)s);"
    dict = {} #{'Nationalid': '', 'Name': '', 'Surname': '','Birthyear':''}

    try:
        Nid = request.forms.get('Nationalid')
        Nid = make_unicode(Nid)
        if(Nid):

            dict["Nationalid"] = Nid
            id_error = False
        else:
            dict["Nationalid"] = ""
            print("ID not given")
            id_error = True
    except:
        print("ID not given")
        return template("templates/insert-artist-error-page", id_error=False, name_error=False,
                        surname_error=False, birthYear_error=False, existence_error=False)
    cur.execute("select * from kalitexnis where ar_taut = %(Nationalid)s", dict)
    data = cur.fetchall()
    if(cur.rowcount):
        return template("templates/insert-artist-error-page", id_error=False, name_error=False,
                        surname_error=False, birthYear_error=False, existence_error=True)

    try:
        name = make_unicode(request.forms.get('Name'))
        if(name):
            dict["Name"] = name
            name_error = False
        else:
            dict["Name"] = ""
            print("No name given!")
            name_error = True
    except:
        print("Name Exception!")
        return template("templates/insert-artist-error-page", id_error=False, name_error=False,
                        surname_error=False, birthYear_error=False, existence_error=False)

    try:
        surname = make_unicode(request.forms.get('Surname'))
        if(surname):
            dict["Surname"] = surname
            surname_error = False
        else:
            dict["Surname"] = ""
            print("No surname given!")
            surname_error = True
    except:
        print("Surname Exception!")
        return template("templates/insert-artist-error-page", id_error=False, name_error=False,
                        surname_error=False, birthYear_error=False, existence_error=False)

    try:
        birthyear = request.forms.get('Birthyear')
        if(birthyear):
            dict["Birthyear"] = birthyear
            birthYear_error = False
        else:
            dict["Birthyear"] = None
            print("No birth year given!")
            birthYear_error = True
    except:
        print("Birth Year Exception!")
        return template("templates/insert-artist-error-page", id_error=False, name_error=False,
                        surname_error=False, birthYear_error=False, existence_error=False)

    error = id_error or name_error or surname_error or birthYear_error
    if(error):
        return template("templates/insert-artist-error-page", id_error=id_error, name_error=name_error,
                        surname_error=surname_error, birthYear_error=birthYear_error, existence_error=False)

    print(query,dict)
    cur.execute(query,dict)
    print("APO TO QUERY EPESTREPSAN : ",cur.rowcount," ROWS" )
    query = "select * from kalitexnis where ar_taut = %(Nationalid)s"
    cur.execute(query,dict)
    print("APO TO QUERY EPESTREPSAN : ",cur.rowcount," ROWS" )
    data = cur.fetchall()
    output = template('templates/view-insert-artist-result', rows=data)
    return output

#our Insert Song page
@route('/insert-song')
def insertSong():
    cur.execute("select distinct code_cd from cd_production order by code_cd")
    data1 = cur.fetchall()

    cur.execute("select ar_taut from kalitexnis order by ar_taut")
    data2= data3 = data4 = cur.fetchall()
    return template('templates/insert-song', rows1=data1, rows2=data2, rows3=data3, rows4=data4)

#our View Insert Song Result page
@route('/view-insert-song-result', method = 'POST')
def viewInsertSongResult():
    query1 = "insert into tragoudi (titlos,sinthetis,etos_par,stixourgos) values(%(Title)s , %(Composer)s, %(ProductionYear)s, %(SongWriter)s);"
    query2 = "insert into singer_prod (cd,tragoudistis,title) values(%(CD)s , %(Singer)s, %(Title)s);"
    dict = {} # {'Title': '', 'ProductionYear': '', 'CD': '', 'Singer': '', 'Composer': '', 'SongWriter': ''}

    try:
        title = make_unicode(request.forms.get('Title'))
        if(title):
            dict["Title"] = title
            title_error = False
        else:
            dict["Title"] = ""
            print("No title given!")
            title_error = True
            #return template("insert-song-error-page", title_error=True, existence_error=False)
    except:
        print("Title Exception!")
        return template("templates/insert-song-error-page", title_error=False, productionYear_error=False,
                        existence_error=False)

    cur.execute("select titlos from tragoudi where titlos = %(Title)s", dict)
    data = cur.fetchall()
    if(cur.rowcount):
        return template("templates/insert-song-error-page", title_error=False, productionYear_error=False,
                        existence_error=True)

    try:
        productionYear = request.forms.get('ProductionYear')
        if(productionYear):
            dict["ProductionYear"] = productionYear
            productionYear_error = False
        else:
            dict["ProductionYear"] = None
            print("No production year given!")
            productionYear_error = True
    except:
        print("Production Year Exception!")
        return template("templates/insert-song-error-page", title_error=False, productionYear_error=False,
                        existence_error=False)

    try:
        cd = request.forms.get('cd')
        if(cd):
            dict["CD"] = cd
        else:
            dict["CD"] = ""
            print("No CD given!")
    except:
        print("CD Exception!")
        return template("templates/insert-song-error-page", title_error=False, productionYear_error=False,
                        existence_error=False)

    try:
        singer = request.forms.get('singer')
        if(singer):
            dict["Singer"] = singer
        else:
            dict["Singer"] = ""
            print("No singer given!")
    except:
        print("Singer Exception!")
        return template("templates/insert-song-error-page", title_error=False, productionYear_error=False,
                        existence_error=False)

    try:
        composer = request.forms.get('composer')
        if(composer):
            dict["Composer"] = composer
        else:
            dict["Composer"] = ""
            print("No composer given!")
    except:
        print("Composer Exception!")
        return template("templates/insert-song-error-page", title_error=False, productionYear_error=False,
                        existence_error=False)

    try:
        songwriter = request.forms.get('songwriter')
        if(songwriter):
            dict["SongWriter"] = songwriter
        else:
            dict["SongWriter"] = ""
            print("No SongWriter given!")
    except:
        print("SongWriter Exception!")
        return template("templates/insert-song-error-page", title_error=False, productionYear_error=False,
                        existence_error=False)

    error = title_error or productionYear_error
    if(error):
        return template("templates/insert-song-error-page", title_error=title_error, productionYear_error=productionYear_error,
                        existence_error=False)

    print(query1,dict)
    cur.execute(query1,dict)
    print(query2,dict)
    cur.execute(query2,dict)

    query3 = """select title, etos_par, cd, tragoudistis, sinthetis, stixourgos
                from singer_prod, tragoudi
                where title = %(Title)s and title = titlos"""
    cur.execute(query3,dict)
    print("APO TO QUERY EPESTREPSAN : ",cur.rowcount," ROWS" )
    data = cur.fetchall()
    return template('templates/view-insert-song-result', rows=data)


#in which address our app is gonna run
run(host='localhost', port=settings.web_port, reloader=True, debug=True)

#ending our connection with the database
cur.close()
conn.close()
