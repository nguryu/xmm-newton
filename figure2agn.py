from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=RuntimeWarning)

# Error bars
x = []
y = []
ye = []
y1 = []
y1e = []
# Lists for table data
src_id = []
type = []
u_type = []
vahr14 = []
f14 = []
hr1 = []
hr2 = []
hr3 = []
hr4 = []
e_hr1 = []
e_hr2 = []
e_hr3 = []
e_hr4 = []
# Type lists
s1_hr1 = []
s1_hr2 = []
s1_hr3 = []
s1_hr4 = []
e_s1_hr1 = []
e_s1_hr2 = []
e_s1_hr3 = []
e_s1_hr4 = []
s1n_hr1 = []
s1n_hr2 = []
s1n_hr3 = []
s1n_hr4 = []
e_s1n_hr1 = []
e_s1n_hr2 = []
e_s1n_hr3 = []
e_s1n_hr4 = []
s2_hr1 = []
s2_hr2 = []
s2_hr3 = []
s2_hr4 = []
e_s2_hr1 = []
e_s2_hr2 = []
e_s2_hr3 = []
e_s2_hr4 = []
lin_hr1 = []
lin_hr2 = []
lin_hr3 = []
lin_hr4 = []
e_lin_hr1 = []
e_lin_hr2 = []
e_lin_hr3 = []
e_lin_hr4 = []
bla_hr1 = []
bla_hr2 = []
bla_hr3 = []
bla_hr4 = []
e_bla_hr1 = []
e_bla_hr2 = []
e_bla_hr3 = []
e_bla_hr4 = []
qso_hr1 = []
qso_hr2 = []
qso_hr3 = []
qso_hr4 = []
e_qso_hr1 = []
e_qso_hr2 = []
e_qso_hr3 = []
e_qso_hr4 = []
agn_hr1 = []
agn_hr2 = []
agn_hr3 = []
agn_hr4 = []
e_agn_hr1 = []
e_agn_hr2 = []
e_agn_hr3 = []
e_agn_hr4 = []

with open('plotdata_agn_a_hr', 'r') as data_file:
    for line in data_file:
        li = line.strip()
        if not li.startswith('#'):
            col = line.split(' ')
            src_id.append(col[0])
            type.append(col[1])
            u_type.append(col[2])
            vahr14.append(float(col[3]))
            f14.append(float(col[4]))
            hr1.append(float(col[10]))
            e_hr1.append(float(col[11]))
            hr2.append(float(col[12]))
            e_hr2.append(float(col[13]))
            hr3.append(float(col[14]))
            e_hr3.append(float(col[15]))
            hr4.append(float(col[16]))
            e_hr4.append(float(col[17]))

# Check what object type the source is, and if it is not a candidate.
for i in range(0, len(src_id)):
    if 'S1' in type[i] and 'A' in u_type[i]:
        s1_hr1.append(hr1[i])
        s1_hr2.append(hr2[i])
        s1_hr3.append(hr3[i])
        s1_hr4.append(hr4[i])
        e_s1_hr1.append(e_hr1[i])
        e_s1_hr2.append(e_hr2[i])
        e_s1_hr3.append(e_hr3[i])
        e_s1_hr4.append(e_hr4[i])
    if 'S1n' in type[i] and 'A' in u_type[i]:
        s1n_hr1.append(hr1[i])
        s1n_hr2.append(hr2[i])
        s1n_hr3.append(hr3[i])
        s1n_hr4.append(hr4[i])
        e_s1n_hr1.append(e_hr1[i])
        e_s1n_hr2.append(e_hr2[i])
        e_s1n_hr3.append(e_hr3[i])
        e_s1n_hr4.append(e_hr4[i])
    if 'S2' in type[i] and 'A' in u_type[i]:
        s2_hr1.append(hr1[i])
        s2_hr2.append(hr2[i])
        s2_hr3.append(hr3[i])
        s2_hr4.append(hr4[i])
        e_s2_hr1.append(e_hr1[i])
        e_s2_hr2.append(e_hr2[i])
        e_s2_hr3.append(e_hr3[i])
        e_s2_hr4.append(e_hr4[i])
    if 'LIN' in type[i] and 'A' in u_type[i]:
        lin_hr1.append(hr1[i])
        lin_hr2.append(hr2[i])
        lin_hr3.append(hr3[i])
        lin_hr4.append(hr4[i])
        e_lin_hr1.append(e_hr1[i])
        e_lin_hr2.append(e_hr2[i])
        e_lin_hr3.append(e_hr3[i])
        e_lin_hr4.append(e_hr4[i])
    if 'Bla' in type[i] and 'A' in u_type[i]:
        bla_hr1.append(hr1[i])
        bla_hr2.append(hr2[i])
        bla_hr3.append(hr3[i])
        bla_hr4.append(hr4[i])
        e_bla_hr1.append(e_hr1[i])
        e_bla_hr2.append(e_hr2[i])
        e_bla_hr3.append(e_hr3[i])
        e_bla_hr4.append(e_hr4[i])
    if 'QSO' in type[i] and 'A' in u_type[i]:
        qso_hr1.append(hr1[i])
        qso_hr2.append(hr2[i])
        qso_hr3.append(hr3[i])
        qso_hr4.append(hr4[i])
        e_qso_hr1.append(e_hr1[i])
        e_qso_hr2.append(e_hr2[i])
        e_qso_hr3.append(e_hr3[i])
        e_qso_hr4.append(e_hr4[i])
    if 'AGN' in type[i] and 'A' in u_type[i]:
        agn_hr1.append(hr1[i])
        agn_hr2.append(hr2[i])
        agn_hr3.append(hr3[i])
        agn_hr4.append(hr4[i])
        e_agn_hr1.append(e_hr1[i])
        e_agn_hr2.append(e_hr2[i])
        e_agn_hr3.append(e_hr3[i])
        e_agn_hr4.append(e_hr4[i])

print 'S1', len(s1_hr1)
print 'S1n', len(s1n_hr1)
print 'S2', len(s2_hr1)
print 'LIN', len(lin_hr1)
print 'QSO', len(qso_hr1)
print 'Bla', len(bla_hr1)
print 'AGN', len(agn_hr1)

# Convert from list to array
s1_hr1 = array(s1_hr1)
s1_hr2 = array(s1_hr2)
s1_hr3 = array(s1_hr3)
s1_hr4 = array(s1_hr4)
e_s1_hr1 = array(e_s1_hr1)
e_s1_hr2 = array(e_s1_hr2)
e_s1_hr3 = array(e_s1_hr3)
e_s1_hr4 = array(e_s1_hr4)
s1n_hr1 = array(s1n_hr1)
s1n_hr2 = array(s1n_hr2)
s1n_hr3 = array(s1n_hr3)
s1n_hr4 = array(s1n_hr4)
e_s1n_hr1 = array(e_s1n_hr1)
e_s1n_hr2 = array(e_s1n_hr2)
e_s1n_hr3 = array(e_s1n_hr3)
e_s1n_hr4 = array(e_s1n_hr4)
s2_hr1 = array(s2_hr1)
s2_hr2 = array(s2_hr2)
s2_hr3 = array(s2_hr3)
s2_hr4 = array(s2_hr4)
e_s2_hr1 = array(e_s2_hr1)
e_s2_hr2 = array(e_s2_hr2)
e_s2_hr3 = array(e_s2_hr3)
e_s2_hr4 = array(e_s2_hr4)
lin_hr1 = array(lin_hr1)
lin_hr2 = array(lin_hr2)
lin_hr3 = array(lin_hr3)
lin_hr4 = array(lin_hr4)
e_lin_hr1 = array(e_lin_hr1)
e_lin_hr2 = array(e_lin_hr2)
e_lin_hr3 = array(e_lin_hr3)
e_lin_hr4 = array(e_lin_hr4)
bla_hr1 = array(bla_hr1)
bla_hr2 = array(bla_hr2)
bla_hr3 = array(bla_hr3)
bla_hr4 = array(bla_hr4)
e_bla_hr1 = array(e_bla_hr1)
e_bla_hr2 = array(e_bla_hr2)
e_bla_hr3 = array(e_bla_hr3)
e_bla_hr4 = array(e_bla_hr4)
qso_hr1 = array(qso_hr1)
qso_hr2 = array(qso_hr2)
qso_hr3 = array(qso_hr3)
qso_hr4 = array(qso_hr4)
e_qso_hr1 = array(e_qso_hr1)
e_qso_hr2 = array(e_qso_hr2)
e_qso_hr3 = array(e_qso_hr3)
e_qso_hr4 = array(e_qso_hr4)
agn_hr1 = array(agn_hr1)
agn_hr2 = array(agn_hr2)
agn_hr3 = array(agn_hr3)
agn_hr4 = array(agn_hr4)
e_agn_hr1 = array(e_agn_hr1)
e_agn_hr2 = array(e_agn_hr2)
e_agn_hr3 = array(e_agn_hr3)
e_agn_hr4 = array(e_agn_hr4)

# =========== Graph Set-up ========== #
# Figure size
xr = 4.
yr = 8.
fig = plt.figure(figsize = (xr, yr)) # (width, height)
# Font size
SMALL_SIZE = 8
MEDIUM_SIZE = 12
LARGE_SIZE = 16
plt.rc('font', size = SMALL_SIZE)          # Controls default text sizes
plt.rc('axes', titlesize = LARGE_SIZE)    # Font size of the axes title
plt.rc('axes', labelsize = SMALL_SIZE)     # Font size of the x and y labels
plt.rc('xtick', labelsize = SMALL_SIZE)    # Font size of the tick labels
plt.rc('ytick', labelsize = SMALL_SIZE)    # Font size of the tick labels
plt.rc('legend', fontsize = SMALL_SIZE)    # Legend font size
# Axes ticks
majorFormatter = FormatStrFormatter('%1.1f')
majorLocator = MultipleLocator(0.5)  # Major tick intervals
minorLocator = MultipleLocator(0.1)  # Minor tick intervals

# ========== Subplot 1 ========== #
sub1 = plt.subplot(311)
sub1.set_position([0.25, 0.15+2/yr+2/yr, 2/xr, 2/yr])  # (left, bottom, width, height)
# Axes parameters
sub1.set_xlim([-1.1, 1.1])
sub1.set_ylim([-1.1, 1.1])
plt.setp(sub1.get_xticklabels(), visible = False)
plt.setp(sub1.get_yticklabels(), visible = False)
sub1.text(-1.45, 0, 'HR4', rotation = 90)
sub1.text(0.6, -1.0, 'HR3')
sub1.text(-1.275, -1.05, '-1', rotation = 90)
sub1.text(-1.275, -0.46, '-0.5', rotation = 90)
sub1.text(-1.275, -0.06,  '0', rotation = 90)
sub1.text(-1.275, 0.5,  '0.5', rotation = 90)
sub1.text(-1.275, 0.95, '1', rotation = 90)
# Set tick marks
sub1.yaxis.set_major_formatter(majorFormatter)
sub1.yaxis.set_major_locator(majorLocator)
sub1.yaxis.set_minor_locator(minorLocator)
# Graph parameters
sub1.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
t = where((e_s1_hr3 <= 0.1) & (e_s1_hr4 <= 0.1))[0]
plt.scatter(s1_hr3[t], s1_hr4[t], color = '#FF0000', marker = '^', s = 5, label = 'SY1')
t = where((e_s1n_hr3 <= 0.1) & (e_s1n_hr4 <= 0.1))[0]
plt.scatter(s1n_hr3[t], s1n_hr4[t], color = '#01DF74', marker = 'v', s = 5, label = 'SY1n')
t = where((e_s2_hr3 <= 0.1) & (e_s2_hr4 <= 0.1))[0]
plt.scatter(s2_hr3[t], s2_hr4[t], color = '#08088A', marker = ',', s = 5, label = 'SY2')
t = where((e_lin_hr3 <= 0.1) & (e_lin_hr4 <= 0.1))[0]
plt.scatter(lin_hr3[t], lin_hr4[t], color = '#FE2EC8', marker = '*', s = 5, label = 'LIN')
t = where((e_bla_hr3 <= 0.1) & (e_bla_hr4 <= 0.1))[0]
plt.scatter(bla_hr3[t], bla_hr4[t], color = '#000000', marker = 'o', s = 5, label = 'Bla')
t = where((e_qso_hr3 <= 0.1) & (e_qso_hr4 <= 0.1))[0]
plt.scatter(qso_hr3[t], qso_hr4[t], color = '#BF00FF', marker = 'D', s = 5, label = 'QSO')
t = where((e_agn_hr3 <= 0.1) & (e_agn_hr4 <= 0.1))[0]
plt.scatter(agn_hr3[t], agn_hr4[t], color = '#AEB404', marker = 'h', s = 5, label = 'AGN')

# ========== Subplot 2 ========== #
sub2 = plt.subplot(312, sharex = sub1)
sub2.set_position([0.25, 0.15+2/yr, 2/xr, 2/yr])
# Axes parameters
sub2.set_xlim([-1.1, 1.1])
sub2.set_ylim([-1.1, 1.1])
plt.setp(sub2.get_xticklabels(), visible = False)
plt.setp(sub2.get_yticklabels(), visible = False)
sub2.text(-1.45, 0, 'HR3', rotation = 90)
sub2.text(0.6, -1.0, 'HR2')
sub2.text(-1.275, -1.05, '-1', rotation = 90)
sub2.text(-1.275, -0.46, '-0.5', rotation = 90)
sub2.text(-1.275, -0.06,  '0', rotation = 90)
sub2.text(-1.275, 0.5,  '0.5', rotation = 90)
sub2.text(-1.275, 0.95, '1', rotation = 90)
# Set tick marks
sub2.yaxis.set_major_formatter(majorFormatter)
sub2.yaxis.set_major_locator(majorLocator)
sub2.yaxis.set_minor_locator(minorLocator)
# Graph parameters
sub2.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
t = where((e_s1_hr2 <= 0.1) & (e_s1_hr3 <= 0.1))[0]
plt.scatter(s1_hr2[t], s1_hr3[t], color = '#FF0000', marker = '^', s = 5, label = 'SY1')
t = where((e_s1n_hr2 <= 0.1) & (e_s1n_hr3 <= 0.1))[0]
plt.scatter(s1n_hr2[t], s1n_hr3[t], color = '#01DF74', marker = 'v', s = 5, label = 'SY1n')
t = where((e_s2_hr2 <= 0.1) & (e_s2_hr3 <= 0.1))[0]
plt.scatter(s2_hr2[t], s2_hr3[t], color = '#08088A', marker = ',', s = 5, label = 'SY2')
t = where((e_lin_hr2 <= 0.1) & (e_lin_hr3 <= 0.1))[0]
plt.scatter(lin_hr2[t], lin_hr3[t], color = '#FE2EC8', marker = '*', s = 5, label = 'LIN')
t = where((e_bla_hr2 <= 0.1) & (e_bla_hr3 <= 0.1))[0]
plt.scatter(bla_hr2[t], bla_hr3[t], color = '#000000', marker = 'o', s = 5, label = 'Bla')
t = where((e_qso_hr2 <= 0.1) & (e_qso_hr3 <= 0.1))[0]
plt.scatter(qso_hr2[t], qso_hr3[t], color = '#BF00FF', marker = 'D', s = 5, label = 'QSO')
t = where((e_agn_hr2 <= 0.1) & (e_agn_hr3 <= 0.1))[0]
plt.scatter(agn_hr2[t], agn_hr3[t], color = '#AEB404', marker = 'h', s = 5, label = 'AGN')

# ========== Subplot 3 ========== #
sub3 = plt.subplot(313, sharex = sub1)
sub3.set_position([0.25, 0.15, 2/xr, 2/yr])
# Axes parameters
sub3.set_xlim([-1.1, 1.1])
sub3.set_ylim([-1.1, 1.1])
plt.setp(sub3.get_xticklabels(), visible = False)
plt.setp(sub3.get_yticklabels(), visible = False)
sub3.text(-1.45, 0, 'HR2', rotation = 90)
sub3.text(0.6, -1.0, 'HR1')
sub3.text(-1.05, -1.275, '-1')
sub3.text(-0.65, -1.275, '-0.5')
sub3.text(-0.02, -1.275, '0')
sub3.text(0.42, -1.275, '0.5')
sub3.text(1.0, -1.275, '1')
sub3.text(-1.275, -1.05, '-1', rotation = 90)
sub3.text(-1.275, -0.46, '-0.5', rotation = 90)
sub3.text(-1.275, -0.06,  '0', rotation = 90)
sub3.text(-1.275, 0.5,  '0.5', rotation = 90)
sub3.text(-1.275, 0.95, '1', rotation = 90)
# Set tick marks
sub3.xaxis.set_major_formatter(majorFormatter)
sub3.yaxis.set_major_formatter(majorFormatter)
sub3.xaxis.set_major_locator(majorLocator)
sub3.xaxis.set_minor_locator(minorLocator)
sub3.yaxis.set_major_locator(majorLocator)
sub3.yaxis.set_minor_locator(minorLocator)
# Graph parameters
sub3.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
t = where((e_s1_hr1 <= 0.1) & (e_s1_hr2 <= 0.1))[0]
plt.scatter(s1_hr1[t], s1_hr2[t], color = '#FF0000', marker = '^', s = 5, label = 'SY1')
t = where((e_s1n_hr1 <= 0.1) & (e_s1n_hr2 <= 0.1))[0]
plt.scatter(s1n_hr1[t], s1n_hr2[t], color = '#01DF74', marker = 'v', s = 5, label = 'SY1n')
t = where((e_s2_hr1 <= 0.1) & (e_s2_hr2 <= 0.1))[0]
plt.scatter(s2_hr1[t], s2_hr2[t], color = '#08088A', marker = ',', s = 5, label = 'SY2')
t = where((e_lin_hr1 <= 0.1) & (e_lin_hr2 <= 0.1))[0]
plt.scatter(lin_hr1[t], lin_hr2[t], color = '#FE2EC8', marker = '*', s = 5, label = 'LIN')
t = where((e_bla_hr1 <= 0.1) & (e_bla_hr2 <= 0.1))[0]
plt.scatter(bla_hr1[t], bla_hr2[t], color = '#000000', marker = 'o', s = 5, label = 'Bla')
t = where((e_qso_hr1 <= 0.1) & (e_qso_hr2 <= 0.1))[0]
plt.scatter(qso_hr1[t], qso_hr2[t], color = '#BF00FF', marker = 'D', s = 5, label = 'QSO')
t = where((e_agn_hr1 <= 0.1) & (e_agn_hr2 <= 0.1))[0]
plt.scatter(agn_hr1[t], agn_hr2[t], color = '#AEB404', marker = 'h', s = 5, label = 'AGN')
lgnd1 = plt.legend(loc = 'upper left', scatterpoints = 1, fontsize = 6)
lgnd1.get_frame().set_linewidth(0.0)

# ========== Output ========== #
fig.savefig('fig2agn.eps',format = 'eps', bbox_inches = 'tight', pad_inches = 0.02, dpi = 1000)