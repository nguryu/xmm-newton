from numpy import *
from scipy.stats import rayleigh
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
star_xo = []
star_xir = []
# Galaxies
agn_f14 = []
agn_var14 = []
agn_xo = []
agn_xir = []

# Read in file and add file elements into lists.
with open('irmatch_stars_a.asc', 'r') as data_file:
    for line in data_file:
        li = line.strip()
        if not li.startswith('#'):
            col = line.split(' ')
            src_id.append(col[0])
            #det_no.append(int(col[4]))
            #var14.append(float(col[3]))
            star_xir.append(float(col[16]))
            f14_max.append(float(col[19]))

# [17] X-ray to IR source separation
# [20] Flux

'''
# Add f14_max and var14 into respective classification lists
for i in range(0, len(src_id)):
    if det_no[i] > 1:
        star_f14.append(float(f14_max[i]))
        star_var14.append(float(var14[i]))
'''
star_xir = array(star_xir)*3.439

# ========== Graph Set-up ========== #
# Figure size
xr = 8.
yr = 10.
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

# Tick marks
xaxis_MajorFormatter = FormatStrFormatter('%d')
xaxis_MajorLocator = MultipleLocator(0.05)
xaxis_MinorLocator = MultipleLocator(0.01)
yaxis_MajorFormatter = FormatStrFormatter('%d')
yaxis_MajorLocator = MultipleLocator(1)
yaxis_MinorLocator = MultipleLocator(0.1)

# ========== Subplot 1 ========== #
sub1 = plt.subplot(821)
sub1.set_position([0.22, 0.2, 3/xr, 2/yr])  # (left, bottom, width, height)
# Axes parameters
sub1.set_xscale('log')
sub1.set_xlim([10**-14, 9.3**-9])
sub1.set_ylim([-0.2, 4.5])
plt.setp(sub1.get_xticklabels(), visible = False)
plt.setp(sub1.get_yticklabels(), visible = True, rotation = 90, fontsize = MEDIUM_SIZE)
sub1.yaxis.set_minor_locator(yaxis_MinorLocator)

# Graph parameters
sub1.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
sub1.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(agn_f14, agn_xo, color = '#FF0000', marker = '^', s = 5, label = 'AGN')

# ========== Subplot 2 ========== #
sub2 = plt.subplot(822)
sub2.set_position([0.22+3/xr, 0.2, 3/xr, 2/yr])
# Axes parameters
sub2.set_xlim([0, 0.34])
sub2.set_ylim([-0.2, 4.5])
plt.setp(sub2.get_xticklabels(), visible = False)
plt.setp(sub2.get_yticklabels(), visible = False)
sub2.xaxis.set_minor_locator(xaxis_MinorLocator)
sub2.yaxis.set_minor_locator(yaxis_MinorLocator)
# Graph parameters
# weight = ones_like(agn_xo) / float(len(agn_xo))  # Weight to normalize graph
sub2.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
# sub2.hist(agn_var14, bins = logspace(0, log10(1.2**50), 50), weights = weight,
#          edgecolor = '#FF0000', linewidth = 0.5, fc = (0,0,0,0), orientation = 'horizontal')

# ========== Subplot 3 ========== #
sub3 = plt.subplot(823)
sub3.set_position([0.22, 0.2-2/yr, 3/xr, 2/yr])  # (left, bottom, width, height)
# Axes parameters
sub3.set_xscale('log')
sub3.set_xlim([10**-14, 9.3**-9])
sub3.set_ylim([-0.2, 4.5])
plt.setp(sub3.get_xticklabels(), visible = False)
plt.setp(sub3.get_yticklabels(), visible = True, rotation = 90, fontsize = MEDIUM_SIZE)
sub3.yaxis.set_minor_locator(yaxis_MinorLocator)
# Graph parameters
sub3.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
sub3.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
# plt.scatter(f14_max, star_xir, color = '#08088A', marker = 's', facecolor = 'None',
#             edgecolor = '#08088A', s = 10, label = 'Star')

# ========== Subplot 4 ========== #
sub4 = plt.subplot(824)
sub4.set_position([0.22+3/xr, 0.2-2/yr, 3/xr, 2/yr])
# Axes parameters
sub4.set_xlim([0, 0.34])
sub4.set_ylim([-0.2, 4.5])
plt.setp(sub4.get_xticklabels(), visible = False)
plt.setp(sub4.get_yticklabels(), visible = False)
sub4.xaxis.set_minor_locator(xaxis_MinorLocator)
sub4.yaxis.set_minor_locator(yaxis_MinorLocator)
# Graph parameters
weight = ones_like(star_xir) / float(len(star_xir))  # Weight to normalize graph
sub4.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
# sub4.hist(star_xir, bins = logspace(0, log10(1.2**50), 50), weights = weight,
#          edgecolor = '#08088A', linewidth = 0.5, fc = (0,0,0,0), orientation = 'horizontal')

# ========== Subplot 5 ========== #
sub5 = plt.subplot(825)
sub5.set_position([0.22, 0.2-0.02-4/yr, 3/xr, 2/yr])  # (left, bottom, width, height)
# Axes parameters
sub5.set_xscale('log')
sub5.set_xlim([10**-14, 9.3**-9])
sub5.set_ylim([-0.2, 4.5])
plt.setp(sub5.get_xticklabels(), visible = False)
plt.setp(sub5.get_yticklabels(), visible = True, rotation = 90, fontsize = MEDIUM_SIZE)
sub5.yaxis.set_minor_locator(yaxis_MinorLocator)

# Graph parameters
sub5.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
sub5.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(agn_f14, agn_xir, color = '#FF0000', marker = '^', s = 5, label = 'AGN')

# ========== Subplot 6 ========== #
sub6 = plt.subplot(826)
sub6.set_position([0.22+3/xr, 0.2-0.02-4/yr, 3/xr, 2/yr])
# Axes parameters
sub6.set_xlim([0, 0.34])
sub6.set_ylim([-0.2, 4.5])
plt.setp(sub6.get_xticklabels(), visible = False)
plt.setp(sub6.get_yticklabels(), visible = False)
sub6.xaxis.set_minor_locator(xaxis_MinorLocator)
sub6.yaxis.set_minor_locator(yaxis_MinorLocator)
# Graph parameters
weight = ones_like(agn_xir) / float(len(agn_xir))  # Weight to normalize graph
sub6.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
sub6.hist(star_var14, bins = logspace(0, log10(1.2**50), 50), weights = weight,
          edgecolor = '#FF0000', linewidth = 0.5, fc = (0,0,0,0), orientation = 'horizontal')

# ========== Subplot 7 ========== #
sub7 = plt.subplot(827)
sub7.set_position([0.22, 0.2-0.02-6/yr, 3/xr, 2/yr])  # (left, bottom, width, height)
# Axes parameters
sub7.set_xscale('log')
sub7.set_xlim([10**-14, 9.3**-9])
sub7.set_ylim([-0.2, 4.5])
plt.setp(sub7.get_xticklabels(), visible = False)
plt.setp(sub7.get_yticklabels(), visible = True, rotation = 90, fontsize = MEDIUM_SIZE)
sub7.yaxis.set_minor_locator(yaxis_MinorLocator)

# Graph parameters
sub7.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
sub7.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(f14_max, star_xir, color = '#08088A', marker = 's', facecolor = 'None',
            edgecolor = '#08088A', s = 10, label = 'Star')

# ========== Subplot 8 ========== #
sub8 = plt.subplot(828)
sub8.set_position([0.22+3/xr, 0.2-0.02-6/yr, 3/xr, 2/yr])
# Axes parameters
sub8.set_xlim([0, 0.34])
sub8.set_ylim([-0.2, 4.5])
plt.setp(sub8.get_xticklabels(), visible = True, fontsize = MEDIUM_SIZE)
plt.setp(sub8.get_yticklabels(), visible = False)
sub8.xaxis.set_major_locator(xaxis_MajorLocator)
sub8.xaxis.set_minor_locator(xaxis_MinorLocator)
sub8.yaxis.set_minor_locator(yaxis_MinorLocator)
# Labels
plt.gcf().text(0.35, 0.2-0.06-6/yr, '$\mathregular{F_{max} (erg s^{-1} cm^{-2})}$', fontsize = MEDIUM_SIZE)
plt.gcf().text(0.70, 0.2-0.06-6/yr, 'Percentage (%)', fontsize = MEDIUM_SIZE)
plt.gcf().text(0.17, 0.3, 'X-ray-to-optical separation (arcsec)', fontsize = MEDIUM_SIZE, rotation = 90)
plt.gcf().text(0.17, -0.15, 'X-ray-to-IR separation', fontsize = MEDIUM_SIZE, rotation = 90)
plt.gcf().text(.82, -0.25, 'Star, N = 3185', fontsize = MEDIUM_SIZE)
# X-Axis
plt.gcf().text(0.20, 0.2-0.04-6/yr, '$\mathregular{10^{-14}}$', fontsize = MEDIUM_SIZE)
plt.gcf().text(0.21+0.13, 0.2-0.04-6/yr, '$\mathregular{10^{-12}}$', fontsize = MEDIUM_SIZE)
plt.gcf().text(0.21+0.275, 0.2-0.04-6/yr, '$\mathregular{10^{-10}}$', fontsize = MEDIUM_SIZE)
# Graph parameters
weight = ones_like(star_xir) / float(len(star_xir))  # Weight to normalize graph
sub8.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
sub8.hist(star_xir, bins = 30, range = (0, 4.5),weights = weight,
edgecolor = '#08088A', linewidth = 0.5, fc = (0,0,0,0), orientation = 'horizontal')
# Rayleigh distribution
mean = sum(star_xir)/len(star_xir)
y = linspace(0.0, 4.5, 100)
param = rayleigh.fit(star_xir)
pdf_fitted = rayleigh.pdf(y)*0.15
sub8.plot(pdf_fitted, y, 'black', linestyle = '--', linewidth = 0.5)

# ========== Output ========== #
fig.savefig('fig6.eps',format = 'eps', bbox_inches = 'tight', pad_inches = 0.02, dpi = 1000)
