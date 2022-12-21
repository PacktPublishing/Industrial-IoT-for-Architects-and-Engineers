import json, boto3, os, sys
import time
import logging
import pymysql

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


###Setup connection to MySQL
DBhost = os.getenv("hostURL")
DBusername = os.getenv('username')
DBpassword = os.getenv('password')
DBname = os.getenv('database')
charSet = "utf8mb4"
cursorType = pymysql.cursors.DictCursor


def lambda_handler(event, context):
    
    #logger.debug(os.environ)
    logger.debug("event: " + json.dumps(event, indent=2))
    
    
    ###flatten some interesting attributes for use in analysis
    event[0]["rated_insulationclass"] = event[0]['equipment']['attributes'].get('InsulationClass', None)
    event[0]["rated_servicefactor"] = event[0]["equipment"]["attributes"].get("ServiceFactor", None)
    event[0]["rated_rpm"] = event[0]["equipment"]["attributes"].get("RPM", None)
    event[0]["rated_voltage"] = event[0]["equipment"]["attributes"].get("Voltage", None)
    event[0]["rated_horsepower"] = event[0]["equipment"]["attributes"].get("Horsepower", None)
    event[0]["rated_current"] = event[0]["equipment"]["attributes"].get("Current", None)
    
    ###convent timestamp to integer for datastore to use as partition
    #print(int(time.time())) #current unix timestamp
    #event[0]["timestamp"] = int(time.time())
    event[0]["timestamp"] = int(int(event[0].get("timestamp", None) ) / 1000)

    ###Get temperature max from insulation class attribute
    insulationClass = event[0]["equipment"]["attributes"].get("InsulationClass", 'B')
    query = "SELECT temp FROM iot.temperature_class_lookup WHERE class = '" + insulationClass + "'"
    logger.debug(query)
    
    try:
        # Create a connection to the Database
        logger.debug("Connecting to DB")
        conn = pymysql.connect(host=DBhost, user=DBusername, passwd=DBpassword, db=DBname, connect_timeout=5, charset=charSet, cursorclass=cursorType)
        logger.debug("SUCCESS: Connection to RDS MySQL")

        # Create a cursor object
        cursor = conn.cursor()  
        
        # SQL query string
        sqlQuery = query
        
        # Execute the sqlQuery
        cursor.execute(sqlQuery)
        
        #Fetch all the rows
        rows = cursor.fetchall()
        for row in rows:
            logger.info("rated temperature for this device = " + row["temp"])
            event[0]["rated_temp"] = int(row["temp"])
    except Exception as err:
        logger.error(err)
        #sys.exit()
    finally:
        conn.close
        
        
    event[0].pop("equipment")

    ###Output the result and return to caller
    logger.debug("event: " + json.dumps(event, indent=2))
    return event
    


