from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Error bars
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

star_hr1 = []
star_hr2 = []
star_hr3 = []
star_hr4 = []


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

# Weights to normalize graph
weight_xo = ones_like(star_xo) / float(len(star_xo))
weight_xir = ones_like(star_xir) / float(len(star_xir))

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
plt.rc('axes', titlesize = LARGE_SIZE)     # Font size of the axes title
plt.rc('axes', labelsize = SMALL_SIZE)     # Font size of the x and y labels
plt.rc('xtick', labelsize = SMALL_SIZE)    # Font size of the tick labels
plt.rc('ytick', labelsize = SMALL_SIZE)    # Font size of the tick labels
plt.rc('legend', fontsize = SMALL_SIZE)    # Legend font size
# Axes ticks
majorFormatter = FormatStrFormatter('%1.0f')
majorLocatorX = MultipleLocator(2)      # Major tick intervals for X-axis
minorLocatorX = MultipleLocator(0.5)   # Minor tick intervals for X-axis
majorLocatorY = MultipleLocator(10)     # Major tick intervals for Y-axis

# ========== Subplot 1 ========== #
sub1 = plt.subplot(611)
sub1.set_position([0.25, 5*(1/yr)+0.28, 5/xr, 1/yr])  # (left, bottom, width, height)
# Axes parameters
sub1.set_xlim([-4.75, 4])
sub1.set_ylim([0, .35])
plt.setp(sub1.get_xticklabels(), visible = False)
plt.setp(sub1.get_yticklabels(), visible = True)
sub1.text(-5.5, 0, 'Percentage (%; X-ray-to-IR)', rotation = 90)
sub1.text(-4.25, 0.25, 'Star')
# Set tick marks
sub1.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
sub1.yaxis.set_major_locator(MultipleLocator(.1))
# Graph parameters
sub1.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
bin = [-4.75, -4.5, -4.25, -4.0, -3.75, -3.5, -3.25, -3, -2.75, -2.5, -2.25, -2, -1.75, -1.5, -1.25, -1,
                    -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25,
                    3.5, 3.75, 4]
sub1.hist(star_xir,
          bins = [-4.75, -4.5, -4.25, -4.0, -3.75, -3.5, -3.25, -3, -2.75, -2.5, -2.25, -2, -1.75, -1.5, -1.25, -1,
                    -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25,
                    3.5, 3.75, 4],
          weights = weight_xir,
          edgecolor = '#FF0000',
          linewidth = 0.5,
          fc = (0,0,0,0),
          orientation = 'vertical',
          histtype = 'step')

# ========== Subplot 2 ========== #
sub2 = plt.subplot(612, sharex = sub1)
sub2.set_position([0.25, 4*(1/yr)+0.27, 5/xr, 1/yr])
# Axes parameters
sub2.set_xlim([-4.75, 4])
sub2.set_ylim([0, 35])
plt.setp(sub2.get_xticklabels(), visible = False)
plt.setp(sub2.get_yticklabels(), visible = True)
# Set tick marks
sub2.yaxis.set_major_formatter(majorFormatter)
sub2.yaxis.set_major_locator(majorLocatorY)
# Graph parameters
sub2.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(star_hr2, star_hr3, color = '#FF0000', marker = '^', s = 1, label = 'Star')

# ========== Subplot 3 ========== #
sub3 = plt.subplot(613)
sub3.set_position([0.25, 3*(1/yr)+0.26, 5/xr, 1/yr])  # (left, bottom, width, height)
# Axes parameters
sub3.set_xlim([-4.75, 4])
sub3.set_ylim([0, 35])
plt.setp(sub3.get_xticklabels(), visible = False)
plt.setp(sub3.get_yticklabels(), visible = True)
# Set tick marks
sub3.yaxis.set_major_formatter(majorFormatter)
sub3.yaxis.set_major_locator(majorLocatorY)
# Graph parameters
sub3.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(star_hr3, star_hr4, color = '#FF0000', marker = '^', s = 1, label = 'Star')

# ========== Subplot 4 ========== #
sub4 = plt.subplot(614)
sub4.set_position([0.25, 2*(1/yr)+0.22, 5/xr, 1/yr])  # (left, bottom, width, height)
# Axes parameters
sub4.set_xlim([-4.75, 4])
sub4.set_ylim([0, 35])
plt.setp(sub4.get_xticklabels(), visible = False)
plt.setp(sub4.get_yticklabels(), visible = True)
sub4.text(-5.5, 0, 'Percentage (%; X-ray-to-optical)', rotation = 90)
# Set tick marks
sub4.yaxis.set_major_formatter(majorFormatter)
sub4.yaxis.set_major_locator(majorLocatorY)
# Graph parameters
sub4.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(star_hr3, star_hr4, color = '#FF0000', marker = '^', s = 1, label = 'Star')

# ========== Subplot 5 ========== #
sub5 = plt.subplot(615)
sub5.set_position([0.25, (1/yr)+0.21, 5/xr, 1/yr])  # (left, bottom, width, height)
# Axes parameters
sub5.set_xlim([-4.75, 4])
sub5.set_ylim([0, 35])
plt.setp(sub5.get_xticklabels(), visible = False)
plt.setp(sub5.get_yticklabels(), visible = True)
# Set tick marks
sub5.yaxis.set_major_formatter(majorFormatter)
sub5.yaxis.set_major_locator(majorLocatorY)
# Graph parameters
sub5.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(star_hr3, star_hr4, color = '#FF0000', marker = '^', s = 1, label = 'Star')

# ========== Subplot 6 ========== #
sub6 = plt.subplot(616, sharex = sub1)
sub6.set_position([0.25, 0.2, 5/xr, 1/yr])
# Axes parameters
sub6.set_xlim([-4.75, 4])
sub6.set_ylim([0, 35])
plt.setp(sub6.get_xticklabels(), visible = True)
plt.setp(sub6.get_yticklabels(), visible = True)
# Set tick marks
sub6.xaxis.set_major_formatter(majorFormatter)
sub6.yaxis.set_major_formatter(majorFormatter)
sub6.xaxis.set_major_locator(majorLocatorX)
sub6.xaxis.set_minor_locator(minorLocatorX)
sub6.yaxis.set_major_locator(majorLocatorY)
# Graph parameters
sub6.errorbar(x, y, yerr = ye, fmt = 'k|', mfc = 'none')
plt.scatter(star_hr1, star_hr2, color = '#FF0000', marker = '^', s = 1, label = 'Star')

# ========== Output ========== #
fig.savefig('fig11.eps',format = 'eps', bbox_inches = 'tight', pad_inches = 0.02, dpi = 1000)