### 导入运行环境

`python 3.7`

```bash
pip install -r requirements.txt
```

### mysql数据库

创建health数据库 端口3306

添加用户health 密码health

### 项目操作

```bash
运行数据库迁移命令
python manage.py makemigrations
python manage.py migrate
运行数据上报网站
python manage.py runserver ip:port
运行定时任务
python ./utils/send.py
```

