import platform
import sys
import os
import json
data={}
os_type=platform.system()
if os_type=="Windows":
    release,version,csd,ptype=platform.win32_ver()
    if hasattr(platform,'win32_edition'):
        edition=platform.win32_edition()
    else:
        edition="Unknown edition"
    data={
        "windows_version": release,
        "edition": edition,
        "build number": version,
        "system_root": os.environ.get("SystemRoot","C:\\Windows"),
        "user_profile": os.environ.get("USERPROFILE"),
        "architecture": platform.machine(),
    }
elif os_type=="Darwin":
    release,version,machine=platform.mac_ver()
    data={
        "macos_version": release,
        "build": version if version else "Unknown",
        "architecture": machine,
        "home_directory": os.path.expanduser("~"),
    }

elif os_type=="Linux":
    try:
        os_release=platform.freedesktop_os_release()
        name=os_release.get("PRETTY_NAME","Linux OS")
        ident=os_release.get("ID","unknown")
    except (AttributeError, OSError):
        name="Linux"
        ident="unknown"
    data={
        "release": platform.release(),
        "name":name,
        "id":ident,
        "architecture":platform.machine(),
        "default_shell": os.environ.get("SHELL","Not Defined"),
    }
    
else:
    data ={
        "platform":platform.platform(),
        "hostname":platform.node(),
        "python_version":sys.version.split()[0],
    }


with open("system_info.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Информация успешно сохранена в system_info.json")  
