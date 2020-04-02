import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import pymysql
import xlwt
import datetime
import schedule

def get_mail_msg(from_addr,to_addr):
    #构造邮件信息
    msg = MIMEMultipart()
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('体温日志')
    now = str(datetime.datetime.now().date())
    msg.attach(MIMEText('{}体温日志'.format(now), 'plain', 'utf-8'))
    exfile = MIMEText(open('./userreport.xls', 'rb').read(), 'base64', 'utf-8')
    exfile["Content-Type"] = 'application/octet-stream'
    exfile["Content-Disposition"] = 'attachment; filename=' + 'userreport.xls'
    msg.attach(exfile)
    return msg


def send_mail(to_addr=''):
    #发送邮件
    from_addr="1051520590@qq.com"
    password="vrjqpuxcpubobbdi"
    to_addr = '1556502096@qq.com'
    smtp_server = 'smtp.qq.com'
    server = smtplib.SMTP_SSL(host=smtp_server)
    server.connect(host=smtp_server, port=465)
    server.login(from_addr, password)
    msg = get_mail_msg(from_addr,to_addr)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

def get_data():
    #从数据库查询每日数据
    db = pymysql.connect("172.30.131.74","root","123456","health" )
    cursor = db.cursor()
    now = str(datetime.datetime.now().date())
    cursor.execute("select tempture,count(tempture) from `day_userreport` where date='{}' group by tempture".format(now))
    data = cursor.fetchall()
    return data

def get_excel(data):
    #构造excel
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('userreport')
    worksheet.write(1,0, label = '温度')
    worksheet.write(1,1, label = '数量')
    for index,item in enumerate(data):
        worksheet.write(index+2,0, item[0])
        worksheet.write(index+2,1, item[1])
    workbook.save('userreport.xls')

def day_job():
    data = get_data()
    get_excel(data)
    send_mail()

if __name__ == "__main__":
    schedule.every().day.at("23:59").do(day_job)
    while True:
        schedule.run_pending()