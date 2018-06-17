/**
use test

--创建表类型.ok
create type XTableType as table(ID int,Names varchar(10));
go
 


--创建存储过程:sp_test
--以表值参数作为输入 
create Procedure sp_test(@tp1 XTableType readonly) --readonly：只读，设置过程中的参数的约束 =default-默认值;output:输出参数
as --存储过程要执行的操作
set NoCount on
select *,getdate() from @tp1; --核心sql语句
set NoCount off
go
**/  


--声明表值参数变量:@tp2
declare @tp2 as XTableType;
  
--将数据插入表值变量
Insert into @tp2(ID,Names)
select 1,'a'
union select 2,'b'
union select 3,'c';
