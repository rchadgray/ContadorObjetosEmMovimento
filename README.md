How i installed openCV on my raspberry Pi 4
https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/

Lots of educational info on openCV
https://www.pyimagesearch.com/

My istallation notes
 1  ifconfig
    2  raspiconfig
    3  raspi-config
    4  sudo raspi-config
    5  sudo raspi-config
    6  sudo apt-get purge wolfram-engine
    7  sudo apt-get purge libreoffice*
    8  sudo apt-get autoremove
    9  sudo apt-get update && sudo apt-get upgrade
   10  sudo apt-get install build-essential cmake pkg-config
   11  sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
   12  sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
   13  sudo apt-get install libxvidcore-dev libx264-dev
   14  sudo apt-get install libfontconfig1-dev libcairo2-dev
   15  sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev
   16  sudo apt-get install libgtk2.0-dev libgtk-3-dev
   17  sudo apt-get install libatlas-base-dev gfortran
   18  sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103
   19  sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
   20  sudo apt-get install python3-dev
   21  wget https://bootstrap.pypa.io/get-pip.py
   22  sudo python get-pip.py
   23  sudo python3 get-pip.py
   24  sudo rm -rf ~/.cache/pip
   25  sudo pip install virtualenv virtualenvwrapper
   26  sudo nano ~/.bashrc
   27  source ~/.bashrc
   28  mkvirtualenv cv -p python3
   29  sudo mkvirtualenv cv -p python3
   30  ls
   31  ls -al
   32  cd .virtualenvs/
   33  ls
   34  cd cv
   35  ls
   36  cd ~
   37  workon cv
   38  cd .virtualenvs/cv/
   39  ls -al
   40  touch foo.py
   41  workon cv
   42  cd ~
   43  pip install "picamera[array]"
   44  pip install opencv-contrib-python==4.1.0.25
   45  workon cv
   46  sudo nano ~/.bashrc
   47  sudo pip3 uninstall virtualenv virtualenvwrapper
   48  sudo pip3 install virtualenv virtualenvwrapper=='4.8.4'
   49  sudo nano ~/.bashrc
   50  mkvirtualenv test
   51  sudo reboot
   52  ls -al
   53  workon cv
   54*
   55  sudo python ./ContadorObjetosEmMovimento.
   56  sudo python ./ContadorObjetosEmMovimento.py
   57  pip list
   58  history
   59  python
   60  sudo nano ContadorObjetosEmMovimento.py
   61  pip list
   62  pyton
   63  python
   64  ./ContadorObjetosEmMovimento.py
   65  pip install opencv-contrib-python==4.1.0.25
   66  python3 ./ContadorObjetosEmMovimento.
   67  python3 ./ContadorObjetosEmMovimento.py



# Contador de objetos em movimento
Contador de objetos em movimento (utilizando OpenCV e Python)

1) Para executar o projeto na Raspberry PI:
- Utilize o código-fonte "ContadorObjetosEmMovimento.py"
- Leia com atenção o seguinte artigo: https://www.embarcados.com.br/objetos-opencv-e-python-raspberry-pi/

2) Para executar na Orange PI PC Plus H3:
- Para instalar os pacotes necessáios, execute os comandos a seguir no terminal:

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo apt-get install python-opencv

- Utilize o código-fonte "ContadorObjetosEmMovimento_OrangePIPc.py"
- Leia com atenção o seguinte artigo: https://www.embarcados.com.br/objetos-opencv-e-python-raspberry-pi/
  Apesar do artigo ter sido idealizado para a Raspberry PI, o raciocínio é análogo.
