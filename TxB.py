clear

apt install figlet -y
apt install toilet -y
apt install cowsay -y
apt install nano -y
apt install ruby -y
gem install lolcat
pkg update && pkg upgrade

clear

#colour
r='\e[1;31m'
g='\e[1;32m'
y='\e[1;33m'
b='\e[1;34m'
p='\e[1;35m'
lb='\e[1;36m'


#logo
figlet Tx Banner | lolcat
echo -e $r "                 ᴛᴏᴏʟ ʙʏ © ᴍʀ.ᴛʜᴇɴᴜx "
echo

#banner
echo -e $g "What's your banner name ?"
read varB
echo

#cowsay
echo -e $g "What's your cowsay name ?"
read varC
echo

echo  "cowsay -f eyes "$varC" | lolcat" > tcowsay.txt
echo "toilet -f big ' $varB' -F gay | lolcat" > tbanner.txt
echo
echo "clear" > tclear.txt

cat "tclear.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc
cat "tcowsay.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc
ls
cat "tbanner.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc

#finish

figlet Finish | lolcat
exit