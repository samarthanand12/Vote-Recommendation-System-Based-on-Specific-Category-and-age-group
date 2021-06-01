import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

file = pd.read_csv('hackathondataset_jaano_india.csv')


print(file.head())

print(file['State'].value_counts())
a=file.columns.tolist()[3:]
print(a)
# sample='Villages with Primary Health Centre within 10km (%) DLHS-4'
sample='Sex Ratio (Number of females per 1000 males)'
# # print(file.sort_values(by=sample, ascending = True)[[sample,"District"]].ne(0).head(10))
# # print(file[~file[sample].isin(["NaN"])][sample].max())
# print((file.sort_values(by=sample, ascending=False)[:100])[[sample,"District"]])
# # print(file.[sample])
# print(file[file[sample] == x]['Value'])

# file[sample] = pd.to_numeric(file[sample])

# s=file[sample].tolist()
# s.sort()
# count=s.count("0")
# print(s)
"""
graph=file.nlargest(10, [sample])[[sample,"District"]]
print(graph[[sample,"District"]])
list1 = graph["District"].tolist()
list2 = graph[sample].tolist()
print(list1,list2)

x_pos = [i for i, _ in enumerate(list1)]

plt.bar(x_pos, list2, align='center',color="green")
plt.xticks(x_pos, list1,fontsize=8,rotation=20)
plt.ylabel('Area wise Value')
plt.xlabel("State wise District")
plt.title(sample)

plt.show()
"""

# graph2=file.nsmallest(50,60,[sample])[[sample,"District"]]
graph2=file.sort_values(sample, ascending = True)[[sample,"District"]]
list2=graph2[sample].tolist()
list1=graph2["District"].tolist()
print(list2)
z=list2.count(0)
list2=list2[z:z+10]
list1=list1[z:z+10]
print(list2,list1)



x_pos = [i for i, _ in enumerate(list1)]

plt.bar(x_pos, list2, align='center',color="green")
plt.xticks(x_pos, list1,fontsize=8,rotation=20)
plt.ylabel('Area wise Value')
plt.xlabel("State wise District")
plt.title(sample)

plt.show()

# graph.plot(x=graph.sample,kind='barh')
# plt.show()