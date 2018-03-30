sudo stty -F /dev/ttyUSB0 1:0:9a7:0:3:1c:7f:15:4:5:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0
sudo echo -n -e '\x2F\x3F\x21\x0D\x0A' > /dev/ttyUSB0
sleep 1
sudo echo -n -e '\x06\x30\x30\x30\x0D\x0A' > /dev/ttyUSB0