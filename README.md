# Program Dumps
> day-to-day workflow automation scripts & programs

<br>

## Index
| pseudonym | raw code | prog lang |
| --- | --- | --- |
| [Mass remane files](#massnamer) | [source code](https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/massnamer.py) | python3 |
| [Monitor mode](#monitormode) | [source code](https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/monitormode.sh) | bash script |
| [Response code checker](#responsor) | [source code](https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/responsor.py) | python3 |
| [Burp Raw Requests To Python](brrtp) | [source code](https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/brrtp.py) | python3 |

<br>

## Notes
- linux users can use `sudo chmod +x <script/program name>` to run directly (eg: `sudo monitormode wlan1 mon`, without `bash` prefix)

<br>
<hr>
<br>

## massnamer
Mass rename files is particular pattern or style you prefer.
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
<hr>
<br>

## monitormode
- Change your network interface to monitor mode (and back to managed mode) with one command.
- Sometimes the script works, interface is changed to monitor mode but unable to detect the change and dispalys failed. Try `iw dev` or similar commands to check the interface mode manually.
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


<br>
<hr>
<br>

## responsor
- display response codes for websites/urls from the given list
- usecase:
    - check subdomains response codes (save subdomains in a list: `subfinder -d example.com > URL_LIST.txt`)
    - have bunch of urls, check response of each
```
[usage]: python3 responsor.py <url_list_file>
```
- Download: `wget https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/responsor.py`
- [Goto source code](https://github.com/Divinemonk/program_dumps/blob/m41n/responsor.py)


<br>
<hr>
<br>

## brrtp
- Burp Raw Requests To Python
- converts raw requests from burp suite to python code
- output:
    - prints the converted python code
    - saves it in a file (named same as `burp_raw_request_file` _name_ with `.py` extenstion)
```
python3 brrtp.py <burp_raw_request_file>
```
- Download: `wget https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/brrtp.py`
- [Goto source code](https://github.com/Divinemonk/program_dumps/blob/m41n/brrtp.py)
