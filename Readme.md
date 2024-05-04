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

[https://lh7-us.googleusercontent.com/pj1Qb1mZMBl_VMsF7t0cZTm1U0oHE60lOrBbj-gvnyteP8vRMt9s4ENMwwoFu4TEiDpEeLg1yX0376WMlWNdBwqRWlpzSf-9xvGG8gFT4XqSo9lBkAY-V-zZAHDP_sYY0ISdU7YtjQ-TM6zFE5KBfbU](https://lh7-us.googleusercontent.com/pj1Qb1mZMBl_VMsF7t0cZTm1U0oHE60lOrBbj-gvnyteP8vRMt9s4ENMwwoFu4TEiDpEeLg1yX0376WMlWNdBwqRWlpzSf-9xvGG8gFT4XqSo9lBkAY-V-zZAHDP_sYY0ISdU7YtjQ-TM6zFE5KBfbU)

Vào config thêm file bin vừa tải ở trên vào:

[https://lh7-us.googleusercontent.com/yWET-uKkrbcL-edkB92e-EUCdsCjVJGnNLOuR-6hwfq_ZCx4kiQ1V3Lqf_8r6jja6qPMb6g48BozqpRG1FLL3kExhp3PTAzaxbSbkHqp8HSrDCpxX20PVo8eg0iAn4sgbr157YcoVgdC6Akivk6lmoc](https://lh7-us.googleusercontent.com/yWET-uKkrbcL-edkB92e-EUCdsCjVJGnNLOuR-6hwfq_ZCx4kiQ1V3Lqf_8r6jja6qPMb6g48BozqpRG1FLL3kExhp3PTAzaxbSbkHqp8HSrDCpxX20PVo8eg0iAn4sgbr157YcoVgdC6Akivk6lmoc)

Tiến hành ấn flash, sau khi flash hoàn thành sẽ có một captive portal trên ESP8266.

[https://lh7-us.googleusercontent.com/0Ngd9fc4cHc1yBQQLPaMXEqBDjq4SEtfkktlRAsUjnhoyBqO8uH4OLQa3hxQ0vWZJkPYJUHj6shW5dxuuapYenxzsMI2tmkIKEL4w0V35rNFtd-BHEEZrdhSpDlMtQQW5XkFrsDHl5hnB3ZU2-oHbLo](https://lh7-us.googleusercontent.com/0Ngd9fc4cHc1yBQQLPaMXEqBDjq4SEtfkktlRAsUjnhoyBqO8uH4OLQa3hxQ0vWZJkPYJUHj6shW5dxuuapYenxzsMI2tmkIKEL4w0V35rNFtd-BHEEZrdhSpDlMtQQW5XkFrsDHl5hnB3ZU2-oHbLo)

**III. Bật monitor mode wifi:**

Gõ lệnh **iwconfig** tìm interface của card wifi, ví dụ : **wlp0s20f3**

[https://lh7-us.googleusercontent.com/eHgvTlNCErr_j5CF8kqA1r4LJp2QmFh4RArHFKGIsaAusXgEvQddFbCySSIT9TU_2S5klI3gwHHI5vVd7pDJNEHjO-J22vpR1IO1SotZqsthi7UxCzIjIyvlXT7w0PG6vti5Pnx10KfsihpPNDWibAg](https://lh7-us.googleusercontent.com/eHgvTlNCErr_j5CF8kqA1r4LJp2QmFh4RArHFKGIsaAusXgEvQddFbCySSIT9TU_2S5klI3gwHHI5vVd7pDJNEHjO-J22vpR1IO1SotZqsthi7UxCzIjIyvlXT7w0PG6vti5Pnx10KfsihpPNDWibAg)

Tiến hành chuyển card wifi sang monitor mode:

[https://lh7-us.googleusercontent.com/3X2ioe__L_klFEMUFVm8RF1PiIKWBcU99Z05j9xyFiDNkO65qGpknEZ3TXPGDKa3hMC9K9FTXCRJJd9Uwa_mIDd7zNkQN8crxh4CtK6r9JeDaaRfQyxT-1uvmii9qH3VMuRpU6Usza_N2wUuyD2tH_U](https://lh7-us.googleusercontent.com/3X2ioe__L_klFEMUFVm8RF1PiIKWBcU99Z05j9xyFiDNkO65qGpknEZ3TXPGDKa3hMC9K9FTXCRJJd9Uwa_mIDd7zNkQN8crxh4CtK6r9JeDaaRfQyxT-1uvmii9qH3VMuRpU6Usza_N2wUuyD2tH_U)

**B. Demo:**

**I. Tấn công:**

1. **Cấu hình captive portal:**

Kết nối captive portal qua wifi, truy cập **172.0.0.1/ssid** thay đổi ssid bằng ssid cần tấn công giả mạo.

[https://lh7-us.googleusercontent.com/ZhsMx-W6ftrqPeThYZ12fPvoZlGdY4x-CcoeArL20Z1xpYVTi_FeMaAAOSQ4cYUjL4uGm0D6lpqNduTc-L4ilNKg6zda3eMNiD_HaZ4cOJrdh3Y_OdH-83-CUH0JoDVzG7FARWNYfy7TDYV4kCY0zA8](https://lh7-us.googleusercontent.com/ZhsMx-W6ftrqPeThYZ12fPvoZlGdY4x-CcoeArL20Z1xpYVTi_FeMaAAOSQ4cYUjL4uGm0D6lpqNduTc-L4ilNKg6zda3eMNiD_HaZ4cOJrdh3Y_OdH-83-CUH0JoDVzG7FARWNYfy7TDYV4kCY0zA8)

Trong danh sách hiển thị wifi nhìn thấy một điểm truy cập có ssid giống với ssid của điểm truy cập cần tấn công.

[https://lh7-us.googleusercontent.com/mkCaG9MipKARbhVcibFBi18qETir2qg_E-65ye5s_KARrw7-nP4Fr9CBouLFiWP0jH5JuBlMcnCmZUvOpVQmPE0VPg1hSmuQQq_3V4tdvBlVK7YEMHx8m2KbJbyWFKGAj506J1AvSNWBgM6RGzA8na8](https://lh7-us.googleusercontent.com/mkCaG9MipKARbhVcibFBi18qETir2qg_E-65ye5s_KARrw7-nP4Fr9CBouLFiWP0jH5JuBlMcnCmZUvOpVQmPE0VPg1hSmuQQq_3V4tdvBlVK7YEMHx8m2KbJbyWFKGAj506J1AvSNWBgM6RGzA8na8)

Tuy nhiên, victim sẽ không tự động truy cập vào điểm truy cập giả mạo. Tấn công, deautheication để khuyến khích victim truy cập điểm cập giả mạo.

[https://lh7-us.googleusercontent.com/yyUlYp6Xnwqrba1lAzOxhE-xtPUGq7LOEyuoIyvKnmZ0iJUUtr-vv-jV21uIC1E8oTcI_WH41v4sEXKg7SGzCZq9tSo5tQz8WJmHOcuk7eb3zG_zVMSUnIZLO5spderXNtW7xvNPccAI8Uo7PLYWmlc](https://lh7-us.googleusercontent.com/yyUlYp6Xnwqrba1lAzOxhE-xtPUGq7LOEyuoIyvKnmZ0iJUUtr-vv-jV21uIC1E8oTcI_WH41v4sEXKg7SGzCZq9tSo5tQz8WJmHOcuk7eb3zG_zVMSUnIZLO5spderXNtW7xvNPccAI8Uo7PLYWmlc)

1. **Tấn công deauthentication:**

Sau khi tải code demo, ta được các tệp dưới đây:

[https://lh7-us.googleusercontent.com/VLFcXIb93Ne5Trvg6byFzs2ShGom_PnSb4CEuzUgHi3u9AJdgforD3uzp91fJXLJ3Jc77QU2ft27XhWApSPPwdVl4iHIXmjCh9Qb77iXyaqkut0IFM7q3xy8mCdVz5EtEXAytDtjYNBSAxpY7sytRqI](https://lh7-us.googleusercontent.com/VLFcXIb93Ne5Trvg6byFzs2ShGom_PnSb4CEuzUgHi3u9AJdgforD3uzp91fJXLJ3Jc77QU2ft27XhWApSPPwdVl4iHIXmjCh9Qb77iXyaqkut0IFM7q3xy8mCdVz5EtEXAytDtjYNBSAxpY7sytRqI)

Trên terminal nhập: **sudo python3 showwificlient.py** để lấy địa chỉ MAC của client, BSSID của điểm truy cập cần tấn công. Ở đây ta tìm kiếm điểm truy cập có tên là banhMi.

Tiến hành nhập interface mà ta thấy ở bước chuẩn bị, ở đây là wlp0s20f3mon.

[https://lh7-us.googleusercontent.com/vywJ9TNkVweL0LmEuQG7C5Gn72LAe8Ahk0EpGGYrvqn2il9Q7F-AhZkzNswDnB3lJfBh7IjYV3mH6ohkapcL4eJ8bZoLN23VROAaBq9wRhykv71Hh6kkW6FoQkYyk0_101oF3KyeWOWRtIQ32GCI5TM](https://lh7-us.googleusercontent.com/vywJ9TNkVweL0LmEuQG7C5Gn72LAe8Ahk0EpGGYrvqn2il9Q7F-AhZkzNswDnB3lJfBh7IjYV3mH6ohkapcL4eJ8bZoLN23VROAaBq9wRhykv71Hh6kkW6FoQkYyk0_101oF3KyeWOWRtIQ32GCI5TM)

Ta có địa chỉ BSSID là  **E8:48:B8:EF:5A:7C**, MAC kết nối tới điểm truy cập SSID banhMi là **00:D2:79:B3:D4:D4:**

[https://lh7-us.googleusercontent.com/sK4cnY0Q5Mo0azkrimxe-w8H-S93AxSF1QY2jmvh3s6wcvPJrLj73fdCeX0L36SmTxJJwhta00UtjLNYQBhQMQ-va2KERGBuupxpo3odk2GlC-DCcfWdxzsBsH8oNACvGEMSz7rcLPJ2GiQaoop4A20](https://lh7-us.googleusercontent.com/sK4cnY0Q5Mo0azkrimxe-w8H-S93AxSF1QY2jmvh3s6wcvPJrLj73fdCeX0L36SmTxJJwhta00UtjLNYQBhQMQ-va2KERGBuupxpo3odk2GlC-DCcfWdxzsBsH8oNACvGEMSz7rcLPJ2GiQaoop4A20)

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

Lúc này, chúng ta mở địa chỉ **172.0.0.1/ssid** sẽ thu được ssid, mật khẩu của điểm truy cập thật.

**II. Phòng thủ:**

Để phát hiện cuộc tấn công deauthen, ta chạy lệnh **sudo python3 detect_deauthen.py** để tiến hành bắt các gói tin beacon và gói tin deauthen.

[https://lh7-us.googleusercontent.com/rgqBD1wY9zqHYhXfMmgUxDzi8X_rQBFoJf_jLnregEEtZ84c_QMO6aVKXqoXrORfl0IyBTdCmfPLOJ1SbL6_apUKhytJvTRFObClSUEKvsIibEf4I6eJvENazVqfNgXAIzOkzprMbqII4t0q9NZWYW8](https://lh7-us.googleusercontent.com/rgqBD1wY9zqHYhXfMmgUxDzi8X_rQBFoJf_jLnregEEtZ84c_QMO6aVKXqoXrORfl0IyBTdCmfPLOJ1SbL6_apUKhytJvTRFObClSUEKvsIibEf4I6eJvENazVqfNgXAIzOkzprMbqII4t0q9NZWYW8)

****Khi có cuộc tấn công, công cụ hiển thị thông tin của cuộc tấn công deauthen:

[https://lh7-us.googleusercontent.com/-JONr__JCoa6-M3TOOKpcHuHkpomAOg3WmKhVDqvm1sCMsrg57zAf6LTNu4B25B9IFtO4wp3aDWezANGJkAY_APrR6iIFkssccfV6Pd2OloYSR1zNOZwIogH0HFWgA9Tjaql2_T-Cdw8ivVYl0I5Vnc](https://lh7-us.googleusercontent.com/-JONr__JCoa6-M3TOOKpcHuHkpomAOg3WmKhVDqvm1sCMsrg57zAf6LTNu4B25B9IFtO4wp3aDWezANGJkAY_APrR6iIFkssccfV6Pd2OloYSR1zNOZwIogH0HFWgA9Tjaql2_T-Cdw8ivVYl0I5Vnc)