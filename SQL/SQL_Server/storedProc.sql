--创建存储过程
CREATE PROC bulkInsertTest
@TE.name VARCHAR(50),
@file_path VARCHAR(50)
AS
BEGIN
bulk insert @TE.name 
from @file_path
with
(
    --BATCHSIZE  = batch_size , --指定批处理中的行数，默认情况下，指定数据文件中的所有数据是一个批处理。 
    FIELDTERMINATOR=',', --字符终止符，默认'/t'(制表符)
    ROWTERMINATOR='0x0a'  --行终止符，默认'/n'(换行符)
    --FIRSTROW=2  --数据从第二行开始插入
)
END
--执行存储过程
EXEC
