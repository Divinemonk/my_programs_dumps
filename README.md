# Program Dumps
> day-to-day workflow automate scripts & programs

## Index
| Name  | Raw code |
| ------------- | ------------- |
|  [Mass remane files](#massnamer) | [source code](https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/massnamer.py)  |
| [Monitor mode](#monitormode) | [source code](https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/monitormode.sh) |


<br>

## massnamer
Mass rename files is perticular pattern or style you prefer.
```
usage: ms.py [-h] [-p PATTERN] [-r] [-pf PREFIX] [-npf NEW_PREFIX] FOLDER

Mass Rename Files

positional arguments:
  FOLDER                path to the folder containing the files

optional arguments:
  -h, --help            show this help message and exit
  -p PATTERN, --pattern PATTERN
                        new file name pattern
  -r, --random          rename files randomly
  -pf PREFIX, --prefix PREFIX
                        rename files starting with the specified prefix
  -npf NEW_PREFIX, --new-prefix NEW_PREFIX
                        new prefix to replace the old prefix
```
- Download: `wget https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/massnamer.py`
- [Goto source code](https://github.com/Divinemonk/program_dumps/blob/m41n/massnamer.py)


<br>

## monitormode
- Change your network interface to monitor mode (and back to managed mode) with one command.
```
[usage]:  `./monitor-mode <interface> <mode>`

interface -> network interface to change
mode      -> `mon` for monitor mode
             `man` for managed mode

RUN script as ROOT: `sudo ./monitor-mode <interface> <mode>`
```
- Download: `wget https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/monitormode.sh`
- [Goto source code](https://github.com/Divinemonk/program_dumps/blob/m41n/monitormode.sh)

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
