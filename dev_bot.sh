# !/bin/bash
docker run -it --rm -v tg_libdata:/usr/local/lib -v /mnt/c/prog/py/gs_bot/app:/app --network bridge python bash
