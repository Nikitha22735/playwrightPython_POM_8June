
from playwright.sync_api import expect, Page, sync_playwright
import time

def getapi(playwright: sync_playwright):
    context = playwright.request.new_context(http_credentails={"username":"admin", "password": "pw"})
    # respBody = context.get("https://dummyjson.com/products", headers={"Autherization":"Bearer 12345"})
    # respBody = context.get("https://dummyjson.com/products", headers={"x-api-key":"12345"})
    respBody = context.get("https://dummyjson.com/products", form={"grant_type":"client_credentials","client_Id":"gfjdhgfj", "client_secret":"gfkjhf"})
    # print(respBody.json())
    response_json = respBody.json()
    assert respBody.status == 200
    print(response_json["products"][0]["title"])
    # assert response_json["products"][0]["title"]=="iphone"

def test_postApi(playwright: sync_playwright):
    context = playwright.request.new_context() 
    requestBody ={
        "title": "iphone",
        "price": 12.99
    }
    strtTime = time.perf_counter()
    respBody = context.post("https://dummyjson.com/products/add", data=requestBody)
    endtTime = time.perf_counter()
    response_json = respBody.json()
    assert respBody.status == 201
    print(response_json)
    assert response_json["title"]=="iphone"
    print(endtTime-strtTime)
    assert endtTime-strtTime<1
