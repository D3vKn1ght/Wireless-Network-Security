# Tấn công kết hợp Deauthentication và Rogue Access Point

**A.Chuẩn bị:**

**I.Công cụ:**

- Airmon-ng
- NodeMCU Flasher : https://github.com/nodemcu/nodemcu-flasher
- Captive Portal: : [https://github.com/D3vKn1ght/ESP8266-Captive-Portal](https://github.com/D3vKn1ght/ESP8266-Captive-Portal)
- Code demo: [https://github.com/D3vKn1ght/Wireless-Network-Security](https://github.com/D3vKn1ght/Wireless-Network-Security).

**II.Triển khai Captive Portal:**

Sau khi tải source code captive portal, tiến hành nạp code vào một ESP8266.

Để đơn giản, có thể sử dụng bản release có sẵn: [https://github.com/D3vKn1ght/ESP8266-Captive-Portal/releases/download/v1.0/WiFi_Captive_Portal.ino.bin](https://github.com/D3vKn1ght/ESP8266-Captive-Portal/releases/download/v1.0/WiFi_Captive_Portal.ino.bin)

Mở **NodeMCU Flasher** kết nối với port của ESP8266.

<img width="80%" src="image/nodemcuflaser.png">

Vào config thêm file bin vừa tải ở trên vào:

<img width="80%" src="image/flaserconfig.png">
Tiến hành ấn flash, sau khi flash hoàn thành sẽ có một captive portal trên ESP8266.

<img width="80%" src="image/captiveaptiveportal.png">

**III. Bật monitor mode wifi:**

Gõ lệnh **iwconfig** tìm interface của card wifi, ví dụ : **wlp0s20f3**

<img width="80%" src="image/iwconfig.png">

Tiến hành chuyển card wifi sang monitor mode:

<img width="80%" src="image/monitormode.png">

**B. Demo:**

**I. Tấn công:**

1. **Cấu hình captive portal:**

Kết nối captive portal qua wifi, truy cập **172.0.0.1/ssid** thay đổi ssid bằng ssid cần tấn công giả mạo.

<img width="80%" src="image/captivessid.png">

Trong danh sách hiển thị wifi nhìn thấy một điểm truy cập có ssid giống với ssid của điểm truy cập cần tấn công.

<img width="80%" src="image/listwifi.png">

Tuy nhiên, victim sẽ không tự động truy cập vào điểm truy cập giả mạo. Tấn công, deautheication để khuyến khích victim truy cập điểm cập giả mạo.

1. **Tấn công deauthentication:**

Sau khi tải code demo, ta được các tệp dưới đây:

<img width="80%" src="image/listfile.png>

Trên terminal nhập: **sudo python3 showwificlient.py** để lấy địa chỉ MAC của client, BSSID của điểm truy cập cần tấn công. Ở đây ta tìm kiếm điểm truy cập có tên là banhMi.

Tiến hành nhập interface mà ta thấy ở bước chuẩn bị, ở đây là wlp0s20f3mon.

<img width="80%" src="image/showwifi1.png>


Ta có địa chỉ BSSID là  **E8:48:B8:EF:5A:7C**, MAC kết nối tới điểm truy cập SSID banhMi là **00:D2:79:B3:D4:D4:**

<img width="80%" src="image/showifi2.png>

Mở một tab mới, nhập lệnh : **sudo python3 deauthen.py.** Nhập interface, bssid, ssid thu được ở trên:

[https://lh7-us.googleusercontent.com/cbiYM3coDCv0dg44ij62rPGaelxhE8C54Nvl_No946St5mfZz719hmPDBC-eNliuLamFbAeCuYBq3fxqIhHmQorZ8wqcqFWy6CvybQrzEXAswK_8KSG4zmiefQ0ze_wyAFWwFFUquEQ3oyZyot2e6wA](https://lh7-us.googleusercontent.com/cbiYM3coDCv0dg44ij62rPGaelxhE8C54Nvl_No946St5mfZz719hmPDBC-eNliuLamFbAeCuYBq3fxqIhHmQorZ8wqcqFWy6CvybQrzEXAswK_8KSG4zmiefQ0ze_wyAFWwFFUquEQ3oyZyot2e6wA)

Công cụ hiển thị thông tin gói tin deauthen, nhấn Enter để tiếp tục tấn công. Sau khi ấn Enter, công cụ hiển thị log đang tấn công deauthen và trên thiết bị kết nối wifi đã bị mất kết nối wifi.

[https://lh7-us.googleusercontent.com/s4cG9U8JuNw6lG6KIA7K4ePsZEehRNoDBrB4rWl99HKBNjnjbl9kk6Rsoq3VyPB1rf8RWfqRti32-IVBGjhRD9lUWWmTfpv3Uqqi16MjymDqayL-gsSpRpxsP1klD11shA-ULovRIVrNlEmvG-6VsRs](https://lh7-us.googleusercontent.com/s4cG9U8JuNw6lG6KIA7K4ePsZEehRNoDBrB4rWl99HKBNjnjbl9kk6Rsoq3VyPB1rf8RWfqRti32-IVBGjhRD9lUWWmTfpv3Uqqi16MjymDqayL-gsSpRpxsP1klD11shA-ULovRIVrNlEmvG-6VsRs)

Lúc này, victim thử kết nối với điểm truy cập sẽ không kết nối được.

[https://lh7-us.googleusercontent.com/Le-y4bGX0WHmnS9FQxcWBqtXio5-NRYuMyAtCxjZi3vtHIeBU5TUXeY9sK3N-jhfFGOJhXaSpcDmzcPgOptmO7WzLOEfAbHCKCctAiOqRwEEHBnGYINwRyNYtzMDwUAyYRBK6d0doovSARw96VXvwjs](https://lh7-us.googleusercontent.com/Le-y4bGX0WHmnS9FQxcWBqtXio5-NRYuMyAtCxjZi3vtHIeBU5TUXeY9sK3N-jhfFGOJhXaSpcDmzcPgOptmO7WzLOEfAbHCKCctAiOqRwEEHBnGYINwRyNYtzMDwUAyYRBK6d0doovSARw96VXvwjs)

Nhận thấy có một điểm truy cập có cấu hình giống với cấu hình thật hiển thị. Khi victim kết nối tới điểm truy cập giả mạo này, một trang web thông báo wifi lỗi thời, cần nhập mật khẩu để cập nhật.

[https://lh7-us.googleusercontent.com/sd48Om7BSTEUuoZboVnBmo1ODwMDeiZaEYWKGIMl4L4NdoTCgpvq1FxllN8fblB3qXghM8XkaUrpI_BVS3SI9uVft1JMfWwbsxJceyz-WGkfM9Y7eibIT7RStns0F84A6w4Sauqppj6pje-k9iu9oZg](https://lh7-us.googleusercontent.com/sd48Om7BSTEUuoZboVnBmo1ODwMDeiZaEYWKGIMl4L4NdoTCgpvq1FxllN8fblB3qXghM8XkaUrpI_BVS3SI9uVft1JMfWwbsxJceyz-WGkfM9Y7eibIT7RStns0F84A6w4Sauqppj6pje-k9iu9oZg)

Khi victim nhập mật khẩu, điểm truy cập giả mạo sẽ chuyển tiếp đến trang web đang cập nhật, vui lòng chờ.

[https://lh7-us.googleusercontent.com/zH4zdblYdmJaD9odY9PdLSnwPnlf4dGVQrK-e7F_Tyi1YA9ZBTECAkksz64Z6kWspIzrreHVzR9lhdip4-F6hP_PsVp728vH58zCme86rHJl5_Odu6tmLK-AyDaDTKCxwZfSCiW3QmhUh77cAP6K7b8](https://lh7-us.googleusercontent.com/zH4zdblYdmJaD9odY9PdLSnwPnlf4dGVQrK-e7F_Tyi1YA9ZBTECAkksz64Z6kWspIzrreHVzR9lhdip4-F6hP_PsVp728vH58zCme86rHJl5_Odu6tmLK-AyDaDTKCxwZfSCiW3QmhUh77cAP6K7b8)

1. **Tấn công deauthentication:**

Lúc này, chúng ta mở địa chỉ **172.0.0.1/pass** sẽ thu được ssid, mật khẩu của điểm truy cập thật.
<img width="80%" src="image/cppass.png">


**II. Phòng thủ:**

Để phát hiện cuộc tấn công deauthen, ta chạy lệnh **sudo python3 detect_deauthen.py** để tiến hành bắt các gói tin beacon và gói tin deauthen.

<img width="80%" src="image/defentsniff.png">

****Khi có cuộc tấn công, công cụ hiển thị thông tin của cuộc tấn công deauthen:

<img width="80%" src="image/defendetect.png">
