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

[image]

On the server let's open an http server on port 53.

![](https://github.com/andersongomes001/ctf_scripts/blob/master/Captura%20de%20tela%20de%202019-11-11%2010-42-54.png?raw=true)
