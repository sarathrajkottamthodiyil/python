import pandas as pd

dict = {"country": ["brazil", "india", "china", "south africa"],
        "capital": ["brasilia", "moscow", "delhi", "beiging", "pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98] }
# import pandas as pd
brics = pd.DataFrame(dict)
print(brics)