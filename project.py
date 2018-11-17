#!   /user/bin/env python
import psycopg2
if __name__ == '__main__':
    DBNAME = "news"
    DB = psycopg2.connect(database=DBNAME)
    q1 = DB.cursor()
    '''query for return the most popular three articles'''
    q1.execute('''SELECT articles.title,count(*) as view
    FROM articles
    JOIN log on
    log.path = concat('/article/', articles.slug)
    GROUP BY articles.title
    ORDER BY view desc limit 3;''')
    post = q1.fetchall()
    print('What are the most popular three articles of all time? ')
    """print Resulte"""
    for i in range(len(post)):
        print i+1, ')', post[i][0], '--', post[i][1], 'views'
    print ''
    q2 = DB.cursor()
    '''query for return the most popular articles authors'''
    q2.execute('''SELECT authors.name,count(*) as view
    FROM authors join articles on
    authors.id = articles.author join log on
    log.path = concat('/article/', articles.slug)
    GROUP BY authors.name
    ORDER BY view desc limit 3;''')
    post1 = q2.fetchall()
    print('Who are the most popular article authors of all time?')
    """print Resulte for most popular authors"""
    for i in range(len(post1)):
        print i+1, ')', post1[i][0], '--', post1[i][1], 'views'
    print''
    q3 = DB.cursor()
    q3.execute('''WITH request as
    (SELECT time::date as date1,count(*) as req
    FROM log
    GROUP BY time::date order by time::date),
    error as
    (SELECT time::date as date2,count(*) as err
    FROM log where status like'404 NOT FOUND'
    GROUP BY time::date order by time::date),
    counterror as
    (SELECT request.date1,
    ROUND(((error.err * 1.0) / request.req *100),3) as sumerr
    FROM request,error where request.date1=error.date2)
    SELECT * from counterror where sumerr > 1;''')
    post2 = q3.fetchall()
    print('On which days did more than 1% of requests lead to errors?')
    print('')
    """print resulte for days with request error >1% with formate date"""
    for result in post2:
        print('{date:%B %d, %Y} - {error_rate:.1f}% errors'.format(
            date=result[0],
            error_rate=result[1]))
    DB.close()
