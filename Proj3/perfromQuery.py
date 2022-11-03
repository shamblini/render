# pip3 install psycopg

# Will return None if there is no results from the SQL query, or a list of results
# If something goes wrong, will return "FAIL"
# if printStatus == True, will print to the terminal a status message to the terminal 

import traceback
import psycopg
import secrets

def performQuery(QueryString, printStatus=False):
    try:
        # make initial connection
        conn = psycopg.connect(
            host=secrets.GetSecret('hostname'),
            dbname=secrets.GetSecret('database'),
            user=secrets.GetSecret('username'),
            password=secrets.GetSecret('pwd')
        )

        # cursors are used to perform queries 
        cur = conn.cursor()
        
        cur.execute(QueryString) # Performs the query
        # return cur.fetchall()
        conn.commit()
        
        if printStatus == True:
            print("performQuery: " , cur.statusmessage)
            
        if (cur.description == None):
            return None
        else:
            return cur.fetchall()
    
    except:
        print("DB conn failed\n")
        traceback.print_exc()
        return "FAIL";
        
    finally:
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()
