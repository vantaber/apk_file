#if not working app store in ubuntu 20.04.02
sudo snap remove snap-store
sudo snap install snap-store

#before install pycharm
sudo apt -y install python3-distutils
sudo apt -y install python3-pip
pip3 install setuptools

sudo apt install -y git
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python3 setup.py install

buildozer init

nano buildozer.spec

#https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user --upgrade Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv

# add the following line at the end of your ~/.bashrc file
export PATH=$PATH:~/.local/bin/

buildozer android debug deploy run





[INFO]:    COMMAND:
cd /home/dima/PycharmProjects/pythonProject/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/pyjnius-sdl2/armeabi-v7a__ndk_target_21/pyjnius && /home/dima/PycharmProjects/pythonProject/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3 setup.py build_ext -v

[WARNING]: ERROR: /home/dima/PycharmProjects/pythonProject/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/hostpython3/desktop/hostpython3/native-build/python3 failed!

# Command failed: ['/usr/bin/python3', '-m', 'pythonforandroid.toolchain', 'create', '--dist_name=mymobilecalc', '--bootstrap=sdl2', '--requirements=python3,kivy', '--arch=armeabi-v7a', '--copy-libs', '--color=always', '--storage-dir=/home/dima/PycharmProjects/pythonProject/.buildozer/android/platform/build-armeabi-v7a', '--ndk-api=21', '--ignore-setup-py', '--debug']
# ENVIRONMENT:
#     SHELL = '/bin/bash'
#     SESSION_MANAGER = 'local/dima-VirtualBox:@/tmp/.ICE-unix/970,unix/dima-VirtualBox:/tmp/.ICE-unix/970'
#     QT_ACCESSIBILITY = '1'
#     COLORTERM = 'truecolor'
#     XDG_CONFIG_DIRS = '/etc/xdg/xdg-ubuntu:/etc/xdg'
#     SSH_AGENT_LAUNCHER = 'gnome-keyring'
#     XDG_MENU_PREFIX = 'gnome-'
#     GNOME_DESKTOP_SESSION_ID = 'this-is-deprecated'
#     GNOME_SHELL_SESSION_MODE = 'ubuntu'
#     SSH_AUTH_SOCK = '/run/user/1000/keyring/ssh'
#     XMODIFIERS = '@im=ibus'
#     DESKTOP_SESSION = 'ubuntu'
#     GTK_MODULES = 'gail:atk-bridge'
#     DBUS_STARTER_BUS_TYPE = 'session'
#     PWD = '/home/dima/PycharmProjects/pythonProject'
#     LOGNAME = 'dima'
#     XDG_SESSION_DESKTOP = 'ubuntu'
#     XDG_SESSION_TYPE = 'wayland'
#     SYSTEMD_EXEC_PID = '970'
#     XAUTHORITY = '/run/user/1000/.mutter-Xwaylandauth.ZIX191'
#     HOME = '/home/dima'
#     USERNAME = 'dima'
#     IM_CONFIG_PHASE = '1'
#     LANG = 'ru_RU.UTF-8'
#     LS_COLORS = 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:'
#     XDG_CURRENT_DESKTOP = 'ubuntu:GNOME'
#     VTE_VERSION = '6800'
#     WAYLAND_DISPLAY = 'wayland-0'
#     GNOME_TERMINAL_SCREEN = '/org/gnome/Terminal/screen/43867db3_842b_4dc9_8c29_a73fe2d5afa5'
#     GNOME_SETUP_DISPLAY = ':1'
#     LESSCLOSE = '/usr/bin/lesspipe %s %s'
#     XDG_SESSION_CLASS = 'user'
#     TERM = 'xterm-256color'
#     LESSOPEN = '| /usr/bin/lesspipe %s'
#     USER = 'dima'
#     GNOME_TERMINAL_SERVICE = ':1.118'
#     DISPLAY = ':0'
#     SHLVL = '1'
#     QT_IM_MODULE = 'ibus'
#     DBUS_STARTER_ADDRESS = 'unix:path=/run/user/1000/bus,guid=e3d289ac00df69b3ade7d19064e3cd55'
#     XDG_RUNTIME_DIR = '/run/user/1000'
#     XDG_DATA_DIRS = '/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop'
#     PATH = '/home/dima/.buildozer/android/platform/apache-ant-1.9.4/bin:/home/dima/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin'
#     GDMSESSION = 'ubuntu'
#     DBUS_SESSION_BUS_ADDRESS = 'unix:path=/run/user/1000/bus,guid=e3d289ac00df69b3ade7d19064e3cd55'
#     _ = '/usr/local/bin/buildozer'
#     PACKAGES_PATH = '/home/dima/.buildozer/android/packages'
#     ANDROIDSDK = '/home/dima/.buildozer/android/platform/android-sdk'
#     ANDROIDNDK = '/home/dima/.buildozer/android/platform/android-ndk-r25b'
#     ANDROIDAPI = '31'
#     ANDROIDMINAPI = '21'
# 
# Buildozer failed to execute the last command
# The error might be hidden in the log above this error
# Please read the full log, and search for it before
# raising an issue with buildozer itself.
# In case of a bug report, please add a full log with log_level = 2

