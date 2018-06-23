import MySQLdb

db = MySQLdb.connect(host='192.168.0.10',  # your host, usually localhost
                     user="root",  # your username
                     passwd="pametequieromucho",  # your password
                     db="senorbowl")  # name of the data base


sql = "SELECT substring(fecha_pedido, 1, 10) as fecha, " \
      "CASE WEEKDAY(fecha_pedido) "\
      "WHEN 0 THEN 'LUN' " \
      "WHEN 1 THEN 'MAR' "\
      "WHEN 2 THEN 'MIE' "\
      "WHEN 3 THEN 'JUE' "\
      "WHEN 4 THEN 'VIE' "\
      "WHEN 5 THEN 'SAB' "\
      "WHEN 6 THEN 'DOM' "\
      "END as dia,"\
    "WEEK(fecha_pedido) as semana,"\
"SUM(IF(LEFT(producto_pedido, 5) = 'salad', 1, 0)) as salads,"\
"SUM(IF(LEFT(producto_pedido, 5) = 'sushi', 1, 0)) as sushi,"\
"SUM(IF(LEFT(producto_pedido, 5) = 'buddh', 1, 0)) as buddha,"\
"SUM(IF(LEFT(producto_pedido, 5) = 'salad', 1, 0)) +  SUM(IF(LEFT(producto_pedido, 5) = 'sushi', 1, 0)) + "\
"SUM(IF(LEFT(producto_pedido, 5) = 'buddh', 1, 0)) as total,"\
"SUM( if ((left(direccion_pedido, 4) = 'uber') AND(descuento > 3500), 1, 0)) as uber,"\
"SUM(IF(LEFT(producto_pedido, 5) = 'salad', 1, 0)) +  SUM(IF(LEFT(producto_pedido, 5) = 'sushi', 1, 0)) + "\
"SUM(IF(LEFT(producto_pedido, 5) = 'buddh', 1, 0)) -SUM( if ((left(direccion_pedido, 4) = 'uber') "\
"AND(descuento > 3500), 1, 0))  as whatsapp "\
"FROM pedido GROUP BY substring(fecha_pedido, 1, 10) ORDER BY substring(fecha_pedido, 1, 10) "\
"DESC LIMIT 7;"

#sql = "SELECT substring(fecha_pedido,1,10), sum(descuento), sum(if(descuento,1,0)) FROM pedido" \
#      " GROUP BY substring(fecha_pedido,1,10) ;"

cur = db.cursor()
cur.execute(sql)
registro = cur.fetchall()

print registro

cur.close()

