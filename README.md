# Weather Stone🔮

> **'Weather Stone'** 은 상자 안에 다양한 날씨(☔️, ☁️, ⚡️)을 재현할 수 있는 디스플레이입니다. <br />
> 좋아하는 시간, 좋아하는 장소의 하늘을 방으로 가져올 수 있고, 일기 예보를 통해 내일의 하늘을 현관 앞에 둘 수 있습니다. <br /> <br />
<img width="400" alt="웨더스톤" src="https://user-images.githubusercontent.com/68539040/174648010-8c14b96d-2b94-4655-b1ac-c46e6902506b.png"> <br />
<br />


본체, 웹 어플리케이션, 서버 총 세 부분으로 구성되어 있습니다. <br />
상자는 투명 아크릴과 여러가지 모듈(LED, 초음파 가습기, 펌프 등) 그리고 라즈베리파이 4로 구성되어 있습니다. <br />
웹 어플리케이션은 사용자 위치의 날씨 API와 미세먼지 API를 받아오고, javascript, html를 사용해 사용자가 LED 색을 지정할 수 있는 UI와 기능을 개발했습니다.
<br /> <br />


### 비오는 날:  <br />
![비](https://user-images.githubusercontent.com/68539040/174646752-c75f19e2-433b-4764-81eb-05aa37f2459b.gif) <br /> <br />
**구현** <br />
![상자구성도](https://user-images.githubusercontent.com/68539040/174644707-e0a2c088-b679-460c-a73d-dc3391e092d2.png) <br />
펌프 모듈과 튜브로 물을 끌어올리고, 튜브에 적절히 구멍을 뚫어 비를 표현했습니다. <br />

```
def weather_rain():
    global pump_status
    while True:
        if pump_status == 1:
            GPIO.output(pump_pin, True)
        elif pump_status == 0:
            GPIO.output(pump_pin, False)
        pixels.show()
```


### 번개:  <br />
![번개](https://user-images.githubusercontent.com/68539040/174645794-2a94f252-e9e6-488f-b495-889318f5778c.gif) <br /> <br />
최소, 최대 랜덤 시간과 랜덤 sleep time을 정의하여 번개를 표현했습니다.  <br />

```
# RANDOM LIGHT
LIGHT_ON_TIME_MIN = 0.01
LIGHT_ON_TIME_MAX = 0.04
LIGHT_OFF_TIME_MIN = 0.15
LIGHT_OFF_TIME_MAX = 0.5

def weather_lightning():
    global led_status

    while True:
        if led_status == 1:
            random_on = uniform(LIGHT_ON_TIME_MIN, LIGHT_ON_TIME_MAX)
            random_off = uniform(LIGHT_OFF_TIME_MIN, LIGHT_OFF_TIME_MAX)

            pixels.fill(LIGHT_RGB)
            pixels.show()
            time.sleep(random_on)
            pixels.fill((0, 0, 0))
            pixels.show()
            time.sleep(random_off)
        pixels.show()
```
<br />



### 안개:  <br />
![안개](https://user-images.githubusercontent.com/68539040/174647819-57f8f9de-6f4b-4f30-a36c-f222d2d8ed04.gif) <br /> <br />
받아온 날씨 정보가 '안개'일때, 초음파 가습기 모듈과 펜 모듈을 가동합니다. <br />
가습기만 가동하니 안개가 위로 피어오르지 않아 펜을 추가했습니다. <br />

```
def weather_fog():
    global diffuser_status
    while True:
        if diffuser_status == 1:
            GPIO.output(diffuser_pin, True)
            GPIO.output(minifan_pin, True)
        elif diffuser_status == 0:
            GPIO.output(diffuser_pin, False)
            GPIO.output(minifan_pin, False)
        pixels.show()
```

<img width="400" alt="과정샷" src="https://user-images.githubusercontent.com/68539040/174648491-f08e8822-6684-4651-ae46-390cc301d530.png"> <br />

### 미세먼지: <br />
![미먼](https://user-images.githubusercontent.com/68539040/174747297-025ed82c-b0f4-405e-8976-b590bd9364b6.gif) <br /> <br />
받아온 날씨 API를 통해 미세먼지 수치에 따라 LED 색상이 변합니다. (매우나쁨:빨강, 나쁨:노랑, 보통:초록, 좋음:파랑) <br /> <hr />










