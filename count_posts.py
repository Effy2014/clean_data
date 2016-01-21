import pandas as pd 
import numpy as np
from datetime import datetime

post = pd.read_csv("/Users/XW/Desktop/GoEnnounce/posts.csv", header = 0)
post["Post Date"] = pd.to_datetime(post["Post Date"])
post[["ID", "Post Date"]].groupby(["Post Date"]).count().reset_index()