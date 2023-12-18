import requests
import json
# import html
from fastapi import FastAPI  # , Request
# from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()


"""@app.middleware("http")
async def redirect_to_https(request: Request, call_next):
    if not request.url.scheme == "https":
        url = request.url.replace(scheme="https")
        return RedirectResponse(url=url)

    return await call_next(request)"""


@app.get("/")
def get_hello():
    return {"message": "New mes* #*  "}


def send_get_request(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            answer = json.loads(response.text)
            # answer["data"]["answer"] = "упс"
            # print(answer["data"]["answer"])
            """answer["data"]["replies"] = map(
                lambda el: el["text"].encode('utf-8').decode('unicode-escape'),
                answer["data"]["replies"])"""
            print("Ответ:")
            print(answer)
        else:
            print(f"Ошибка при запросе: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")


if __name__ == '__main__':
    # Пример URL для GET-запроса
    # url = 'https://bot.jaicp.com/chatapi/pTkdWLRY:c0b87539a53a1ec0334bac00041bb7881d76518e?clientId=test&query=/start'

    # Вызов функции для отправки GET-запроса и вывода ответа
    # send_get_request(url)
    uvicorn.run(app, host="0.0.0.0", port=8000)  # , ssl_keyfile="key.pem", ssl_certfile="cert.pem")
