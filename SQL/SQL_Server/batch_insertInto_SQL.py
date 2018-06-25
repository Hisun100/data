def batch_insertInto_SQL(splited_files_dir, conn, cursor, table_name):
    import os
    import time
    print ("开始写入SQL Server：%s"%(time.ctime()))
    start = time.time()
    all_files = os.listdir(splited_files_dir) #获取目录下的所有文件
    chunk_size =1000
    for file in all_files:
        file = splited_files_dir+'/'+file
        print('%s开始处理：%s'%(file,time.ctime()))
        if os.path.isfile(file):
            with open(file,'r',encoding='UTF-8') as f:
                items = f.readlines() #读入数据，列表，每条记录用一个字符串表示，每条记录的每个字段的值用逗号隔开
        #    del items[0]   
        #    for item in items:
        #        print(item)
                #文本处理：使得每条记录的每个字段的值加上单引号 
            line_decorator = lambda x: "('" + x.strip('\r\n').replace(',', "', '") + "')"
            all_rows = [line_decorator(row) for row in items]
            sql_insert = 'INSERT INTO ' + table_name + ' VALUES '
            n, k = len(all_rows) // chunk_size, len(all_rows) % chunk_size  #取整n:每个完整批次所含的记录数，取模          
            for i in range(n):
                multi_rows = ', '.join(all_rows[(i)*chunk_size:(i+1)*chunk_size])
#                print(sql_insert + multi_rows) #打印插入语句            
                cursor.execute(sql_insert + multi_rows)
#                conn.commit()
            if k:
                multi_rows = ', '.join(all_rows[-k:])
#                print(sql_insert + multi_rows)
                cursor.execute(sql_insert + multi_rows)
#                conn.commit()
    #提交事务
    try: 
        conn.commit()
        print("OK..本次数据写入SQL Sever共耗时：%f分钟"%((time.time()-start)/60))
    except:
        conn.rollback()
        print('出现异常，事务回滚！！')
