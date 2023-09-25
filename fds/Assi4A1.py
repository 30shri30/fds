import numpy as np
import matplotlib.pyplot as p
np.random.seed(42)
random_data=np.random.randint(1,100,50)
fig,axs=p.subplots(2,2,figsize=(12,8))
fig.suptitle("random integer data visualization")
axs[0,0].plot(random_data,color='b',marker='o',linestyle='-')
axs[0,0].set_title("line chart")
axs[0,0].set_xlabel("index")
axs[0,0].set_ylabel("value")

axs[0,1].scatter(range(50),random_data,color='g',marker='x')
axs[0,1].set_title("scatter plot")
axs[0,1].set_xlabel("index")
axs[0,1].set_ylabel("value")

axs[1,0].hist(random_data,bins=10,color='r',alpha=0.7)
axs[1,0].set_title("histogram ")
axs[1,0].set_xlabel("value")
axs[1,0].set_ylabel("freqyency")

axs[1,1].boxplot(random_data,vert=False,patch_artist=True,boxprops=dict(facecolor='yellow'))
axs[1,1].set_title("Box plot")
p.tight_layout(rect=[0,0,1,0.95])
p.show()
