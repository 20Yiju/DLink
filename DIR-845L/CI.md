## D-Link DIR-845L OS Command Injection Vulnerability

**Credit** : 정이주 (wjddlwn2637@korea.ac.kr)  

**Vendor** : D-Link  

**Product** : DIR-845L Router 

**Firmware Link** : Firmware file is attached. Or you can download firmware at (https://www.mydlink.co.kr/2013/beta_board/product_detail.php?no=146&model=DIR-845L)

![Untitled](https://github.com/goldds96/Report/assets/86287862/825ee633-8b3a-48ce-88a8-9e65db8d2f4b)



## Detailed Description

 
**Vulnerability Type** : OS Command Injection  

**Affected Version** : Firmware version <= v1.01KRb03  

**Description** : Command Injection Vulnerability exists in **cgibin** binary in **DIR-845L** router firmware **version ≤ v1.0.4**. In **ssdpcgi_main** function, HTTP request header field parsing data obtaind by the program via **getenv(”HTTP_ST”)** is pass to **lxmldbc_system**. And in **lxmldbc_system**, data pass directly to **system** without any filtering. Since there is no proper filtering process, attacker can send malicious data and can execute arbitrary command.  

![Screenshot from 2024-03-11 13-48-48](https://github.com/20Yiju/DLink/assets/79932335/81fa83da-80d4-40e5-815d-ff6d9b753534)
![Screenshot from 2024-03-11 13-49-26](https://github.com/20Yiju/DLink/assets/79932335/73dfe558-e030-4fa4-aeba-c1df61ee808c)
![Screenshot from 2024-03-11 13-51-12](https://github.com/20Yiju/DLink/assets/79932335/e13da747-f69d-4d44-9b8a-58e9266f7057)


## PoC
PoC code is attached.  
To reproduce this vulnerability, you can emulate firmware by using FirmAE(https://github.com/pr0v3rbs/FirmAE)  

![Screenshot from 2024-03-11 13-56-17](https://github.com/20Yiju/DLink/assets/79932335/9ed3074e-6bfa-49cf-81e5-9e3da37ba690)

If emulation is success, you can access web interface  
![Screenshot from 2024-03-11 13-56-38](https://github.com/20Yiju/DLink/assets/79932335/5f658655-f704-4bda-93da-c18f943877c3)

Finally, run the PoC code.  
![Screenshot from 2024-03-11 13-59-06](https://github.com/20Yiju/DLink/assets/79932335/23054f7c-455a-4786-a90a-dd151a40c539)
