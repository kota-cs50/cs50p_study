def main():
    time = input("What time is it? ")
    calc_time = convert(time)

    meal_time = None
    if 7.0 <= calc_time <= 8.0:
        meal_time = "breakfast time"
    elif 12.0 <= calc_time <= 13.0:
        meal_time = "lunch time"
    elif 18.0 <= calc_time <= 19.0:
        meal_time = "dinner time"

    if meal_time:
        print(meal_time)

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/ 60


if __name__ == "__main__":
    main()
