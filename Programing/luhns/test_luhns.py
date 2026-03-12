import pandas as pd
from luhns import checks

data = pd.read_csv("data.csv")
data["number"] = data["number"].astype(str)

for check_digit in checks:
    result = data["number"].apply(check_digit) == data["is_valid"]
    per = (result.sum() / result.shape[0]) * 100
    name = f"result_{check_digit.__name__}"
    data[name] = result

    print(data[["number", name]])
    print("The sucess percent for {} is :".format(name), per)


data.to_csv("Results.csv", index=False,header=True)
