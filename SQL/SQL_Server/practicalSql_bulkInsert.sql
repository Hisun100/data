/**
--新建测试数据表
CREATE TABLE test.dbo.ipTE 
(   ip1 varchar(25),
    ip2 varchar(25)
);
--执行BULK INSERT导入csv文件操作：5百万条记录只需45s
bulk insert test.dbo.ipTE 
from 'H:\PY_Learn\work\massiveIP.txt'
with
(
    --BATCHSIZE  = batch_size , --指定批处理中的行数，默认情况下，指定数据文件中的所有数据是一个批处理。 
    FIELDTERMINATOR=',', --字符终止符，默认'/t'(制表符)
    ROWTERMINATOR='0x0a'  --行终止符，默认'/n'(换行符)
    --FIRSTROW=2  --数据从第二行开始插入
)
**/
select count(*) as total from  test.dbo.ipTE ; --查询表中的记录总数
