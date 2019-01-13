# custom-component-store

![overview](images/demo.gif)

## Installation

```bash
git clone https://github.com/ludeeus/custom-component-store.git
cd custom-component-store/
sudo docker build --tag=custom-component-store .
sudo docker run -d --name custom-component-store -p 9999:9999 -v /path/to/HA/config:/config custom-component-store
```

Now Open browser to `http://DOCKERHOST:9999`

## Upgrade

```bash
cd custom-component-store/
git pull
sudo docker rm -f custom-component-store
sudo docker run -d --name custom-component-store -p 9999:9999 -v /path/to/HA/config:/config custom-component-store
```

Now Open browser to `http://DOCKERHOST:9999`
