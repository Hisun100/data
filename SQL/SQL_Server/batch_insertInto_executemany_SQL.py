def batch_insertInto_executemany_SQL(items, conn, cursor, table_name, filed_num):
    """
    作用：将一个批次的数据一次性插入SQL Server数据库 by insert into ... values
    注意：存放数据的数据表已存在;
    参数说明：
    table_name --存放数据的数据表
    filed_num --存放数据的数据表所含字段数
    
    """
    import time
    start = time.time()
#    items=['10.197.50.156,10.197.223.201\n', '10.197.181.239,10.197.235.20\n']
#    items=['10.197.50.156\n','10.197.223.201\n', '10.197.181.239\n','10.197.235.20\n']
    with open(f_path) as f:
        items = f.readlines()
    #文本处理：使得每条记录的每个字段的值加上单引号后，放入一个字符串变量中 
    if filed_num == 1 :
#        line_decorator = lambda x:  "('"+ x.strip('\r\n') +"')"
#        all_rows = []   
#        for row in items:
#            all_rows.append(row)
        return None
    line_decorator = lambda x: "'" + x.strip('\r\n').replace(',', "', '") + "'" 
    all_rows = [tuple(eval(line_decorator(row))) for row in items]   
    #构建插入的SQL 语句
    sql_insert = 'INSERT INTO ' + table_name +' VALUES (' + (("%s,")*filed_num)[:-1] + ")"
    print(sql_insert)   
    #提交事务
    try:          
        cursor.executemany(sql_insert,all_rows)
        conn.commit()
    except:
        conn.rollback()
        print('出现异常，事务回滚！！')
#    mins = (time.time()-start)/60
    print("本次数据写入SQL Sever共耗时：%f分钟"%((time.time()-start)/60))
    return None 
