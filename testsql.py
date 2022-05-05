import psycopg2

conn = psycopg2.connect("dbname=sandbox user=techlauncher password=tl2022ioenergy host=io-db-dev-core.cluster-cz9fjfdq3ayr.ap-southeast-2.rds.amazonaws.com port=5432 sslmode=require")
cur = conn.cursor()
sql = "select * from public.customer_account_data limit 3"
cur.execute(sql)
print([list(row) for row in cur.fetchall()])
cur.close()
conn.close()