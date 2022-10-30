# WALLPAPER4LINUX

This application uses [PixaBay](https://pixabay.com/) [api](https://pixabay.com/api/docs/) for downloading images and use these downloaded images as desktop home screen wallpaper. 


Pre-requisite - 
  - To use this application user need to have a [PixaBay](https://pixabay.com/) account. 
  - Generate access token from your account and keep it noted somewhere. To know about, how to generate access token please watch this [video](https://www.youtube.com/watch?v=6X1l_J-8QOE&t=44s) by [Video Pizzazz](https://www.youtube.com/c/VideopizzazzLLC). 

### Installation -
- Required python3 version for this app is `python3.8`
- Create application home directory -

    `$ mkdir $HOME/.wallapaper4linux`

- Create a vitual environtment to run this application

    `$ python3.8 -m venv $HOME/.wallapaper4linux/envPy`
 
- Activate virtual environent - 

    `$ source $HOME/.wallapaper4linux/envPy/bin/activate`

- Download wheel file from this [URL](link_to_whl_file)

- Execute below command to install application - 

  `$ pip install wallpaper4linux-1.0b0-py3-none-any.whl`

- After this application is installed, you need to add your PixaBay   **access-token** (generated above) in bashrc file.

  - Open `.bashrc` file - 

      `$ vim ~/.bashrc`
  - Add below line at the end of bashrc file -

     `PX_ACCESS_TOKEN=<your-access-token-key>`

  - Save and close the file and execute below command - 
  
      `$ bash`

- Now application is installed successfully.

- To Setup application follow below steps - 
  - Create service file
    ```bash
    $ cd /lib/systemd/system
    $ sudo vim wallpaper4linux.service
    ```
  - Put the content as shown below in created `wallpaper4linux.service` file -
    ```bash
    [Unit]
    Description=Linux Wallpaper application
    After=multi-user.target
    After=network-online.target
    Wants=network-online.target

    [Service]
    Type=simple
    ExecStart=<user-home-path>/.wallpaper4linux/envPy/bin/w4l-app-start
    Restart=always
    user=<your-user-name>
    Group=<your-user-name>

    [Install]
    WantedBy=multi-user.target
    ```

  - Finally Save and close the file. Now that we have created our service, we need to  activate it, for that execute the following command in sequence.
    ```bash
    $ sudo chmod 644 /lib/systemd/system/wallpaper4linux.service
    $ sudo systemctl daemon-reload
    $ sudo systemctl enable wallpaper4linux.service
    $ sudo systemctl start wallpaper4linux.service
    ```
  - To ensure that our service starts only after newtork is properly up, please execute below commands -
    ```bash
    $ sudo systemctl enable systemd-networkd-wait-online.service
    $ sudo systemctl start systemd-networkd-wait-online.service
    ```

- This completes the installation and setup of **Wallpaper4Linux** application.
- Now, you will be able to enjoy new desktop every-day. 

**--THANKS--**


  
