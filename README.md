# Weather Stone๐ฎ

> **'Weather Stone'** ์ ์์ ์์ ๋ค์ํ ๋ ์จ(โ๏ธ, โ๏ธ, โก๏ธ)์ ์ฌํํ  ์ ์๋ ๋์คํ๋ ์ด์๋๋ค. <br />
> ์ข์ํ๋ ์๊ฐ, ์ข์ํ๋ ์ฅ์์ ํ๋์ ๋ฐฉ์ผ๋ก ๊ฐ์ ธ์ฌ ์ ์๊ณ , ์ผ๊ธฐ ์๋ณด๋ฅผ ํตํด ๋ด์ผ์ ํ๋์ ํ๊ด ์์ ๋ ์ ์์ต๋๋ค. <br /> <br />
<img width="400" alt="แแฐแแฅแแณแแฉแซ" src="https://user-images.githubusercontent.com/68539040/174648010-8c14b96d-2b94-4655-b1ac-c46e6902506b.png"> <br />
<br />


๋ณธ์ฒด, ์น ์ดํ๋ฆฌ์ผ์ด์, ์๋ฒ ์ด ์ธ ๋ถ๋ถ์ผ๋ก ๊ตฌ์ฑ๋์ด ์์ต๋๋ค. <br />
์์๋ ํฌ๋ช ์ํฌ๋ฆด๊ณผ ์ฌ๋ฌ๊ฐ์ง ๋ชจ๋(LED, ์ด์ํ ๊ฐ์ต๊ธฐ, ํํ ๋ฑ) ๊ทธ๋ฆฌ๊ณ  ๋ผ์ฆ๋ฒ ๋ฆฌํ์ด 4๋ก ๊ตฌ์ฑ๋์ด ์์ต๋๋ค. <br />
์น ์ดํ๋ฆฌ์ผ์ด์์ ์ฌ์ฉ์ ์์น์ ๋ ์จ API์ ๋ฏธ์ธ๋จผ์ง API๋ฅผ ๋ฐ์์ค๊ณ , javascript, html๋ฅผ ์ฌ์ฉํด ์ฌ์ฉ์๊ฐ LED ์์ ์ง์ ํ  ์ ์๋ UI์ ๊ธฐ๋ฅ์ ๊ฐ๋ฐํ์ต๋๋ค.
<br /> <br />


### ๋น์ค๋ ๋ :  <br />
![แแต](https://user-images.githubusercontent.com/68539040/174646752-c75f19e2-433b-4764-81eb-05aa37f2459b.gif) <br /> <br />
**๊ตฌํ** <br />
![์์๊ตฌ์ฑ๋](https://user-images.githubusercontent.com/68539040/174644707-e0a2c088-b679-460c-a73d-dc3391e092d2.png) <br />
ํํ ๋ชจ๋๊ณผ ํ๋ธ๋ก ๋ฌผ์ ๋์ด์ฌ๋ฆฌ๊ณ , ํ๋ธ์ ์ ์ ํ ๊ตฌ๋ฉ์ ๋ซ์ด ๋น๋ฅผ ํํํ์ต๋๋ค. <br />

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


### ๋ฒ๊ฐ:  <br />
![๋ฒ๊ฐ](https://user-images.githubusercontent.com/68539040/174645794-2a94f252-e9e6-488f-b495-889318f5778c.gif) <br /> <br />
์ต์, ์ต๋ ๋๋ค ์๊ฐ๊ณผ ๋๋ค sleep time์ ์ ์ํ์ฌ ๋ฒ๊ฐ๋ฅผ ํํํ์ต๋๋ค.  <br />

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



### ์๊ฐ:  <br />
![แแกแซแแข](https://user-images.githubusercontent.com/68539040/174647819-57f8f9de-6f4b-4f30-a36c-f222d2d8ed04.gif) <br /> <br />
๋ฐ์์จ ๋ ์จ ์ ๋ณด๊ฐ '์๊ฐ'์ผ๋, ์ด์ํ ๊ฐ์ต๊ธฐ ๋ชจ๋๊ณผ ํ ๋ชจ๋์ ๊ฐ๋ํฉ๋๋ค. <br />
๊ฐ์ต๊ธฐ๋ง ๊ฐ๋ํ๋ ์๊ฐ๊ฐ ์๋ก ํผ์ด์ค๋ฅด์ง ์์ ํ์ ์ถ๊ฐํ์ต๋๋ค. <br />

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

<img width="400" alt="แแชแแฅแผแแฃแบ" src="https://user-images.githubusercontent.com/68539040/174648491-f08e8822-6684-4651-ae46-390cc301d530.png"> <br />

### ๋ฏธ์ธ๋จผ์ง: <br />
![แแตแแฅแซ](https://user-images.githubusercontent.com/68539040/174747297-025ed82c-b0f4-405e-8976-b590bd9364b6.gif) <br /> <br />
๋ฐ์์จ ๋ ์จ API๋ฅผ ํตํด ๋ฏธ์ธ๋จผ์ง ์์น์ ๋ฐ๋ผ LED ์์์ด ๋ณํฉ๋๋ค. (๋งค์ฐ๋์จ:๋นจ๊ฐ, ๋์จ:๋ธ๋, ๋ณดํต:์ด๋ก, ์ข์:ํ๋) <br /> <hr />










