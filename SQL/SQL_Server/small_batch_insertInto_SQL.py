def small_batch_insertInto_SQL0(f_path, conn, cursor, table_name='test01.dbo.ip_TE'):
    """
    作用：将一个批次的数据一次性插入SQL Server数据库 by insert into ... values
    注意：存放数据的数据表已存在;
    参数说明：
    f_path -- 带插入的数据文件   
    状态说明：一次只能插入1000条记录左右,但写入速度要较executemany快100倍少一些（0.001633分钟，1000）
    """  
    import time
    print ("开始写入SQL Server：%s"%(time.ctime()))
    start = time.time()
#    items=['10.197.50.156,10.197.223.201\n', '10.197.181.239,10.197.235.20\n']
#    items=['10.197.50.156\n','10.197.223.201\n', '10.197.181.239\n','10.197.235.20\n']
    with open(f_path,'r') as f:
        items = f.readlines()
#        print(items)
    line_decorator = lambda x: "('" + x.strip('\r\n').replace(',', "', '") + "')" 
    all_rows = [line_decorator(row) for row in items]
    #一次性插入SQL Server数据库
    sql_insert = 'INSERT INTO ' +  table_name +' VALUES '       
    multi_rows = ', '.join(all_rows)
#    print(sql_insert + multi_rows) #打印插入语句  
    #提交事务
    try: 
        cursor.execute(sql_insert + multi_rows)
#        cursor.execute("""
#        INSERT INTO test01.dbo.ip_TE VALUES ('10.197.174.208'), ('10.197.187.52'), ('10.197.245.78')
#        """)
        conn.commit()
        print("本次数据写入SQL Sever完成：%s"%(time.ctime()))
        print("本次数据写入SQL Sever共耗时：%f分钟"%((time.time()-start)/60))
    except:
        conn.rollback()
        print('出现异常，事务回滚！！')
    return None
