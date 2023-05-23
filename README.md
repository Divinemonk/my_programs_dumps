# Program Dumps
> day-to-day useful scripts & programs

## Content


<br>

## massnamer
Mass rename files is perticular pattern or style.

<br>

## monitormode
Change your network interface to monitor mode (and back to managed mode) with one command
```
[usage]:  `./monitor-mode <interface> <mode>`

interface -> network interface to change
mode      -> `mon` for monitor mode
             `man` for managed mode

RUN script as ROOT: `sudo ./monitor-mode <interface> <mode>`
```

### Manual commands:
- method 1 (used in script)
```
ip link set <interface> down
iw <interface> set monitor control (OR iw <interface> set type managed)
ip link set <interface> up
```
- method 2
```
sudo ifconfig <interface> down
sudo iwconfig <interface> mode monitor
sudo ifconfig <interface> up
```
- Check \<interface\> name using `iw dev` or `ifconfig`
