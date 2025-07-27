import pandas as pd
from scipy import stats
from math import sqrt, factorial

def S(group):
    mean = group['extent'].mean()
    sum = 0;
    for i in range(len(group['extent'])):
        sum += (group['extent'].iloc[i]-mean)**2
    return sum

# уровень доверия 95%
level_trust = 0.95


data = pd.read_csv('data.csv', header=None, names=['var','name', 'extent'])
mask = data['var'].values == 8
pl = data[mask]
group_data = pl.groupby('name')
planets = list(group_data.groups.keys())
N=0

for n in planets:
    mask = pl['name'].values == n
    group_name = pl[mask]
    mean_X = group_name['extent'].mean()
    N = len(group_name['extent'])
    t = stats.t.ppf((level_trust+1)/2, N - 1)
    tl=stats.t.ppf(level_trust, N - 1)
    chi1 = stats.chi2.ppf((1-level_trust)/2,N-1)
    chi0 = stats.chi2.ppf((1+level_trust)/2,N-1)
    chi = stats.chi2.ppf(1-level_trust,N-1)
    
    #доверительный интервал для среднего
    left_for_mean = mean_X - (t*sqrt(S(group_name)/(N-1)))/(sqrt(N))
    right_for_mean = mean_X + (t*sqrt(S(group_name)/(N-1)))/(sqrt(N))
    #print(t, mean_X, sqrt(S(group_name)/(N-1)), sqrt(N))

    LEFT_for_mean = mean_X - (tl*sqrt(S(group_name)/(N-1)))/(sqrt(N))
    
    c=sqrt(N/(N+1))
    
    right_for_x = mean_X + (t*sqrt(S(group_name)/(N-1)))/c
    left_for_x = mean_X - (t*sqrt(S(group_name)/(N-1)))/c

    #доверительный интервал для дисперсии
    right_for_disp = S(group_name)/chi1
    left_for_disp = S(group_name)/chi0

    RIGHT_for_disp = S(group_name)/chi

    print("Планета:  ", n)
    print("Оценка мат. ожидания: ", format(mean_X, '.4f'), " | Оценка дисперсии: ", format(S(group_name)/(N-1),'.4f'))
    print("Среднее. Уровень доверия 0.95:")
    print("Центр. интервал ", [format(float(left_for_mean), '.4f'), format(float(right_for_mean), '.4f')], " | Прав. интервал: ",[format(float(LEFT_for_mean),'.4f'),"inf"])

    print("Дисперсия. Уровень доверия 0.95:")
    print("Центр. интервал ", [format(float(left_for_disp), '.4f'), format(float(right_for_disp), '.4f')]," | Прав. интервал: ",[0, format(float(RIGHT_for_disp),'.4f')])
    print("Оценка будущего значения с вероятностью 0.95: ", [format(float(left_for_x),".4f"),format(float(right_for_x),".4f")])
    print()

# уровень доверия 99%
level_trust = 0.99


for n in planets:
    mask = pl['name'].values == n
    group_name = pl[mask]
    mean_X = group_name['extent'].mean()
    N = len(group_name['extent'])
    t = stats.t.ppf((level_trust+1)/2, N-1)
    tl = stats.t.ppf(level_trust, N-1)
    chi1 = stats.chi2.ppf((1-level_trust)/2,N-1)
    chi0 = stats.chi2.ppf((1+level_trust)/2,N-1)
    chi = stats.chi2.ppf(1-level_trust,N-1)
    
    #доверительный интервал для среднего
    right_for_mean = mean_X + (t*sqrt(S(group_name)/(N-1)))/(sqrt(N))
    left_for_mean = mean_X - (t*sqrt(S(group_name)/(N-1)))/(sqrt(N))

    LEFT_for_mean = mean_X - (tl*sqrt(S(group_name)/(N-1)))/(sqrt(N))

    #доверительный интервал для дисперсии
    right_for_disp = S(group_name)/chi1
    left_for_disp = S(group_name)/chi0

    RIGHT_for_disp = S(group_name)/chi

    print("Планета:  ", n)
    print("Оценка мат. ожидания: ", format(mean_X, '.4f'), " | Оценка дисперсии: ", format(S(group_name)/(N-1),'.4f'))
    print("Среднее. Уровень доверия 0.99:")
    print("Центр. интервал ", [format(float(left_for_mean), '.4f'), format(float(right_for_mean), '.4f')], " | Прав. интервал: ",[format(float(LEFT_for_mean),'.4f'),"inf"])

    print("Дисперсия. Уровень доверия 0.99:")
    print("Центр. интервал ", [format(float(left_for_disp), '.4f'), format(float(right_for_disp), '.4f')]," | Прав. интервал: ",[0, format(float(RIGHT_for_disp),'.4f')])
    print()




