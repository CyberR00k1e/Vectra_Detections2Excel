import requests
import pandas as pd
import openpyxl

vectra_rest_API_token="enter the Vectra token"
response = requests.get(url="https://demo.vectra.io/api/v2.3/detections",headers={"Authorization": vectra_rest_API_token}).json()
test=(response["results"])
len = len(test)


for i in range(len):
    df = pd.DataFrame(test).to_excel("test.xlsx")

