echo "deb http://pools.corp.deepin.com/debian unstable main contrib non-free" > /etc/apt/sources.list
apt-get update
apt-cache rdepends libqt5core5a > deb.list
sed -e '/libqt5core5a/d' -e '/Reverse/d' -e 's/^ *//' deb.list > pkg.list
rm deb.list
apt-get -y install python3-apt
python3 checksource.py
