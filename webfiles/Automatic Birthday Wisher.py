import pandas as pd
import datetime

Gamil_ID = ""
Gamil_PSWD = ""
def sendEmail(to,sub,msg):
    pass

if __name__ == "__main__":
    path = (r"../docs/data.xlsx")
    df = pd.read_excel(path)
    # print(df)
    YearNow = datetime.datetime.now().strftime("%Y")
    writeIND = []
    today = datetime.datetime.now().strftime("%d-%m")
    for index, item in df.iterrows():
        bday = item["Birthday"].strftime("%d-%m")
        if (today == bday) and YearNow not in str(item["Year"]):
            sendEmail(item["Email"],"Happy Birthday",item["Dialogue"])
            writeIND.append(index)
    if writeIND == None:
        for i in writeIND:
            yr = df.loc[i,"Year"]
            df.loc[i,"Year"] = str(yr) + "," + str(YearNow)
            df.to_excel(r"../docs/data.xlsx",index=False)


