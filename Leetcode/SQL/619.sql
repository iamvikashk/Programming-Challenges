select ifnull((select t.num from (select num,count(num) as counts from my_numbers group by num having counts = 1) t order by t.num desc limit 1),null) as num