while true
do
	echo "Start . . ."
        date
        python grafana.py grafana.txt file_b.txt file_m.txt
        Rscript grafana.R
	sleep 5s
	date
	echo "Finish . . ."
done
