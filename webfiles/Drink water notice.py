import time
from plyer import notification

if __name__ == "__main__":
    while True:
     notification.notify(
        title="Please drink water Now!!",
        message=(
            "The National Academies of Sciences, Engineering and Medicine determined that "
            "an adequate daily fluid intake is: "
            "About 15.5 cups (3.7 liters) of fluids for men. "
            "About 11.5 cups (2.7 liters) of fluids for women."
        ),
        app_icon=r"I:\Study\Golu lession\Python      Projects\images\icon.ico",  
        timeout=5
    )
     time.sleep(60*15)

