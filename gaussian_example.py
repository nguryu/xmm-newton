import numpy as np
import matplotlib.pyplot as plt
import emcee

# Function to return the density p(x) for specific values.
# First argument, x, is the position of a single walker (N-dimensional numpy array).
# The rest are constant and come from args = [] in emcee.Ensembler
def lnprob(x, mu, icov):
    diff = x - mu
    return -np.dot(diff, np.dot(icov, diff))/2.0

# Set up specific values of hyperparameters in 50 dimensions.
ndim = 50
means = np.random.rand(ndim)
cov = 0.5 - np.random.rand(ndim ** 2).reshape((ndim, ndim))  # cov is the \Sigma
cov = np.triu(cov)  # Upper triangle array.
cov += cov.T - np.diag(cov.diagonal())
cov = np.dot(cov, cov)

# Compute inverse of cov.
icov = np.linalg.inv(cov)

# Use 250 walkers.
# Guess starting point for each of the 250 walkers. This position will be a
# 50-dimensional vector so the initial guess should be a 250x50 array.
nwalkers = 250
p0 = np.random.rand(ndim * nwalkers).reshape((nwalkers, ndim))
print(p0)

sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args = [means, icov])

pos, prob, state = sampler.run_mcmc(p0, 100)  # Save final position of walkers to 'pos' after 100 steps.
sampler.reset()  # Clears the previous parameters to have a fresh start.
sampler.run_mcmc(pos, 1000)  # 1000 steps is chosen arbitrarily.
# sampler now has a property EnsembleSampler.chain that is a numpy array with the
# shape (250, 1000, 50) => (nwalkers, 1000, ndim).
# A more useful object is EnsembleSampler.flatchain which has the shape (250000, 50)
# and has all the samples reshaped into a flat list.
# => Now have 250000 unbiased samples of the density p(x).

for i in range(ndim):
    plt.figure()
    plt.hist(sampler.flatchain[:,i], 100, color = "k", histtype = "step")
    plt.title("Dimension {0:d}".format(i))

print("mean acceptance fraction: {0:.3f}".format(np.mean(sampler.acceptance_fraction)))
plt.show()
