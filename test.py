import screeninfo
for monitor in screeninfo.get_monitors():
    print(f'monitor width: {monitor.width}; monitor height:{monitor.height}')
