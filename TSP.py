from scipy.optimize import linprog
import numpy as np

# Grafikteki noktaların koordinatları
points = [(0, 0), (1, 1), (2, 2), (3, 3)]

# Her noktadan diğerine olan mesafeler
distances = [[0, 1, 2, 3], [1, 0, 1, 2], [2, 1, 0, 1], [3, 2, 1, 0]]

# Her noktanın bir kez ziyaret edilmesini istediğimizi belirten bir boole dizisi
visited = [1, 1, 1, 1]

# Ağırlıkların sınırları
bounds = list(zip([0]*len(points), visited))

# Hedef fonksiyonumuz (toplam mesafe)
c = [-1*sum(distances[i]) for i in range(len(points))]

# Kısıtlamalarımız
A = []
b = []
for i in range(len(points)):
   row = [0]*len(points)
   row[i] = 1
   A.append(row)
   b.append(1)

res = linprog(c, A_ub=np.array(A), b_ub=np.array(b), bounds=bounds, method='highs')

print('En kısa yol: ', res.success)
print('Toplam mesafe: ', -res.fun)
