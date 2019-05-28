from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Initialize arrays to store data in.
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
# Stars
star_f14 = []
star_var14 = []
orst_f14 = []
orst_var14 = []
prst_f14 = []
prst_var14 = []
vrst_f14 = []
vrst_var14 = []
flst_f14 = []
flst_var14 = []
# Galaxies
sy1n_f14 = []
sy1n_var14 = []
sy1_f14 = []
sy1_var14 = []
sy2_f14 = []
sy2_var14 = []
lin_f14 = []
lin_var14 = []
bla_f14 = []
bla_var14 = []
qso_f14 = []
qso_var14 = []
agn_f14 = []
agn_var14 = []
# Compact objects
bhb_f14 = []
bhb_var14 = []
bstr_f14 = []
bstr_var14 = []
apsr_f14 = []
apsr_var14 = []
rpsr_f14 = []
rpsr_var14 = []
ins_f14 = []
ins_var14 = []
mgr_f14 = []
mgr_var14 = []
cv_f14 = []
cv_var14 = []

# Read in file and add file elements into lists.
with open('plotdata_star_a_var', 'r') as data_file:
    for line in data_file:
        li = line.strip()
        if not li.startswith('#'):
            col = line.split(' ')
            src_id.append(col[0])
            f14_max.append(float(col[2]))
            det_no.append(int(col[4]))
            var14.append(float(col[3]))

# Add f14_max and var14 into respective classification lists
for i in range(0, len(src_id)):
    if det_no[i] > 1:
        star_f14.append(float(f14_max[i]))
        star_var14.append(float(var14[i]))

# ========== Graph Set-up ========== #
# Figure size
xr = 4.
yr = 3.
fig = plt.figure(figsize = (xr, yr)) # (width, height)
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

# ========== Subplot 1 ========== #
sub1 = plt.subplot(132)
sub1.set_position([0.22, 0.2, 1.7/xr, 2/yr])  # (left, bottom, width, height)
# Axes parameters
sub1.set_xscale('log')
sub1.set_yscale('log')
sub1.set_xlim([10**-14, 9.3**-9])
sub1.set_ylim([0.8, 4000])
plt.setp(sub1.get_xticklabels(), visible = False)
plt.setp(sub1.get_yticklabels(), visible = False)
# Labels
plt.gcf().text(0.3, 0.09, '$\mathregular{F_{max} (erg s^{-1} cm^{-2})}$', fontsize = SMALL_SIZE)
plt.gcf().text(0.65, 0.09, 'Percentage (%)', fontsize = SMALL_SIZE)
plt.gcf().text(0.14, 0.5, '$\mathregular{V_{var}}$', fontsize = SMALL_SIZE, rotation = 90)
# X-Axis
plt.gcf().text(0.2, 0.15, '$\mathregular{10^{-14}}$')
plt.gcf().text(0.35, 0.15, '$\mathregular{10^{-12}}$')
plt.gcf().text(0.5, 0.15, '$\mathregular{10^{-10}}$')
# Y-Axis
plt.gcf().text(0.18, 0.2, '1', rotation = 90)
plt.gcf().text(0.18, 0.38, '10', rotation = 90)
plt.gcf().text(0.18, 0.58, '$\mathregular{10^{2}}$', rotation = 90)
plt.gcf().text(0.18, 0.76, '$\mathregular{10^{3}}$', rotation = 90)
# Graph parameters
sub1.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
sub1.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(star_f14, star_var14, color = '#FF0000', marker = '^', s = 5, label = 'Star')
'''
plt.scatter(orst_f14, orst_var14, color = '#01DF74', marker = 'v', s = 10, label = 'OrVr')
plt.scatter(prst_f14, prst_var14, color = '#08088A', marker = ',', s = 10, label = 'PrSt')
plt.scatter(vrst_f14, vrst_var14, color = '#FE2EC8', marker = '*', s = 10, label = 'VrSt')
plt.scatter(flst_f14, flst_var14, color = '#000000', marker = 'o', s = 10, label = 'FlSt')
'''
lgnd1 = plt.legend(loc = 'upper left', scatterpoints = 1, fontsize = 6)
lgnd1.get_frame().set_linewidth(0.0)

# ========== Subplot 2 ========== #
sub2 = plt.subplot(133)
sub2.set_position([0.22+1.7/xr, 0.2, 0.90/xr, 2/yr])
# Axes parameters
sub2.set_yscale('log')
sub2.set_xlim([0, 0.34])
sub2.set_ylim([0.8, 4000])
plt.setp(sub2.get_xticklabels(), visible = False)
plt.setp(sub2.get_yticklabels(), visible = False)
plt.gcf().text(0.635, 0.154, '0')
plt.gcf().text(0.695, 0.154, '10')
plt.gcf().text(0.76, 0.154, '20')
plt.gcf().text(0.83, 0.154, '30')
# Set tick marks
x2MajorFormatter = FormatStrFormatter('%1.1f')
x2MajorLocator = MultipleLocator(.10)   # Major tick intervals
x2MinorLocator = MultipleLocator(.02)   # Minor tick intervals
sub2.xaxis.set_major_formatter(x2MajorFormatter)
sub2.xaxis.set_major_locator(x2MajorLocator)
sub2.xaxis.set_minor_locator(x2MinorLocator)
# Graph parameters
weight = ones_like(star_var14) / float(len(star_var14))  # Weight to normalize graph
sub2.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
sub2.hist(star_var14, bins = logspace(0, log10(1.2**50), 50), weights = weight,
          edgecolor = '#FF0000', linewidth = 0.5, fc = (0,0,0,0), orientation = 'horizontal')

# ========== Output ========== #
fig.savefig('fig4star.eps',format = 'eps', bbox_inches = 'tight', pad_inches = 0.02, dpi = 1000)
