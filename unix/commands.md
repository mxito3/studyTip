# journalctl
```shell
  journalctl -u rpc.service  --since yesterday
  journalctl _PID=8888 --since yesterday
```
# netstat 
查看占用某端口的进程的pid
```shell
sudo netstat -antup | grep 30303
```
# scp 
下载服务器文件夹
scp  -r name@ip:/home/xhy/github/blockchain_service ./

# 查看sudo user
grep -Po '^sudo.+:\K.*$' /etc/group
