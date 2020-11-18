- 创建数据库
```sql
mysqladmin -u root -p create Blog
create database Blog;
```
- 导入表
```sql
create database test;
use test;
source ~/a.sql;
```
- 导出
```sql
mysqldump -u 用户名 -p 数据库名 > 导出的文件名 
```
- 描述表
```sql 
desc tableName;(表格的形式)
```
- 读取数据表
```sql
select * from tableName;
```
- 创建表
```sql
create table if not exists blog(id int primary key auto_increment,title char not null,comment longtext not null);

```
- 删除数据库
```sql
mysqladmin -uroot -p drop Blog
drop database Blog;
```
- 删除表
```sql
drop table Blog;
```
- 插入内容：
```sql
insert into Blog (id,title,comment)values(2,"hello","hello world")  //可以不插入id字段，因为是自增的
insert into blog(title,text) values("ede","deede"),("dededede","defegrfgtg"); //插入多条数据
```
- where语句
```sql
select * from blog where binary comment="hello Yp";                //binary指定区分大小写
select * from blog where id>=1;  
select id from blog where id>1;
```
- update语句
```sql
update blog set text="i love such life" where id=4;
```
- delete语句
```sql
delete from blog where id =1;    //删除blog表中id是1的记录
```
- like语句
```sql
select * from blog where text like "%such%";     //%匹配所有字符串
```
- union语句
```sql
select text from blog where text="i love such world! union select country from apps where country="cn";
select text title from blog where text="i love such life" and  title like "%i" union select country from apps where country="cn";
```
- 排序
```sql
select * from blog order by id asc;//升序
select * from blog order by id desc;//降序
```
- 分组(group by语句)
```sql
select name, count(*) from employee_tbl group by name;   //根据name分组，结果是一个两列属性分别是name和count(*)的二维表,count(*)值是每个不同名字的数量 
select name,sum(singin) as signinCount from employee_tbl group by name; //一列是name,另一列是signinCount(属性singin的和)
select name,sum(singin) as signinCount from employee_tbl group by name with rollup;//with rollup在分组的基础上再进行一次相同的统计(sum,即给signin列求和，name属性是null)
select coalesce(name,'总数'),sum(singin) as signinCount from employee_tbl group by name with rollup;//在上一条分组的基础上修改name值为空的记录的name属性是总数
```
- 连接(join/right join/left join)
```sql
select a.runoob_id,a.runoob_author,b.runoob_count from runoob_tbl a join tcount_tbl b on a.runoob_author=b.runoob_author;
select a.runoob_id,a.runoob_author,b.runoob_count from runoob_tbl a left join tcount_tbl b on a.runoob_author=b.runoob_author;
//以左表为基础，连接之后的表的runoob_author是左表的全部
select a.runoob_id,a.runoob_author,b.runoob_count from runoob_tbl a right join tcount_tbl b on a.runoob_author=b.runoob_author;
//以右表为基础，连接之后的表的runoob_author是右表的全部
格式：......join tableName on somecheck
```

- 一对多关系
```sql
create table `users` (
    `id` int unsigned not null auto_increment, 
    `name` varchar(100) not null, 
    primary key(`id`) 
); 

create table `phone_numbers` (
    `id` int unsigned not null auto_increment, 
    `user_id` int unsigned not null, 
    `phone_number` varchar(25) not null, 
    index pn_user_index(`user_id`), 
    foreign key (`user_id`) references users(`id`) on delete cascade, 
    primary key(`id`) 
); 

//现在，您可以轻松地通过简单的连接获取用户的电话号码;
select 
    pn.`phone_number` 
from 
    `users` as u, 
    `phone_numbers` as pn 
where 
    u.`name`='John' 
    and 
```
- 多对多关系
```sql
需求：
1）一个学生可以学多门课
2）一个课有多个学生学学生表和课程表之间多对多关系需要借助中间表,在中间表中维护学生和课程的关系
create Table student(num varchar(20) primary key,name varchar(10));
create table course(id varchar(20) primary key,name varchar(50));
create table selectCourse(id int auto_increment primary key,sid varchar(20),cid varchar(20),
//一般需要在中间表中 用两个外键来关联两个表
constraint fk_sid foreign key (sid) references student(num),
constraint fk_cid foreign key (cid) references course(id));
```
- 用事件写定时任务

```sql
delimiter //
create procedure reset_reward_daily()
begin
update  reward_check set is_reward=0;
end//
delimiter ;


create event reset_daily
on schedule every 1 day
STARTS '2019-04-05 00:00:00'
do call reset_reward_daily();

alter event reset_daily on completion preserve enable;//打开定时任务
alter event reset_daily on completion preserve disable;//关闭定时任务
```
- 删除event
```sql
DELETE FROM mysql.event
WHERE db = 'reward';
```
- 打开调度器
```sql
SET @@global.event_scheduler = 1;
```
- 开启外网访问
```shell
    开放 0.0.0.0
    vi /etc/mysql/my.cnf
    [mysqld]
    #skip-grant-tables
    bind-address=0.0.0.0
    
    设置密码登录
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'youpassword' WITH GRANT OPTION;
    FLUSH PRIVILEGES;

    限制ip
    GRANT ALL PRIVILEGES ON *.* TO 'jack'@'10.10.50.127' IDENTIFIED BY '654321' WITH GRANT OPTION;
```
- 更改密码
```    
    vi /etc/mysql/my.cnf
    [mysqld]
    skip-grant-tables
    use mysql
    update user set authentication_string=PASSWORD("") where user='root';
```

- 修改字符集为utf8-mb4
```shell
> vim /etc/my.cnf
# 对本地的mysql客户端的配置
[client]
default-character-set = utf8mb4

# 对其他远程连接的mysql客户端的配置
[mysql]
default-character-set = utf8mb4

# 本地mysql服务的配置
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
```
## 全局变量
    - 查询global变量
    show global variables like 'wait_timeout%';
    show global variables  where variable_name like "wait_timeout%";

    - 查询session变量
    show session variables like 'wait_timeout';
    show session variables  where variable_name like "wait_timeout%";

    - 设置全局变量
    set global wait_timeout=60;
