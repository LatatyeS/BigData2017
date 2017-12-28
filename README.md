# homework1

Создаем docker 

docker pull sequenceiq/hadoop-docker:2.7.1

docker run -it sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash

Положим файл с данными в докер в папку home
 
 docker cp sample.csv name:/home/sample.csv
 Аналогично положим все мапперы и редьюссеры

создадим папку hdfs

cd $HADOOP_PREFIX
bin/hdfs dfs -mkdir my_hdfs

положим туда файл с данными
bin/hdfs dfs -put /home/sample.csv my_hdfs

запустим map reduce:

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input my_hdfs/ -output hdfs_output/currentcol -mapper "python /home/map1.py" -reducer "python /home/reduce1.py" -file /home/map1.py -file home/reduce1.py

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input hdfs_output/currentcol -output hdfs_output/meantimeprod -mapper "python /home/map2.py"  -reducer "python /home/reduce2.py" -file /home/map2.py -file home/reduce2.py

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input hdfs_output/meantimeprod -input hdfs_output/currentcol -output hdfs_output/new_data -mapper "python /home/map3.py"  -reducer "python /home/reduce3.py" -file /home/map3.py -file home/reduce3.py

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input hdfs_output/new_data -output hdfs_output/data_filtred -mapper "python /home/map4.py"  -reducer "python /home/reduce4.py" -file /home/map4.py -file home/reduce4.py

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input hdfs_output/data_filtred -output hdfs_output/eventfile -mapper "python /home/map5.py"  -reducer "python /home/reduce5.py" -file /home/map5.py -file home/reduce5.py

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input hdfs_output/data_filtred -output hdfs_output/pt -mapper "python /home/map6.py"  -reducer "python /home/reduce6.py" -file /home/map6.py -file home/reduce6.py
