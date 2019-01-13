# custom-component-store

1. Clone 
2. Build
3. Run
4. Open browser to `http://DOCKERHOST:9999`

```bash
git clone https://github.com/ludeeus/custom-component-store.git
cd custom-component-store./
sudo docker build --tag=custom-component-store .
sudo docker run -d --name custom-component-store -p 9999:9999 -v /path/to/HA/config:/config custom-component-store
```

![overview](images/demo.gif)