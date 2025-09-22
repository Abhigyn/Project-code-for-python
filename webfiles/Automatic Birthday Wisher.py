import pandas as pd
import datetime



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


