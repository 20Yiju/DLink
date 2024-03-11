## D-Link DIR-845L OS Command Injection Vulnerability

**Credit** : 정이주 (wjddlwn2637@gmail.com)  

**Vendor** : D-Link  

**Product** : DIR-845L Router 

**Firmware Link** : Firmware file is attached. Or you can download firmware at (https://www.mydlink.co.kr/2013/beta_board/product_detail.php?no=146&model=DIR-845L)

![Untitled](https://github.com/goldds96/Report/assets/86287862/825ee633-8b3a-48ce-88a8-9e65db8d2f4b)



## Detailed Description

 
**Vulnerability Type** : OS Command Injection  

**Affected Version** : Firmware version <= v1.01KRb03  

**Description** : Command Injection Vulnerability exists in **cgibin** binary in **DIR-845L** router firmware **version ≤ v1.0.4**. In **ssdpcgi_main** function, HTTP request header field parsing data obtaind by the program via **getenv(”HTTP_ST”)** is pass to **lxmldbc_system**. And in **lxmldbc_system**, data pass directly to **system** without any filtering. Since there is no proper filtering process, attacker can send malicious data and can execute arbitrary command.  





## PoC
PoC code is attached.  
To reproduce this vulnerability, you can emulate firmware by using FirmAE(https://github.com/pr0v3rbs/FirmAE)  



If emulation is success, you can access web interface  

Finally, run the PoC code.  
