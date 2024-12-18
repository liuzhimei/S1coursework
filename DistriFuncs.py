import numpy as np
from scipy.stats import norm
from scipy.stats import crystalball, truncexpon, uniform, truncnorm


def g_s(x, mu, sigma, beta, m):
    crystall_ball_distri = crystalball(beta, m, loc=mu, scale=sigma)
    normalization = crystall_ball_distri.cdf(5) - crystall_ball_distri.cdf(0)
    return crystall_ball_distri.pdf(x) / normalization

def g_b(x):
    return uniform.pdf(x, loc=0, scale=5)

def h_s(y, lambda_param):
    scale = 1 / lambda_param
    b = 10 / scale
    return truncexpon(b, loc=0, scale=scale).pdf(y)

def h_s_cdf(y, lambda_param):
    scale = 1 / lambda_param
    b = 10 / scale
    return truncexpon(b, loc=0, scale=scale).cdf(y)

def density_h_s_cdf(y, Ns, lambda_param):
    return Ns * h_s_cdf(y, lambda_param)

def h_b(y, mu_b, sigma_b):
    a = (0 - mu_b) / sigma_b
    b = (10 - mu_b) / sigma_b
    return truncnorm(a, b, loc=mu_b, scale=sigma_b).pdf(y)

def F(x, y, f, mu, sigma, beta, m, lambda_param, mu_b, sigma_b):
    return f * g_s(x, mu, sigma, beta, m) * h_s(y, lambda_param) + (1-f) * g_b(x) * h_b(y, mu_b, sigma_b)

def total_density(sample, N, f, mu, sigma, beta, m, lambda_param, mu_b, sigma_b):
    x, y = sample
    return N, N * F(x, y, f, mu, sigma, beta, m, lambda_param, mu_b, sigma_b)

def total_density_x(x_sample, N, f, mu, sigma, beta, m):
    return N, N * (f * g_s(x_sample, mu, sigma, beta, m) + (1-f) * g_b(x_sample))