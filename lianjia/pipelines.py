# -*- coding: utf-8 -*-


import mysql.connector
from lianjia import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user = MYSQL_USER,password= MYSQL_PASSWORD,host =MYSQL_HOSTS,database=MYSQL_DB)
cur = cnx.cursor(buffered=True)
class Sql:
    @classmethod
    def insert_tenement_message(cls,title,rental,distance,area,room_number,floor,direction,year_build):
        sql = 'INSERT INTO tenement_message(`title`,`rental`,`distance`,`area`,`room_number`,`floor`,`direction`,`year_build`) VALUES (%(title)s,%(rental)s,%(distance)s,%(area)s,%(room_number)s,%(floor)s,%(direction)s,%(year_build)s)'
        value = {
            'title':title,
            'rental':rental,
            'distance':distance,
            'area':area,
            'room_number':room_number,
            'floor':floor,
            'direction':direction,
            'year_build':year_build,
        }
        cur.execute(sql,value)
        cnx.commit()
    @classmethod
    def select_title(cls,title):#这个是利用标题去重的，虽然按照区域划分应该不会重复，只是预防万一
        sql= 'SELECT EXISTS (SELECT 1 FROM tenement_message WHERE title = %(title)s)'
        value = {
            'title':title
        }
        cur.execute(sql,value)
        return  cur.fetchall()[0]



class LianjiaPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        ret = Sql.select_title(title)
        if ret[0] ==1:

            print('房子已经存在')
        else:
            rental = item['rental']
            distance = item['distance']
            area = item['area']
            room_number = item['room_number']
            floor = item['floor']
            direction = item ['direction']
            year_build = item['year_build']
            Sql.insert_tenement_message(title,rental,distance,area,room_number,floor,direction,year_build)
            print('开始存租房信息')





