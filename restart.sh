sudo kill -15 `ps x | grep Python | grep server.py | grep $1 | grep -v grep | awk '{print $1}'`

until [[ `ps x | grep Python | grep server.py | grep $1 | grep -v grep | awk '{print $1}'` -eq 0 ]]
do
  echo waiting for server $1 stop
  sleep 0.8
done
nohup python3  server.py --port=$1 > web_std_out.log 2>&1 &
sleep 3
exit 0


