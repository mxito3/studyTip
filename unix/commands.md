# journalctl
```shell
  journalctl -u rpc.service  --since yesterday
  journalctl _PID=8888 --since yesterday
```
# netstat 
查看占用某端口的进程的pid
sudo netstat -antup | grep 30303
