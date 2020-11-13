import RPi.GPIO as GPIO
import time
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(25, GPIO.IN)
​
try:
 pir = 0
 while 1 :
     if GPIO.input(25) == True :
         pir = "1"
         GPIO.output(16,GPIO.HIGH)
     else :
         pir = "0"
         GPIO.output(16,GPIO.LOW)
     URL = 'http://rltkwpdntm.pythonanywhere.com/iot?pir=%s' % (pir)   # 이렇게 URL에 ?pir=%s 로 pir값을 넣어야 /iot 페이지에 pir값이 전달된다. 그래야 flask_app.py의 @app.route('/iot')의 request.args.get('pir') 을 통해 값이 전달된다.
     response = requests.get(URL)      # 위의 URL에서 GET 요청을 한 것의 결과를 response에 담는다
     print(URL)
     print("Result:" + response.text)  # response에 들어있는 text 내용을 출력한다. 여기서는 response가 flask의 /iot 페이지이기 때문에 flask_app.py 코드의 @app.route('/iot') 부분에서 처리된 내용이 여기에 들어온다.
     time.sleep(10)
except KeyboardInterrupt:               # Ctrl+C 하면 KeyboardInterrupt
  GPIO.cleanup()​