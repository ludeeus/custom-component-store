# custom-installer

1. Clone 
2. Build
3. Run
4. Open browser to `http://DOCKERHOST:9999`

```bash
git clone https://github.com/ludeeus/custom-installer.git
cd custom-installer/
sudo docker build --tag=custom-installer .
sudo docker run -d --name custom-installer -p 9999:9999 -v /path/to/HA/config:/config custom-installer
```