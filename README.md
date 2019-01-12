# custom-installer

1. Clone 
2. Build

```bash
sudo docker build --tag=custom-installer .
```

3. Run

```bash
sudo docker run -d --name custom-installer -p 9999:9999 -v /path/to/HA/config:/config
```