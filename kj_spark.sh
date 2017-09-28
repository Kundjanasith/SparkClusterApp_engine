echo "Kundjanasith Thonglek"
echo "kundjanasith@datascienceth.com"
echo $1
# visualization
time spark-submit --class "W2V" --master spark://ssw2-ssw-master-0.novalocal:7077  target/scala-2.10/spark-sample_2.10-1.0.jar $1 &> grafana.txt
# configuration
rm -rf file_b.txt
rm -rf file_m.txt
rm -rf grafana.txt
echo "USED,FREE" > MEMORY_API/file_b.csv
echo "0,0"	>> MEMORY_API/file_b.csv
echo "USED,FREE" > MEMORY_API/file_m.csv
echo "0,0"      >> MEMORY_API/file_m.csv
