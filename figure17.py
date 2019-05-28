from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Initialize lists to store data in.
x = []
y = []
ye = []
y1 = []
y1e = []
src_id = []
type = []
f14_max = []
var14 = []
det_no = []
x_ir = []
xir_cp = []
x_o = []
xo_cp = []
# Stars
star_xo = []
star_xir = []
star_xo_cp = []
star_xir_cp = []
# Galaxies
sy1n_xo = []
sy1n_xir = []
sy1_xo = []
sy1_xir = []
sy2_xo = []
sy2_xir = []
lin_xo = []
lin_xir = []
bla_xo = []
bla_xir = []
qso_xo = []
qso_xir = []
agn_xo = []
agn_xir = []
# Compact objects
bhb_xo = []
bhb_xir = []
bstr_xo = []
bstr_xir = []
apsr_xo = []
apsr_xir = []
rpsr_xo = []
rpsr_xir = []
ins_xo = []
ins_xir = []
mgr_xo = []
mgr_xir = []
cv_xo = []
cv_xir = []

# Read in file and add file elements into lists.
with open('plotdata_star_a_var', 'r') as data_file:
    for line in data_file:
        li = line.strip()
        if not li.startswith('#'):
            col = line.split(' ')
            src_id.append(col[0])
            f14_max.append(float(col[2]))
            var14.append(float(col[3]))
            det_no.append(int(col[4]))
            x_ir.append(float(col[5]))
            xir_cp.append(col[6])
            x_o.append(float(col[7]))
            xo_cp.append(col[8])

# Add x_o and x_ir into respective classification lists
for i in range(0, len(src_id)):
    if det_no[i] > 1:
        star_xo.append(x_o[i])
        star_xir.append(x_ir[i])
        # Find sources that do not have optical or IR counterparts
        if 'N' in xo_cp[i] or 'N' in xir_cp[i]:
            star_xo_cp.append(x_o[i])
            star_xir_cp.append(x_ir[i])

# ========== Graph Set-up ========== #
# Figure size
xr = 7.
yr = 3.
fig = plt.figure(figsize = (xr, yr))  # (width, height)
# Font size
SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12
plt.rc('font', size = SMALL_SIZE)          # Controls default text sizes
plt.rc('axes', titlesize = BIGGER_SIZE)    # Font size of the axes title
plt.rc('axes', labelsize = SMALL_SIZE)     # Font size of the x and y labels
plt.rc('xtick', labelsize = SMALL_SIZE)    # Font size of the tick labels
plt.rc('ytick', labelsize = SMALL_SIZE)    # Font size of the tick labels
plt.rc('legend', fontsize = SMALL_SIZE)    # Legend font size
# Axes ticks
majorFormatter = FormatStrFormatter('%1.0f')
majorLocator = MultipleLocator(2)    # Major tick intervals
minorLocator = MultipleLocator(0.5)  # Minor tick intervals

# ========== Subplot 1 ========== #
sub1 = plt.subplot(131)
sub1.set_position([0.09, 0.2, 2/xr, 2/yr])
# Axes parameters
sub1.set_xlim([-7, 5])
sub1.set_ylim([-7, 5])
plt.yticks(rotation = 90)
plt.setp(sub1.get_xticklabels(), visible = True)
plt.setp(sub1.get_yticklabels(), visible = True)
sub1.text(-9, 0, '$\mathregular{log(F_{X}/F_{IR})}$', rotation = 90)
sub1.text(-2.5, -9, '$\mathregular{log(F_{X}/F_{O})}$')
# Set tick marks
sub1.yaxis.set_major_formatter(majorFormatter)
sub1.yaxis.set_major_locator(majorLocator)
sub1.yaxis.set_minor_locator(minorLocator)
# Graph parameters
sub1.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(star_xo, star_xir, color = '#08088A', marker = ',', s = 3, label = 'Star')
plt.scatter(star_xo_cp, star_xir_cp, facecolors = 'None', edgecolors = '#08088A', linewidth = 0.5, s = 25)  # Point out sources without optical and IR counterparts
lgnd1 = plt.legend(loc = 'upper left', scatterpoints = 1, fontsize = 5)
lgnd1.get_frame().set_linewidth(0.0)

# ========== Subplot 2 ========== #
sub2 = plt.subplot(132, sharey = sub1)
sub2.set_position([0.09+2/xr, 0.2, 2/xr, 2/yr])
# Axes parameters
sub2.set_xlim([-7, 5])
sub2.set_ylim([-7, 5])
plt.setp(sub2.get_xticklabels(), visible = True)
plt.setp(sub2.get_yticklabels(), visible = False)
sub2.text(-2.5, -9, '$\mathregular{log(F_{X}/F_{O})}$')
# Set tick marks
sub2.yaxis.set_major_formatter(majorFormatter)
sub2.yaxis.set_major_locator(majorLocator)
sub2.yaxis.set_minor_locator(minorLocator)
# Graph parameters
sub2.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(agn_xo, agn_xir, color = '#FF0000', marker = '^', s = 3, label = 'AGN')
plt.scatter(sy1n_xo, sy1n_xir, color = '#AEB404', marker = '*', s = 3, label = 'G')
lgnd2 = plt.legend(loc = 'upper left', scatterpoints = 1, fontsize = 5)
lgnd2.get_frame().set_linewidth(0.0)

# ========== Subplot 3 ========== #
sub3 = plt.subplot(133, sharey = sub1)
sub3.set_position([0.09+2/xr+2/xr, 0.2, 2/xr, 2/yr])
# Axes parameters
sub3.set_xlim([-7, 5])
sub3.set_ylim([-7, 5])
plt.setp(sub3.get_xticklabels(), visible = True)
plt.setp(sub3.get_yticklabels(), visible = False)
sub3.text(-2.5, -9, '$\mathregular{log(F_{X}/F_{O})}$')
# Set tick marks
sub3.xaxis.set_major_formatter(majorFormatter)
sub3.yaxis.set_major_formatter(majorFormatter)
sub3.xaxis.set_major_locator(majorLocator)
sub3.xaxis.set_minor_locator(minorLocator)
sub3.yaxis.set_major_locator(majorLocator)
sub3.yaxis.set_minor_locator(minorLocator)
# Graph parameters
sub3.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(cv_xo, cv_xir, color = '#FF0000', marker = '*', s = 3, label = 'XGS')
plt.scatter(bhb_xo, bhb_xir, color = '#01DF74', marker = '^', s = 3, label = 'GPS')
plt.scatter(mgr_xo, mgr_xir, color = '#08088A', marker = 'D', s = 3, label = 'SNR')
plt.scatter(bstr_xo, bstr_xir, color = '#FE2EC8', marker = 'v', s = 3, label = 'ULX')
plt.scatter(apsr_xo, apsr_xir, color = '000000', marker = ',', s = 3, label = 'CO')
plt.scatter(rpsr_xo, rpsr_xir, color = '#BF00FF', marker = '*', s = 3, label = 'Mixed')
lgnd3 = plt.legend(loc = 'upper left', scatterpoints = 1, fontsize = 5)
lgnd3.get_frame().set_linewidth(0.0)

# ========== Output ========== #
fig.savefig('fig17.eps',format = 'eps', bbox_inches = 'tight', pad_inches = 0.02, dpi = 1000)
